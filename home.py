import streamlit as st

first_page = st.Page("01.py", title="Initialization", icon="⚙️")
second_page = st.Page("02.py", title="Data visualization", icon="💻")

pg = st.navigation([first_page,second_page])
pg.run()