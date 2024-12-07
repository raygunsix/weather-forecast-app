import streamlit as st
import plotly.express as px
from backend import get_data

images = {"Clear":"images/clear.png",
          "Clouds":"images/cloud.png",
          "Rain":"images/rain.png",
          "Snow":"images/snow.png"}

# Add ui elements
st.title("Upcoming Weather Forecast")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:

    # Get the data
    filtered_data = get_data(place, days)

    if filtered_data:

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create temp plot
            figure = px.line(x=dates, y=temperatures,
                            labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)
    else:
        status_message = st.info("No data for that city. Please try again")
