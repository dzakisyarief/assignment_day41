import streamlit as st 

def get_contact():
    st.title("Contacts")
    st.write("Feel free to reach out to me through:")

    # Linkedin
    st.markdown(
        "[![Linkedin](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/dzakisyarief/)"
    )

    # GitHub
    st.markdown(
        "[![GitHub](https://img.shields.io/badge/GitHub-Profile-black)](https://github.com/dzakisyarief)"
    )

    # Email 
    st.write("📧 Email: dzakisyarief02@gmail.com")
    