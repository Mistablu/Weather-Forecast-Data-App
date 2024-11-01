import streamlit as st
import plotly.express as px
st.title("weather forecast for the next days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

dates=["2022-25-10","2022-26-10","2022-27-10","2022-28-10",]
temperatures = [10,11,12,13]
temperatures = [days*i for i in temperatures]

figure = px.line(x=dates,y=temperatures,labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)

