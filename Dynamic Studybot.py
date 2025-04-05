import streamlit as st
import random

# --- Language Selection ---
language = st.radio("Choose your preferred language:", ["English", "Spanish", "French"])

# --- Objective Input ---
# --- Mascot Selection ---
mascots = {
    "Abe (History Hero)": {"icon": "🧔", "voice": "Let’s explore the past and learn from it."},
    "Beaky the Beaker (Science Buddy)": {"icon": "🧪", "voice": "Science is all about asking why and experimenting!"},
    "Infinity (Math Mentor)": {"icon": "♾️", "voice": "Let’s solve this step by step together."},
    "Lexi the Book (ELA Guide)": {"icon": "📘", "voice": "Every question is a new story to tell."},
    "Owlbot (General Helper)": {"icon": "🦉", "voice": "Wisdom begins with curiosity."}
}
mascot_choice = st.selectbox("Choose your learning companion:", list(mascots.keys()))
mascot_icon = mascots[mascot_choice]["icon"]
mascot_voice = mascots[mascot_choice]["voice"]
st.title(f"{mascot_icon} Dynamic StudyBot")
st.write(f"You are learning with {mascot_choice}. {mascot_voice}")
objectives_input = st.text_area("Learning Objectives:")

if objectives_input:
    objectives = [line.strip() for line in objectives_input.splitlines() if line.strip()]

 # Initialize current objective
if 'current_objective' not in st.session_state:
    st.session_state.current_objective = random.choice(objectives)

# --- Confidence Check ---
st.subheader("🧭 Confidence Check")
confidence = st.slider("How confident are you about this topic?", 1, 5)

# --- Natural Language Question Generator ---
def generate_simple_question(objective):
    if "sherman" in objective.lower():
        return "How did General Sherman's 'total war' strategy change life for people in the South?"
    elif "gettysburg" in objective.lower():
        return "What happened at Gettysburg, and why do people say it changed the direction of the Civil War?"
    elif "vicksburg" in objective.lower():
        return "What was the Siege of Vicksburg, and how did it help the Union win the war?"
    elif "emancipation" in objective.lower():
        return "How did the Emancipation Proclamation affect enslaved people and the goals of the war?"
    elif "african american soldiers" in objective.lower():
        return "What challenges and contributions did African American soldiers face during the Civil War?"
    elif "anaconda" in objective.lower():
        return "Why was the Union’s strategy called the 'Anaconda Plan,' and what was it supposed to do to the South?"
    else:
        return f"Can you explain what this topic means and why it was important during the Civil War?"

def generate_moderate_question(objective):
    return f"What important things happened in this topic? How did they affect the people or the outcome of the war?"

def generate_advanced_question(objective):
    return f"What were the deeper effects of this topic—like how it changed politics, society, or the economy? Who was impacted most, and how?"

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
        "gettysburg": "Gettysburg was a major battle in the Civil War. It was a turning point because the Union stopped the Confederates.",
        "anaconda": "The Anaconda Plan was a Union strategy to block Southern ports and cut off supplies, squeezing the South like a snake."
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
def is_answer_good(response, objective):
    keywords = {
        "sherman": ["sherman", "total war", "destruction", "south", "march"],
        "gettysburg": ["gettysburg", "turning point", "union", "confederacy", "battle"],
        "vicksburg": ["vicksburg", "mississippi", "control", "siege", "confederacy"],
        "emancipation": ["emancipation", "slavery", "freedom", "lincoln"],
        "african american soldiers": ["african american", "black soldiers", "union", "carney", "bazaar"],
        "anaconda": ["anaconda", "blockade", "ports", "supplies", "strategy"]
    }
    matched = []
    for key in keywords:
        if key in objective.lower():
            matched = keywords[key]
            break
    response_words = response.lower().split()
    return any(word in response_words for word in matched)

def generate_scaffold(objective, response):
    return f"{mascot_icon} Good effort. Let's think deeper: who was affected by this? What changed because of it?"

st.subheader(f"🧠 Question from {mascot_choice}")
st.write(f"{mascot_icon} {question}")

# --- Student Response ---
student_response = st.text_input("Your answer:")

if st.button("Submit"):
    if "snake" in student_response.lower() and "anaconda" in st.session_state.current_objective.lower():
        st.info("That's a creative image! 🐍 But the Anaconda Plan wasn’t about real snakes. It was a Union strategy to block Southern ports and squeeze the Confederacy, like a snake wrapping around its prey.")
    elif is_answer_good(student_response, st.session_state.current_objective):
        st.success(f"{mascot_icon} Great answer! ✅")
        st.session_state.current_objective = random.choice(objectives)
    else:
        st.warning(generate_scaffold(st.session_state.current_objective, student_response))

if st.button("Need a Hint?"):
    st.info(generate_scaffold(st.session_state.current_objective, ""))

