<link rel="stylesheet" type="text/css" href="docs/custom.css">
<div align="center">
  <a
href="https://github.com/statikfintechllc/AscendAI/blob/master/About Us/LICENSE.md">
    <img src="https://img.shields.io/badge/FAIR%20USE-black?style=for-the-badge&logo=dragon&logoColor=gold" alt="Fair Use License"/>
  </a>
  <a href="https://github.com/statikfintechllc/AscendAI/blob/master/About Us/LICENSE.md">
    <img src="https://img.shields.io/badge/GREMLINGPT%20v1.0-darkred?style=for-the-badge&logo=dragon&logoColor=gold" alt="GremlinGPT License"/>
  </a>
</div>
<div align="center">
  <a
href="https://github.com/statikfintechllc/AscendAI/blob/master/About Us/WHY_GREMLINGPT.md">
    <img src="https://img.shields.io/badge/Why-black?style=for-the-badge&logo=dragon&logoColor=gold" alt="Why"/>
  </a>
  <a href="https://github.com/statikfintechllc/AscendAI/blob/master/About Us/WHY_GREMLINGPT.md">
    <img src="https://img.shields.io/badge/GremlinGPT-darkred?style=for-the-badge&logo=dragon&logoColor=gold" alt="GremlinGPT"/>
  </a>
</div>

<h1 align="center">GremlinGPT: The Real Autonomous Agent v1.0.3</h1>

<div align="center">
  <a href="https://github.com/statikfintechllc/AscendAI/blob/master/GremlinGPT">
    <img src="https://img.shields.io/badge/build-v1.0.3-darkred?labelColor=black" alt="Build Status"/>
  </a>
  <a href="https://github.com/statikfintechllc/AscendAI/blob/master/About%20Us/FOUNDER_LOG.md">
    <img src="https://img.shields.io/badge/Founder's%20Log-Manifesto-darkred?labelColor=black" alt="Founder's Log"/>
  </a>
  <br/>
  <a href="https://github.com/statikfintechllc">
    <img src="https://img.shields.io/badge/contributors-2-darkred?labelColor=black" alt="Contributors"/>
  </a>
  <a href="https://github.com/statikfintechllc/AscendAI/blob/master/About%20Us/FOUNDER_STATEMENT.md">
    <img src="https://img.shields.io/badge/Founder's%20Log-Statement-darkred?labelColor=black" alt="Founder's Log"/>
  </a>
</div>

---

<h1 align="center">AscendAI Traffic</h1>
<h1 align="center">
	
  <a href="https://raw.githubusercontent.com/statikfintechllc/AscendAI/main/docs/traffic_graph.png">
    <img src="https://raw.githubusercontent.com/statikfintechllc/AscendAI/main/docs/traffic_graph.png" alt="Traffic Graph" />
  </a>
</h1>

---

## Table of Contents

- [Founder's Log & Manifesto](#founders-log--manifesto)
- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [System Components](#system-components)
- [Installation](#installation)
- [Running the System](#running-the-system)
- [Remote Access using ngrok](#remote-access-using-ngrok)
- [API Endpoints](#api-endpoints)
- [Recovery & Snapshots](#recovery--snapshots)
- [Troubleshooting](#troubleshooting)
- [System Infrastructure](#system-infrastructure)
- [License](#license)

---

## Founder's Log & Manifesto

> I built an AI system that builds itself.  
> Not in a lab.  
> Not at a venture-backed startup.  
> Not on fiber internet with a dev team holding my hand...

Read the [FOUNDER_LOG.md](https://github.com/statikfintechllc/AscendAI/blob/master/About%20Us/FOUNDER_LOG.md) and the [FOUNDER_STATEMENT.md](https://github.com/statikfintechllc/AscendAI/blob/master/About%20Us/FOUNDER_STATEMENT.md) for the full journey and philosophy.

---

## Overview

**GremlinGPT** is a fully local, modular, self-evolving AI agent platform—**no cloud**, **no external APIs**, no hidden data leaks.

- Autonomous FSM-driven agent loop
- Self-wiring NLP/memory stack (Chroma/FAISS)
- DOM/web/stock scraper, persistent trading signals, recursive self-training
- Bulletproof, production-grade, **red/black/gold/silver-themed** PWA dashboard for chat, tasks, memory, and trading

---

## Features

- **Zero cloud dependence**: runs 100% offline and local
- **Persistent, auto-recovering agent core**
- **State-of-the-art PWA dashboard**: mobile + desktop, instant install, works offline
- **Floating chat (always-on), tabbed navigation** (Tasks / Memory / Trading)
- **Self-training and auto-mutation**: logs errors, auto-patches, and retrains
- **Signal/ticker scanner**: EMA, VWAP, breakout, penny stock focus
- **Vector memory with UMAP, metadata, tagging**
- **Remote access with ngrok for secure AI on the go**
- **Auto-saving, crash recovery, and live snapshotting**

---

## Architecture

- **Backend:** Python (Flask/FastAPI), persistent vector DBs, FSM agent loop
- **Frontend:** Modern PWA (Bootstrap, vanilla JS), custom dark theme, tabbed UI, floating chat
- **Memory:** Chroma, FAISS, SentenceTransformer, full vector store, auto-index
- **Scraper:** Playwright, BeautifulSoup, async router, DOM/stock/ticker feeds
- **Trading Core:** Real-time signal inference, estimator, audit/history
- **Self-training:** Log watcher, mutation engine, agent self-healing
- **All panels and actions call live REST endpoints—no stubs, no nulls**

---

## System Components

- **backend/**: API router, task/memory planners, logs, and snapshots
- **agent_core/**: Task queue, FSM/agent logic, tool dispatcher
- **nlp_engine/**: Tokenizer, transformer, parser, mutation diff
- **memory/**: Chroma/FAISS vector DB, metadata, embeddings
- **scraper/**: DOM navigator, Playwright, async router
- **self_training/**: Watchdog, feedback ingestion, retrainer
- **trading_core/**: Stock scanner, signal/rule engine, estimator
- **frontend/**: PWA dashboard (chat, tasks, memory, trading)

---

## Installation

**1. Clone the repo**

```bash
git clone https://github.com/statikfintechllc/AscendAI.git
cd AscendAI/AscendNet/GremlinGPT
```

**2. Install Conda environments**

```bash
cd conda_envs && chmod +x create_envs.sh && ./create_envs.sh
```

or

```bash
cd .. && chmod +x install.sh && ./install.sh
```

**3. Bootstrap NLP models (one time)**

```bash
conda activate gremlin-nlp
python -c "from transformers import AutoTokenizer, AutoModel; AutoTokenizer.from_pretrained('bert-base-uncased'); AutoModel.from_pretrained('bert-base-uncased')"
python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"
```

⸻

## Running the System

```bash
cd run
chmod +x start_all.sh
./start_all.sh
```

- Backend server launches (Flask or FastAPI, port 5000 or 5050)
- FSM agent loop, task queue, memory, scraper all start
- **Dashboard ready at:** http://localhost:5000/ or http://localhost:5050/

⸻

## Remote Access using ngrok

- **To securely access GremlinGPT dashboard from anywhere:**

```bash
ngrok http 5000
```

or

```bash
ngrok http 5050
```

- Use the HTTPS URL provided by ngrok in your browser or mobile
- Full dashboard, all agent controls, remote chat and signal monitoring

⸻

## API Endpoints

- All dashboard features are live-wired to these REST endpoints:

Endpoint
Description
/api/chat
Chat with GremlinGPT agent
/api/agent/tasks
Task queue (view/manage/inject)
/api/memory/graph
Visualize memory embeddings
/api/trading/signals
Real-time penny stock signals

*Extend as you add more features (FSM control, scraping, estimator, etc.)*

⸻

## Recovery & Snapshots

- **Auto-saves:**
- Agent state, task queue, memory embeddings

**Key locations:**
- run/checkpoints/state_snapshot.json (full system snapshot)
- 
- run/checkpoints/task_queue.json (queue state)

**Recovery:**
- On crash/reboot, system auto-restores FSM, queue, and memory

**Manual monitoring:**

```bash
tail -f run/logs/runtime.log
```

⸻

## Troubleshooting

- Port conflict? Change in config.yaml or stop existing service
- Scraper fails? Set headless=False in playwright_handler.py and retry
- No memory? Verify embedder paths and Chroma/FAISS setup
- Training loop not updating? Run retrainer manually or inspect watchdog logs

⸻

## System Infrastructure

**Docs:**
*See [docs](https://github.com/statikfintechllc/AscendAI/blob/master/GremlinGPT/docs) for:*

- System architecture (system_overview.md)
- Module tree (full_structure_tree.txt)
- Agent logic (fsm_architecture.md)
- Memory/embeddings (memory_pipeline.md)
- Trading rules/signals (trading_signals.md)
- Self-training (self_training.md)
- Remote ops (ngrok_integration.md)
- Daemon/service setup (gremlin.service.md)
- Automated shell scripting (automated_shell.md)

**Live system trace:**

```bash
python run/module_tracer.py
```

⸻

## License

<div align="center">
  <a href="https://github.com/statikfintechllc/AscendAI/blob/master/About Us/LICENSE.md">
    <img src="https://img.shields.io/badge/FAIR%20USE-black?style=for-the-badge&logo=dragon&logoColor=gold" alt="Fair Use License"/>
  </a>
  <a href="https://github.com/statikfintechllc/AscendAI/blob/master/About Us/LICENSE.md">
    <img src="https://img.shields.io/badge/GREMLINGPT%20v1.0.3-darkred?style=for-the-badge&logo=dragon&logoColor=gold" alt="GremlinGPT License"/>
  </a>
</div>

FAIR USE for research, non-commercial, and education.
Contact for commercial/enterprise licensing.
© 2025 StatikFintechLLC / AscendAI Project.

