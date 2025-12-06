# ADR-006: Exercise Structure and Solution Provision

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-05
- **Feature:** physical-ai-robotics-textbook
- **Context:** To support hands-on learning and knowledge retention for the "Physical AI & Humanoid Robotics Textbook", a consistent approach to integrating exercises and providing solutions within the textbook content is required.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

Each chapter will include 2-5 exercises, designed to range in difficulty and encourage practical application. Exercises will be embedded directly within the chapter's Markdown/MDX file, with clear and unambiguous prompts, explicit expected outcomes, and accurate, well-explained solutions provided immediately within the textbook content itself.

<!-- For technology stacks, list all components:
     - Framework: Next.js 14 (App Router)
     - Styling: Tailwind CSS v3
     - Deployment: Vercel
     - State Management: React Context (start simple)
-->

## Consequences

### Positive

-   **Immediate Feedback**: Solutions are readily available for self-assessment, enhancing the learning experience.
-   **Integrated Learning**: Exercises and solutions are seamlessly part of the content flow, reducing context switching.
-   **Simplified Access**: No external links or separate repositories required for exercises or solutions.
-   **Author Guidance**: Clear structure for exercise creation and solution writing.

<!-- Example: Integrated tooling, excellent DX, fast deploys, strong TypeScript support -->

### Negative

-   **"Spoilers"**: Solutions being immediately visible might reduce the challenge for some learners.
-   **Complexity for Interactive Exercises**: Embedding highly interactive or complex coding challenges might be limited by Markdown/MDX capabilities without significant custom development.
-   **Content Bloat**: Including solutions directly increases the overall length of chapter files.

<!-- Example: Vendor lock-in to Vercel, framework coupling, learning curve -->

## Alternatives Considered

-   **Separate Solution Repository**: Solutions could be hosted in a separate Git repository; provides more challenge but adds friction for learners and increases maintenance complexity.
-   **External Exercise Platform**: Integration with platforms like CodePen, Jupyter notebooks, or custom web apps; offers greater interactivity but adds external dependencies, cost, and integration overhead.
-   **No Solutions Provided**: Leaves learners to figure out solutions entirely; might be too challenging for a self-paced textbook without instructor support.

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
