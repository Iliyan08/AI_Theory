
import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "your-openai-api-key"

# Streamlit App Configuration
st.set_page_config(page_title="Custom GPT Interface", layout="centered")

# Title and Description
st.title("Custom GPT Interface")
st.markdown("""
Welcome to the custom GPT application! Enter your query below to receive a response powered by your fine-tuned GPT model.
""")

# User Input
user_input = st.text_area("Enter your query here:", placeholder="Type your question or prompt...")

# Submit Button
if st.button("Get Response"):
    if user_input.strip():
        try:
            # Call the custom GPT model (assuming it's hosted or accessible via API)
            response = openai.Completion.create(
                engine="custom-gpt-model",  # Replace with your model's engine name
                prompt=user_input,
                max_tokens=150,
                n=1,
                stop=None,
                temperature=0.7
            )

            # Display the response
            st.markdown("**Response:**")
            st.write(response.choices[0].text.strip())
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a query before submitting.")

# Footer
st.markdown("---")
st.markdown("Created with ❤️ using [Streamlit](https://streamlit.io/)")