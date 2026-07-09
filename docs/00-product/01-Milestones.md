
## 1. Purpose

This document defines the learning and product evolution path for Project Altas. It connects the study of AI engineering concepts with the gradual development of a practical platform, ensuring that each new capability is supported by a clear understanding of its design, behavior, and trade-offs.

## 2. Milestone Philosophy

Project Altas follows a learning-driven approach to product development:

- Each milestone introduces one major AI engineering concept.
- Learning progresses incrementally, from foundational engineering practices to advanced AI applications.
- The platform grows only as the builder's understanding grows.
- Later milestones build on the concepts, interfaces, and lessons established in earlier milestones.
- Complex concerns such as RAG, agents, MCP, evaluation, and production operations should not be compressed into the first release.

This approach keeps the system understandable, makes architectural decisions easier to evaluate, and creates space to learn from each stage before adding further complexity.

## 3. Milestone Overview

| No. | Name | Main Learning Focus | Platform Capability Added | Expected Output | Estimated Duration |
|---:|---|---|---|---|---|
| 1 | Foundation | Core project and LLM application engineering | A structured, configurable CLI chat application | A maintainable foundation and working MVP | 2–4 weeks |
| 2 | Knowledge Systems | Retrieval-augmented generation | Grounded responses from indexed documents | A document question-answering workflow | 2–3 weeks |
| 3 | Memory | Context and conversation state | Bounded conversational memory | A stateful chat experience with explicit memory behavior | 1 week |
| 4 | Tools and Skills | Function calling and controlled capabilities | Registered tools and reusable skills | A system that can safely invoke selected functions | 2 weeks |
| 5 | Agents | Reasoning, planning, and execution loops | Goal-directed tool selection and execution | A constrained agent capable of completing multi-step tasks | 3 weeks |
| 6 | MCP Integration | Standardized AI system integration | MCP-based access to tools, context, and external systems | An MCP client or server integrated with the platform | 2 weeks |
| 7 | Evaluation | Systematic AI quality measurement | Repeatable evaluation and regression checks | An evaluation suite with defined metrics and test cases | 2 weeks |
| 8 | Production Readiness | Reliable operation and delivery | Hardened, observable, deployable services | A containerized system with CI/CD and operational safeguards | 3 weeks |
| 9 | Advanced Applications | Applied AI system design | Domain-oriented assistants and workflows | One or more realistic applications built on the platform | Ongoing |

## 4. Technology Progression

Project Altas milestones are organized around AI engineering concepts and platform responsibilities, not individual technologies. Tools and frameworks such as LangChain are introduced when they help implement, examine, or compare the concept being studied. They support the learning path rather than define it.

| Technology / Tool        | Introduced In                      | Purpose                                                                                  |
| ------------------------ | ---------------------------------- | ---------------------------------------------------------------------------------------- |
| Git                      | Milestone 1 — Foundation           | Manage source history and support incremental development                                |
| GitHub                   | Milestone 1 — Foundation           | Host the repository and support collaborative development workflows                      |
| uv                       | Milestone 1 — Foundation           | Manage Python versions, environments, and dependencies reproducibly                      |
| Python                   | Milestone 1 — Foundation           | Provide the primary implementation language for the platform                             |
| LangChain Core           | Milestone 1 — Foundation           | Provide foundational abstractions for prompts, models, messages, and runnable components |
| LCEL                     | Milestone 1 — Foundation           | Compose and inspect explicit LLM application pipelines                                   |
| Prompt templates         | Milestone 1 — Foundation           | Define reusable, parameterized, and versionable prompts                                  |
| LLM provider abstraction | Milestone 1 — Foundation           | Isolate provider-specific behavior behind a stable platform interface                    |
| LangChain RAG            | Milestone 2 — Knowledge Systems    | Compose document ingestion, retrieval, and grounded generation workflows                 |
| Embeddings               | Milestone 2 — Knowledge Systems    | Represent text for semantic comparison and retrieval                                     |
| Vector store             | Milestone 2 — Knowledge Systems    | Index and retrieve document chunks by semantic similarity                                |
| Conversation memory      | Milestone 3 — Memory               | Manage bounded conversational state and model context                                    |
| LangChain Tools          | Milestone 4 — Tools and Skills     | Define structured capabilities that models can request                                   |
| Skill registry           | Milestone 4 — Tools and Skills     | Register, discover, validate, and control reusable platform skills                       |
| LangGraph                | Milestone 5 — Agents               | Model stateful workflows and bounded agent execution graphs                              |
| MCP                      | Milestone 6 — MCP Integration      | Standardize access to tools, resources, context, and external systems                    |
| LangSmith                | Milestone 7 — Evaluation           | Trace, evaluate, and compare AI application behavior                                     |
| Docker                   | Milestone 8 — Production Readiness | Package the platform into reproducible runtime environments                              |
| GitHub Actions           | Milestone 8 — Production Readiness | Automate tests, quality checks, builds, and deployment workflows                         |
| FastAPI                  | Milestone 8 — Production Readiness | Expose platform capabilities through a production-oriented API boundary                  |

## 5. Detailed Milestones

### Milestone 1 — Foundation

#### Learning Objective

Learn how to structure and operate a small but maintainable LLM application using disciplined software engineering practices.

#### Prerequisites

None

#### Platform Capability

The platform provides a simple CLI chat experience backed by a configurable LLM provider abstraction, managed prompts, and consistent logging.

#### Key Concepts

- Project structure and module boundaries
- Git workflow and incremental development
- Python environment and dependency management with `uv`
- Configuration and secret separation
- Structured logging
- LLM provider abstraction
- Prompt organization and lifecycle management
- CLI interaction design

#### Example Deliverables

- Documented repository structure
- Reproducible `uv` environment
- Configuration and logging modules
- Provider-neutral LLM interface
- Versioned prompt definitions
- Simple CLI chat application
- Basic unit tests for foundational components

#### Completion Criteria

- A new contributor can set up and run the project from documented instructions.
- The CLI can send a prompt to a configured LLM and display the response.
- Provider-specific code is isolated behind a clear interface.
- Configuration, secrets, prompts, and logs have explicit ownership and locations.
- The foundation is understandable without requiring knowledge of RAG, agents, or MCP.

### Milestone 2 — Knowledge Systems

#### Learning Objective

Understand the complete RAG pipeline and how retrieval quality affects the grounding, relevance, and reliability of model responses.

#### Prerequisites

- Milestone 1 — Foundation

#### Platform Capability

The platform can ingest documents, index their content, retrieve relevant passages, and generate responses grounded in retrieved evidence.

#### Key Concepts

- Document loading and normalization
- Text chunking strategies
- Embeddings
- Vector stores
- Similarity search and retrieval
- Context assembly
- Grounded response generation
- Source attribution and retrieval limitations

#### Example Deliverables

- Document ingestion pipeline
- Configurable chunking experiment
- Vector index creation and persistence
- Retrieval interface
- Document question-answering CLI
- Responses with source references

#### Completion Criteria

- Supported documents can be loaded, chunked, embedded, and indexed.
- Queries retrieve relevant source passages through a defined interface.
- Generated answers distinguish retrieved evidence from unsupported information.
- Chunking and retrieval choices are documented and testable.
- The builder can explain the major failure modes of a RAG pipeline.

### Milestone 3 — Memory

#### Learning Objective

Learn how conversation state is represented, bounded, selected, and supplied to a model, and how those choices influence behavior.

#### Prerequisites

- Milestone 1 — Foundation
- Milestone 2 — Knowledge Systems

#### Platform Capability

The platform supports stateful conversations with explicit short-term memory policies and clear memory boundaries.

#### Key Concepts

- Conversation history
- Short-term memory
- Context windows and token limits
- Message selection and truncation
- Summarization strategies
- Session boundaries
- Memory persistence versus model context
- Privacy and data retention considerations

#### Example Deliverables

- Session-based conversation history
- Configurable memory window
- History truncation or summarization strategy
- Memory inspection and reset controls
- Tests for session isolation and context selection

#### Completion Criteria

- The system maintains relevant context across multiple turns.
- Separate sessions do not leak context into one another.
- Memory limits and selection behavior are explicit and configurable.
- Users can inspect or clear stored conversational state.
- The builder can explain the difference between stored memory and context sent to the model.

### Milestone 4 — Tools and Skills

#### Learning Objective

Understand how models request external actions through structured interfaces and how applications validate and control those actions.

#### Prerequisites

- Milestone 1 — Foundation
- Milestone 2 — Knowledge Systems
- Milestone 3 — Memory

#### Platform Capability

The platform can register approved tools and skills, expose their schemas to the model, execute validated calls, and return results to the conversation.

#### Key Concepts

- Function calling
- Tool schemas and interfaces
- Input validation
- Skill registration and discovery
- Execution permissions
- Error handling
- Result serialization
- Controlled access to external capabilities

#### Example Deliverables

- Tool interface and registry
- Several small, deterministic tools
- Reusable skill definitions
- Tool-call validation and execution pipeline
- Tool invocation logs
- Permission and failure-handling policies

#### Completion Criteria

- Tools can be registered through a consistent interface.
- The model can select and call an approved tool using validated arguments.
- Unknown, malformed, or disallowed calls fail safely.
- Tool execution is observable and testable.
- The boundary between model requests and application-controlled execution is clear.

### Milestone 5 — Agents

#### Learning Objective

Learn how agents select actions, use tools, plan work, observe results, and continue through bounded execution loops.

#### Prerequisites

- Milestone 1 — Foundation
- Milestone 2 — Knowledge Systems
- Milestone 3 — Memory
- Milestone 4 — Tools and Skills

#### Platform Capability

The platform can run a constrained agent that completes multi-step tasks using approved tools, explicit limits, and observable state transitions.

#### Key Concepts

- Agent reasoning and action selection
- Planning and task decomposition
- Tool use
- Observation and feedback
- Execution loops
- Termination conditions
- State machines and orchestration
- Workflows versus agents
- Guardrails and human approval

#### Example Deliverables

- Bounded agent execution loop
- Agent state and trace model
- Multi-step tool-use task
- Deterministic workflow for comparison
- Step, time, and cost limits
- Optional human approval checkpoints

#### Completion Criteria

- The agent can complete a defined multi-step task with approved tools.
- Every action and observation is recorded in an understandable trace.
- Execution terminates successfully or stops at a configured limit.
- Failures and retries are handled explicitly.
- The builder can justify when a deterministic workflow is preferable to an agent.

### Milestone 6 — MCP Integration

#### Learning Objective

Understand MCP as a standardized way to expose tools, context, resources, and external systems to AI applications.

#### Prerequisites

- Milestone 1 — Foundation
- Milestone 2 — Knowledge Systems
- Milestone 3 — Memory
- Milestone 4 — Tools and Skills
- Milestone 5 — Agents

#### Platform Capability

The platform can connect to an MCP server or expose selected capabilities through an MCP-compatible interface.

#### Key Concepts

- MCP architecture and roles
- Clients, servers, and transports
- Tools, resources, and prompts
- Capability discovery
- Schema-based interoperability
- Connection lifecycle
- Trust and permission boundaries
- Integration with external systems

#### Example Deliverables

- Minimal MCP client or server
- Capability discovery flow
- Adapter between MCP capabilities and the platform tool registry
- Integration with one external MCP system
- Connection and permission documentation

#### Completion Criteria

- The platform can discover and use capabilities from a compatible MCP endpoint, or expose its own capabilities through MCP.
- MCP data is translated through clear internal boundaries.
- Connection failures and unsupported capabilities are handled safely.
- Trust, access, and configuration requirements are documented.
- The builder can explain what MCP standardizes and what remains application-specific.

### Milestone 7 — Evaluation

#### Learning Objective

Learn how to measure AI system quality systematically and detect regressions across prompts, retrieval, tools, and agent behavior.

#### Prerequisites

- Milestone 1 — Foundation
- Milestone 2 — Knowledge Systems
- Milestone 3 — Memory
- Milestone 4 — Tools and Skills
- Milestone 5 — Agents
- Milestone 6 — MCP Integration

#### Platform Capability

The platform includes repeatable evaluation datasets, metrics, test runners, and reports for its major AI behaviors.

#### Key Concepts

- Prompt evaluation
- Retrieval evaluation
- Groundedness and answer relevance
- Agent behavior evaluation
- Test datasets and expected outcomes
- Deterministic and model-based evaluators
- Regression testing
- Quality, latency, and cost measurement
- Evaluation limitations and bias

#### Example Deliverables

- Versioned evaluation dataset
- Prompt regression suite
- Retrieval relevance tests
- Agent trajectory checks
- Quality, latency, and cost report
- Baseline results for future comparison

#### Completion Criteria

- Core platform behaviors have defined evaluation criteria.
- Evaluations can be run repeatedly against versioned test cases.
- Results make regressions visible across relevant quality dimensions.
- Automated scores are supplemented by appropriate human review.
- Changes to prompts or retrieval behavior can be compared with a recorded baseline.

### Milestone 8 — Production Readiness

#### Learning Objective

Understand the engineering and operational practices required to run an AI system reliably, securely, and observably.

#### Prerequisites

- Milestone 1 — Foundation
- Milestone 2 — Knowledge Systems
- Milestone 3 — Memory
- Milestone 4 — Tools and Skills
- Milestone 5 — Agents
- Milestone 6 — MCP Integration
- Milestone 7 — Evaluation

#### Platform Capability

The platform can be packaged, tested, deployed, monitored, and operated with defined safeguards and recovery paths.

#### Key Concepts

- Configuration hardening
- Error handling and resilience
- Structured logs, metrics, and traces
- Docker
- CI/CD
- Deployment environments
- Secret management
- Authentication and authorization basics
- Rate limits, timeouts, and retries
- Cost, privacy, and operational risk

#### Example Deliverables

- Hardened configuration validation
- Consistent error model
- Observability instrumentation
- Docker image and local container workflow
- CI pipeline for tests and quality checks
- Deployment pipeline and runbook
- Basic security and threat review

#### Completion Criteria

- The application starts predictably and rejects invalid configuration.
- Critical operations expose useful logs, metrics, and traces.
- Automated checks run before deployment.
- The system can be built and run from a reproducible container image.
- Secrets and sensitive data are handled through documented controls.
- Common failures have documented detection and recovery procedures.

### Milestone 9 — Advanced Applications

#### Learning Objective

Apply the accumulated platform capabilities to realistic AI applications and learn how domain needs shape architecture, evaluation, and user experience.

#### Prerequisites

- Milestone 1 — Foundation
- Milestone 2 — Knowledge Systems
- Milestone 3 — Memory
- Milestone 4 — Tools and Skills
- Milestone 5 — Agents
- Milestone 6 — MCP Integration
- Milestone 7 — Evaluation
- Milestone 8 — Production Readiness

#### Platform Capability

The platform supports domain-oriented applications that combine knowledge, memory, tools, agents, MCP, evaluation, and operational controls where appropriate.

#### Key Concepts

- Domain modeling
- Application-specific orchestration
- Human-in-the-loop interaction
- Structured and unstructured data integration
- Domain-specific evaluation
- Reusable platform boundaries
- User experience for AI uncertainty
- Application-level safety and permissions

#### Example Deliverables

- ChatBI assistant for governed data exploration
- Research assistant with cited sources
- Document assistant for analysis and transformation
- Workflow assistant with approvals and audit trails
- Comparative architecture notes across applications

#### Completion Criteria

- At least one realistic application solves a clearly defined user problem.
- The application reuses platform components through stable interfaces.
- AI capabilities are selected because they serve the use case, not merely to demonstrate technology.
- Domain-specific quality, safety, and operational criteria are defined and evaluated.
- Lessons from the application produce clear improvements to the underlying platform.

## 6. Relationship to MVP

The Project Altas MVP should be derived from Milestone 1 only. Its purpose is to establish a sound engineering foundation and a simple, understandable LLM interaction loop.

The MVP should not attempt to include RAG, agents, MCP, or production deployment. These capabilities introduce distinct concepts and architectural trade-offs that belong to later milestones. Keeping them outside the MVP preserves a focused learning path and prevents premature complexity.

## Document Information

**Status:** Approved

**Version:** 1.0

**Owner:** Project Altas

**Audience:** Everyone

**Created:** 2026-07-09

**Last Updated:** 2026-07-09

**Related Documents:**
- [[00-Project Charter]] — Foundational mission, vision, and guiding principles.
- [[02-MVP]] — First release derived from Milestone 1 — Foundation.
- [[00-Tech Stack]] — Technology progression aligned with the milestones.
