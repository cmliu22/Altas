## Status

Accepted

## Context

Project Altas is expected to grow beyond a single script into a reusable AI engineering platform with multiple modules. Planned areas include configuration, prompts, provider adapters, CLI, RAG, tools, agents, MCP, evaluation, and future application layers.

The `src/` layout is a widely adopted convention in modern Python projects. It prevents accidental imports from the repository root, better reflects how packages are installed and consumed, and integrates naturally with modern tooling such as `uv`, pytest, Ruff, and packaging workflows.

The project needs a package layout that:

- separates importable source code from repository-level files,
- prevents accidental imports from the repository root,
- supports reliable testing and packaging,
- scales cleanly as modules are added,
- works well with `uv`, pytest, Ruff, and standard Python tooling.

## Decision

Project Altas will use a `src/`-based package layout.

The initial structure created through `uv init --package` should use:

```text
src/
    altas/
        __init__.py
```

Importable application and platform code should live under `src/altas/`. Repository-level files such as documentation, tests, configuration, scripts, and project metadata should remain outside the importable package unless there is a clear packaging reason to include them.

This ADR defines only the package boundary. It intentionally does not define the internal package organization; packages and modules should evolve incrementally as architectural responsibilities emerge, and future structural changes may be recorded by additional ADRs.

## Alternatives Considered

- **Flat package layout:** Simpler at the start, but easier to accidentally import code from the repository root and less protective as the project grows.
- **Single-script layout:** Useful for experiments, but not appropriate for a reusable platform with multiple architectural responsibilities.
- **Multiple top-level packages:** May become useful later, but would add unnecessary structure before clear package boundaries exist.

## Consequences

- Tests and local commands must import the installed package rather than relying on repository-root imports.
- The package boundary is clearer from the beginning of implementation.
- Future modules can be added under `src/altas/` without mixing source code with repository operations.
- Tooling configuration for `uv`, pytest, Ruff, and packaging should account for the `src/` layout.
- The `src/` layout introduces a slightly deeper directory structure than a flat project, which may feel less familiar to new Python developers.
- Contributors must understand that importable code belongs under `src/altas/`.

## Related Documents

- [[00-Tech Stack]] - Defines the technology direction and planned stack.
- [[02-Minimum Viable Product (MVP)]] - Defines the first release constraints.
- [[01-Milestones]] - Defines when technologies are introduced.
- [[ADR-002 Use uv For Python Environment and Dependency Management]] - Records the decision to use `uv`.

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
- [[ADR-002 Use uv For Python Environment and Dependency Management]] - Records the decision to use `uv`.
