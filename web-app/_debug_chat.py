"""Debug Ollama chat - capture raw response."""
import os, sys, json, time
os.environ["PORT"] = "8001"
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import multiprocessing, uvicorn, httpx, asyncio

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

async def test():
    base = "http://127.0.0.1:8001"
    
    for test_num, msg in enumerate([
        "Say hello in 5 words. No tools.",
        "What projects do I have? Use get_project_list."
    ], 1):
        print(f"\n{'='*60}")
        print(f"TEST {test_num}: {msg[:50]}...")
        print(f"{'='*60}")
        async with httpx.AsyncClient(timeout=300) as c:
            try:
                r = await c.post(f"{base}/api/chat", json={
                    "session_id": f"debug-t{test_num}",
                    "message": msg,
                    "project": None
                }, timeout=300)
                d = r.json()
                print(f"  Status: {r.status_code}")
                engine = d.get('engine','?')
                print(f"  Engine: {repr(engine)}")
                resp = d.get('response','')
                if resp:
                    # Strip emoji/unicode for terminal
                    safe = resp.encode('ascii', 'replace').decode('ascii')
                    print(f"  Response: {safe[:500]}")
                else:
                    print(f"  Response: (empty)")
                tools = d.get('tools_used',[])
                if tools:
                    print(f"  Tools: {len(tools)} used")
                    for t in tools:
                        safe_args = json.dumps(t.get('args',{})).encode('ascii','replace').decode('ascii')
                        print(f"    - {t['tool']}({safe_args}) -> {t.get('status','?')}")
                else:
                    print(f"  Tools: none")
                print(f"  Raw response keys: {list(d.keys())}")
            except Exception as e:
                print(f"  ERROR: {e}")
    
    print("\nDONE")

if __name__ == "__main__":
    print("Starting server...")
    start()
    try:
        asyncio.run(test())
    finally:
        stop()
