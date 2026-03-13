#!/usr/bin/env python3
"""Run deep research via Parallel AI Task API."""

import json
import sys
import time
import urllib.request
import urllib.error

API_KEY = sys.argv[1] if len(sys.argv) > 1 else ""
BASE_URL = "https://api.parallel.ai/v1/tasks/runs"
PROCESSOR = "pro"

QUERIES = {
    "tools-deep": {
        "input": (
            "Comprehensive deep research on Claude Code and Claude Cowork capabilities for office tasks in 2025-2026. "
            "Cover these topics in detail:\n"
            "1. Claude Code capabilities for working with Google Sheets, Excel - creating, editing spreadsheets, formulas, data analysis. Real workflow examples and limitations.\n"
            "2. Claude Code/Cowork for creating PPTX presentations - supported templates, working with existing presentations, practical examples.\n"
            "3. Claude Code for PDF documents - reading, analysis, data extraction, PDF creation. Real use cases for office workers.\n"
            "4. Detailed comparison: Claude Code vs ChatGPT Code Interpreter vs Microsoft Copilot for office tasks (spreadsheets, documents, presentations). What's better for which tasks?\n"
            "5. Claude Cowork mode - what is it, how it works, how it differs from regular Claude, advantages for teamwork and office processes.\n"
            "Focus on practical capabilities, not marketing. Include specific examples and limitations."
        ),
        "output_file": "02-research-tools-deep.md"
    },
    "competitors-deep": {
        "input": (
            "Comprehensive competitive analysis of AI courses for office workers in 2025-2026. "
            "Cover these topics in detail:\n"
            "1. Courses on ChatGPT and AI for accountants, financial specialists, HR - structure, pricing, student outcomes, reviews.\n"
            "2. AI courses in Uzbekistan 2025-2026 - what do local platforms offer? Najot Talim, PDP Academy, others. Any AI productivity courses?\n"
            "3. Coursera, Udemy, LinkedIn Learning - most popular AI productivity and AI for office workers courses. Ratings, student counts, structure, what makes them successful.\n"
            "4. Corporate AI training in CIS and Uzbekistan - which companies train employees on AI tools? Formats, results, case studies.\n"
            "5. Prompt engineering courses for non-programmers 2025-2026 - best practices, course structure, common mistakes in teaching.\n"
            "Provide specific course names, prices, and links where possible."
        ),
        "output_file": "02-research-competitors-deep.md"
    },
    "methodology-deep": {
        "input": (
            "Deep research on methodology and format for teaching AI tools to office workers. "
            "Cover these topics in detail:\n"
            "1. Specific office tasks of accountants, HR, marketers, project managers that can be automated with AI. List tasks with time savings estimate for each profession.\n"
            "2. How to properly structure a practical AI course for working adults. Optimal lesson length, practice vs theory ratio, retention strategies, engagement techniques.\n"
            "3. Time audit methodology - how to measure time savings when implementing AI tools. Frameworks and metrics used in corporate training.\n"
            "4. Prompt templates and frameworks for office tasks that show best results - RISEN, RACE, CO-STAR and others. Comparison for non-technical users.\n"
            "5. How to overcome office workers' resistance to AI. Specific tactics, examples of successful adoption, what works in CIS region.\n"
            "Provide concrete data, research findings, and practical recommendations."
        ),
        "output_file": "02-research-methodology-deep.md"
    }
}


def create_task(query_input):
    data = json.dumps({
        "input": query_input,
        "processor": PROCESSOR,
        "task_spec": {
            "output_schema": {"type": "text"}
        }
    }).encode()

    req = urllib.request.Request(
        BASE_URL,
        data=data,
        headers={
            "x-api-key": API_KEY,
            "Content-Type": "application/json"
        }
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def get_status(run_id):
    req = urllib.request.Request(
        f"{BASE_URL}/{run_id}",
        headers={"x-api-key": API_KEY}
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def get_result(run_id):
    req = urllib.request.Request(
        f"{BASE_URL}/{run_id}/result",
        headers={"x-api-key": API_KEY}
    )
    with urllib.request.urlopen(req, timeout=3600) as resp:
        return json.loads(resp.read())


def main():
    if not API_KEY:
        print("Usage: python parallel-research.py <API_KEY>")
        sys.exit(1)

    output_dir = "/Users/kdinov/Desktop/OSNOVA/projects/active/ai-edu-assistant/courses/claude-cowork-office"

    # Launch all tasks
    tasks = {}
    for name, config in QUERIES.items():
        print(f"Launching: {name}...")
        try:
            result = create_task(config["input"])
            run_id = result.get("run_id")
            tasks[name] = {"run_id": run_id, "config": config, "status": "running"}
            print(f"  -> run_id: {run_id}")
        except Exception as e:
            print(f"  -> ERROR: {e}")
            tasks[name] = {"run_id": None, "config": config, "status": "failed"}

    # Poll until all complete
    print("\nWaiting for results (polling every 30s, max 45 min)...")
    max_polls = 90  # 45 min
    for poll in range(max_polls):
        all_done = True
        for name, task in tasks.items():
            if task["status"] in ("completed", "failed"):
                continue
            all_done = False
            try:
                status = get_status(task["run_id"])
                current = status.get("status", "unknown")
                if current == "completed":
                    task["status"] = "completed"
                    print(f"  [{name}] completed!")
                    # Get result
                    try:
                        res = get_result(task["run_id"])
                        output = res.get("output", {})
                        content = output if isinstance(output, str) else json.dumps(output, indent=2, ensure_ascii=False)
                        filepath = f"{output_dir}/{task['config']['output_file']}"
                        with open(filepath, "w") as f:
                            f.write(f"# Deep Research: {name}\n\n")
                            f.write(f"**Processor:** {PROCESSOR}\n")
                            f.write(f"**Run ID:** {task['run_id']}\n\n---\n\n")
                            f.write(content)
                        print(f"  [{name}] saved to {filepath}")
                    except Exception as e:
                        print(f"  [{name}] error getting result: {e}")
                elif current == "failed":
                    task["status"] = "failed"
                    print(f"  [{name}] FAILED: {status}")
                else:
                    print(f"  [{name}] still {current}... (poll {poll+1})")
            except Exception as e:
                print(f"  [{name}] poll error: {e}")

        if all_done:
            print("\nAll tasks completed!")
            break

        time.sleep(30)
    else:
        print("\nTimeout reached. Some tasks may still be running.")


if __name__ == "__main__":
    main()
