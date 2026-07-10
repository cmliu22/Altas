# Minimum Viable Product

## 1. Purpose

This document defines the first usable release of Project Altas. The MVP establishes a practical foundation for learning how an LLM application is structured and operated without introducing the concepts reserved for later milestones.

The MVP is not the complete Altas platform. It is a deliberately limited first release from which the platform can evolve as understanding grows.

## 2. MVP Definition

The Project Altas MVP is a local-first CLI-based LLM chat application that demonstrates core AI application engineering foundations, including project structure, configuration, logging, LLM provider abstraction, prompt management, and a simple user interaction loop.

## 3. Relationship to Milestone 1

The MVP implements Milestone 1 — Foundation as defined in [[01-Milestones]]. Its scope is limited to the engineering foundation required for a small, maintainable LLM application.

Completing the MVP should allow the builder to understand:

- How a basic LLM application is structured
- How prompts are managed separately from application logic
- How provider-specific LLM code can be isolated
- How configuration and secrets should be handled
- How logging helps inspect application behavior
- How a CLI can provide a simple interface before adding web or API layers

## 4. User Scenario

A user opens a terminal, runs the Altas CLI, enters a message, and receives a response from the configured LLM provider. The request passes through configuration loading, prompt management, the LLM provider abstraction, and structured logging before the response is displayed.

This scenario provides one clear interaction path through the foundational components without requiring additional interfaces or AI capabilities.

## 5. Functional Scope

The MVP includes only the following capabilities:

- Local project setup
- Reproducible Python environment using `uv`
- Basic CLI chat command
- Configuration loading
- Secret management through environment variables
- LLM provider abstraction
- At least one initial LLM provider implementation
- Prompt template management
- Structured logging
- Basic unit tests for foundational components
- Minimal README instructions for running the MVP

## 6. Out of Scope

The following capabilities are explicitly excluded from the MVP:

- RAG
- Document ingestion
- Embeddings
- Vector stores
- Conversation memory
- Tools and skills
- Agents
- MCP
- Evaluation framework
- Web UI
- FastAPI service
- Docker
- CI/CD
- Authentication
- Cloud deployment
- ChatBI
- Multi-user support

These capabilities belong to later milestones and should not be introduced until their underlying concepts become the active learning focus.

## 7. Platform Components

| Component | Responsibility | MVP Expectation |
|---|---|---|
| CLI Interface | Accept user input and display model responses | Provide one simple chat command and a clear interaction loop |
| Configuration | Load and validate non-secret application settings | Support local configuration with explicit defaults and useful errors |
| Secret Management | Supply sensitive provider credentials | Read secrets from environment variables without hardcoding them |
| Prompt Manager | Store, load, and format prompts separately from application logic | Provide at least one reusable prompt template |
| LLM Provider Interface | Define the platform-facing contract for LLM interactions | Keep application logic independent of provider-specific SDK details |
| Initial LLM Provider | Connect the provider interface to one supported LLM service | Send a request and return a normalized response |
| Logging | Record important events across the request flow | Produce structured logs without exposing secrets |
| Tests | Verify foundational behavior in isolation | Cover configuration, prompts, provider boundaries, and other core components with basic unit tests |
| README | Explain how to prepare and run the project | Provide minimal, accurate setup and CLI usage instructions |

## 8. Success Criteria

The MVP is complete when:

- A user can set up the project locally by following the README instructions.
- A user can run a CLI command and receive a response from the configured LLM.
- Provider-specific logic is isolated behind an interface.
- Prompts are stored separately from application logic.
- Configuration and secrets are not hardcoded.
- Logs make the basic request flow observable.
- Foundational components have basic unit tests.
- The MVP remains simple enough to understand before learning RAG, tools, agents, or MCP.

## 9. MVP Completion Checklist

- [ ] Establish the local project structure.
- [ ] Configure a reproducible Python environment using `uv`.
- [ ] Implement configuration loading and validation.
- [ ] Load secrets from environment variables.
- [ ] Create separately managed prompt templates.
- [ ] Define the LLM provider interface.
- [ ] Implement at least one initial LLM provider.
- [ ] Implement the basic CLI chat interaction.
- [ ] Add structured logging across the request flow.
- [ ] Add basic unit tests for foundational components.
- [ ] Document local setup and MVP usage in the README.

## 10. Future Evolution

Later milestones will extend the MVP with knowledge systems and RAG, conversation memory, tools and skills, agents, MCP integration, evaluation, production readiness, and advanced applications. Each extension should be introduced through its corresponding milestone so that platform growth remains aligned with the learning path.

## Document Information

**Status:** Approved

**Version:** 1.0

**Owner:** Project Altas

**Audience:** Contributors

**Created:** 2026-07-09

**Last Updated:** 2026-07-09

**Related Documents:**

- [[00-Project Charter]] — Project mission and vision.
- [[01-Milestones]] — Learning roadmap from which this MVP is derived.
- [[00-Tech Stack]] — Technologies selected to implement the MVP.
