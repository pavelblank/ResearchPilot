import httpx, asyncio

async def main():
    async with httpx.AsyncClient(timeout=30.0) as c:
        tests = [
            ("OpenAlex", {"sources": "openalex", "year_from": "", "year_to": ""}),
            ("OpenAlex + year", {"sources": "openalex", "year_from": "2022", "year_to": "2024"}),
            ("Crossref", {"sources": "crossref", "year_from": "", "year_to": ""}),
            ("Crossref + year", {"sources": "crossref", "year_from": "2022", "year_to": "2024"}),
            ("Semantic Scholar", {"sources": "semantic", "year_from": "", "year_to": ""}),
            ("Semantic + year", {"sources": "semantic", "year_from": "2022", "year_to": "2024"}),
            ("PubMed", {"sources": "pubmed", "year_from": "", "year_to": ""}),
            ("PubMed + year", {"sources": "pubmed", "year_from": "2022", "year_to": "2024"}),
            ("All sources", {"sources": "openalex,crossref,semantic,pubmed", "year_from": "", "year_to": ""}),
            ("All + year", {"sources": "openalex,crossref,semantic,pubmed", "year_from": "2022", "year_to": "2024"}),
        ]
        
        for name, params in tests:
            p = {"q": "cybersecurity higher education", "max_results": "5", "sort": "relevance"}
            p.update(params)
            try:
                r = await c.get("http://127.0.0.1:8000/api/research/search", params=p)
                d = r.json()
                total = d.get("total", 0)
                errors = d.get("source_errors", {})
                print(f"[{total:2d}] {name:25s} errors={errors}")
            except Exception as e:
                print(f"[ERR] {name:25s} exception={e}")

asyncio.run(main())
