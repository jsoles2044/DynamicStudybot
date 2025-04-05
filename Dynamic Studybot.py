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

#import streamlit as st
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
        if "sherman" in objective.lower():
            return "What were some of the effects on the South caused by General Sherman's strategy of total war?"
        elif "gettysburg" in objective.lower():
            return "Why was the Battle of Gettysburg an important turning point in the Civil War?"
        elif "vicksburg" in objective.lower():
            return "How did the Siege of Vicksburg affect the South during the Civil War?"
        elif "emancipation" in objective.lower():
            return "What did the Emancipation Proclamation do, and why was it important?"
        elif "african american soldiers" in objective.lower():
            return "What role did African American soldiers play in the Civil War?"
        else:
            return f"What was the main issue or effect related to this topic: '{objective.lower()}'?"

    def generate_moderate_question(objective):
        return f"What happened during this topic, and why did it matter? Try to include causes or effects. ({objective.lower()})"

    def generate_advanced_question(objective):
        return f"What were the economic, political, or social consequences of this event or idea? Who was most affected and how? ({objective.lower()})"

    if confidence <= 2:
        question = generate_simple_question(st.session_state.current_objective)
    elif confidence == 3:
        question = generate_moderate_question(st.session_state.current_objective)
    else:
        question = generate_advanced_question(st.session_state.current_objective)

    # --- Vocabulary Support ---
    def explain_keywords(objective):
        keywords = {
            "emancipation": "Emancipation means being set free, especially from slavery.",
            "total war": "Total war is when an army destroys not just other soldiers but farms, railroads, and supplies.",
            "siege": "A siege is when an army surrounds a place and cuts off supplies to force it to give up.",
            "confederacy": "The Confederacy was the group of southern states that left the U.S. during the Civil War.",
            "union": "The Union was the northern states that stayed together during the Civil War.",
            "gettysburg": "Gettysburg was a major battle in the Civil War. It was a turning point because the Union stopped the Confederates."
        }
        found = [keywords[key] for key in keywords if key in objective.lower()]
        return found

    if st.button("Help me understand this question"):
        vocab_explanations = explain_keywords(st.session_state.current_objective)
        if vocab_explanations:
            for explanation in vocab_explanations:
                st.info(explanation)
        else:
            st.info("There are no difficult words detected in this objective.")

    # --- Scaffolding Logic ---
    def is_answer_good(response):
        return len(response.strip().split()) > 5  # simple length check

    def generate_scaffold(objective, response):
        return f"Good effort. Let's think deeper: who was affected by this? What changed because of it? ({objective.lower()})"

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

    # --- Hint Option ---
    if st.button("Need a Hint?"):
        st.info(generate_scaffold(st.session_state.current_objective, ""))
else:
    st.info("Please paste in at least one learning objective to begin.")

