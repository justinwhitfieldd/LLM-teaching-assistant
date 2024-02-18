import streamlit as st
import initializeLLM as LLM

st.image("Resources/banner.png", caption=None, width=None, use_column_width="auto", clamp=False, channels="RGB", output_format="auto")

col1, col2 = st.columns([1,8])
with col1:
    st.image("Resources/logo.png", caption=None, width=None, use_column_width="auto", clamp=False, channels="RGB", output_format="auto")
with col2:
    st.header("Bully - Teaching Assistant")

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

col1, col2 = st.columns([2,1])
with col1:
    userSelectedPrompt = st.selectbox(
        "What can I help you today with?", key="prompt", options=["Explain Concept", "Code Review", "Take a Quiz"], index=0)

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
