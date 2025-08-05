import speech_recognition as sr
import streamlit as st

questions = [
    "Client's full name?",
    "Diagnosis?",
    "Services required?",
    "Living situation?",
    "Support goals?",
    "Evacuation point?",
    "Alerts to be aware of?",
    "Allergies?"
]

def run_voice_intake():
    recognizer = sr.Recognizer()
    responses = {}
    st.session_state.setdefault('current_question', 0)

    if st.session_state.current_question < len(questions):
        question = questions[st.session_state.current_question]
        st.markdown(f"### 🗣️ {question}")

        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("🎤 Start Recording"):
                with sr.Microphone() as source:
                    st.info("Recording... Speak now. You have up to 2 minutes.")
                    try:
                        audio = recognizer.listen(source, timeout=3, phrase_time_limit=120)
                        response = recognizer.recognize_google(audio)
                        st.success(f"You said: {response}")
                        responses[question] = response
                        st.session_state.current_question += 1
                    except sr.UnknownValueError:
                        st.error("Sorry, I couldn't understand. Please try again.")
                    except sr.WaitTimeoutError:
                        st.error("Listening timed out. Try again.")
        with col2:
            if st.button("⏭️ Skip / Next Question"):
                st.session_state.current_question += 1

    elif st.session_state.current_question >= len(questions):
        st.success("✅ Voice intake complete.")
        return responses

    return responses
