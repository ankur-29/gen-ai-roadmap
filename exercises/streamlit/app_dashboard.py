import streamlit as st

st.title("Simple Dashboard")
st.write("Mini dashboard showing monthly sales.")

months = ["January", "February", "March", "April"]

sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

selected_month = st.selectbox( "Select Month", months)

st.metric(
    label="Sales",
    value=sales[selected_month]
)

st.bar_chart(list(sales.values()))