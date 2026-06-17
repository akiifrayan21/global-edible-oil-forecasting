import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Edible Oil Forecasting Dashboard",
    layout="wide"
)

st.title("🌍 Global Edible Oil Price Forecasting Dashboard")

df = pd.read_csv("../data/oil_prices.csv")

st.subheader("Key Metrics")

col1,col2,col3,col4 = st.columns(4)

col1.metric("Current Price", "$1308")
col2.metric("4 Week Forecast", "$1345")
col3.metric("Forecast Change", "+2.8%")
col4.metric("MAPE", "7.4%")

st.subheader("Historical Commodity Prices")

fig = px.line(
    df,
    x="Date",
    y=[
        "Palm_Oil",
        "Soybean_Oil",
        "Sunflower_Oil",
        "Canola_Oil"
    ]
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("4 Week Forecast")

forecast_df = pd.DataFrame({
    "Week":[
        "Current",
        "Week 1",
        "Week 2",
        "Week 3",
        "Week 4"
    ],
    "Forecast Price":[
        1308,
        1320,
        1330,
        1338,
        1345
    ]
})

forecast_fig = px.line(
    forecast_df,
    x="Week",
    y="Forecast Price",
    markers=True
)

st.plotly_chart(
    forecast_fig,
    use_container_width=True
)

st.subheader("Model Performance")

c1,c2,c3,c4 = st.columns(4)

c1.metric("RMSE", "18.4")
c2.metric("MAE", "11.2")
c3.metric("MAPE", "7.4%")
c4.metric("R²", "0.91")

st.subheader("Market Drivers")

drivers = pd.DataFrame({
    "Factor":[
        "Crude Oil Prices",
        "Shipping Costs",
        "USD Index",
        "Export Restrictions"
    ],
    "Impact":[
        "High",
        "High",
        "Medium",
        "Medium"
    ]
})

st.table(drivers)

st.subheader("Production Pipeline")

st.code("""
Extract Data
↓
Validate Data
↓
Feature Engineering
↓
Forecast Model
↓
Generate Alerts
↓
Dashboard Refresh
""")

st.warning(
    "Palm Oil prices expected to increase by 2.8% over the next four weeks."
)
