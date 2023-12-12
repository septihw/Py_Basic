import streamlit as st 

st.title("Septi.HW")

inventory_menu = ["sosial media", "portofolio", "abcd"]
selected = st.sidebar.selectbox("Inventory", inventory_menu)

if selected == inventory_menu[0]: 
    st.write("instgaram")

if selected == inventory_menu[1]:
    st.write("foto")

if selected == inventory_menu[2]:
    st.write("efg")