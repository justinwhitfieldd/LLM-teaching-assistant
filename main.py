import streamlit as st
import initializeLLM as LLM
import time

# Added the PATENT Lab banner on the top
st.image("Resources/banner-new.png", caption=None, width=None, use_column_width="auto", clamp=False, channels="RGB", output_format="auto")
st.divider()

# Here we added the title of the app with the logo
col1, col2, col3 = st.columns([2,1,6])
with col2:
    st.image("Resources/logo.png", caption=None, width=None, use_column_width="auto", clamp=False, channels="RGB", output_format="auto")
with col3:
    st.header("Bully - Teaching Assistant")
st.divider()

# Introduced the bot application
col1, col2, col3 = st.columns([1,9,2])
with col1:
    st.image("Resources/logo.png", caption=None, width=None, use_column_width="auto", clamp=False, channels="RGB", output_format="auto")
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

# This markdown is for the user and assistant to reverse the direction of the text-alignment
st.markdown(
    """ <style>
            .st-emotion-cache-janbn0 {
            flex-direction: row-reverse;
            text-align: right;}
        </style>""", unsafe_allow_html=True)


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # generate LLM response
    response = LLM.get_response_wFunction(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
