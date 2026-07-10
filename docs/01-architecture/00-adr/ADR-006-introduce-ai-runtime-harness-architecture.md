# ADR-006: Introduce AI Runtime Harness Architecture

## Status

Accepted

## Context

Project Altas currently separates application responsibilities from provider responsibilities. The Application Layer coordinates user-facing use cases, while the Provider Layer isolates communication with external model providers.

As AI capabilities grow to include RAG, memory, tools, agents, MCP, and evaluation, direct model invocation becomes insufficient. These capabilities require consistent orchestration around context, execution state, tool coordination, observability, validation, and evaluation.

The project therefore needs a dedicated runtime orchestration boundary before advanced AI capabilities are added.

## Decision

Project Altas will introduce an AI Runtime Harness layer between the Application Layer and AI Providers.

The AI Runtime Harness is responsible for AI execution lifecycle management. It is an Altas architectural boundary, not a commitment to a specific framework or package structure.

Responsibilities may include:

- execution orchestration,
- context preparation,
- memory coordination,
- tool execution coordination,
- tracing and observability,
- evaluation hooks,
- safety and validation boundaries.

Application code should express the user-facing use case and delegate AI execution concerns to the harness. Provider implementations should remain behind provider abstractions and should not become the place where application orchestration, memory, tools, evaluation, or safety rules are mixed together.

## Alternatives Considered

- **Direct provider invocation:** Simple for the MVP, but does not provide a stable place for context, memory, tool execution, tracing, and evaluation concerns as capabilities grow.
- **Application-owned orchestration:** Keeps early code close to the use case, but risks mixing user-facing coordination with AI runtime behavior.
- **Provider-owned orchestration:** Centralizes provider calls, but couples execution lifecycle behavior to external provider implementations.
- **Framework-owned architecture:** May accelerate implementation, but makes Altas architecture depend too directly on LangChain, LangGraph, or another framework.

## Consequences

- Responsibilities between application use cases, runtime execution, and provider communication become clearer.
- The platform can evolve from simple LLM calls to more complex AI systems without moving orchestration concerns into unrelated layers.
- Production engineering practices such as tracing, evaluation hooks, validation, and safety boundaries have a natural architectural home.
- Framework capabilities such as LangChain or LangGraph can support implementation without defining the Altas architecture.
- The architecture introduces additional conceptual complexity.
- More runtime components may need to be designed, tested, and maintained as the platform grows.

## Implementation Guidance

- The initial harness should remain small and grow only when a real execution responsibility appears.
- The harness should define responsibilities and boundaries before detailed module organization is introduced.
- Frameworks may help implement harness behavior, but Altas-owned boundaries should remain clear.
- The harness should remain valid across simple LLM calls, RAG, memory, tools, agents, MCP, and evaluation.

The AI Runtime Harness provides the execution boundary for AI capabilities, while specialized frameworks such as LangGraph may implement specific workflow or agent execution patterns inside this boundary.

## Document Information

**Status:** Approved

**Version:** 1.0

**Owner:** Project Altas

**Audience:** Developers

**Created:** 2026-07-10

**Last Updated:** 2026-07-10

**Related Documents:**

- [[00-Tech Stack]] - Defines the technology direction and planned stack.
- [[01-Milestones]] - Defines when AI Runtime Harness capabilities should be introduced.
- [[02-Minimum Viable Product (MVP)]] - Defines the first release constraints.
- [[ADR-003-adopt-langchain-core-as-initial-ai-framework]] - Records the initial AI framework decision.
- [[ADR-005-use-layered-application-architecture]] - Records the layered architecture that the runtime harness refines.
