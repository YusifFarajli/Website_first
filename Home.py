import streamlit as st
import pandas as pd
st.set_page_config(layout='wide')
col1,col2 =st.columns(2)
with col1 :
    st.image("images/photo.png",)
with col2:
    st.title("Ardit Sulce")
    content="""
    "Lorem ipsum dolor sit amet,
     consectetur adipiscing elit. Quisque quis facilisis velit. Nunc justo lorem, feugiat molestie faucibus ac, 
     consequat nec magna. Praesent convallis tortor et tortor dapibus, a tincidunt felis finibus. Quisque purus nisl, 
     malesuada id lacinia nec, sollicitudin ut eros. Mauris mollis mauris in felis viverra, eget pulvinar lorem porta. 
     Sed id ullamcorper massa, eget tempus libero. Proin eu rhoncus mauris. Mauris ac pharetra turpis..
    """
    st.info(content)

col3,empty_col,col4=st.columns([1.5,0.5,1.5])
df =pd.read_csv("data.csv",sep=";")

with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[Source code](https;//pythonhow.com)")

with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[Source code](https;//pythonhow.com)")

