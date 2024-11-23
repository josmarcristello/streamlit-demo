import streamlit as st

st.set_page_config(page_title="TNA - Experimental Interface", page_icon=":arrow_up:")

st.title("TNA - Experimental Interface")

version = "Beta 0.1.0"
release_date = "2024-November-22"

release_date = "2024-July-14"
# Display the version and release date in the app
st.success(f"**Version:** {version}. **Release Date:** {release_date}", icon="🔧")
