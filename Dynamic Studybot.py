import streamlit as st
import random

# --- Language Selection ---
language = st.radio("Choose your preferred language:", ["English", "Spanish", "French"])

# --- Objective Input ---
st.title("📚 Dynamic StudyBot")
st.write("Paste your learning objectives below. One per line.")
objectives_input = st.text_area("Learning Objectives:")

if objectives_input:
    objectives = [line.strip() for line in objectives_input.splitlines() if line.strip()]

    # Initialize current objective
    if 'current_objective' not in st.session_state:
        st.session_state.current_objective = random.choice(objectives)

    # --- Question Generation ---
    def generate_question(objective, language="English"):
        return f"What do you know about: {objective}?"

    # --- Scaffolding Logic ---
    def is_answer_good(response):
        return len(response.strip().split()) > 5  # simple length check

    def generate_scaffold(objective, response):
        return f"That's a good start. Think about this: {objective.lower()}—what's one example you remember?"

    question = generate_question(st.session_state.current_objective, language)
    st.subheader("🧠 Question")
    st.write(question)

    # --- Student Response ---
    student_response = st.text_input("Your answer:")

    if st.button("Submit"):
        if is_answer_good(student_response):
            st.success("Great answer! ✅")
            st.session_state.current_objective = random.choice(objectives)
        else:
            st.warning(generate_scaffold(st.session_state.current_objective, student_response))
else:
    st.info("Please paste in at least one learning objective to begin.")