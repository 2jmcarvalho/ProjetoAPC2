import streamlit as st
from transformers import Conversation

def main():
    st.title("ChatGPT with Streamlit")
    st.write("Talk to me!")

    user_input = st.text_input("You:", "")

    if st.button("Send"):
        if user_input.strip() != "":
            with st.spinner("Thinking..."):
                conversation = Conversation("User", "ChatGPT", user_input)
                conversation.add_user_input(user_input)
                response = conversation.generate_response()
            st.text_area("ChatGPT:", value=response, height=150, max_chars=None, key=None)

if __name__ == "__main__":
    main()
