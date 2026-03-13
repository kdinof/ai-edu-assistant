#!/usr/bin/env python3
"""
Perplexity Research Compiler
Conducts multi-query research and compiles results into a structured document.
"""

import argparse
import json
import sys
import time
from datetime import datetime
from pathlib import Path

from search import search_perplexity, get_api_key


def conduct_research(
    topic: str,
    questions: list[str],
    model: str = "sonar-pro",
    output_path: str = None,
    delay: float = 1.0,
) -> dict:
    """
    Conduct multi-query research on a topic.

    Args:
        topic: Main research topic/title
        questions: List of research questions to investigate
        model: Perplexity model to use
        output_path: Path to save the compiled report
        delay: Delay between API calls (rate limiting)

    Returns:
        dict with compiled research results
    """
    api_key = get_api_key()
    if not api_key:
        raise ValueError("PERPLEXITY_API_KEY not found")

    results = {
        "topic": topic,
        "timestamp": datetime.now().isoformat(),
        "model": model,
        "sections": [],
        "all_sources": [],
        "total_tokens": 0,
    }

    print(f"\n🔍 Starting research: {topic}")
    print(f"   Model: {model}")
    print(f"   Questions: {len(questions)}")
    print("-" * 50)

    for i, question in enumerate(questions, 1):
        print(f"\n[{i}/{len(questions)}] {question[:60]}{'...' if len(question) > 60 else ''}")

        try:
            result = search_perplexity(
                query=question,
                model=model,
                api_key=api_key,
            )

            section = {
                "question": question,
                "content": result["content"],
                "citations": result.get("citations", []),
                "tokens": result.get("usage", {}).get("total_tokens", 0),
            }
            results["sections"].append(section)
            results["total_tokens"] += section["tokens"]

            # Collect all unique sources
            for url in result.get("citations", []):
                if url not in results["all_sources"]:
                    results["all_sources"].append(url)

            sources_count = len(result.get('citations', []))
            tokens_used = section["tokens"]
            print(f"    ✓ {sources_count} sources, {tokens_used} tokens")

        except Exception as e:
            print(f"    ✗ Error: {e}")
            results["sections"].append({
                "question": question,
                "content": f"[Error: {e}]",
                "citations": [],
                "tokens": 0,
            })

        # Rate limiting
        if i < len(questions):
            time.sleep(delay)

    print("-" * 50)
    print(f"✓ Research complete: {len(results['all_sources'])} unique sources, {results['total_tokens']} total tokens")

    # Compile markdown report
    report = compile_report(results)

    if output_path:
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(report, encoding="utf-8")
        print(f"\n✓ Report saved to: {output_file}")

    return {"results": results, "report": report}


def compile_report(results: dict) -> str:
    """Compile research results into a markdown report."""
    lines = [
        f"# {results['topic']}",
        "",
        f"**Date:** {results['timestamp'][:10]}",
        f"**Model:** {results['model']}",
        f"**Questions investigated:** {len(results['sections'])}",
        "",
        "---",
        "",
        "## Executive Summary",
        "",
        "_[Add your synthesis here after reviewing the findings]_",
        "",
        "---",
        "",
    ]

    # Add each section
    for i, section in enumerate(results["sections"], 1):
        lines.append(f"## {i}. {section['question']}")
        lines.append("")
        lines.append(section["content"])
        lines.append("")

        if section.get("citations"):
            lines.append("**Sources for this section:**")
            for j, url in enumerate(section["citations"], 1):
                lines.append(f"- [{j}] {url}")
            lines.append("")

        lines.append("---")
        lines.append("")

    # Add consolidated sources
    if results["all_sources"]:
        lines.append("## All Sources")
        lines.append("")
        for i, url in enumerate(results["all_sources"], 1):
            lines.append(f"{i}. {url}")
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Conduct multi-query research using Perplexity API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive mode (will prompt for questions)
  python research.py --topic "EdTech trends 2025"

  # With questions from command line
  python research.py --topic "AI in education" \\
    --questions "What are the main AI applications in education?" \\
    --questions "How is AI changing student assessment?" \\
    --output research/ai-education.md

  # With questions from file (one per line)
  python research.py --topic "Market analysis" \\
    --questions-file questions.txt \\
    --output research/market.md
        """,
    )
    parser.add_argument(
        "--topic", "-t",
        required=True,
        help="Main research topic/title",
    )
    parser.add_argument(
        "--questions", "-q",
        action="append",
        help="Research question (can specify multiple)",
    )
    parser.add_argument(
        "--questions-file", "-f",
        help="File with questions (one per line)",
    )
    parser.add_argument(
        "--output", "-o",
        help="Output file path for the report",
    )
    parser.add_argument(
        "--model", "-m",
        default="sonar-pro",
        choices=["sonar", "sonar-pro", "sonar-reasoning"],
        help="Model to use (default: sonar-pro)",
    )
    parser.add_argument(
        "--delay", "-d",
        type=float,
        default=1.0,
        help="Delay between API calls in seconds (default: 1.0)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output raw JSON instead of markdown",
    )

    args = parser.parse_args()

    # Collect questions
    questions = args.questions or []

    if args.questions_file:
        questions_path = Path(args.questions_file)
        if questions_path.exists():
            with open(questions_path) as f:
                file_questions = [
                    line.strip()
                    for line in f
                    if line.strip() and not line.startswith("#")
                ]
                questions.extend(file_questions)
        else:
            print(f"Error: Questions file not found: {args.questions_file}")
            sys.exit(1)

    # Interactive mode if no questions provided
    if not questions:
        print(f"Topic: {args.topic}")
        print("Enter research questions (one per line, empty line to finish):")
        while True:
            try:
                q = input("> ").strip()
                if not q:
                    break
                questions.append(q)
            except EOFError:
                break

    if not questions:
        print("Error: No questions provided")
        sys.exit(1)

    try:
        result = conduct_research(
            topic=args.topic,
            questions=questions,
            model=args.model,
            output_path=args.output,
            delay=args.delay,
        )

        if args.json:
            print(json.dumps(result["results"], indent=2, ensure_ascii=False))
        elif not args.output:
            print("\n" + "=" * 60)
            print(result["report"])

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nResearch interrupted")
        sys.exit(1)


if __name__ == "__main__":
    main()
