# ADR-005: Use Layered Application Architecture

## Status

Accepted

## Context

Project Altas is transitioning from architecture into implementation. As the project grows from a simple CLI application into a reusable AI engineering platform, source code must remain understandable, testable, and maintainable.

Without architectural boundaries, responsibilities tend to become mixed. That would make future milestones such as RAG, memory, agents, MCP, and evaluation increasingly difficult to implement without coupling unrelated concerns.

The project therefore needs a stable architectural pattern before writing significant application code.

## Decision

Project Altas will use a layered application architecture.

The architecture will describe responsibilities conceptually rather than by concrete files or package names. The recommended layers are:

- **User Interface:** Receives user input, displays output, and contains no business logic.
- **Application:** Coordinates use cases, orchestrates workflows, and connects user-facing entry points to domain services.
- **Domain Services:** Implements project logic, defines interfaces and business behavior, and remains independent of infrastructure.
- **Infrastructure:** Implements communication with external systems, including LLM providers, configuration loading, persistence, logging, and future integrations.

Dependencies always point inward:

```text
User Interface
    -> Application
        -> Domain Services
            -> Infrastructure abstractions
```

Higher layers may depend on lower-level abstractions, but core project logic should never depend directly on external provider implementations.

## Alternatives Considered

- **Flat script organization:** Easy initially, but difficult to scale as responsibilities grow.
- **Feature-first organization:** May become appropriate later, but is unnecessary during the MVP.
- **Framework-driven organization:** Organizes code around LangChain or other external libraries, but couples project architecture to implementation choices.

## Consequences

- Responsibilities are separated more clearly.
- Testing becomes easier because use cases and project logic can be exercised without full infrastructure.
- Infrastructure implementations can be replaced with less disruption.
- Future expansion is simpler as new capabilities are introduced.
- Incremental milestones can build on stable architectural boundaries.
- The architecture introduces slightly more files than a flat script organization.
- The dependency rule requires discipline during implementation.
- Small project stages may initially feel more structured than necessary.

## Implementation Guidance

- Initial implementation should remain intentionally small.
- Modules should only be introduced when required.
- Empty future directories should not be created prematurely.
- Architectural boundaries should remain stable even if module organization changes.

## Document Information

**Status:** Approved

**Version:** 1.0

**Owner:** Project Altas

**Audience:** Developers

**Created:** 2026-07-10

**Last Updated:** 2026-07-10

**Related Documents:**

- [[00-Tech Stack]] - Defines the technology direction and planned stack.
- [[02-Minimum Viable Product (MVP)]] - Defines the first release constraints.
- [[01-Milestones]] - Defines when technologies are introduced.
- [[ADR-001 Choose Python as the Primary Language]] - Records the decision to use Python as the primary language.
- [[ADR-002 Use uv For Python Environment and Dependency Management]] - Records the decision to use `uv`.
- [[ADR-003 Adopt Langchain Core as Initial AI Framework]] - Records the decision to adopt LangChain Core as the initial AI framework.
- [[ADR-004 Use a src-based Package Layout]] - Records the decision to use a `src/`-based package layout.
