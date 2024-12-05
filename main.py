import streamlit as st
import plotly.express as px

def get_data(days):
    dates = ["2024-12-01", "2024-12-02", "2024-12-03"]
    temperatures = [10, 11, 15]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures

st.title("Upcoming Weather Forecast")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

d, t = get_data(days)

figure = px.line(x=d, y=t,
                 labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)