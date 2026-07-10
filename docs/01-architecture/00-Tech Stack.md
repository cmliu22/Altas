# Tech Stack

## 1. Purpose

This document defines the technology direction for Project Altas. It identifies the initial tools required for the MVP, explains why each technology belongs in the platform, and clarifies when planned technologies should be introduced.

The Tech Stack is a living architecture document. It will evolve as the platform grows, learning priorities change, and architectural decisions become stable.

## 2. Technology Selection Philosophy

- Technologies serve learning and architecture, not the other way around.
- Concepts should be understood before frameworks are used to implement them.
- The Milestone 1 stack should remain minimal and focused on the MVP.
- A technology should be introduced only when it solves a real engineering or learning problem.
- Provider-specific logic should be isolated behind Altas-owned abstractions.
- The stack should remain modular and replaceable where practical.

Project Altas should avoid adopting technologies solely because they are popular or commonly associated with AI applications. Each addition should have a clear responsibility and an appropriate place in the milestone path.

## 3. Selection Criteria

Technology choices should be evaluated using the following criteria:

- Educational value
- Production relevance
- Documentation quality
- Community and ecosystem maturity
- Modularity
- Local development friendliness
- Long-term maintainability
- Low unnecessary complexity

No single criterion determines a decision. The appropriate choice should balance the needs of the active milestone with the long-term architecture direction.

## 4. Milestone 1 Initial Stack

Because implementation has not started, the following technologies are planned for the MVP. They become Active when they are introduced into the working codebase.

| Area | Technology | Purpose | Status | Notes |
|---|---|---|---|---|
| Runtime target | Local-first CLI | Provide the simplest usable interface and execution environment | Planned for MVP | Avoids premature web and deployment concerns |
| Primary language | Python | Implement the platform and access the AI engineering ecosystem | Planned for MVP | Primary language for the initial platform |
| Package and environment management | uv | Manage Python versions, dependencies, and reproducible environments | Planned for MVP | Supports a fast, unified local workflow |
| AI framework | LangChain Core | Provide focused abstractions for models, prompts, messages, and runnables | Planned for MVP | Use only the core capabilities required |
| Pipeline composition | LCEL | Compose explicit and inspectable LLM application pipelines | Planned for MVP | Keeps the initial request flow understandable |
| CLI framework | Typer | Provide a typed and maintainable command-line interface | Planned for MVP | Appropriate for the local-first interaction model |
| Configuration | Pydantic Settings | Load and validate application configuration | Planned for MVP | Separates configuration from application logic |
| Secrets | Environment variables | Supply provider credentials without hardcoding sensitive values | Planned for MVP | Local secret files must not be committed |
| Logging | Python standard logging | Make the basic application flow observable | Planned for MVP | Start with the standard library before adding observability platforms |
| Testing | pytest | Verify foundational components and boundaries | Planned for MVP | Initial focus is unit testing |
| Linting and formatting | Ruff | Provide fast, consistent Python linting and formatting | Planned for MVP | Keeps the development toolchain compact |
| Documentation | Markdown, Obsidian, markdownlint | Maintain portable documentation with local knowledge navigation and style checks | Active | Documentation foundation already exists |
| Version control | Git | Record project history and support incremental development | Active | Already used by the repository |
| Remote repository | GitHub | Host the project and support public collaboration | Active | Repository front door and future automation platform |
| IDE | VS Code | Provide the primary development and documentation environment | Active | Supports Python, Markdown, and repository tooling |

## 5. LLM Provider Strategy

The MVP will start with a Chinese OpenAI-compatible model provider. Candidate providers include Mimo, MiniMax, Qwen, or similar providers. The exact provider remains TBD and should be selected before implementation begins.

Provider selection should consider:

- API compatibility
- Documentation quality
- Cost
- Stability
- Network accessibility
- Streaming support
- Tool-calling support
- Future embedding support

Application logic must not depend directly on a vendor SDK. Altas should define its own LLM provider interface and implement provider adapters that translate between the platform contract and provider-specific APIs.

```text
Application
    ↓
Altas LLM Provider Interface
    ↓
Provider Adapter
    ↓
Chinese OpenAI-compatible provider
```

This boundary allows the initial provider to be replaced or supplemented without requiring changes throughout the application.

## 6. Planned Technology Progression

Technologies outside Milestone 1 remain planned until their corresponding learning milestone becomes active.

| Technology | Introduced In | Purpose | Current Status |
|---|---|---|---|
| LangChain RAG | Milestone 2 — Knowledge Systems | Compose document ingestion, retrieval, and grounded response workflows | Planned |
| Embeddings | Milestone 2 — Knowledge Systems | Represent content for semantic comparison and retrieval | Planned |
| Vector store | Milestone 2 — Knowledge Systems | Index and retrieve document chunks by semantic similarity | Planned |
| Conversation memory | Milestone 3 — Memory | Manage bounded conversational state and model context | Planned |
| LangChain Tools | Milestone 4 — Tools and Skills | Define structured capabilities that models can request | Planned |
| Skill registry | Milestone 4 — Tools and Skills | Register, discover, validate, and control reusable skills | Planned |
| LangGraph | Milestone 5 — Agents | Model stateful workflows and bounded agent execution | Planned |
| MCP SDK / MCP integration | Milestone 6 — MCP Integration | Connect tools, resources, context, and external systems through a standard protocol | Planned |
| LangSmith | Milestone 7 — Evaluation | Trace, evaluate, and compare AI application behavior | Planned |
| FastAPI | Milestone 8 — Production Readiness | Expose platform capabilities through an API boundary | Planned |
| Docker | Milestone 8 — Production Readiness | Package reproducible application runtime environments | Planned |
| GitHub Actions | Milestone 8 — Production Readiness | Automate testing, quality checks, builds, and delivery workflows | Planned |
| PostgreSQL | Later / if needed | Provide durable relational storage when application requirements justify it | Planned |
| Redis | Later / if needed | Provide caching or transient coordination when application requirements justify it | Planned |

## 7. Explicitly Deferred Technologies

The following technologies and capabilities are deliberately excluded from the MVP:

- RAG stack
- Vector database
- Conversation memory
- Tools and skills
- Agents
- MCP
- FastAPI
- Docker
- PostgreSQL
- Redis
- Cloud deployment
- Production observability

These concerns are deferred for scope discipline, not because they lack importance. Each introduces concepts, dependencies, and architectural tradeoffs that should be studied when its milestone becomes active. Adding them during Milestone 1 would obscure the foundational request flow and create complexity before the platform has a demonstrated need for it.

## 8. Architecture Layers

The initial stack should support the following conceptual layers:

- **Interface Layer:** Accepts user input and presents system output. The MVP uses a CLI; later interfaces may include APIs or applications.
- **Application Layer:** Coordinates use cases and request flows without depending on provider-specific implementation details.
- **Platform Core:** Defines Altas-owned contracts, prompt management, shared models, and foundational behavior.
- **Provider Adapters:** Translate platform contracts into calls to external model providers and normalize their responses.
- **Infrastructure and Tooling:** Supports configuration, logging, testing, dependency management, documentation, and development workflows.

These layers describe responsibility boundaries, not a detailed folder structure. The implementation structure should be designed separately when the MVP architecture is defined.

## 9. ADR Candidates

The following decisions are likely candidates for future Architecture Decision Records:

- Choose Python as the primary language
- Use `uv` for Python environment and dependency management
- Use LangChain Core as the initial AI framework
- Use Typer for the CLI interface
- Use Pydantic Settings for configuration
- Define an Altas-owned LLM provider abstraction
- Start with a Chinese OpenAI-compatible provider
- Delay RAG, agents, MCP, and the production stack until later milestones

This document identifies the decisions that may require an ADR; it does not replace the ADRs themselves.

## 10. Technology Decision Summary

This section provides a concise architectural summary of why each core technology has been selected. It does not replace Architecture Decision Records. It serves as a high-level decision index, a quick reference for contributors, and a bridge between this document and future ADRs. Future versions of this table may reference ADR identifiers once those ADRs are created.

| Technology | Why It Was Chosen | Alternatives Considered | Future ADR |
|---|---|---|---|
| Python | Mature AI ecosystem, excellent library support, and strong educational value | C#, Go | ADR-001 |
| uv | Fast, modern, unified Python package and environment management | pip + venv, Poetry, Conda | ADR-002 |
| LangChain Core | Modular abstractions for prompts, models, runnables, and retrieval without introducing unnecessary complexity | LlamaIndex, direct SDK usage | ADR-003 |
| Typer | Modern, typed CLI development with minimal boilerplate | argparse, Click | ADR-004 |
| Pydantic Settings | Type-safe configuration management and validation | python-dotenv, custom configuration | ADR-005 |
| Altas Provider Interface | Vendor-independent architecture that isolates provider-specific implementation details | Direct provider SDK integration | ADR-006 |
| Chinese OpenAI-Compatible Provider | Practical access, OpenAI-compatible APIs, and reduced access friction during development | OpenAI, Anthropic, local-only inference | ADR-007 |

The technologies listed above represent the current architectural direction of Project Altas. Individual decisions will eventually be documented in dedicated Architecture Decision Records (ADRs), where alternatives, trade-offs, and long-term implications can be discussed in greater detail.

## 11. Maintenance Rules

- Update this document when a technology is introduced, replaced, deferred, or removed.
- Create an ADR when a major technology choice has long-term architectural impact or requires explanation of meaningful alternatives.
- Distinguish clearly between Active, Planned, Deferred, and Deprecated technologies.
- Keep milestone timing aligned with the approved roadmap.
- Do not rewrite this document wholesale unless the architecture direction changes significantly.

## Document Information

**Status:** Draft

**Version:** 0.1

**Owner:** Project Altas

**Audience:** Developers

**Created:** 2026-07-09

**Last Updated:** 2026-07-09

**Related Documents:**

- [[00-Project Charter]] — Defines the mission and architecture-minded values behind technology choices.
- [[01-Milestones]] — Defines when technologies should be introduced along the learning roadmap.
- [[02-Minimum Viable Product (MVP)]] — Defines the first release constraints that shape the initial stack.
- [[00-Documentation Standards]] — Defines how this architecture document should be maintained.
