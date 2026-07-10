# ADR-001: Choose Python as the Primary Language

## Status

Accepted

## Context

Project Altas is an AI engineering platform and learning laboratory. Its primary language needs to support both incremental learning and practical implementation across LLM applications, model providers, embeddings, evaluation, local inference integrations, and data processing.

Python provides direct access to the strongest ecosystem for these concerns and is the primary language of LangChain and many related AI tools. Selecting the language before the first project initialization also establishes a consistent foundation for dependencies, tooling, examples, and future platform components.

## Decision

Project Altas will use Python as its primary implementation language.

Altas-owned interfaces and modular boundaries should prevent this choice from creating unnecessary coupling between platform responsibilities and specific third-party libraries.

## Alternatives Considered

- **C#:** A strong general-purpose language with enterprise relevance, but its AI ecosystem is less aligned with the learning path and planned LangChain work.
- **Go:** Well suited to infrastructure and services, but less suitable for AI experimentation and LangChain-centered learning.
- **TypeScript:** Strong for web applications and user interfaces, but not the best fit for the initial local-first AI engineering workflow.

## Consequences

- Project Altas gains access to a mature AI ecosystem and broad library support.
- LangChain and other planned AI tooling can be integrated through their primary language ecosystem.
- Python provides strong educational value and supports rapid, readable experimentation.
- Runtime performance may be lower than Go or other compiled languages for some workloads.
- Python packaging and environment management require deliberate tooling and conventions.
- Other languages may still be introduced later when a specific platform responsibility justifies them.

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
