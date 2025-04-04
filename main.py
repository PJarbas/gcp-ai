import os
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import List
from dotenv import load_dotenv

load_dotenv()

# https://ai.google.dev/gemini-api/docs/migrate

client = genai.Client(api_key="your-key")


class AIExplanation(BaseModel):
    explanation: str = Field(description="A simple explanation of AI.")
    key_concepts: List[str] = Field(description="List of key concepts related to AI.")


# --- Dynamic Prompt and System Instruction ---
system_instruction = """
You are a helpful and informative AI assistant.
Your goal is to answer user questions clearly and concisely.
When explaining complex topics, break them down into simpler terms.
You will provide your response in a structured JSON format as defined by the user's schema.
"""

dynamic_prompt = "Explain how Artificial Intelligence (AI) works in simple terms for someone with no technical background. Please format your response as a JSON object with fields 'explanation' (string) and 'key_concepts' (list of strings)."

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=dynamic_prompt,
    config=types.GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=1,
        response_mime_type="application/json",
        response_schema=AIExplanation
    ),
)

print(response.text)
