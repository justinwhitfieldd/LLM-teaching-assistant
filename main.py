import streamlit as st
import streamlit.components.v1 as components
import initializeLLM as LLM
import base64

def load_css():
    with open("Resources/styles.css", "r") as f:
        css = f"<style>{f.read()}</style>"
        st.markdown(css, unsafe_allow_html=True)

def initialize_session_state():
    if "history" not in st.session_state:
        st.session_state.history = []

def get_last_human_response():
   # Iterate through history in reverse order
   for idx in range(len(st.session_state.history) - 1, -1, -1):
       # Get the current history item
       item = st.session_state.history[idx]
       # Check if the item is from the "human" role
       if item['role'] == 'human':
           return item['content']
   return None

def on_click_callback():
    human_prompt = st.session_state.human_prompt
    st.session_state.history.append({"role": "user", "content": human_prompt})
    if st.session_state.user_selected_prompt == None:
        response = LLM.get_response_wFunction(human_prompt)
        st.session_state.history.append({"role": "assistant", "content": response})
    elif st.session_state.user_selected_prompt == "Explain Concept":
        modified_prompt = "Please provide a detailed explanation about " + human_prompt + " that a naive high school student can comprehend. Also, please provide a couple of code examples to use them along with the explanation."
        response = LLM.get_response_wFunction(modified_prompt)
        st.session_state.history.append({"role": "assistant", "content": response})
        st.session_state.user_selected_prompt = None
    elif st.session_state.user_selected_prompt == "Quiz Time":
        quiz_prompt = "Please prepare a multiple-choice question about " + human_prompt + " with four possible choice as A, B, C, and D. Three of them should be incorrect, and only one should be correct. Make sure to list each choice option on a separate line."
        quiz_prompt = LLM.get_response_wFunction(quiz_prompt)
        quiz_modified_prompt = quiz_prompt + "<br> <br> Enter the correct response as (A,B,C,D) for the above quiz question"
        st.session_state.history.append({"role": "assistant", "content": quiz_modified_prompt})
        assistant_correct_answer = "Can you provide a single alphabet for the correct choice for the follwoing multiple-choice question. <br>" + quiz_prompt
        quiz_correct_answer = LLM.get_response_wFunction(assistant_correct_answer)
        st.session_state.history.append({"role": "assistant", "content": quiz_correct_answer})
        # user_response = get_last_human_response()
        # while user_response != None:
        #     user_response = get_last_human_response()
        #human_response = st.session_state.human_prompt
        #st.session_state.history.append({"role": "user", "content": human_response})
        
        # Need to do something about the call_back based on human_prompt and see if it's related to quiz or not
        # One idea is to check if the human_prompt = A, B, C or D and if it's then it's related to Quiz 
        # OR use a global variable to trigger the second part of Quiz again
        last_message = st.session_state.history[-1]
        if last_message["role"] == 'human':
            st.session_state.history.append({"role": "assistant", "content": last_message["content"]})
        # if user_response:
        #     if quiz_correct_answer.lower() == user_response.lower():
        #         response = "Great Job! That's corect way to go!"
        #         st.session_state.history.append({"role": "assistant", "content": response})
        #         st.session_state.user_selected_prompt = None
        #     else:
        #         response = "I'm sorry, but the correct answer is - Option " + quiz_correct_answer
        #         st.session_state.history.append({"role": "assistant", "content": response})
        #         st.session_state.user_selected_prompt = None



        # Check the last message and see if the "human" has responded. and then make sure it's A, B, C, or D. Keep asking them until they do.
        #check_user_response()




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

# Introduced the bot application
col1, col2, col3 = st.columns([1,9,2])
with col1:
    st.image("Resources/ai_icon.png", caption=None, width=None, use_column_width="auto", clamp=False, channels="RGB", output_format="auto")
with col2:
    code = '''Hello bulldawgs! I am a virtual teaching assistant for
Introduction to Computer Programming.'''
    st.code(code, language=None)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    st.session_state.user_selected_prompt = st.radio("You can choose one of the following prompt if you would like:", (None, "Explain Concept", "Quiz Time"),index=0)
    st.markdown("") 
    st.markdown("")

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