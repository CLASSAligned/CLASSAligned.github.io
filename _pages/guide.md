---
permalink: /guide/
title: "CLASS AlignED - Project Guide"
author_profile: true
redirect_from:
  - /CLASSALIGNED26/guide/
  - /CLASSALIGNED26/guide.html
---

**Bridging the gap between AI policy and classroom practice**

CLASS AlignED is an AI-powered system that helps educators align course design with university AI policies by transforming syllabi and policy documents into **actionable, policy-aware teaching recommendations**.

---

# Project documents (PDFs in `/src/`)

The following PDFs live **at the root** of the repository’s [`src/`](https://github.com/CLASSAligned/CLASSAligned.github.io/tree/main/src) folder (not every PDF nested under project subfolders there). Titles and descriptions are taken from each document’s metadata and text (abstract, syllabus header, policy summary, or tech-stack outline).

| Title | File | Description |
|:------|:-----|:------------|
| **CLASS AlignED Tech Stack** | [PDF](/src/CLASS%20AlignED%20Tech%20Stack.pdf) | Short architecture brief comparing a “university IT–friendly” stack: Zotero + Better BibTeX for reference ingestion; Python (pydantic, pandas) with PDF/text extraction; OpenAI embeddings with **Postgres + pgvector**; **LlamaIndex** for RAG; **FastAPI** + **Next.js** (or React) for the app, with notes on reranking and operating at faculty scale. |
| **Bridging Policy and Practice: The CLASS AlignED Framework for Responsible AI Integration in Higher Education** (7-page) | [PDF](/src/CLASS_AlignED_ADMI26-Paper.pdf) | ADMI26 research paper presenting the **CLASS AlignED** framework: faculty-centered, policy-aware design that combines automated syllabus analysis, learning-objective alignment, computational resource mapping, and institutional AI governance checks to produce actionable teaching recommendations, with emphasis on AI, HPC, and Science Gateways in undergraduate curricula. |
| **Bridging Policy and Practice: The CLASS AlignED Framework for Responsible AI Integration in Higher Education** (extended) | [PDF](/src/CLASS_AlignED_ADMI26-Paper%20(1).pdf) | Longer edition of the same paper (additional material beyond the 7-page version), covering the same framework, methodology, and contribution with more detail. |
| **MATA 621 — Applied Ordinary Differential Equations (Spring 2026)** | [PDF](/src/MATA%20621%20Applied%20Ordinary%20Dif%20Equations%20Spring%202026.pdf) | Tentative **3-credit online** syllabus: instructor Dr. Weizheng Gao; supplemental Zill & Cullen differential-equations text; **MATLAB** required; policies, schedule, and course requirements for the differential equations course. |
| **BIOL 443 (Section D3) — Principles of Immunology** | [PDF](/src/Principles%20of%20Immunology.pdf) | Course syllabus for the immunology survey: instructor Dr. Preety Panwar, credit hours, virtual contact expectations, and overview of course topics and policies. |
| **BIOL 443 (Section D3) — Principles of Immunology** (copy) | [PDF](/src/Principles%20of%20Immunology%20copy.pdf) | Same syllabus content as the file above (duplicate copy in `src/`). |
| **Artificial Intelligence Governance: UNC System Framework and ECSU Policies** | [PDF](/src/School%20AI%20Usage%20Policy%20for%20ECSU_UNC%20System.pdf) | Policy-oriented document summarizing how **generative AI** is governed under the **UNC System** and at **ECSU**: academic integrity, student conduct, syllabus-level rules, library and instructional guidance, and IT/data-security considerations. |
| **Artificial Intelligence Governance: UNC System Framework and ECSU Policies** (copy) | [PDF](/src/School%20AI%20Usage%20Policy%20for%20ECSU_UNC%20System%20(1).pdf) | Same policy summary as the row above (duplicate copy in `src/`). |

---

## Program source files (`src/`)

The table below describes **authored** program and configuration files under [`src/`](https://github.com/CLASSAligned/CLASSAligned.github.io/tree/main/src): the Streamlit demo app, Colab notebooks for the MVP pipeline, dependency pins, and GraphRAG workspace text configs. Large generated outputs (JSON under `processed/`, vector DB files, caches) are not listed.

| Path | Description |
|:-----|:------------|
| [`src/README.md`](https://github.com/CLASSAligned/CLASSAligned.github.io/blob/main/src/README.md) | Top-level project documentation: problem/solution overview, tech stack, how to run GraphRAG CLI and the Streamlit UI, and environment setup (`GEMINI_API_KEY`, virtualenv). |
| [`CLASS_ALIGNED_MVP_UI_DEMO/requirements.txt`](https://github.com/CLASSAligned/CLASSAligned.github.io/blob/main/src/CLASS_ALIGNED_MVP_UI_DEMO/requirements.txt) | Python dependencies for the UI demo: **Streamlit**, **pypdf**, **python-docx**, **python-dotenv**, **google-genai**. |
| [`CLASS_ALIGNED_MVP_UI_DEMO/app/streamlit_app.py`](https://github.com/CLASSAligned/CLASSAligned.github.io/blob/main/src/CLASS_ALIGNED_MVP_UI_DEMO/app/streamlit_app.py) | **Streamlit** entrypoint: file upload for syllabus (PDF/DOCX) and policy (PDF), “Run Analysis” action, and UI sections for course summary, learning outcomes, assessments, policies, AI recommendations, and GraphRAG-style insights (with helpers to format assessment/policy items). |
| [`CLASS_ALIGNED_MVP_UI_DEMO/app/pipeline.py`](https://github.com/CLASSAligned/CLASSAligned.github.io/blob/main/src/CLASS_ALIGNED_MVP_UI_DEMO/app/pipeline.py) | **Core processing pipeline**: saves uploads under `raw/`, extracts text from PDF/DOCX, builds chunks and JSON artifacts under `processed/`, calls **Gemini** for structured syllabus/policy extraction, runs **GraphRAG** via subprocess for contextual queries, and assembles results for the UI (paths are parameterized to a project root—defaults in-repo point at a Desktop copy; adjust for your machine). |
| [`CLASS_ALIGNED_MVP_UI_DEMO/app/config.py`](https://github.com/CLASSAligned/CLASSAligned.github.io/blob/main/src/CLASS_ALIGNED_MVP_UI_DEMO/app/config.py) | Shared **path constants** (`raw/`, `processed/`, GraphRAG workspace), default **Gemini** model name, and env loading—intended as a small config module for imports. |
| [`CLASS_ALIGNED_MVP_UI_DEMO/app/report_builder.py`](https://github.com/CLASSAligned/CLASSAligned.github.io/blob/main/src/CLASS_ALIGNED_MVP_UI_DEMO/app/report_builder.py) | Placeholder module for **report/export** building (currently empty; reserved for future formatted faculty reports). |
| [`CLASS_AlignED_MVP/code/Notebook_One.ipynb`](https://github.com/CLASSAligned/CLASSAligned.github.io/blob/main/src/CLASS_AlignED_MVP/code/Notebook_One.ipynb) | **Colab** notebook (NB1): mount Drive, install **pypdf** / **python-docx**, extract syllabus text, split into sections and chunks, write `processed/text/*.json`, `processed/chunks/*.jsonl`, and **`processed/manifest.json`** listing each document. |
| [`CLASS_AlignED_MVP/code/Notebook_Two.ipynb`](https://github.com/CLASSAligned/CLASSAligned.github.io/blob/main/src/CLASS_AlignED_MVP/code/Notebook_Two.ipynb) | **Colab** notebook (NB2): load manifest and chunks, define a **Gemini** JSON schema for course metadata, outcomes, assessments, policies, relations, and AI teaching recommendations with **chunk_id** evidence, then run extraction per syllabus into `processed/extracted/*_extracted.json`. |
| [`CLASS_AlignED_MVP/code/Notebook_Three.ipynb`](https://github.com/CLASSAligned/CLASSAligned.github.io/blob/main/src/CLASS_AlignED_MVP/code/Notebook_Three.ipynb) | **Colab** notebook (NB3): set **GraphRAG** workspace paths under `processed/graphrag_workspace`, run **`graphrag init`**, and prepare indexing/query workflows against the chunked syllabus data. |
| [`.../processed/graphrag_workspace/settings.yaml`](https://github.com/CLASSAligned/CLASSAligned.github.io/tree/main/src/CLASS_AlignED_MVP/processed/graphrag_workspace) | **GraphRAG** workspace configuration (present under both `CLASS_AlignED_MVP` and `CLASS_ALIGNED_MVP_UI_DEMO`): models, chunking, storage, and pipeline options used by `graphrag index` / `graphrag query`. Each project has its own copy next to its prompts and inputs. |
| [`.../processed/graphrag_workspace/prompts/*.txt`](https://github.com/CLASSAligned/CLASSAligned.github.io/tree/main/src/CLASS_AlignED_MVP/processed/graphrag_workspace/prompts) | **Prompt templates** for GraphRAG (e.g. local/basic/drift/global search, extract graph/claims, community reports, summarization). These text files steer how the graph and retrieval stages behave during indexing and querying. |

---

# Problem

As AI adoption grows in higher education, faculty face a major challenge:

- Universities provide **AI policies**, but
- Faculty lack **practical guidance** on how to apply them in real courses

This creates a **policy–practice gap** — policies exist, but instructors don't know how to implement them in assignments, assessments, or lesson planning.

---

# Solution

CLASS AlignED solves this by ingesting course syllabi and university AI policies, structuring and analyzing them using AI, and generating clear, policy-aligned recommendations for teaching. Instead of interpreting policy manually, faculty receive ready-to-use guidance.

---

# System Overview

## 1. Input

Upload your course syllabus (PDF/DOCX) and university AI policy.

## 2. Processing

Extract text, chunk content, and structure data using AI.

## 3. AI Recommendation Engine

Uses **Gemini (LLM)** to extract learning outcomes, assessments, and policies. Uses **GraphRAG** to connect syllabus, policy, and contextual knowledge to generate grounded recommendations.

## 4. Output

- Course summary
- Learning outcomes
- Assessment breakdown
- Policy interpretation
- AI-supported teaching recommendations

---

# Tech Stack

**Core AI:** Gemini API for structured extraction and reasoning; GraphRAG for knowledge graph and contextual querying.

**Backend:** Python with JSON/JSONL pipelines and subprocess-based GraphRAG integration.

**Document Processing:** pypdf for PDF parsing; python-docx for DOCX parsing.

**UI:** Streamlit for the interactive frontend demo.

---

# Projects

## CLASS\_AlignED\_MVP

The original backend system that processes syllabus and policy documents, chunks and extracts structured data, runs GraphRAG indexing and querying, and outputs JSON results, graph-based insights, and faculty-facing reports. It is CLI-based with end-to-end pipeline support and policy-aware AI recommendations.

## CLASS\_ALIGNED\_MVP\_UI\_DEMO

A user-facing application built on top of the MVP, adding a file upload interface, automatic file routing to `raw/syllabi` and `raw/policies`, integrated pipeline execution, and clean UI outputs including course summaries, learning outcomes, assessments, policies, AI recommendations, and GraphRAG insights. The goal is to make the system usable by non-technical faculty.

---

# How It Works

1. User uploads syllabus and policy
2. Files are saved to structured directories
3. Text is extracted and chunked
4. Gemini extracts structured course data
5. GraphRAG builds relationships and context
6. System generates recommendations, reports, and insights

---

# Key Innovation

CLASS AlignED doesn't just analyze documents — it transforms static policies into **actionable teaching strategies**.

---

# Impact

CLASS AlignED reduces faculty uncertainty around AI usage, embeds policy into real classroom workflows, and supports scalable adoption of AI in education. It is especially impactful for institutions with limited resources.

---

# Running the Project

## 1. Set Up Environment

```bash
python -m venv graphrag-env
source graphrag-env/bin/activate
pip install -r requirements.txt
```

## 2. Set API Key

Create a `.env` file:

<pre style="background-color: transparent;"><code>GEMINI_API_KEY=your_api_key_here</code></pre>

## 3. Run the Backend (Optional)

```bash
cd processed/graphrag_workspace
graphrag index --root .
graphrag query --root . --method local "Identify AI-supported teaching strategies"
```

## 4. Run the UI

```bash
cd ~/Desktop/CLASS_ALIGNED_MVP_UI_DEMO
streamlit run app/streamlit_app.py
```

---

# Using the UI

Upload your course syllabus (PDF or DOCX) and your university AI policy. The system will automatically save files to the correct directories, extract and chunk text, run Gemini extraction, and run a GraphRAG query. Results are displayed in the UI as a course summary, learning outcomes, assessments, policies, AI recommendations, and GraphRAG insights.

---

# Notes

- Ensure your `GEMINI_API_KEY` is valid and loaded
- Initialize the GraphRAG workspace before querying
- If GraphRAG errors occur, re-run `graphrag index --root .`

---

# Future Work

- Stronger policy–recommendation alignment
- Improved GraphRAG grounding with research datasets
- Better UI/UX for faculty workflows
- Integration with LMS platforms such as Blackboard and Canvas

---

# Example Use Case

An instructor uploads a syllabus and their university's AI policy. The system returns AI-supported assignment ideas, policy-compliant usage guidelines, and suggestions to improve engagement and learning outcomes.
