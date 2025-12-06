# ADR-003: Chapter Structure Format

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-05
- **Feature:** physical-ai-robotics-textbook
- **Context:** The "Physical AI & Humanoid Robotics Textbook" requires a consistent and clear presentation of its 12 chapters to ensure educational effectiveness, maintainability, and a unified user experience within the Docusaurus platform.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

Each chapter will adhere to a defined Markdown/MDX structure. This includes a clear title, sequential chapter numbering, an introduction with learning objectives and prerequisites, main content with code examples and visual aids, embedded exercises, and a summary/conclusion. Content will reside in `docs/[chapter-slug]/index.md` files.

<!-- For technology stacks, list all components:
     - Framework: Next.js 14 (App Router)
     - Styling: Tailwind CSS v3
     - Deployment: Vercel
     - State Management: React Context (start simple)
-->

## Consequences

### Positive

-   **Educational Consistency**: Predictable structure aids learner comprehension and navigation.
-   **Maintainability**: Standardized format simplifies content updates and reviews.
-   **Automated Processing**: Enables easier generation of TOCs and potentially content validation.
-   **Author Guidance**: Provides clear guidelines for content creators.

<!-- Example: Integrated tooling, excellent DX, fast deploys, strong TypeScript support -->

### Negative

-   **Rigidity**: May constrain authors if some chapter topics naturally deviate from the standard structure.
-   **Initial Overhead**: Authors must conform to the structure, requiring initial familiarization.

<!-- Example: Vendor lock-in to Vercel, framework coupling, learning curve -->

## Alternatives Considered

-   **Free-form Content**: Chapters could have highly varied structures, offering flexibility but risking inconsistency and reduced navigability.
-   **External Content Management System (CMS)**: Using a CMS could enforce structure, but adds complexity and external dependency not aligned with static site goals.

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
