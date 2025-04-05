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

# --- Confidence Check ---
st.subheader("🧭 Confidence Check")
confidence = st.slider("How confident are you about this topic?", 1, 5)

# --- Question Generation ---
def generate_simple_question(objective):
    return f"Let's start with something simple. Can you describe one fact or idea about this topic: '{objective.lower()}'?"

def generate_moderate_question(objective):
    return f"Can you explain this topic in your own words: '{objective.lower()}'? What details do you remember?"

def generate_advanced_question(objective):
    return f"Why is this topic important in history? How did it affect people or events? ({objective.lower()})"

if confidence <= 2:
    question = generate_simple_question(st.session_state.current_objective)
elif confidence == 3:
    question = generate_moderate_question(st.session_state.current_objective)
else:
    question = generate_advanced_question(st.session_state.current_objective)

# --- Scaffolding Logic ---
def is_answer_good(response):
    return len(response.strip().split()) > 5  # simple length check

def generate_scaffold(objective, response):
    return f"That's a good start. Here's a hint to help: Think about who was involved, what happened, or why it mattered. ({objective.lower()})"

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