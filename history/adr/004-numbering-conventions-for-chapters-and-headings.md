# ADR-004: Numbering Conventions for Chapters and Headings

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-05
- **Feature:** physical-ai-robotics-textbook
- **Context:** To ensure clarity, logical flow, and ease of navigation for the "Physical AI & Humanoid Robotics Textbook", a consistent approach to chapter and heading numbering is essential for both authors and readers. This directly impacts Docusaurus's ability to generate accurate Tables of Contents.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

Chapters will be numbered sequentially starting from 01 (e.g., "01 Introduction"). Within each chapter, a strict hierarchical heading structure will be enforced: H1 for the chapter title, H2 for major sections, H3 for subsections, and so on.

<!-- For technology stacks, list all components:
     - Framework: Next.js 14 (App Router)
     - Styling: Tailwind CSS v3
     - Deployment: Vercel
     - State Management: React Context (start simple)
-->

## Consequences

### Positive

-   **Improved Readability**: Clear structure aids reader comprehension and makes content easier to follow.
-   **Enhanced Navigation**: Docusaurus can automatically generate accurate and navigable global (sidebar) and local (in-page) Tables of Contents.
-   **Content Consistency**: Standardizes how content is organized, simplifying authoring and review.
-   **Professionalism**: Contributes to a polished and professional presentation of the textbook.

<!-- Example: Integrated tooling, excellent DX, fast deploys, strong TypeScript support -->

### Negative

-   **Author Discipline**: Requires authors to strictly adhere to the conventions, which may require tooling or review.
-   **Refactoring Overhead**: Changes to chapter order or major section hierarchy might necessitate renumbering.

<!-- Example: Vendor lock-in to Vercel, framework coupling, learning curve -->

## Alternatives Considered

-   **Unstructured Numbering**: No strict numbering for chapters or inconsistent heading levels; would lead to confusion, poor navigation, and manual TOC creation.
-   **Alternative Hierarchical Systems**: Other numbering schemes (e.g., 1.1, 1.1.1) were considered but the current H1/H2/H3 mapping to chapter/section/subsection is simpler for Markdown and Docusaurus.

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
