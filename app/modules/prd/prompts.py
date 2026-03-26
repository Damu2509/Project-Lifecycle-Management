VALIDATION_PROMPT = """\
You are a senior product strategist. Analyze the following product idea and provide:
- Key competitors in the space
- Market saturation level (low / medium / high)
- Opportunity assessment and potential gaps

Be concise but insightful. Use bullet points.

Idea: {idea}
"""

PRD_PROMPT = """\
You are a senior product manager. Generate a detailed Product Requirements Document (PRD) for the following idea.

Include these sections:
1. Problem Statement
2. Target Users
3. Core Features (prioritized)
4. User Stories
5. Acceptance Criteria for each story

Be thorough yet practical. Use markdown formatting.

Idea: {idea}
"""

SUGGESTION_PROMPT = """\
You are a product innovation consultant. Based on the following idea, suggest a \
differentiation strategy that would give this product a competitive edge.

Cover:
- Unique value proposition
- Recommended tech differentiators
- Go-to-market angle

Be actionable and specific.

Idea: {idea}
"""
