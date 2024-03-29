import streamlit as st
import streamlit.components.v1 as components
import initializeLLM as LLM
import base64

userSelectedPrompt = None

def load_css():
    with open("Resources/styles.css", "r") as f:
        css = f"<style>{f.read()}</style>"
        st.markdown(css, unsafe_allow_html=True)

def initialize_session_state():
    if "history" not in st.session_state:
        st.session_state.history = []

def on_click_callback():
    human_prompt = st.session_state.human_prompt
    st.session_state.history.append({"role": "user", "content": human_prompt})
    if userSelectedPrompt == None:
        response = "Please select one of the prompt before I can proceed to help you!"
        st.session_state.history.append({"role": "assistant", "content": response})
    else:
        response = LLM.get_response_wFunction(human_prompt)
        st.session_state.history.append({"role": "assistant", "content": response})

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
    userSelectedPrompt = st.radio("In order for me to best serve you, please choose one of the following prompt:", ["Explain Concept", "Take a Quiz"],index=None,)

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