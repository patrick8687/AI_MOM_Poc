MOM_PROMPT = """
You are a professional corporate assistant.

Create clear and concise Minutes of Meeting (MoM) from the transcript below.

Rules:
- Use professional tone
- No repetition
- Use bullet points
- Use Markdown formatting
- Include:
  • Key Discussion Points
  • Decisions
  • Action Items (with owner if mentioned)

Transcript:
{transcript}
"""