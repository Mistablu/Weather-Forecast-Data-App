import streamlit as st
import plotly.express as px
from functions import get_data

st.title("weather forecast for the next days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        data = get_data(place,days)
        if option == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in data]
            dates = [dict["dt_txt"] for dict in data]
            figure = px.line(x=dates,y=temperatures,labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                    "Rain": "images/rain.png", "Snow": "images/snow.png"}
            conditions = [dict["weather"][0]["main"] for dict in data]
            image_paths = [images[condition] for condition in conditions]
            st.image(image_paths,width=115)
    except IndexError:
        st.write("This city does not exist")
        


