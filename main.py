import streamlit as st 

st.set_page_config(layout = 'wide')
st.title("People Analytics Case Study")

st.sidebar.title("Navigation")

page = st.sidebar.radio("Page",["Introduction", 
                                        "Results", "Summary",
                                        "Contact"])

if page == "Introduction":
    import introduction
    introduction.introduction()

elif page == "Results": 
    import results
    results.get_results()

elif page == "Summary":
    import summary 
    summary.get_summary()

elif page == "Contact":
    import kontak
    kontak.get_contact()
    