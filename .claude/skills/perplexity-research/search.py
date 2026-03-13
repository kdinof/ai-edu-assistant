#!/usr/bin/env python3
"""
Perplexity Research Tool
Performs deep web research using Perplexity API and outputs structured results with citations.
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path

try:
    import requests
except ImportError:
    print("Error: requests library required. Install with: pip install requests")
    sys.exit(1)


def get_api_key():
    """Get API key from environment or .env file."""
    # Check environment variable first
    api_key = os.environ.get("PERPLEXITY_API_KEY")
    if api_key:
        return api_key

    # Check .env file in project root
    env_paths = [
        Path(__file__).parent.parent.parent.parent / ".env",  # OSNOVA/.env
        Path.cwd() / ".env",
    ]

    for env_path in env_paths:
        if env_path.exists():
            with open(env_path) as f:
                for line in f:
                    if line.startswith("PERPLEXITY_API_KEY="):
                        return line.split("=", 1)[1].strip().strip('"').strip("'")

    return None


def search_perplexity(
    query: str,
    model: str = "sonar",
    api_key: str = None,
    search_recency: str = None,
    return_citations: bool = True,
    max_tokens: int = 4000,
    temperature: float = 0.2,
) -> dict:
    """
    Perform a search using Perplexity API.

    Args:
        query: The search query
        model: Model to use (sonar, sonar-pro, sonar-reasoning)
        api_key: Perplexity API key
        search_recency: Filter by recency (day, week, month, year)
        return_citations: Whether to include citation URLs
        max_tokens: Maximum tokens in response
        temperature: Response randomness (0.0-1.0)

    Returns:
        dict with 'content', 'citations', 'model', 'query', 'timestamp', and 'usage' keys
    """
    if not api_key:
        api_key = get_api_key()

    if not api_key:
        raise ValueError(
            "PERPLEXITY_API_KEY not found. Set it as environment variable or in .env file."
        )

    url = "https://api.perplexity.ai/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a research assistant. Provide comprehensive, factual answers "
                    "with specific details and data. Always cite your sources. "
                    "Structure your response clearly with sections if the topic is complex. "
                    "If information is uncertain or conflicting, note that explicitly."
                ),
            },
            {
                "role": "user",
                "content": query,
            },
        ],
        "return_citations": return_citations,
        "max_tokens": max_tokens,
        "temperature": temperature,
    }

    if search_recency:
        payload["search_recency_filter"] = search_recency

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()

        result = {
            "content": data["choices"][0]["message"]["content"],
            "citations": data.get("citations", []),
            "model": model,
            "query": query,
            "timestamp": datetime.now().isoformat(),
            "usage": data.get("usage", {}),
        }

        return result

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            raise ValueError("Invalid API key")
        elif e.response.status_code == 429:
            raise ValueError("Rate limit exceeded. Please wait and try again.")
        else:
            raise ValueError(f"API error: {e.response.status_code} - {e.response.text}")
    except requests.exceptions.Timeout:
        raise ValueError("Request timed out. Try again or use a simpler query.")
    except Exception as e:
        raise ValueError(f"Request failed: {str(e)}")


def check_setup() -> dict:
    """
    Verify API configuration and connectivity.

    Returns:
        dict with 'success', 'api_key_found', 'api_key_valid', and 'message' keys
    """
    result = {
        "success": False,
        "api_key_found": False,
        "api_key_valid": False,
        "message": "",
    }

    # Check if API key exists
    api_key = get_api_key()
    if not api_key:
        result["message"] = "❌ PERPLEXITY_API_KEY not found.\n\nSetup options:\n1. Add to .env file: PERPLEXITY_API_KEY=pplx-your-key\n2. Set environment variable: export PERPLEXITY_API_KEY=pplx-your-key"
        return result

    result["api_key_found"] = True

    # Validate key format
    if not api_key.startswith("pplx-"):
        result["message"] = f"⚠️ API key found but format looks incorrect (should start with 'pplx-').\nCurrent prefix: {api_key[:10]}..."
        return result

    # Test API connectivity with minimal request
    try:
        response = requests.post(
            "https://api.perplexity.ai/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": "sonar",
                "messages": [{"role": "user", "content": "test"}],
            },
            timeout=10,
        )

        if response.status_code == 200:
            result["api_key_valid"] = True
            result["success"] = True
            result["message"] = "✅ Setup verified!\n\n• API key: Found\n• API key format: Valid (pplx-...)\n• API connection: Working\n\nReady to use."
        elif response.status_code == 401:
            result["message"] = "❌ API key is invalid or expired.\n\nGet a new key at: https://www.perplexity.ai/settings/api"
        elif response.status_code == 429:
            result["api_key_valid"] = True
            result["success"] = True
            result["message"] = "✅ API key valid (rate limited - wait and retry)"
        else:
            result["message"] = f"⚠️ Unexpected response: {response.status_code}\n{response.text[:200]}"

    except requests.exceptions.Timeout:
        result["message"] = "⚠️ Connection timeout. Check your internet connection."
    except Exception as e:
        result["message"] = f"❌ Connection failed: {str(e)}"

    return result


def format_markdown(result: dict, include_metadata: bool = True) -> str:
    """Format search result as markdown."""
    lines = []

    if include_metadata:
        lines.append(f"# Research: {result['query']}")
        lines.append("")
        lines.append(f"**Date:** {result['timestamp'][:10]}")
        lines.append(f"**Model:** {result['model']}")
        lines.append("")
        lines.append("---")
        lines.append("")

    lines.append(result["content"])

    if result.get("citations"):
        lines.append("")
        lines.append("---")
        lines.append("")
        lines.append("## Sources")
        lines.append("")
        for i, url in enumerate(result["citations"], 1):
            lines.append(f"{i}. {url}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Perform deep web research using Perplexity API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Simple search
  python search.py "EdTech market Uzbekistan 2025"

  # Use specific model
  python search.py "AI trends" --model sonar-pro

  # Save to file
  python search.py "market analysis" --output research/report.md

  # Filter by recency
  python search.py "latest news" --recency week

  # Check setup
  python search.py --check-setup
        """,
    )
    parser.add_argument(
        "query",
        nargs="?",
        help="Search query (can also use --query)",
    )
    parser.add_argument(
        "--query", "-q",
        dest="query_flag",
        help="Search query",
    )
    parser.add_argument(
        "--model", "-m",
        default="sonar",
        choices=["sonar", "sonar-pro", "sonar-reasoning"],
        help="Model to use (default: sonar)",
    )
    parser.add_argument(
        "--output", "-o",
        help="Output file path (markdown)",
    )
    parser.add_argument(
        "--recency", "-r",
        choices=["day", "week", "month", "year"],
        help="Filter results by recency",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output raw JSON instead of markdown",
    )
    parser.add_argument(
        "--no-metadata",
        action="store_true",
        help="Exclude metadata header in markdown output",
    )
    parser.add_argument(
        "--check-setup",
        action="store_true",
        help="Verify API configuration and connectivity",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=4000,
        help="Maximum tokens in response (default: 4000)",
    )

    args = parser.parse_args()

    # Check setup mode
    if args.check_setup:
        result = check_setup()
        print(result["message"])
        sys.exit(0 if result["success"] else 1)

    # Get query from positional or flag argument
    query = args.query or args.query_flag
    if not query:
        parser.error("Query is required (positional argument or --query)")

    try:
        result = search_perplexity(
            query=query,
            model=args.model,
            search_recency=args.recency,
        )

        if args.json:
            output = json.dumps(result, indent=2, ensure_ascii=False)
        else:
            output = format_markdown(result, include_metadata=not args.no_metadata)

        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(output, encoding="utf-8")
            print(f"Results saved to: {output_path}")
        else:
            print(output)

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
