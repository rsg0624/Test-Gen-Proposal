
import streamlit as st
from generate_text import generate_proposal

st.set_page_config(page_title="Momar Gen AI Proposal Generator", layout="centered")
st.title("🤖 Momar AI Product Assistant")

client_type = st.text_input("Client Type (e.g., Food Processing, Logistics Hub)")
issue = st.text_area("Describe the Maintenance Challenge")

if st.button("Recommend Product"):
    proposal = generate_proposal(client_type, issue)
    st.markdown("---")
    st.markdown(proposal)
