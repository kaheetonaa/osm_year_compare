import streamlit as st
import folium
from streamlit_folium import st_folium
st.set_page_config(
    page_title="OSM Data comparision",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded")
st.session_state.approved=0
st.write('# Initialisation')
st.write('Firstly, zoom to the area preferable (zoom level should exceed 13)')
m = folium.Map(location=[0,0], zoom_start=0)
output = st_folium(m, width=400, height=400)
st.write('Zoom level: '+ str(output['zoom']))
st.write('Then choose the time.')
st.session_state.year = st.selectbox(
    "The year you want to compare",
    (2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023),
)
st.session_state.key=0
if st.button("Submit"):
    if (output['zoom']>13):
        st.session_state.center=[output['center']['lng'],output['center']['lat']]
        st.session_state.bound=[output['bounds']['_southWest']['lng'],output['bounds']['_southWest']['lat'],output['bounds']['_northEast']['lng'],output['bounds']['_northEast']['lat']]
        st.write(st.session_state.bound)
        st.write(st.session_state.center)
        st.write("You selected:", st.session_state.year)
        st.write("OK.")
        st.session_state.approved=1
if st.button("Proceed"):
   
   if st.session_state.approved==1:
       st.switch_page("02.py")
   else:
        st.write('You have to submit first!')
       