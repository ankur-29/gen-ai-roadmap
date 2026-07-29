import streamlit as st

st.title("Product Form")

st.sidebar.header("Add Product")

product_name = st.sidebar.text_input("Product Name")

category = st.sidebar.selectbox(
    "Category",
    [
        "Electronics",
        "Books",
        "Clothing",
        "Food",
        "Sports"
    ]
)

price = st.sidebar.number_input(
    "Price",
    min_value=0.0,
    value=0.0
)

if st.sidebar.button("Add Product"):

    st.success("Product Added Successfully!")

    st.write("### Product Details")

    st.write(f"**Product Name:** {product_name}")
    st.write(f"**Category:** {category}")
    st.write(f"**Price:** ₹{price:.2f}")