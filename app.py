import streamlit as st
import plotly.express as px

from database import get_bookings, get_branches, get_services, get_payments
from metrics import (
    clean_data,
    total_bookings,
    completed_bookings,
    cancelled_bookings,
    cancellation_rate,
    booking_status_summary
)

# -------------------
# CONFIG
# -------------------
st.set_page_config(page_title="Booking Dashboard", layout="wide")

st.title("📊 Booking Intelligence Dashboard")

# -------------------
# LOAD DATA
# -------------------
bookings = clean_data(get_bookings())
branches = get_branches()
services = get_services()
payments = get_payments()

if bookings.empty:
    st.warning("No data available")
    st.stop()

# =========================================================
# KPI SECTION
# =========================================================
st.subheader("📌 Key Metrics")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Bookings", total_bookings(bookings))
c2.metric("Completed", completed_bookings(bookings))
c3.metric("Cancelled", cancelled_bookings(bookings))
c4.metric("Cancellation %", cancellation_rate(bookings))

st.divider()

# =========================================================
# 1. BOOKING STATUS (BAR WITH LABELS)
# =========================================================
st.subheader("📊 Booking Status Breakdown")

status_df = booking_status_summary(bookings)

fig1 = px.bar(
    status_df,
    x="booking_status",
    y="count",
    color="booking_status",
    text="count",   # 👈 DATA LABELS
    title="Booking Status Distribution"
)

fig1.update_traces(textposition="outside")  # 👈 label position

st.plotly_chart(fig1, use_container_width=True)

# =========================================================
# 2. TOP BRANCHES (IMPROVED VISUAL)
# =========================================================
st.subheader("🏢 Top Branch Performance")

branch_df = bookings.merge(branches, on="branch_id", how="left")

branch_summary = branch_df["branch_name"].value_counts().reset_index()
branch_summary.columns = ["Branch", "Bookings"]

fig2 = px.bar(
    branch_summary,
    x="Branch",
    y="Bookings",
    text="Bookings",   # 👈 labels
    title="Bookings by Branch"
)

fig2.update_traces(textposition="outside")

st.plotly_chart(fig2, use_container_width=True)

# =========================================================
# 3. SERVICE MIX (DONUT CHART)
# =========================================================
st.subheader("🛎️ Service Distribution")

service_df = bookings.merge(services, on="service_id", how="left")

service_summary = service_df["service_tier"].value_counts().reset_index()
service_summary.columns = ["Tier", "Bookings"]

fig3 = px.pie(
    service_summary,
    names="Tier",
    values="Bookings",
    hole=0.4,   # 👈 makes it donut
    title="Service Tier Distribution"
)

st.plotly_chart(fig3, use_container_width=True)

# =========================================================
# 4. PAYMENT STATUS (PIE)
# =========================================================
st.subheader("💳 Payment Status")

payment_summary = payments["payment_status"].value_counts().reset_index()
payment_summary.columns = ["Status", "Count"]

fig4 = px.pie(
    payment_summary,
    names="Status",
    values="Count",
    title="Payment Distribution"
)

st.plotly_chart(fig4, use_container_width=True)

# =========================================================
# 5. TOP INSIGHT TABLE (NEW ADDITION)
# =========================================================
st.subheader("📄 Top Branch Insight Table")

top_table = branch_summary.sort_values("Bookings", ascending=False).head(5)

st.dataframe(top_table, use_container_width=True)


st.subheader("🏢 Branch-wise Booking Status")

# Merge bookings with branches
branch_status_df = bookings.merge(branches, on="branch_id", how="left")

# Create grouped data
branch_status_summary = branch_status_df.groupby(
    ["branch_name", "booking_status"]
).size().reset_index(name="count")

# Stacked bar chart
fig5 = px.bar(
    branch_status_summary,
    x="branch_name",
    y="count",
    color="booking_status",
    barmode="stack",
    text="count",
    title="Branch-wise Booking Status Distribution"
)

fig5.update_traces(textposition="inside")

st.plotly_chart(fig5, use_container_width=True)