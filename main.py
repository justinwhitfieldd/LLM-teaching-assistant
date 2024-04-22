import streamlit as st
import random
import initializeLLM as LLM
import base64
import time

quiz_timer = 15

def load_css():
    with open("Resources/styles.css", "r") as f:
        css = f"<style>{f.read()}</style>"
        st.markdown(css, unsafe_allow_html=True)

def initialize_session_state():
    if "history" not in st.session_state:
        st.session_state.history = []

@st.cache_data(ttl=15)
def generate_quiz_question(topic):
    quiz_prompt = "Please prepare a multiple-choice question about " + topic + " with four possible choice as A), B), C), and D). Three of them should be incorrect, and only one should be correct. Make sure to list each choice option on a separate line. Also, provide the correct answer on the next line as well."
    response = LLM.get_response_wFunction(quiz_prompt)

    #st.write(response)
    lines = response.split("\n")
    
    question = lines[0]
    options = []
    correct_answer = None

    for line in lines[1:]:
        if line.strip().startswith(("A)", "B)", "C)", "D)", "E)", "F)", "G)", "H)", "I)", "J)")):
            options.append(line.strip())
        elif line.strip().startswith("Correct answer:") or line.strip().startswith("Correct Answer:") or line.strip().startswith("correct Answer:") or line.strip().startswith("correct answer:"):
            correct_answer = line.strip().split(":", 1)[-1].strip()
            #st.write(correct_answer)

    return question, correct_answer, options, 15

def explain_concept():
    st.header("Explain Concept")
    # Implement your code to explain a concept here
    topic = st.text_input("Enter a single word topic you would like to get a detailed explanation about:")
    if topic:
        modified_prompt = "Please provide a detailed explanation about " + topic + " that a naive high school student can comprehend. Also, please provide a couple of code examples to use them along with the explanation."
        response = LLM.get_response_wFunction(modified_prompt)
        st.markdown(response, unsafe_allow_html=True)

def quiz_time():
    st.header("Quiz Time")
    topic = st.text_input("Enter the topic for the quiz:")

    if topic:
        # Generate a quiz question based on the topic
        question, answer, options, quiz_timer = generate_quiz_question(topic)
        
        st.warning('Please submit your response within 15 seconds to get the feedback otherwise it will generate a new question!:', icon="⚠️")
        st.write()
        st.write("Question:", question)
        selected_option = st.radio("Select an option:", options, index=None, key=topic)

        if selected_option is not None:
            submitted = st.button("Submit")
            if submitted:
                if selected_option == answer:
                    st.write("Correct!")
                else:
                    st.write("Incorrect. The correct answer is:", answer)
                    
                with st.empty():
                    while quiz_timer:
                        time_now = '{:02d}'.format(quiz_timer)
                        st.write(f"The time remaining to re-generate a new Quiz Question (in seconds) :{time_now}")
                        time.sleep(1)
                        quiz_timer -= 1
                    st.write(f"The time remaining to re-generate a new Quiz Question (in seconds) :{time_now}")
                    new_question = st.button("Generate New Question")
                    if new_question:
                        topic = None  # Reset the selected option
                        st.rerun()
                        quiz_time()  # Re-run the quiz_time function to generate a new question
    else:
        st.write("Please enter a topic to generate a quiz question.")


def on_click_callback():
    human_prompt = st.session_state.human_prompt
    st.session_state.history.append({"role": "user", "content": human_prompt})
    response = LLM.get_response_wFunction(human_prompt)
    st.session_state.history.append({"role": "assistant", "content": response})

def chat():
    # Introduced the bot application
    col1, col2, col3 = st.columns([1,9,2])
    with col1:
        st.image("Resources/ai_icon.png", caption=None, width=None, use_column_width="auto", clamp=False, channels="RGB", output_format="auto")
    with col2:
        code = '''Hello bulldawgs! I am a virtual teaching assistant for
    Introduction to Computer Programming.'''
        st.code(code, language=None)

    chat_placeholder = st.container()
    prompt_placeholder = st.form("chat-form")

    # Define the base64 encoded image data for the icons
    ai_icon_path = 'Resources/ai_icon.png'
    user_icon_path = 'Resources/user_icon.png'

    with open(ai_icon_path, 'rb') as f:
        ai_icon_data = f.read()
    ai_icon_base64 = base64.b64encode(ai_icon_data).decode('utf-8')

    with open(user_icon_path, 'rb') as f:
        user_icon_data = f.read()
    user_icon_base64 = base64.b64encode(user_icon_data).decode('utf-8')

    with chat_placeholder:
        for chat in st.session_state.history:
            icon_base64 = ai_icon_base64 if chat["role"] == 'assistant' else user_icon_base64
            div = f"""
                <div class="chat-row 
                    {'' if chat["role"] == 'assistant' else 'row-reverse'}">
                    <img class="chat-icon" src="data:image/png;base64,{icon_base64}"
                        width=32 height=32>
                    <div class="chat-bubble
                        {'ai-bubble' if chat["role"] == 'assistant' else 'human-bubble'}">
                            &#8203;{chat["content"]}
                    </div>
                </div>
            """
            st.markdown(div, unsafe_allow_html=True)
        
        for _ in range(3):
            st.markdown("")

    with prompt_placeholder:
        cols = st.columns((6, 1))
        cols[0].text_input(
            "Chat",
            value="Type your message here to Chatbot-TA!",
            label_visibility="collapsed",
            key="human_prompt",
        )
        cols[1].form_submit_button(
            "Submit", 
            type="primary", 
            on_click=on_click_callback, 
        )

    # New Chat Button
    if st.button("New Chat"):
        st.session_state.history = []
        st.rerun()



if __name__ == "__main__":
    load_css()
    initialize_session_state()

    # Added the PATENT Lab banner on the top
    st.image("Resources/banner-new.png", caption=None, width=None, use_column_width="auto", clamp=False, channels="RGB", output_format="auto")
    st.divider()

    # Here we added the title of the app with the logo
    col1, col2, col3 = st.columns([2,1,6])
    with col2:
        st.image("Resources/ai_icon.png", caption=None, width=None, use_column_width="auto", clamp=False, channels="RGB", output_format="auto")
    with col3:
        st.header("Bully - Teaching Assistant")
    st.divider()

    # Add a selectbox to the sidebar for the user to choose a prompt
    prompt = st.sidebar.selectbox("Select Prompt", ["Chat", "Explain Concept", "Quiz Time"])

    if prompt == "Explain Concept":
        explain_concept()
    elif prompt == "Quiz Time":
        quiz_time()
    else:
        chat()
