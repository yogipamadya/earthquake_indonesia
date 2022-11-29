import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")


st.title("Heatmap of Earthquake in Indonesia 2000-2020")

filepath = "https://raw.githubusercontent.com/yogipamadya/earthquake_indonesia/main/eq2000-2020.csv"
m = leafmap.Map(center=[0,113],zoom=4)
m.add_heatmap(
    filepath,
    latitude="latitude",
    longitude="longitude",
    value="mag",
    name="map",
    radius=15,
)

m.to_streamlit(height=700)
