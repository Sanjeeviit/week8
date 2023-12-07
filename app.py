#import streamlit as st
st.title("Sanjeev Streamlit Calculator")
#def addition(a+b):
  #return a+b
  
#a = st.number_input('first number')
#b = st.number_input('second number')
import streamlit as st

st.title("Calculator")

def addition(a, b):
    return a + b

a = st.number_input('Enter the first number')
b = st.number_input('Enter the second number')

result = addition(a, b)

st.write(f"The result of addition is: {result}")
