import streamlit as st
import streamlit.components.v1 as components
import initializeLLM as LLM
import base64

# # Added the PATENT Lab banner on the top
# st.image("Resources/banner-new.png", caption=None, width=None, use_column_width="auto", clamp=False, channels="RGB", output_format="auto")
# st.divider()

# # Here we added the title of the app with the logo
# col1, col2, col3 = st.columns([2,1,6])
# with col2:
#     st.image("Resources/logo.png", caption=None, width=None, use_column_width="auto", clamp=False, channels="RGB", output_format="auto")
# with col3:
#     st.header("Bully - Teaching Assistant")
# st.divider()

# # Introduced the bot application
# col1, col2, col3 = st.columns([1,9,2])
# with col1:
#     st.image("Resources/logo.png", caption=None, width=None, use_column_width="auto", clamp=False, channels="RGB", output_format="auto")
# with col2:
#     code = '''Hello bulldawgs! I am a virtual teaching assistant for
# Introduction to Computer Programming. In order for me to
# best serve you, please choose one of the following prompt.'''
#     st.code(code, language=None)

# st.write("")
# st.write("")

# # Added the prompt for the user to select and ask further questions about
# col1, col2 = st.columns([2,1])
# with col1:
#     userSelectedPrompt = st.selectbox(
#         "What can I help you today with?", key="option", options=["Explain Concept", "Code Review", "Take a Quiz"], index=0)

# # This markdown is for the user and assistant to reverse the direction of the text-alignment
# # st.markdown(
# #     """ <style>
# #             .st-emotion-cache-janbn0 {
# #             flex-direction: row-reverse;
# #             text-align: right;}
# #         </style>""", unsafe_allow_html=True)

# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # React to user input
# if prompt := st.chat_input("What is up?"):
#     # Display user message in chat message container
#     st.chat_message("user").markdown(prompt)
#     # Add user message to chat history
#     st.session_state.messages.append({"role": "user", "content": prompt})

#     # generate LLM response
#     response = LLM.get_response_wFunction(prompt)
#     # Display assistant response in chat message container
#     with st.chat_message("assistant"):
#         st.markdown(response)
#     # Add assistant response to chat history
#     st.session_state.messages.append({"role": "assistant", "content": response})

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
Introduction to Computer Programming. In order for me to
best serve you, please choose one of the following prompt.'''
    st.code(code, language=None)

st.write("")
st.write("")

# Added the prompt for the user to select and ask further questions about
col1, col2 = st.columns([2,1])
with col1:
    userSelectedPrompt = st.selectbox(
        "What can I help you today with?", key="option", options=["Explain Concept", "Code Review", "Take a Quiz"], index=0)

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
    st.markdown("**Chat**")
    cols = st.columns((6, 1))
    cols[0].text_input(
        "Chat",
        value="What's up!",
        label_visibility="collapsed",
        key="human_prompt",
    )
    cols[1].form_submit_button(
        "Submit", 
        type="primary", 
        on_click=on_click_callback, 
    )

components.html("""
<script>
const streamlitDoc = window.parent.document;

const buttons = Array.from(
    streamlitDoc.querySelectorAll('.stButton > button')
);
const submitButton = buttons.find(
    el => el.innerText === 'Submit'
);

streamlitDoc.addEventListener('keydown', function(e) {
    switch (e.key) {
        case 'Enter':
            submitButton.click();
            break;
    }
});
</script>
""", 
    height=0,
    width=0,
)