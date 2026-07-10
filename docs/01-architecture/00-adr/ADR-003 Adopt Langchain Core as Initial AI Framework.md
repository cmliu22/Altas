# ADR-003: Adopt LangChain Core as the Initial AI Framework

## Status

Accepted

## Context

Project Altas exists partly to understand LangChain and modern AI application architecture. Milestone 1 needs a focused way to study prompts, models, messages, runnables, and simple LLM composition without introducing RAG, agents, LangGraph, or advanced orchestration.

LangChain Core provides the foundational abstractions needed for this learning scope. It also creates a path toward later LangChain capabilities while allowing the MVP request flow to remain small and inspectable.

## Decision

Project Altas will use LangChain Core as the initial AI framework for prompts, models, messages, runnables, and simple LLM composition.

LangChain abstractions will remain conceptually separate from Altas-owned application and provider interfaces. Capabilities outside the Milestone 1 scope will not be introduced merely because the framework supports them.

## Alternatives Considered

- **Direct provider SDK usage:** Simpler initially, but less useful for learning framework-level model, prompt, and composition abstractions and more likely to encourage provider coupling.
- **LlamaIndex:** Strong for RAG and knowledge systems, but less aligned with the initial Milestone 1 focus.
- **LangGraph:** Valuable for agents and stateful workflows, but too advanced for the MVP and reserved for a later milestone.

## Consequences

- The project gains a focused entry point into the LangChain ecosystem.
- The initial framework supports later growth into RAG, tools, memory, and LangGraph.
- Model and prompt composition can be studied without coupling application logic directly to one provider SDK.
- LangChain Core adds a framework dependency whose abstractions must be understood rather than adopted uncritically.
- Altas-owned boundaries must remain distinct so framework choices can be changed where practical.
- Advanced LangChain capabilities remain deferred until their corresponding milestones.

## Related Documents

- [[00-Tech Stack]] — Defines the technology direction and planned stack.
- [[02-Minimum Viable Product (MVP)]] — Defines the first release constraints.
- [[01-Milestones]] — Defines when technologies are introduced.

## Document Information

**Status:** Approved

**Version:** 1.0

**Owner:** Project Altas

**Audience:** Developers

**Created:** 2026-07-09

**Last Updated:** 2026-07-09

**Related Documents:**

- [[00-Tech Stack]] — Defines the technology direction and planned stack.
- [[02-Minimum Viable Product (MVP)]] — Defines the first release constraints.
- [[01-Milestones]] — Defines when technologies are introduced.
