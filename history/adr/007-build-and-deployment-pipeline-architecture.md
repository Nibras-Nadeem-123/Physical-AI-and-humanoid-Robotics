# ADR-007: Build and Deployment Pipeline Architecture

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-05
- **Feature:** physical-ai-robotics-textbook
- **Context:** The "Physical AI & Humanoid Robotics Textbook" is a Docusaurus-based static website. A robust and efficient build and deployment pipeline is required to convert the Markdown/MDX source into a deliverable static site, ensuring performance, reliability, and ease of publishing.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

The build and deployment pipeline will be centered around Docusaurus's static site generation capabilities. The Docusaurus build command will produce a `build/` directory containing all static assets (HTML, CSS, JS, images). This `build/` output will then be deployed to a static web hosting service (e.g., GitHub Pages, Netlify, Vercel). The pipeline will include steps for content review, accessibility audits, performance optimization, and final build verification.

<!-- For technology stacks, list all components:
     - Framework: Next.js 14 (App Router)
     - Styling: Tailwind CSS v3
     - Deployment: Vercel
     - State Management: React Context (start simple)
-->

## Consequences

### Positive

-   **Performance**: Static assets lead to fast loading times and reduced server load.
-   **Security**: Minimal server-side logic reduces attack surface inherent in static sites.
-   **Scalability**: Static hosting services are highly scalable and cost-effective.
-   **Simplicity**: Docusaurus abstracts much of the build complexity, simplifying the pipeline.
-   **Cost-effectiveness**: Static hosting is generally inexpensive.

<!-- Example: Integrated tooling, excellent DX, fast deploys, strong TypeScript support -->

### Negative

-   **No Server-Side Logic**: Cannot support dynamic user interactions that require a backend without external services.
-   **Build Time**: For very large textbooks, the Docusaurus build process might take significant time.
-   **Deployment Configuration**: Initial setup of the deployment to a static host requires configuration (e.g., `package.json` scripts, CI/CD workflows).

<!-- Example: Vendor lock-in to Vercel, framework coupling, learning curve -->

## Alternatives Considered

-   **Server-Side Rendering (SSR) / Dynamic Site Generation (DSG)**: Using frameworks like Next.js or Gatsby with SSR/DSG could provide more dynamic capabilities but adds server-side complexity and potentially higher hosting costs.
-   **Custom Build Scripts**: Developing entirely custom build scripts using Webpack/Rollup; offers maximum control but significantly increases development and maintenance effort compared to Docusaurus's built-in system.
-   **Monolithic Application Deployment**: Deploying the entire Node.js Docusaurus application to a traditional web server; reduces benefits of static hosting (performance, security, cost).

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
