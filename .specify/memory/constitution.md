<!--
Version Change: 0.0.0 → 1.0.0 (MAJOR: Initial creation of the constitution)
Modified Principles: All principles are new.
Added Sections: "Writing & Content Standards", "Development Workflow"
Removed Sections: None
Templates Requiring Updates:
  - .specify/templates/plan-template.md: ✅ updated
  - .specify/templates/spec-template.md: ✅ updated
  - .specify/templates/tasks-template.md: ✅ updated
  - .specify/templates/commands/sp.clarify.md: ✅ updated
  - .specify/templates/commands/sp.constitution.md: ✅ updated
  - .specify/templates/commands/sp.specify.md: ✅ updated
Follow-up TODOs: None
-->
# Physical AI & Humanoid Robotics Textbook Constitution

## Core Principles

### I. Educational Clarity & Accessibility
Content must be clear, concise, and accessible to a diverse audience, from beginners to advanced learners. Complex topics should be explained with progressive detail, avoiding unnecessary jargon or defining it thoroughly when used. The language should be inclusive and easy to understand for a global audience.

### II. Technical Accuracy & Verifiability
All technical information, code examples, and theoretical explanations must be rigorously accurate and verifiable against current scientific and engineering knowledge. Factual correctness, logical consistency, and empirical evidence are paramount. Where claims are made, they must be supported by reliable sources or clear reasoning.

### III. Hands-on Learning & Practical Relevance
The textbook prioritizes practical application and experiential learning. Content must integrate hands-on exercises, lab activities, and real-world case studies wherever appropriate to solidify understanding. The goal is to equip readers with actionable knowledge and skills directly applicable to the field.

### IV. Consistency & Cohesion
Maintain absolute consistency in terminology, formatting, writing style, code conventions, and narrative flow across all 12 chapters and supplementary materials (glossary, exercises, diagrams). This ensures a unified and professional learning experience, minimizing cognitive load from structural inconsistencies.

### V. Continuous Improvement & Versioning
The textbook is conceived as a living document. Content will be regularly reviewed, updated, and versioned to reflect rapid advancements in Physical AI and Humanoid Robotics. Mechanisms for feedback and iteration must be in place to ensure ongoing relevance and quality.

## Writing & Content Standards

### Writing Quality Rules
-   **Clarity**: Avoid unnecessary jargon. If technical terms are used, they MUST be defined clearly in context or referenced in the glossary. Sentences should be direct and unambiguous.
-   **Conciseness**: Every word must serve a purpose. Eliminate verbose phrasing and redundant explanations.
-   **Grammar & Spelling**: Adhere strictly to standard English grammar and spelling. Automated tools (e.g., Grammarly) and human review are mandatory.
-   **Active Voice**: Prefer active voice over passive voice to make explanations more direct and engaging.

### Style Guidelines
-   **Markdown Syntax**: All content MUST use GitHub Flavored Markdown (GFM) for consistency.
-   **Heading Structure**: Chapter titles MUST use H1. Major sections within a chapter MUST use H2, and sub-sections H3, H4, etc., in a strict hierarchical order.
-   **Code Blocks**: Code examples MUST be enclosed in fenced code blocks with appropriate language highlighting specified (e.g., ````python`, ````cpp`). Code comments within examples MUST be clear and minimal.
-   **Images & Diagrams**: All visual aids MUST include descriptive alt text and captions. They must be clear, high-resolution, and directly relevant to the surrounding text.
-   **Tone**: Maintain a professional, educational, and encouraging tone throughout.

### Technical Accuracy Standards
-   **Fact-checking**: All factual assertions, statistics, and historical information MUST be meticulously fact-checked against multiple reputable sources.
-   **Code Verification**: All code examples provided MUST be tested and verified to be syntactically correct, semantically accurate, and executable in the specified environment.
-   **Scientific Rigor**: Present concepts with scientific and engineering rigor. Avoid oversimplification that leads to inaccuracy. Cite sources for complex or contested theories.

### Glossary/Exercise Consistency Rules
-   **Glossary Integration**: All new or complex technical terms introduced in any chapter MUST be added to the comprehensive glossary. Definitions MUST be concise, unambiguous, and consistent with their usage throughout the textbook.
-   **Exercise Structure**: Exercises and labs MUST have clear objectives, detailed instructions, and explicit expected outcomes. Difficulty levels SHOULD be indicated where appropriate.
-   **Solution Provision**: If solutions are provided (e.g., for self-assessment), they MUST be accurate, well-explained, and follow the same code/writing standards as the main content.

### Chapter Structure Principles
-   **Logical Flow**: Chapters MUST follow a logical progression, building knowledge incrementally from foundational concepts to advanced topics.
-   **Modular Design**: Each chapter SHOULD be designed to be reasonably self-contained, allowing readers to focus on specific areas without constant cross-referencing to previous chapters for basic understanding.
-   **Learning Outcomes**: Every chapter MUST begin with a clearly stated set of measurable learning outcomes, outlining what the reader is expected to know or be able to do upon completion.

## Development Workflow

### Collaboration and Versioning Rules
-   **Version Control**: All textbook content, code, and supplementary materials MUST be managed using Git. The central repository is the single source of truth.
-   **Branching Strategy**: A clear branching strategy (e.g., `main` for published content, `develop` for integration, `feature/X` for new chapters/major revisions, `bugfix/Y` for corrections) MUST be followed.
-   **Review Process**: All proposed changes (via Pull Requests) MUST undergo a thorough peer review by at least one other designated contributor before merging into `develop` or `main`. Reviewers MUST verify adherence to all constitution principles.
-   **Semantic Versioning**: The textbook content will adhere to semantic versioning (MAJOR.MINOR.PATCH).
    -   **MAJOR**: Significant content overhauls, reordering of chapters, or fundamental shifts in pedagogical approach.
    -   **MINOR**: Addition of new chapters, major updates to existing chapters, or significant new exercise sets.
    -   **PATCH**: Typographical corrections, minor clarifications, broken link fixes, or small updates to code examples.

### AI Rewriting and Consistency Policies
-   **Human Oversight**: Any content generated or rewritten by AI tools MUST always undergo rigorous review and approval by a human editor. The editor is responsible for ensuring accuracy, pedagogical effectiveness, originality, and alignment with the textbook's voice.
-   **Consistency Check**: AI tools utilized for content generation, rewriting, or style/grammar checks MUST be configured and trained to maintain the established tone, terminology, formatting, and stylistic guidelines outlined in this constitution.
-   **Attribution & Transparency**: While AI assistance is encouraged for efficiency, the ultimate intellectual ownership and responsibility for content accuracy rests with human authors. Internal documentation (e.g., commit messages, internal wikis) MAY note where AI tools were used to aid creation, but public-facing attribution of AI within the textbook itself is generally discouraged unless explicitly required.

## Governance

This Constitution establishes the foundational principles and standards for the "Physical AI & Humanoid Robotics Textbook" project. It supersedes all other informal practices or guidelines.

### Amendment Procedure
-   Proposed amendments to this Constitution MUST be submitted as a Pull Request to the project repository.
-   Amendments require a 2/3 majority approval from the core editorial team.
-   All amendments MUST be documented with a clear rationale and impact analysis.
-   The `CONSTITUTION_VERSION` MUST be incremented according to semantic versioning rules with each amendment.

### Compliance & Enforcement
-   All contributors are expected to read, understand, and adhere to these principles.
-   During content reviews and code reviews (Pull Requests), adherence to this Constitution MUST be explicitly verified.
-   Failure to comply may result in requests for revision or rejection of contributions.

**Version**: 1.0.0 | **Ratified**: 2025-12-05 | **Last Amended**: 2025-12-05
