## Status

Accepted

## Context

Project Altas needs a fast, reproducible, and modern local development workflow before the first Python project is initialized. The workflow should manage environments and dependencies consistently on both a Windows PC and a MacBook without requiring heavyweight environment management.

Using one tool for the primary package and environment workflow reduces setup ambiguity and gives contributors a clear, repeatable way to prepare and run the project.

## Decision

Project Altas will use `uv` for Python environment and dependency management.

Project setup and contributor instructions should treat `uv` as the standard local workflow while preserving compatibility with conventional Python project metadata where practical.

## Alternatives Considered

- **pip + venv:** Simple, standard, and widely understood, but less unified for dependency resolution, environment management, and reproducible project commands.
- **Poetry:** Mature and widely used, but introduces a heavier workflow than the initial project requires.
- **Conda:** Useful for scientific environments and native dependencies, but unnecessary for the MVP and heavier than needed for the planned stack.

## Consequences

- Dependency installation and environment creation should be fast.
- The project gains a consistent, reproducible local workflow across Windows and macOS.
- Package and environment operations can be managed through a compact toolchain.
- Contributors must learn a newer tool.
- Compatibility with standard Python workflows and external tooling must be considered as the project evolves.
- The decision should be revisited if future platform requirements expose material limitations.

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
