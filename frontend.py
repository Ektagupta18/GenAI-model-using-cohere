import streamlit as st
import backend as bk

st.title("GenAI Project")
input=st.text_input("INPUT")
generate_button=st.button("Generate")

if generate_button:
    output=bk.get_text_output(input)
    st.write(output)