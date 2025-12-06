---
id: 002
title: Update constitution for Physical AI & Humanoid Robotics Textbook - Phase 0: Preparation
stage: constitution
date: 2025-12-04
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: docs/constitution-update
user: user
command: /sp.constitution
labels: ["constitution", "project-setup", "robotics", "ai-textbook"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
- ./.specify/memory/constitution.md
tests:
null
---

## Prompt

/sp.constitution

Project: Physical AI & Humanoid Robotics Textbook - Phase 0: Preparation

Core principles:
- Accuracy: All tools, versions, and setup instructions must be correct and verified.
- Clarity: Instructions must be clear for students and developers with basic AI/robotics knowledge.
- Reproducibility: Anyone following this phase should be able to set up the environment successfully.
- Modularity: Preparation should support the full 13-week course structure and future Spec-Kit-Plus integrations.

Key standards:
- Audience: Students and professionals in AI, robotics, and computer science.
- Format: Docusaurus textbook deployed on GitHub Pages.
- Features to enable:
  - Module-based chapters
  - Interactive AI chatbot (RAG)
  - Spec-Kit-Plus integration for subagents and reproducibility
  - Optional content personalization
  - Optional Urdu translation

Constraints:
- Development environment must include Node.js, npm, Docusaurus CLI, Spec-Kit-Plus templates.
- GitHub repo must be initialized and ready for deployment.
- Gemini/Claude Code API key must be configured for AI content generation.
- Content architecture must follow a 13-week course structure:
  1. Introduction & Physical AI fundamentals
  2. ROS 2: Robotic nervous system
  3. Gazebo & Unity: Digital twin simulation
  4. NVIDIA Isaac: AI-Robot brain
  5. Vision-Language-Action (VLA)
  6. Capstone: Autonomous humanoid
- Include labs, exercises, quizzes, and assessment guidelines placeholders.

Success criteria:
- Clear, step-by-step Phase 0 checklist created.
- Environment setup is reproducible.
- Repo and project scaffold ready for Phase 1 content development.
- Fully Spec-Kit-Plus-ready for AI-native extensions and automation.

/exit

## Response snapshot

The project constitution has been updated to version 1.1.0. This is a MINOR version bump due to significant content changes for a new project phase.

Files flagged for manual follow-up (consistency checks):
- .specify/templates/plan-template.md: ⚠ pending
- .specify/templates/spec-template.md: ⚠ pending
- .specify/templates/tasks-template.md: ⚠ pending
- .specify/templates/commands/sp.implement.md: ⚠ pending
- .specify/templates/commands/sp.git.commit_pr.md: ⚠ pending
- .specify/templates/commands/sp.constitution.md: ⚠ pending
- .specify/templates/commands/sp.clarify.md: ⚠ pending
- .specify/templates/commands/sp.checklist.md: ⚠ pending
- .specify/templates/commands/sp.adr.md: ⚠ pending
- .specify/templates/commands/sp.plan.md: ⚠ pending
- .specify/templates/commands/sp.phr.md: ⚠ pending
- .specify/templates/commands/sp.specify.md: ⚠ pending
- .specify/templates/commands/sp.tasks.md: ⚠ pending
- .specify/templates/commands/sp.analyze.md: ⚠ pending

Suggested commit message:
docs: amend constitution to v1.1.0 (Phase 0: Preparation for Physical AI & Humanoid Robotics Textbook)

## Outcome

- ✅ Impact: Updated project constitution for a new phase.
- 🧪 Tests: N/A
- 📁 Files: ./.specify/memory/constitution.md
- 🔁 Next prompts: N/A
- 🧠 Reflection: Successfully updated the constitution with new project details and created a PHR.

## Evaluation notes (flywheel)

- Failure modes observed: None.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
