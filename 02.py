import streamlit as st
import leafmap.foliumap as leafmap
from ohsome import OhsomeClient
import geopandas as gpd
import io

update_date='2024-08-21'

def save_geojson_with_bytesio(dataframe):
    #Function to return bytesIO of the geojson
    shp = io.BytesIO()
    dataframe.to_file(shp,  driver='GeoJSON')
    return shp

st.set_page_config(
    page_title="OSM Data comparision",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded")
st.write('# Data visulization')

style_1 = {
    "stroke": True,
    "color":"#0000ff",
    "fill": True,
    "fillColor": "#0000ff",
    "fillOpacity": .3,
}

style_2 = {
    "stroke": True,
    "color":"#ff0000",
    "fill": True,
    "fillColor": "#ff0000",
    "fillOpacity": .3,
}

def drawMap():
    st.write('# Compare OSM data '+str(st.session_state.year)+' - 2024')
    st.write('It can take up to several minutes downloading data from the server')
    client = OhsomeClient()
    m = leafmap.Map(center=[0,0],zoom=0)
    response = client.elements.geometry.post(bboxes=[st.session_state.bound[0],st.session_state.bound[1],st.session_state.bound[2],st.session_state.bound[3]],
		time=str(st.session_state.year)+"-01-01,"+update_date,
		filter="building=* and geometry:polygon")
    response_gdf = response.as_dataframe().reset_index()
    response_00=response_gdf[response_gdf['@snapshotTimestamp']==str(st.session_state.year)+"-01-01"]
    response_01=response_gdf[response_gdf['@snapshotTimestamp']==update_date]
    m.add_gdf(response_00,style=style_1 ,layer_name=st.session_state['year'])
    m.add_gdf(response_01,style=style_2 ,layer_name='2024')

    m.to_streamlit()

    st.download_button(
        label="Download full data",
        data=save_geojson_with_bytesio(response_gdf),
        file_name='osm_data_full'+'.geojson',
        mime='application/geo+json',
    )

    col_1,col_2=st.columns(2)
    with col_1:
        st.write('## Year '+ str(st.session_state['year']))
        st.write('number of building is '+str(response_00.count()[0]))
        st.download_button(
            label="Download data "+str(st.session_state['year']),
            data=save_geojson_with_bytesio(response_00),
            file_name='osm_data'+str(st.session_state['year'])+'.geojson',
            mime='application/geo+json',
        )
    with col_2:
        st.write('## Year 2024')
        st.write('number of building is '+str(response_01.count()[0]))
        st.download_button(
            label="Download data 2024",
            data=save_geojson_with_bytesio(response_01),
            file_name='osm_data_2024'+'.geojson',
            mime='application/geo+json',
        )


if "year" not in st.session_state or "bound" not in st.session_state:
    st.write('you have to select year first!')
else:
    drawMap()
