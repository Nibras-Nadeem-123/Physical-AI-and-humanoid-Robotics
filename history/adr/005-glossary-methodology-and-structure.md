# ADR-005: Glossary Methodology and Structure

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-05
- **Feature:** physical-ai-robotics-textbook
- **Context:** The "Physical AI & Humanoid Robotics Textbook" requires a centralized and easily accessible repository for technical terms and their definitions to support reader comprehension and consistent terminology usage across all 12 chapters.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

A single, comprehensive glossary will be implemented as a dedicated Markdown/MDX file (e.g., `docs/glossary/index.md`) within the Docusaurus `docs/` directory. All new or complex technical terms from any chapter will be added, defined concisely, presented alphabetically, and linked in the Docusaurus sidebar to ensure searchability and easy access.

<!-- For technology stacks, list all components:
     - Framework: Next.js 14 (App Router)
     - Styling: Tailwind CSS v3
     - Deployment: Vercel
     - State Management: React Context (start simple)
-->

## Consequences

### Positive

-   **Centralized Knowledge**: All definitions are in one place, easy for readers to find.
-   **Consistency**: Enforces consistent definitions and terminology across the textbook.
-   **Searchability**: A single location enhances search functionality for terms.
-   **Simplified Management**: Easier for authors to add and update terms in one file.
-   **Docusaurus Integration**: Seamlessly integrates into the Docusaurus navigation and search.

<!-- Example: Integrated tooling, excellent DX, fast deploys, strong TypeScript support -->

### Negative

-   **Single File Size**: A very large glossary file could potentially become unwieldy to edit manually, though Docusaurus handles rendering efficiently.
-   **Potential for Conflicts**: Multiple authors modifying a single file simultaneously could lead to merge conflicts, requiring careful version control practices.

<!-- Example: Vendor lock-in to Vercel, framework coupling, learning curve -->

## Alternatives Considered

-   **Chapter-specific Glossaries**: Each chapter could have its own mini-glossary; this would lead to fragmentation, redundancy, and make global search difficult.
-   **External Glossary Tool/Database**: Using a separate system for glossary management; adds complexity, integration overhead, and deviates from the static site generation principle.

<!-- Group alternatives by cluster:
     Alternative Stack A: Remix + styled-components + Cloudflare
     Alternative Stack B: Vite + vanilla CSS + AWS Amplify
     Why rejected: Less integrated, more setup complexity
-->

## References

- Feature Spec: /mnt/c/Users/DELL/OneDrive/Desktop/specs/002-physical-ai-robotics-textbook/spec.md
- Implementation Plan: /mnt/c/Users/DELL/OneDrive/Desktop/specs/002-physical-ai-robotics-textbook/plan.md
- Related ADRs: null
- Evaluator Evidence: null <!-- link to eval notes/PHR showing graders and outcomes -->
