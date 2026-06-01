"""Test ResearchPilot tools - direct test of tool execution and Ollama tool calling.
Fails fast after 2-3 attempts max."""
import os, json, sys
os.environ["PORT"] = "8001"

os.chdir(os.path.dirname(os.path.abspath(__file__)))

import main

import httpx
import asyncio

ResearchPilot_TOOLS = main.ResearchPilot_TOOLS
execute_tool = main.execute_tool

async def test_direct_tool():
    """Test executing a tool directly."""
    print("=== Test: get_project_list ===")
    result = await execute_tool("get_project_list", {})
    print(json.dumps(result, indent=2)[:500])
    print()

    print("=== Test: read_system_core ===")
    result = await execute_tool("read_system_core", {"filename": "SYSTEM-PROTOCOLS.md"})
    print(f"Content length: {len(result.get('content',''))} chars")
    print()

    print("=== Test: search_files ===")
    result = await execute_tool("search_files", {"query": "12-Point", "max_results": 5})
    print(json.dumps(result, indent=2)[:500])
    print()

    print("=== Test: read_file ===")
    result = await execute_tool("read_file", {"path": "00-SYSTEM-CORE/ResearchPilot-SYSTEM-SPECIFICATION.md"})
    print(f"Content length: {len(result.get('content',''))} chars")
    print()

async def test_ollama_tool_call():
    """Test Ollama's tool calling with our ERA tools. Max 2 iterations."""
    print("=== Test: Ollama tool call ===")
    async with httpx.AsyncClient(timeout=60.0) as c:
        r = await c.get("http://localhost:11434/api/tags", timeout=3.0)
        if r.status_code != 200:
            print("FAIL: Ollama not reachable")
            return
        print("OK: Ollama reachable")

        model = "qwen2.5:3b"
        messages = [
            {"role": "system", "content": main.ResearchPilot_SYSTEM},
            {"role": "user", "content": "What projects do I have? Use the get_project_list tool."}
        ]

        payload = {
            "model": model,
            "messages": messages,
            "tools": ResearchPilot_TOOLS,
            "stream": False,
            "options": {"num_ctx": 32768}
        }

        r = await c.post("http://localhost:11434/api/chat", json=payload, timeout=180.0)
        data = r.json()
        msg = data.get("message", {})
        tool_calls = msg.get("tool_calls", [])

        if tool_calls:
            print(f"OK: Tool calls received: {len(tool_calls)}")
            for tc in tool_calls:
                fn = tc["function"]["name"]
                args = tc["function"]["arguments"]
                print(f"  Tool: {fn}, args: {args}")
                result = await execute_tool(fn, args)
                print(f"  Result: {json.dumps(result)[:200]}")
                messages.append({"role": "assistant", "content": msg.get("content", ""), "tool_calls": tool_calls})
                messages.append({"role": "tool", "content": json.dumps(result, ensure_ascii=False), "name": fn})

            payload2 = {
                "model": model,
                "messages": messages,
                "stream": False,
                "options": {"num_ctx": 32768}
            }
            r2 = await c.post("http://localhost:11434/api/chat", json=payload2, timeout=180.0)
            data2 = r2.json()
            content = data2.get("message", {}).get("content", "")
            print(f"\nFinal response: {content[:800]}")
        else:
            content = msg.get("content", "")
            print(f"No tool calls. Content: {content[:300]}")

async def test_full_cycle():
    """Simulate the full tool-calling cycle with max 2 rounds."""
    print("\n=== Test: Full tool cycle (max 2 rounds) ===")
    async with httpx.AsyncClient(timeout=120.0) as c:
        model = "qwen2.5:3b"
        messages = [
            {"role": "system", "content": main.ResearchPilot_SYSTEM},
            {"role": "user", "content": "What projects do I have? Use get_project_list."}
        ]

        max_iterations = 2
        all_tool_uses = []

        for iteration in range(max_iterations):
            payload = {
                "model": model,
                "messages": messages,
                "stream": False,
                "options": {"num_ctx": 32768}
            }
            if iteration == 0:
                payload["tools"] = ResearchPilot_TOOLS

            r = await c.post("http://localhost:11434/api/chat", json=payload, timeout=180.0)
            data = r.json()
            msg = data.get("message", {})
            tool_calls = msg.get("tool_calls", [])

            if tool_calls:
                print(f"Iteration {iteration}: {len(tool_calls)} tool call(s)")
                messages.append({"role": "assistant", "content": msg.get("content", ""), "tool_calls": tool_calls})
                for tc in tool_calls:
                    fn = tc["function"]["name"]
                    fn_args = tc["function"]["arguments"]
                    if isinstance(fn_args, str):
                        try:
                            fn_args = json.loads(fn_args)
                        except json.JSONDecodeError:
                            fn_args = {}
                    print(f"  -> {fn}({json.dumps(fn_args)})")
                    result = await execute_tool(fn, fn_args)
                    all_tool_uses.append({"tool": fn, "args": fn_args})
                    content_str = json.dumps(result, ensure_ascii=False)
                    messages.append({"role": "tool", "content": content_str, "name": fn})
                continue

            content = msg.get("content", "")
            print(f"\nFinal response: {content[:600]}")
            print(f"\nTools used: {len(all_tool_uses)}")
            for tu in all_tool_uses:
                print(f"  - {tu['tool']}({json.dumps(tu['args'])})")
            return

        print(f"Reached max {max_iterations} iterations, got {len(all_tool_uses)} tool calls")
        # If still going, one more attempt for final response
        if all_tool_uses:
            payload = {
                "model": model,
                "messages": messages,
                "stream": False,
                "options": {"num_ctx": 32768}
            }
            r = await c.post("http://localhost:11434/api/chat", json=payload, timeout=180.0)
            data = r.json()
            content = data.get("message", {}).get("content", "")
            print(f"\nFinal response: {content[:600]}")

async def run_tests():
    await test_direct_tool()
    await test_ollama_tool_call()
    await test_full_cycle()

if __name__ == "__main__":
    asyncio.run(run_tests())
