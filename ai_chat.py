import streamlit as st
from database import get_bookings, get_branches, get_services
from metrics import clean_data
from ai_insights import generate_insight

st.set_page_config(page_title="AI Insights", layout="wide")

st.title("🤖 AI Insights Engine")

bookings = clean_data(get_bookings())
branches = get_branches()
services = get_services()

if st.button("Generate AI Insights"):

    merged = bookings.merge(branches, on="branch_id", how="left") \
                     .merge(services, on="service_id", how="left")

    ai_data = merged[[
        "booking_id",
        "booking_status",
        "branch_name",
        "service_name"
    ]].head(40).to_dict(orient="records")

    result = generate_insight(ai_data)

    st.success(result)