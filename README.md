# Project Altas

> Built to understand AI systems, not merely to use them.

## Repository Status

| Item | Status |
|---|---|
| Current Phase | Foundation |
| Current Focus | Tech Stack and Architecture |
| Next Goal | MVP Implementation |
| Implementation Status | Not Started |

## What is Altas?

Project Altas is a long-term AI engineering platform and learning laboratory. It is one continuously evolving codebase for studying how modern AI systems are designed, built, evaluated, and operated.

It is not simply:

- A chatbot
- A RAG demo
- A LangChain tutorial

Instead, Altas incrementally explores:

- LLM applications
- LangChain and LangGraph
- Retrieval-augmented generation
- Memory
- Tools
- Agents
- Model Context Protocol
- Evaluation
- Production engineering

Each capability is introduced through a focused milestone so that the concepts, design choices, and tradeoffs remain understandable as the platform grows.

## Why Project Altas?

The best way to understand AI engineering is to build real systems step by step. Altas turns that principle into a long-running engineering project: establish the foundations, introduce one major concept at a time, and examine how each addition changes the architecture.

The project also supports a long-term path toward becoming an AI Solution Architect—someone able to connect AI capabilities, software engineering, system design, evaluation, and operational concerns into coherent solutions.

## Project Philosophy

Project Altas favors understanding over speed.

Rather than assembling disconnected AI examples, every capability is introduced only after the necessary architectural foundations have been established.

The goal is not simply to build an AI platform, but to understand why each component exists, what problem it solves, and how it interacts with the rest of the system.

## Why Follow This Project?

Most repositories present finished code. Project Altas documents the path that produces it:

- Architectural thinking
- Engineering decisions
- Documentation
- Tradeoffs
- Implementation

The learning journey is intentionally public from the first commit onward. Readers can follow not only what the system becomes, but why it takes each step.

## Current Status

- [x] Foundation documentation complete
- [ ] Tech stack
- [ ] Architecture Decision Records
- [ ] MVP implementation
- [ ] Knowledge systems
- [ ] Memory
- [ ] Tools
- [ ] Agents
- [ ] MCP
- [ ] Evaluation
- [ ] Production readiness

Project planning and the initial documentation foundation are complete. Implementation has not started. The next work is to define the initial tech stack and architecture before beginning the MVP.

## Core Technologies

The technologies below describe the current direction. They are planned unless the repository shows them as implemented.

| Technology | Purpose |
|---|---|
| Python | Primary language for the platform |
| uv | Reproducible Python environments and dependency management |
| LangChain | LLM application components, prompts, retrieval, and tools |
| LangGraph | Stateful workflows and bounded agent execution |
| FastAPI | API boundary for later service-based capabilities |
| MCP | Standardized integration with tools, resources, and external systems |
| Docker | Reproducible application packaging and runtime environments |
| GitHub Actions | Automated testing, quality checks, and delivery workflows |

## Engineering Principles

- Learn by building.
- Understand concepts before depending on frameworks.
- Treat documentation as part of engineering.
- Establish architecture before optimizing it.
- Add complexity incrementally.
- Work through small, understandable milestones.
- Let Git capture history while documents explain decisions.

## Roadmap

1. Foundation
2. Knowledge Systems / RAG
3. Memory
4. Tools and Skills
5. Agents
6. MCP Integration
7. Evaluation
8. Production Readiness
9. Advanced Applications

```text
Foundation
    │
    ▼
Knowledge Systems / RAG
    │
    ▼
Memory
    │
    ▼
Tools and Skills
    │
    ▼
Agents
    │
    ▼
MCP Integration
    │
    ▼
Evaluation
    │
    ▼
Production Readiness
    │
    ▼
Advanced Applications
```

See [Milestones](docs/00-product/01-Milestones.md) for the complete learning and product evolution path.

## Documentation

- [Project Charter](docs/00-product/00-Project%20Charter.md) — Defines the mission, scope, and guiding principles.
- [Milestones](docs/00-product/01-Milestones.md) — Defines the learning-driven roadmap and technology progression.
- [Minimum Viable Product](docs/00-product/02-MVP.md) — Defines the boundaries and success criteria for the first working release.
- [Documentation Standards](docs/99-meta/00-Documentation%20Standards.md) — Defines how official project knowledge is created and maintained.

## Planned MVP

The first working release is intentionally limited to a local-first CLI-based LLM chat application. It will establish project structure, configuration, logging, LLM provider abstraction, prompt management, and a simple user interaction loop.

RAG, agents, MCP, and production deployment are deliberately excluded from the MVP. They belong to later milestones, where each can be learned and introduced with the attention it deserves.

## Project Structure

```text
Altas/
├── .obsidian/
├── docs/
│   ├── 00-product/
│   ├── 01-architecture/
│   └── 99-meta/
├── notes/
├── .gitignore
└── README.md
```

- `.obsidian/` contains local knowledge-base configuration.
- `docs/` contains reviewed, official project documentation.
- `notes/` contains working notes, research, and learning material that has not become stable project knowledge.
- `README.md` is the public entry point to the repository.

Implementation directories will be added when the MVP begins.

## Getting Started

Implementation has not yet begun. The project is currently in the planning and architecture phase.

Setup instructions will be added once the MVP implementation starts. Until then, begin with the [Project Charter](docs/00-product/00-Project%20Charter.md), then review the [Milestones](docs/00-product/01-Milestones.md) and [MVP](docs/00-product/02-MVP.md).

## License

License information will be added before the first public release.

## Follow the Journey

Project Altas is intentionally being developed in public. Every milestone, architecture decision, and implementation step will be documented as the project evolves.

Follow the engineering journey—not only the finished software.
