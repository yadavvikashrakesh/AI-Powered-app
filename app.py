import streamlit as st

from utils.ai import get_ai_response
from utils.prompts import create_app_prompt


# --------------------------------
# Page Configuration
# --------------------------------

st.set_page_config(
    page_title="AppForge AI",
    page_icon="🚀",
    layout="wide"
)


# --------------------------------
# Custom Header
# --------------------------------

st.title("🚀 APPFORGE AI")

st.subheader(
    "AI-POWERED APP DEVELOPMENT ASSISTANT"
)

st.write(
    "Turn your app idea into an understandable "
    "development plan, starter code and learning roadmap."
)


# --------------------------------
# Get Hugging Face Token
# --------------------------------

try:
    hf_token = st.secrets["HF_TOKEN"]

except Exception:
    st.error(
        "❌ HF_TOKEN not found. "
        "Please add your Hugging Face token "
        "to .streamlit/secrets.toml"
    )
    st.stop()


# --------------------------------
# User Input
# --------------------------------

idea = st.text_area(
    "💡 Describe your app idea",
    placeholder=(
        "Example: I want to build an AI Resume Analyzer."
    ),
    height=150
)


# --------------------------------
# Generate AI Response
# --------------------------------

if st.button("🚀 Analyze My Idea", use_container_width=True):

    if not idea.strip():

        st.warning(
            "⚠️ Please enter an app idea."
        )

    else:

        prompt = create_app_prompt(idea)

        with st.spinner(
            "🤖 AppForge AI is analyzing your idea..."
        ):

            try:

                answer = get_ai_response(
                    prompt,
                    hf_token
                )

                st.success(
                    "✅ Analysis completed!"
                )

                st.subheader(
                    "🤖 AppForge AI Response"
                )

                st.markdown(answer)

            except Exception as e:

                st.error(
                    f"❌ Hugging Face Error: {e}"
                )