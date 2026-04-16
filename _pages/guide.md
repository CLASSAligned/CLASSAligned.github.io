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
