import streamlit as st

st.title("Price Calculator")

price = st.number_input(
    "Enter Product Price",
    min_value=0.0,
    value=1000.0
)

discount = st.slider(
    "Discount Percentage",
    min_value=0,
    max_value=90,
    value=10
)

if st.button("Calculate Price"):
    final_price = price - (price * discount / 100)

    st.success(f"Final Price: {final_price:.2f}")

    table = [
        ["Original Price", f"₹{price:.2f}"],
        ["Discount", f"{discount}%"],
        ["Final Price", f"₹{final_price:.2f}"]
    ]

    st.table(table)