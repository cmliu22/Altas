
## 1. Purpose

This document defines how official Project Altas documentation should be created, structured, maintained, and reviewed. It establishes a consistent approach for preserving stable knowledge and making engineering decisions understandable over time.

## 2. Documentation Philosophy

Project Altas treats documentation as part of engineering, not as an afterthought.

- Documentation should explain decisions, responsibilities, and intent rather than duplicate code.
- Stable knowledge belongs in `docs/`.
- Temporary thinking, exploration, and unvalidated ideas belong in `notes/`.
- Git records the history of changes; documents should describe their own current status, version, audience, and relationships.
- Every official document should have a single responsibility.

Documentation should evolve alongside the platform while remaining focused, trustworthy, and useful to future readers.

## 3. Documentation Hierarchy

Project Altas documentation follows a hierarchy in which each layer answers a different question:

- The Project Charter answers why the project exists.
- Milestones answer how the project evolves and what is learned.
- The MVP answers what is built first.
- Architecture documents answer how the system is designed.
- Architecture Decision Records (ADRs) answer why important technical decisions were made.
- Implementation shows how those decisions are realized in code.

```text
Project Charter — Why does Altas exist?
    └── Milestones — How does it evolve, and what is learned?
        └── MVP — What is built first?
            └── Architecture — How is the system designed?
                └── ADRs — Why were important technical choices made?
                    └── Implementation — How are those choices realized?
```

This hierarchy separates product intent, learning progression, system design, technical decisions, and implementation details.

## 4. Folder Organization

- `docs/00-product/` contains stable product direction, scope, milestones, and release definitions.
- `docs/01-architecture/` contains stable system design, technical direction, interfaces, and architectural views.
- `docs/99-meta/` contains standards and guidance governing the documentation itself.
- `notes/` contains temporary thinking, experiments, research, meeting notes, and ideas that have not become stable project knowledge.

Content in `docs/` is official documentation and should be reviewed, maintained, and safe to treat as the current project baseline. Content in `notes/` is working material and may be incomplete, speculative, or temporary. Stable conclusions from notes should be incorporated into the appropriate official document rather than treating the notes as authoritative.

## 5. Official Document Structure

Every official document should follow this general structure:

1. Title
2. Purpose
3. Main content
4. Document Information

The main content should be organized according to the document's single responsibility. Every official document should end with a `Document Information` section that identifies its lifecycle state, version, ownership, audience, dates, and relationships.

## 6. Document Information Standard

Use the following format at the end of every official document:

```text
## Document Information

**Status:** Draft | Review | Approved | Deprecated

**Version:** X.Y or X.Y.Z

**Owner:** Project Altas

**Audience:** Everyone | Contributors | Developers | Architects | Operators | End Users

**Created:** YYYY-MM-DD

**Last Updated:** YYYY-MM-DD

**Related Documents:**

- [[Document Name]] ([relative/path/to/document.md](relative/path/to/document.md)) — Short description of the relationship.
```

Project Altas intentionally keeps both Obsidian wiki links and Markdown repository links because the documentation is designed to work equally well in Obsidian, GitHub, and any standard Markdown viewer. Wiki links provide excellent local knowledge navigation, while Markdown links provide portable repository navigation. Together they maximize portability without sacrificing usability.

Related documents should include both link forms and describe the relationship between documents rather than merely list filenames. Markdown links should display the repository path and use a path relative to the document containing the link. When useful, documents should point backward to the foundations on which they depend and forward to the documents they enable.

## 7. Document Lifecycle

- **Draft:** The document is being developed and may contain incomplete or unapproved content.
- **Review:** The document is sufficiently complete for focused feedback and approval.
- **Approved:** The document is accepted as the current project baseline. Changes should be deliberate and appropriately scoped.
- **Deprecated:** The document is no longer current but remains available for historical context. Its replacement should be identified when one exists.

## 8. Versioning

Project Altas uses simple semantic-style versioning for documents:

- **Major version:** A large change to meaning, scope, or structure.
- **Minor version:** A new section or meaningful clarification that preserves the document's primary intent.
- **Patch version:** A correction to typos, grammar, wording, or formatting that does not change meaning.

Filenames should remain stable as documents evolve. The version belongs inside the document, while Git provides the complete history of changes.

## 9. Naming Conventions

- Use numbered prefixes when they provide a helpful reading order.
- Use stable filenames.
- Avoid version numbers in filenames.
- Use clear, descriptive names.
- Folder names may use numeric prefixes for ordering.
- Official document filenames should remain readable in both Obsidian and GitHub.

Examples:

- `00-Project Charter.md`
- `01-Milestones.md`
- `02-MVP.md`
- `Documentation Standards.md`

## 10. Writing Principles

- Write for humans first.
- Prefer clarity over jargon.
- Be concise but not vague.
- Avoid marketing language.
- Separate concepts from implementation.
- Use tables for comparison.
- Use diagrams when they improve understanding.
- Add a blank line before Markdown lists to satisfy MD032 and improve readability.
- Keep each document focused on one responsibility.

## 11. Cross-Document Relationships

Project Altas documentation should form a useful knowledge graph rather than a collection of isolated files. Every official document should identify meaningful related documents in its `Document Information` section.

Backward links show the foundations, decisions, or source documents on which the current document depends. Forward links show the documents, designs, or releases that the current document enables. Links should support useful navigation; exhaustive linking should be avoided when it does not clarify a meaningful relationship.

## 12. When to Create an ADR

Create an Architecture Decision Record when:

- There are multiple reasonable technical options.
- The decision has long-term architectural impact.
- Future readers would need to understand why the choice was made.

Do not create an ADR for:

- Simple implementation details.
- Obvious choices.
- Temporary experiments.
- Product scope decisions that belong in MVP or roadmap documents.

An ADR should capture the context, considered options, decision, and consequences once the architectural choice is stable enough to preserve.

## 13. When to Update Documentation

Update official documentation when:

- Project scope changes.
- Architecture changes.
- Stable decisions are made.
- Interfaces or workflows change.
- A document becomes misleading or stale.

Do not update official documentation for:

- Temporary experiments.
- Unvalidated ideas.
- Half-finished prototypes.

Working observations should remain in `notes/` until they become stable knowledge that belongs in an official document.

## 14. Documentation Maintenance Workflow

### Documentation Maintenance Philosophy

Project Altas documentation is a connected knowledge graph rather than a collection of isolated files. Every approved document becomes part of that graph. Creating or significantly changing one document may therefore require reviewing related documents to preserve consistency and useful navigation.

Documentation maintenance is part of normal engineering work rather than a separate documentation activity.

### Maintenance Triggers

Related Documents in affected documents should be reviewed for consistency when:

1. A new official document is approved.
2. A major document revision changes scope or purpose.
3. Architecture changes significantly.
4. A milestone is completed or redefined.
5. An ADR is approved or deprecated.

### Standard Workflow

1. Create or update the document.
2. Complete or verify its `Document Information` section.
3. Review Related Documents in the new document.
4. Review Related Documents in all affected documents.
5. Add, remove, or refine relationships where they improve navigation.
6. Verify that the documentation graph remains coherent.
7. Commit all related documentation updates together as one documentation change.

### Maintenance Principles

- Review before updating.
- Prefer meaningful relationships over exhaustive linking.
- Avoid duplicate information.
- Preserve stable filenames.
- Keep navigation intentional.
- Update only documents that are genuinely affected.

### AI-Assisted Maintenance

AI assistants such as Codex may be used to:

- Identify affected documents.
- Review documentation consistency.
- Suggest relationship updates.
- Perform targeted edits.
- Preserve approved document structure.
- Avoid unnecessary rewrites.

> Documentation maintenance is part of engineering. Every approved document should strengthen the overall documentation graph rather than exist in isolation.

## 15. AI Collaboration Guidelines

- AI can draft, edit, and review documentation.
- Humans approve final decisions.
- Approved documents should receive targeted edits instead of full rewrites.
- AI should preserve approved structure unless explicitly asked to redesign it.
- Large rewrites require explicit approval.
- Architectural decisions should be captured in ADRs once stable.

AI-assisted changes should follow the same standards for accuracy, scope, review, and maintainability as human-authored changes.

## 16. Documentation Checklist

- [ ] The document has a clear purpose.
- [ ] The document is stored in the correct folder.
- [ ] Terminology is consistent with related documents.
- [ ] The document avoids unnecessary duplication.
- [ ] The intended audience is appropriate and identified.
- [ ] A complete `Document Information` section is included.
- [ ] Related Documents include both Obsidian wiki links and relative Markdown repository links and describe meaningful relationships.
- [ ] Markdown lists are preceded by a blank line.
- [ ] The version and status are correct.
- [ ] The writing is concise and professional.

## Document Information

**Status:** Approved

**Version:** 1.0

**Owner:** Project Altas

**Audience:** Contributors

**Created:** 2026-07-09

**Last Updated:** 2026-07-09

**Related Documents:**

- [[00-Project Charter]] ([../00-product/00-Project Charter.md](<../00-product/00-Project Charter.md>)) — Defines the mission and values that guide the documentation culture.
- [[01-Milestones]] ([../00-product/01-Milestones.md](../00-product/01-Milestones.md)) — Defines the learning roadmap that documentation should support.
- [[02-MVP]] ([../00-product/02-MVP.md](../00-product/02-MVP.md)) — Defines the first release whose documentation should follow these standards.
- [[00-Tech Stack]] ([../01-architecture/00-Tech Stack.md](<../01-architecture/00-Tech Stack.md>)) — Applies these standards to the project's technology direction.
