import streamlit as st

def page_header(title: str, size: float, weight: int, top: int = 30, bottom: int = 20) -> None:
    """For custom page headers/titles."""
    st.markdown(f"""
    <h1 style="text-align: center; font-size: {size}rem; margin-top: -{top}px;  margin-bottom: {bottom}px; font-weight: {weight}">
    {title}
    </h1>
    """, unsafe_allow_html=True)

def translate_role(user_role: str) -> str:
    """Translates the role for the Streamlit app."""
    return "assistant" if user_role == "model" else user_role