# ADR-001: Why Docusaurus

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-05
- **Feature:** physical-ai-robotics-textbook
- **Context:** The project requires creating a comprehensive 12-chapter online textbook on Physical AI & Humanoid Robotics. Key requirements include interactive content, accessibility (WCAG 2.1 AA), efficient navigation, integrated search, responsive design, and maintainability.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

Docusaurus will be used as the static site generator for the textbook. This decision encompasses using Docusaurus's core functionalities for documentation, its plugin ecosystem for search and other features, and its theme customization capabilities.

<!-- For technology stacks, list all components:
     - Framework: Next.js 14 (App Router)
     - Styling: Tailwind CSS v3
     - Deployment: Vercel
     - State Management: React Context (start simple)
-->

## Consequences

### Positive

-   **Ease of Documentation**: Markdown/MDX native support simplifies content authoring.
-   **Built-in Features**: Provides out-of-box navigation, search, and versioning capabilities.
-   **Community Support**: Large active community and comprehensive documentation.
-   **Performance**: Generates static HTML, leading to fast load times and good SEO.
-   **Accessibility**: Provides a good foundation for meeting WCAG 2.1 AA standards.
-   **Maintainability**: Standardized structure and conventions reduce maintenance overhead.

<!-- Example: Integrated tooling, excellent DX, fast deploys, strong TypeScript support -->

### Negative

-   **Customization Limitations**: While customizable, deeply custom UI/UX might require more effort than a completely custom React app.
-   **Dependency on Docusaurus Ecosystem**: Tied to Docusaurus's release cycles and feature set.
-   **Learning Curve**: New contributors may need to learn Docusaurus conventions.

<!-- Example: Vendor lock-in to Vercel, framework coupling, learning curve -->

## Alternatives Considered

-   **Custom React/Next.js Application**: Full control over UI/UX, but higher development effort for core features (navigation, search, markdown rendering, build pipeline).
-   **Jekyll/Hugo/MkDocs**: Other static site generators; Docusaurus was preferred for its React foundation (easier custom components) and strong focus on documentation.
-   **GitBook**: Commercial platform, potentially higher cost, less control over hosting and build pipeline.

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
