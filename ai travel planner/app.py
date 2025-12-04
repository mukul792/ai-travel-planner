import streamlit as st
from src.core.planner import TravelPlanner
from dotenv import load_dotenv

st.set_page_config(page_title="AI Travel Planner")
st.title("AI Travel Itinerary Planner")
st.write("Plan your trip itinerary by entering your city and number of days")

load_dotenv()

with st.form("planner_form"):
    city = st.text_input("Enter the city name for your trip")
    days = st.number_input("Number of days for your trip", min_value=1, max_value=30, value=1)
    
    submitted = st.form_submit_button("Generate itinerary")

    if submitted:
        if city:
            planner = TravelPlanner()
            planner.set_city(city)
            planner.set_days(days)

            itinerary = planner.create_itinerary()

            st.subheader("📄 Your Itinerary")
            st.markdown(itinerary)
        else:
            st.warning("Please enter a city name to continue")
