"""Build an offline vocabulary graph from research.md; Python standard library only."""
from pathlib import Path
import hashlib
import html
import json
import re

ROOT = Path(__file__).resolve().parent
REPORT = ROOT / "research.md"
TERMS = {
    "Generative AI (GenAI)": [r"generative AI", r"GenAI"],
    "Large language model (LLM)": [r"large language models?", r"LLMs?"],
    "Prompt": [r"prompts?"],
    "Token": [r"tokens?"],
    "Context window": [r"context windows?"],
    "Hallucination": [r"hallucinations?"],
    "Retrieval-augmented generation (RAG)": [r"retrieval-augmented generation", r"RAG"],
    "Retrieval": [r"retrieval", r"retriev(?:e|es|ed|ing)"],
    "Chunking": [r"chunking"],
    "Embedding": [r"embeddings?"],
    "Vector database": [r"vector databases?"],
    "Grounding": [r"grounding"],
    "AI agent": [r"AI agents?"],
    "Tool calling": [r"tool calling"],
    "Application programming interface (API)": [r"application programming interfaces?", r"APIs?"],
    "Multimodal": [r"multimodal"],
    "Prompt injection": [r"prompt injection"],
    "Human-in-the-loop": [r"human-in-the-loop"],
    "Evaluation": [r"evaluation"],
    "Latency": [r"latency"],
}

# AI-assisted semantic annotations, not outputs of a trained classifier.
# Keys identify a case and its body paragraph (1 or 2). Quotes must be exact.
# An annotation contributes to I only when that paragraph has no explicit alias.
IMPLICIT = {
    "Generative AI (GenAI)": {
        "1.1": "propose an implementation", "1.2": "insecure code",
        "2.1": "receive a synthesized answer", "2.2": "produce a confident error",
        "3.1": "generate a reply", "3.2": "invented refund policies",
        "4.1": "produce concept art", "4.2": "a generated asset",
        "5.1": "produce a summary", "5.2": "inventing a deadline",
    },
    "Large language model (LLM)": {"1.2": "hallucination of nonexistent APIs", "2.2": "before private content reaches the model", "3.1": "generate a reply using approved help articles", "3.2": "invented refund policies", "5.2": "long conversations that exceed a context window"},
    "Prompt": {"2.1": "ask a question about internal procedures", "3.1": "a customer's question"},
    "Hallucination": {"2.2": "produce a confident error", "5.2": "inventing a deadline"},
    "Grounding": {"1.1": "relevant source code", "2.1": "with references", "3.1": "using approved help articles", "5.1": "attach evidence or timestamps", "5.2": "compare summaries with the recording"},
    "Tool calling": {"1.1": "call tools to inspect files and run tests", "3.1": "use an API to retrieve order information", "5.2": "tasks are sent to other systems through an API"},
    "Human-in-the-loop": {"1.1": "reviewer effort", "2.2": "Citations must be checked", "4.1": "drafts accepted by reviewers", "5.1": "after participants review the notes"},
    "Evaluation": {"1.1": "Useful measures include", "1.2": "run appropriate tests", "2.1": "A useful pilot measures", "3.1": "Success should be measured", "4.1": "Useful measures include", "5.1": "A pilot can measure"},
}


def main():
    source = REPORT.read_text(encoding="utf-8")
    sections = re.split(r"(?=^## [1-5]\. )", source, flags=re.M)[1:]
    cases = []
    for number, section in enumerate(sections, 1):
        title = section.splitlines()[0].removeprefix("## ")
        body = section.split("Existing implementations:")[0]
        paragraphs = [p.strip() for p in body.split("\n\n")[1:] if p.strip()]
        if len(paragraphs) != 2:
            raise ValueError(f"Expected 2 body paragraphs in case {number}")
        cases.append({"id": str(number), "title": title, "paragraphs": paragraphs})
    if len(cases) != 5:
        raise ValueError("Expected 5 cases")
    paragraphs = {f"{c['id']}.{i}": p for c in cases for i, p in enumerate(c["paragraphs"], 1)}
    records = []
    for term, aliases in TERMS.items():
        pattern = re.compile(r"(?<!\w)(?:" + "|".join(aliases) + r")(?!\w)", re.I)
        for pid, paragraph in paragraphs.items():
            hits = [m.group() for m in pattern.finditer(paragraph)]
            quote = IMPLICIT.get(term, {}).get(pid)
            if quote and quote not in paragraph:
                raise ValueError(f"Evidence not found: {term}, {pid}: {quote}")
            records.append({"term": term, "paragraph": pid, "case": pid.split('.')[0], "explicit_occurrences": len(hits), "explicit_matches": hits, "explicit": int(bool(hits)), "implicit": int(bool(quote) and not hits), "implicit_evidence": quote if quote and not hits else None})
    totals = lambda term, case=None: tuple(sum(r[k] for r in records if r["term"] == term and (case is None or r["case"] == case)) for k in ("explicit", "implicit"))
    data = {"report_sha256": hashlib.sha256(REPORT.read_bytes()).hexdigest(), "scope": "Only the two body paragraphs of each of the five cases; headings, implementation lists, introduction, and conclusions excluded.", "method": "E = paragraphs containing a literal alias (case-insensitive word boundaries); I = additional paragraphs with a documented semantic annotation and no literal alias. Counts have the same unit: paragraphs. I is an AI-assisted interpretation, not an objective word count. Unannotated implicit uses may be missed.", "aliases": TERMS, "cases": cases, "records": records}
    (ROOT / "graph-data.json").write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    esc = html.escape
    parts = ['<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Vocabulary usage graph</title><style>body{font:16px/1.6 system-ui,sans-serif;margin:0;color:#172235;background:#f6f8fb}main{max-width:1080px;margin:auto;padding:30px 20px}h1{font-size:30px;line-height:1.2}h2{font-size:22px}p{max-width:90ch}table{border-collapse:collapse;width:100%;font-size:14px;background:white}th,td{text-align:left;padding:9px;border-bottom:1px solid #dce3eb}th{background:#e9eef6}td:not(:first-child){white-space:nowrap;font-variant-numeric:tabular-nums}.overflow{overflow:auto}.graph{min-width:720px;width:100%;height:auto;background:white}details{margin:20px 0}summary{font-weight:600;cursor:pointer}.legend{padding:12px 0}.e{color:#225fb8}.i{color:#a34814}code{overflow-wrap:anywhere;font-size:13px}@media print{body{background:white}main{padding:0}.overflow{overflow:visible}details{display:block}summary{break-after:avoid}}</style><main><h1>Vocabulary → research cases</h1><p>Aliaskar Avgust · EPAM introductory assignment · 9 November 2026</p><h2>Counting method</h2>']
    parts += [f'<p>{esc(data["scope"])}</p>',f'<p>{esc(data["method"])}</p>', '<p>Aliases include plurals and abbreviations listed in the data file. Concepts are counted independently: a paragraph can contain both “prompt” and “prompt injection”. RAG does not imply use of a vector database; no such implicit link is assumed.</p>', '<div class="legend"><strong class="e">E: explicit paragraphs</strong> · <strong class="i">I: implicit paragraphs</strong>. At most 2 per case and 10 overall for each term; E and I are disjoint for a given term and paragraph.</div><h2>All terms and cases</h2><div class="overflow"><table><thead><tr><th>Vocabulary term</th>']
    parts += [f'<th>Case {c["id"]}<br>E / I</th>' for c in cases] + ['<th>Total<br>E / I</th></tr></thead><tbody>']
    for term in TERMS:
        parts.append(f'<tr><th>{esc(term)}</th>')
        for case in cases:
            e,i=totals(term,case['id']); parts.append(f'<td>{e} / {i}</td>')
        e,i=totals(term); parts.append(f'<td><strong>{e} / {i}</strong></td></tr>')
    parts.append('</tbody></table></div><h2>Relationship graphs</h2><p>Each edge connects a research case with a vocabulary term used in its body. Blue solid edges show explicit use; orange dashed edges show implicit use. Each term displays both frequencies, including zero.</p>')
    for case in cases:
        active = [(term, *totals(term,case['id'])) for term in TERMS if sum(totals(term,case['id']))]
        height=max(230,len(active)*48+40); center=height/2
        parts.append(f'<section><h3>{esc(case["title"])}</h3><div class="overflow"><svg class="graph" viewBox="0 0 1020 {height}" role="img" aria-label="Vocabulary relationship graph for {esc(case["title"])}"><title>{esc(case["title"])}: explicit and implicit paragraph frequencies</title>')
        for idx,(term,e,i) in enumerate(active):
            y=36+idx*48
            if e: parts.append(f'<path d="M 196 {center-3} C 300 {center-3},300 {y-3},410 {y-3}" stroke="#225fb8" stroke-width="{1+e}" fill="none" opacity=".6"/>')
            if i: parts.append(f'<path d="M 196 {center+3} C 300 {center+3},300 {y+3},410 {y+3}" stroke="#a34814" stroke-width="{1+i}" stroke-dasharray="7 5" fill="none" opacity=".7"/>')
            parts.append(f'<circle cx="414" cy="{y}" r="5" fill="#172235"/><text x="430" y="{y+5}" font-size="16" fill="#172235">{esc(term)}</text><text x="900" y="{y+5}" font-size="16" fill="#172235">E {e} / I {i}</text>')
        parts.append(f'<rect x="15" y="{center-28}" width="181" height="56" rx="9" fill="#e9eef6"/><text x="105" y="{center+6}" text-anchor="middle" font-size="18" fill="#172235">Research case {case["id"]}</text></svg></div></section>')
    parts.append('<h2>Implicit-use evidence</h2><p>Paragraph IDs use case.paragraph, for example 2.1 = the first body paragraph of case 2. These annotations were prepared with AI assistance. They are interpretive judgments and can be reviewed or changed.</p><div class="overflow"><table><tr><th>Term</th><th>Paragraph</th><th>Exact evidence from research.md</th></tr>')
    for r in records:
        if r['implicit']: parts.append(f'<tr><td>{esc(r["term"])}</td><td>{r["paragraph"]}</td><td>{esc(r["implicit_evidence"])}</td></tr>')
    parts += ['</table></div><h2>Reproducibility</h2><p>Run <code>python3 build_graph.py</code> from this directory to regenerate this page and graph-data.json. No external packages or network connection are required. The data file also includes literal match counts and aliases.</p>',f'<p>Report SHA-256: <code>{data["report_sha256"]}</code></p></main></html>']
    (ROOT / "vocabulary-graph.html").write_text("\n".join(parts)+"\n",encoding="utf-8")
    print(f"Generated {len(cases)} case graphs for {len(TERMS)} terms.")
    print(f"Explicit term-paragraph pairs: {sum(r['explicit'] for r in records)}; implicit: {sum(r['implicit'] for r in records)}.")


if __name__ == '__main__':
    main()
