"""Comprehensive system test: tools, chat, plugins, auto-start, file access."""
import os, sys, json, time, signal
os.environ["PORT"] = "8001"
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import multiprocessing, uvicorn, httpx

SERVER_PROC = None

def run_server():
    os.environ["PORT"] = "8001"
    uvicorn.run("main:app", host="127.0.0.1", port=8001, log_level="error")

def start():
    global SERVER_PROC
    SERVER_PROC = multiprocessing.Process(target=run_server, daemon=True)
    SERVER_PROC.start()
    time.sleep(5)

def stop():
    if SERVER_PROC:
        SERVER_PROC.terminate()
        SERVER_PROC.join()

def test(name, ok, detail=""):
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {name}" + (f" - {detail}" if detail else ""))

async def run_tests():
    print("=" * 60)
    print("ERA SYSTEM - COMPREHENSIVE TEST SUITE")
    print("=" * 60)

    base = "http://127.0.0.1:8001"
    passed = 0
    failed = 0

    async def check(name, http_method, url, expected_status=200, json_body=None, expect_key=None):
        nonlocal passed, failed
        try:
            async with httpx.AsyncClient(timeout=30) as c:
                if http_method == "GET":
                    r = await c.get(url)
                elif http_method == "POST":
                    r = await c.post(url, json=json_body or {})
                elif http_method == "DELETE":
                    r = await c.delete(url)
                ok = r.status_code == expected_status
                if ok and expect_key:
                    data = r.json()
                    ok = expect_key in data
                test(name, ok, f"HTTP {r.status_code}")
                if ok:
                    passed += 1
                else:
                    failed += 1
                    try:
                        print(f"    Response: {r.text[:200]}")
                    except:
                        pass
                return r.json() if ok else None
        except Exception as e:
            test(name, False, str(e)[:80])
            failed += 1
            return None

    # ─── 1. STATUS ───
    print("\n1. SYSTEM STATUS")
    data = await check("GET /api/status", "GET", f"{base}/api/status", expect_key="active")
    if data:
        test("  Active engine shown", data["active"] != "", data["active"])

    # ─── 2. SETTINGS ───
    print("\n2. SETTINGS")
    data = await check("GET /api/settings", "GET", f"{base}/api/settings", expect_key="ai_engines")
    if data:
        enabled = [e for e in data["ai_engines"] if e.get("enabled")]
        test(f"  {len(enabled)} engine(s) enabled", len(enabled) > 0)

    # ─── 3. TOOLS ───
    print("\n3. DIRECT TOOLS EXECUTION")
    import main as m
    r = await m.execute_tool("get_project_list", {})
    test("get_project_list", "projects" in r, f"{len(r.get('projects',[]))} projects")

    r = await m.execute_tool("read_system_core", {"filename": "SYSTEM-PROTOCOLS.md"})
    test("read_system_core", "content" in r, f"{len(r.get('content',''))} chars")

    r = await m.execute_tool("search_files", {"query": "ERA", "max_results": 3})
    test("search_files", r.get("count", 0) > 0, f"{r.get('count',0)} results")

    r = await m.execute_tool("list_directory", {"path": "01-PROJECTS"})
    test("list_directory", "items" in r, f"{r.get('count',0)} items")

    r = await m.execute_tool("get_system_structure", {})
    test("get_system_structure", "structure" in r)

    r = await m.execute_tool("read_knowledge_base", {})
    test("read_knowledge_base", "content" in r, f"{len(r.get('content',''))} chars")

    # ─── 4. CHAT ───
    print("\n4. AI CHAT (Ollama)")
    data = await check("New session", "POST", f"{base}/api/chat/new", expect_key="session_id")
    if data:
        sid = data["session_id"]
        test(f"  Session: {sid}", True)
        print("  Sending: 'What projects do I have? Use get_project_list.'")
        try:
            async with httpx.AsyncClient(timeout=300) as c:
                r = await c.post(f"{base}/api/chat", json={
                    "session_id": sid,
                    "message": "What projects do I have? Use get_project_list.",
                    "project": None
                }, timeout=300)
                d = r.json()
                test("/api/chat response", "response" in d, f"Engine: {d.get('engine','?')}")
                if d.get("response"):
                    resp_preview = d["response"][:300]
                    test("  Has content", len(d["response"]) > 20, resp_preview)
                if d.get("tools_used"):
                    test(f"  Tools used: {len(d['tools_used'])}", True)
                    for t in d["tools_used"]:
                        test(f"    {t['tool']}", t['status'] == 'ok')
        except Exception as e:
            test("/api/chat POST", False, str(e)[:100])

    # ─── 5. TOOLS LIST ───
    print("\n5. TOOLS LIST")
    await check("GET /api/tools", "GET", f"{base}/api/tools", expect_key="tools")

    # ─── 6. PROJECTS ───
    print("\n6. PROJECTS")
    data = await check("GET /api/projects", "GET", f"{base}/api/projects")
    if data:
        test(f"  {len(data)} project(s)", len(data) > 0)

    # ─── 7. LIBRARY ───
    print("\n7. LIBRARY")
    await check("GET /api/library", "GET", f"{base}/api/library")

    # ─── 8. EXTRACTIONS ───
    print("\n8. EXTRACTIONS")
    await check("GET /api/extractions", "GET", f"{base}/api/extractions")

    # ─── 9. KNOWLEDGE BASE ───
    print("\n9. KNOWLEDGE BASE")
    await check("GET /api/knowledge-base", "GET", f"{base}/api/knowledge-base", expect_key="content")

    # ─── 10. PLUGINS ───
    print("\n10. PLUGINS")
    data = await check("GET /api/plugins", "GET", f"{base}/api/plugins", expect_key="plugins")
    if data:
        test(f"  {len(data['plugins'])} plugins", len(data['plugins']) > 0)
        for p in data['plugins']:
            test(f"  {p['icon']} {p['name']}", True, f"connected={p['connected']}")

    # ─── 11. AUTO-START ───
    print("\n11. AUTO-START")
    await check("GET /api/auto-start", "GET", f"{base}/api/auto-start", expect_key="enabled")

    # ─── SUMMARY ───
    print(f"\n{'=' * 60}")
    total = passed + failed
    print(f"RESULTS: {passed}/{total} passed, {failed}/{total} failed")
    if failed == 0:
        print("ALL TESTS PASSED")
    else:
        print(f"SOME TESTS FAILED")
    print(f"{'=' * 60}")
    return failed == 0

if __name__ == "__main__":
    print("Starting server...")
    start()
    try:
        import asyncio
        success = asyncio.run(run_tests())
    finally:
        stop()
    sys.exit(0 if success else 1)
