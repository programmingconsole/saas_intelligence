import streamlit as st
from ai_utils import generate_summary, generate_questions, chat_with_ai

st.set_page_config(page_title="AI Summary & QnA & Chat", layout="centered")
st.title("📘 AI Summary, QnA Generator & Continuous Chat 🤖")

# -----------------------------
# Text Input Section
# -----------------------------
text = st.text_area("Enter your text:", height=200)

col1, col2 = st.columns(2)

with col1:
    if st.button("Summarize"):
        if text.strip():
            with st.spinner("Generating summary..."):
                summary = generate_summary(text)
                st.success("✅ Summary Generated:")
                st.write(summary)

with col2:
    if st.button("Generate Questions"):
        if text.strip():
            with st.spinner("Generating questions..."):
                questions = generate_questions(text)
                st.success("✅ Questions Generated:")
                st.write(questions)

# -----------------------------
# Continuous Chat Section
# -----------------------------
st.subheader("💬 Continuous Chat with AI")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [{"role": "system", "content": "You are a helpful AI assistant."}]

# Display chat messages
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    elif msg["role"] == "assistant":
        with st.chat_message("assistant"):
            st.markdown(msg["content"])

# Chat input
prompt = st.chat_input("Type your message...")
if prompt:
    # Append user message
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response synchronously
    with st.chat_message("assistant"):
        reply = chat_with_ai(prompt, st.session_state.chat_history)
        st.markdown(reply)