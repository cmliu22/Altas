
## 1. Purpose

This document defines the reference development environments supported by Project Altas. It exists to make onboarding, machine replacement, and cross-platform development predictable and reproducible across Windows and macOS.

This is an engineering standard, not an installation tutorial. It describes the approved environment shape, the tools Project Altas expects contributors to use, and the reasoning behind those choices.

## 2. Design Philosophy

Project Altas treats the development environment as part of the project's architecture. A simple, reproducible environment reduces setup ambiguity and keeps attention on learning, implementation, and system design.

The development environment should follow these principles:

- Keep the development environment simple.
- Prefer standard tooling with broad ecosystem support.
- Avoid unnecessary layers and overlapping tools.
- Minimize machine-specific differences.
- Let `uv` manage project environments.
- Keep project configuration portable across supported operating systems.
- Prefer reproducibility over novelty.

The goal is not to use the newest or most elaborate local setup. The goal is to define a stable baseline that is easy to understand, easy to replace, and easy to troubleshoot.

The development environment should evolve more slowly than the project implementation. Application code is expected to change frequently as Project Altas grows, while the underlying development environment should remain stable, predictable, and intentionally maintained. Stability in the environment reduces unnecessary variables during development and troubleshooting.

## 3. Supported Operating Systems

| Operating System | Status | Notes |
|---|---|---|
| Windows 11 | Primary supported platform | Reference Windows environment for Project Altas development. |
| macOS (Apple Silicon) | Fully supported development platform | Reference macOS environment for Project Altas development. |

Future Linux support is expected, but Linux is not currently standardized as an official Project Altas development environment.

## 4. Windows Reference Environment

The Windows reference environment should remain compact and based on standard tooling.

| Component | Standard |
|---|---|
| Git | Official Git for Windows installation |
| Python | Official Python installer from python.org |
| uv | Official `uv` installation |
| VS Code | Primary editor for development and documentation |

Python on Windows should be installed in the simplest practical way. Project Altas should avoid Conda unless a future requirement specifically justifies it, such as scientific packages or native dependency workflows that cannot be handled cleanly by the standard Python toolchain.

Unnecessary Python version managers should also be avoided. A single clear Python installation, combined with `uv` for project environments, is easier to verify and maintain than several overlapping Python management layers.

## 5. macOS Reference Environment

The macOS reference environment uses Apple-provided Git as the bootstrap tool, Homebrew as the primary package manager, and `uv` as the project environment manager.

```text
Apple Git
    |
    v
Homebrew
    |-- Python
    |-- uv
    |-- other CLI tools
    v
VS Code
    |
    v
Project Altas
```

Apple Git is acceptable as the initial Git tool on macOS. Homebrew manages developer tools after bootstrap and should remain the primary package manager for the macOS development environment.

Homebrew Python is the primary development Python on macOS. The macOS system Python should not be modified, replaced, or used as the project runtime. Project-level environments belong to `uv`, which should create and manage isolated environments for Project Altas.

Manual installations and additional Python version managers should be avoided unless a future project requirement justifies them. Keeping Homebrew as the primary package manager makes the environment easier to reason about and troubleshoot.

## 6. Standard Development Tools

| Tool | Purpose |
|---|---|
| Git | Version control for project history and local changes. |
| GitHub | Remote repository hosting, collaboration, and future automation. |
| Python | Primary implementation language for Project Altas. |
| uv | Python environment and dependency management. |
| VS Code | Primary development and documentation editor. |
| Obsidian | Local knowledge navigation for Markdown documentation. |
| markdownlint | Markdown style checking for documentation quality. |
| Ruff | Python linting and formatting. |
| pytest | Python test execution. |

These tools define the expected contributor baseline. Additional tools may be introduced when they solve a clear project need, but they should not replace the standard workflow without an approved documentation update.

## Reference Environment Versions

This section provides a snapshot of the current reference versions used by Project Altas. These versions are reference baselines rather than strict requirements.

| Component | Reference Version | Notes |
|---|---|---|
| Python | 3.14.x | Keep reasonably current on the latest stable minor release. |
| uv | Latest stable | Update regularly after verifying compatibility. |
| Git | Recent stable release | Apple Git or Git for Windows are both acceptable. |
| VS Code | Latest stable | Primary development environment. |

These versions represent the current reference environment for Project Altas. Minor version differences are acceptable provided they do not affect reproducibility or compatibility.

## 7. Environment Verification

Environment verification commands should be run before troubleshooting setup issues. They confirm which tools are available, which executable paths are active, and whether the shell environment matches the expected standard.

For macOS:

```shell
git --version
python --version
python3 --version
which -a python3
which uv
uv --version
echo $PATH
```

For Windows:

```shell
git --version
python --version
where python
where uv
uv --version
```

Verification output should be reviewed before changing installations, editing shell configuration, or adding new tooling. Many environment problems are caused by path order, duplicate installations, or tools installed outside the reference stack.

## 8. Upgrade Policy

Project Altas should keep development tools reasonably current without adopting upgrades solely because a newer version exists.

- Keep Python on a recent stable release.
- Keep `uv` updated.
- Keep Homebrew packages reasonably current on macOS.
- Do not upgrade solely for the newest version.
- Prefer stable tooling over frequent changes.
- Review major upgrades before adopting them.

Major upgrades should be evaluated for compatibility, project impact, contributor disruption, and documentation changes. Stability and reproducibility matter more than chasing the latest release.

## Environment Ownership

```text
Operating System
        ↓
Package Manager
        ↓
Language Runtime
        ↓
Project Environment
        ↓
Repository
```

Windows ownership:

| Layer | Owner |
|---|---|
| Operating System | Windows |
| Package Manager | Winget or manual installer |
| Language Runtime | Official Python installation |
| Project Environment | uv |
| Repository | Project Altas |

macOS ownership:

| Layer | Owner |
|---|---|
| Operating System | macOS |
| Package Manager | Homebrew |
| Language Runtime | Homebrew Python |
| Project Environment | uv |
| Repository | Project Altas |

Each layer owns a distinct responsibility. Troubleshooting should begin by identifying which layer is responsible before changing configuration or reinstalling software.

## 9. Environment Principles

Project Altas development environments should follow these operating principles:

- Use one primary Python installation.
- Use one primary package manager per operating system.
- Use one project environment manager.
- Keep `PATH` predictable.
- Never modify the system Python on macOS.
- Let `uv` own project environments.
- Keep repository configuration portable.
- Avoid machine-specific assumptions in project documentation and scripts.
- Prefer explicit verification over guesswork.

These principles reduce environment drift and make cross-platform development easier to support.

## 10. Common Pitfalls

Windows pitfalls:

- Multiple Python installations can make `python` resolve differently across terminals.
- `PATH` conflicts can cause Git, Python, or `uv` commands to use an unexpected executable.
- Proxy or network configuration issues can affect GitHub access and package downloads.

macOS pitfalls:

- Accidentally using the macOS system Python can create confusing permissions and dependency issues.
- Mixing Homebrew, manual installers, and version managers can make tool resolution unpredictable.
- Installing unnecessary Python version managers adds maintenance burden without improving the standard workflow.
- Editing system files or modifying system-provided Python can make the machine harder to restore and troubleshoot.

Troubleshooting should start with the verification commands in this document, then proceed by removing ambiguity rather than adding more tooling.

## 11. Future Evolution

This standard will evolve as Project Altas introduces additional engineering infrastructure. Expected future updates include:

- CI environments.
- Docker-based workflows.
- Production deployment tooling.
- Standardized Linux development support.

Future changes should preserve the goals of reproducibility, simplicity, maintainability, and minimal unnecessary tooling.

## Document Information

**Status:** Approved

**Version:** 1.0

**Owner:** Project Altas

**Audience:** Contributors

**Created:** 2026-07-09

**Last Updated:** 2026-07-09

**Related Documents:**

- [[00-Documentation Standards]] - Defines the structure and maintenance rules for official Project Altas documentation.
- [[00-Tech Stack]] - Defines the project technology direction that the development environment supports.
- [[ADR-002-use-uv-for-python-environment-and-dependency-management]] - Records the decision to use `uv` for Python environment and dependency management.
