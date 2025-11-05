import streamlit as st


#UI
st.title("Calculator")
st.write("Enter a number:")

#input
n = st.number_input("Enter an integer", value = 1, step = 1)

#results

square = n ** 2
cube = n ** 3
fifth_power = n ** 5

#Displaying

st.write(f"The square of {n} is : {square}")
st.write(f"The cube of {n} is : {cube}")
st.write(f"The fifth power of {n} is : {fifth_power}")
