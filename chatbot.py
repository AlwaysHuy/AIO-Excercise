import streamlit as st
from hugchat import hugchat
from hugchat.login import Login

st.title('Simple ChatBot')

# Sidebar for login
with st.sidebar:
    st.title('HugChat Login')
    hf_email = st.text_input('Enter Email:')
    hf_pass = st.text_input('Enter Password:', type='password')
    
    if not (hf_email and hf_pass):
        st.warning('Please enter your account information!')
    else:
        st.success('Proceed to entering your prompt message!')
        
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

# Function to generate response
@st.cache_data(ttl=86400)  # Cache data for 1 day (86400 seconds)
def generate_response(prompt_input, email, passwd):
    sign = Login(email, passwd)
    cookies = sign.login()
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    response = chatbot.chat(prompt_input)
    
    # Extract only the serializable data from the Message object
    serializable_response = {
        'text': response.text,  # Assuming text attribute exists
        # Add more attributes as needed based on actual structure
    }
    
    return serializable_response

# Main interaction with the chatbot
if hf_email and hf_pass:
    prompt = st.text_input("Your message:", disabled=not (hf_email and hf_pass))
    if prompt:
        with st.chat_message("user"):
            st.write(prompt)
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = generate_response(prompt, hf_email, hf_pass)
                st.write(response['text'])  # Display the text part of the response
                st.session_state.messages.append({"role": "assistant", "content": response['text']})







     