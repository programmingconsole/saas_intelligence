# ai_utils.py
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# -----------------------------
# Generate Summary
# -----------------------------
def generate_summary(text: str) -> str:
    """
    Generate a summary for the given text.
    """
    messages = [
        {"role": "system", "content": "You are a helpful assistant that summarizes text concisely."},
        {"role": "user", "content": text}
    ]
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    return response.choices[0].message.content

# -----------------------------
# Generate Questions
# -----------------------------
def generate_questions(text: str) -> list:
    """
    Generate a list of questions based on the text.
    """
    messages = [
        {"role": "system", "content": "You are a helpful assistant that creates questions from the given text."},
        {"role": "user", "content": text}
    ]
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    questions_text = response.choices[0].message.content
    questions = [q.strip() for q in questions_text.split("\n") if q.strip()]
    return questions

# -----------------------------
# Continuous Chat (Synchronous)
# -----------------------------
def chat_with_ai(prompt: str, history: list) -> str:
    """
    Chat with AI using continuous context.
    """
    # Append user message
    history.append({"role": "user", "content": prompt})

    # Synchronous response
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=history
    )

    reply = response.choices[0].message.content
    # Save assistant reply in history
    history.append({"role": "assistant", "content": reply})

    return reply