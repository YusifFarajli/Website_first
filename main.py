import streamlit as st
st.set_page_config(layout='wide')
col1,col2 =st.columns(2)
with col1 :
    st.image("images/photo.png",)
with col2:
    st.title("Ardit Sulce")
    content="""
    Hi,I am a Python programmer.I study at the UNEC(University of Economics).
    """
    st.info(content)
