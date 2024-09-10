import streamlit as st
import folium
from streamlit_folium import st_folium
import datetime

st.set_page_config(
    page_title="OSM Data comparision",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded")
st.write('# Initialisation')
st.write('Firstly, zoom to the area preferable (zoom level should exceed 13)')
m = folium.Map(location=[0,0], zoom_start=0)
output = st_folium(m, width=400, height=400)
st.write('Zoom level: '+ str(output['zoom']))
st.write('Then choose the time.')
st.session_state.year_1 = st.date_input("First compare date", datetime.date(2010, 1, 1),datetime.date(2008, 1, 1),datetime.date(2024, 8, 21))
st.session_state.year_2 = st.date_input("Second compare date", datetime.date(2010, 1, 1),datetime.date(2008, 1, 1),datetime.date(2024, 8, 21))
st.session_state.key=0
if st.button("Submit"):
    if (output['zoom']>13):
        st.session_state.center=[output['center']['lng'],output['center']['lat']]
        st.session_state.bound=[output['bounds']['_southWest']['lng'],output['bounds']['_southWest']['lat'],output['bounds']['_northEast']['lng'],output['bounds']['_northEast']['lat']]
        st.write(st.session_state.bound)
        st.write(st.session_state.center)
        st.write("You selected:", st.session_state.year_1,"and", st.session_state.year_2)
        st.write("OK.")
       