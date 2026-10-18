
import requests
import streamlit as st

st.set_page_config(
    page_title="LocalBiz AI",
    page_icon="🛍️"
)

st.title("🛍️ LocalBiz AI")
st.subheader("Your AI assistant for small businesses")

st.write(
    "Create product descriptions quickly "
    "with the help of local AI."
)

product = st.text_input(
    "What is your product name?",
    placeholder="Example: Handmade cotton bag"
)

features = st.text_area(
    "Describe your product features",
    placeholder="Example: Reusable, lightweight, washable"
)

audience = st.text_input(
    "Who are your customers?",
    value="Everyday shoppers"
)

if st.button("Generate Description"):
    if not product.strip() or not features.strip():
        st.warning("Please enter the product name and features.")
    else:
        prompt = f"""
        Write an attractive but truthful product description.
        Product: {product}
        Features: {features}
        Target customers: {audience}
        Do not invent specifications or unsupported claims.
        Keep the description concise and engaging.
        """

        try:
            with st.spinner("AI is writing your description..."):
                response = requests.post(
                    "http://localhost:11434/api/generate",
                    json={
                        "model": "gemma3:1b",
                        "prompt": prompt,
                        "stream": False
                    },
                    timeout=120
                )

                response.raise_for_status()
                description = response.json()["response"]

            st.success("Description generated!")
            st.subheader("Your product description")
            st.write(description)

        except requests.RequestException:
            st.error(
                "Could not connect to Ollama. "
                "We will fix this in the next steps."
            )