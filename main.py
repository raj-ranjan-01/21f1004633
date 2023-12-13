import streamlit as st

def find_largest_number(number1,number2,number3):
  return max(number1, number2, number3)

st.title('Find the Largest Number')
st.write("Enter three numbers below:")

number1 = st.number_input('Enter first number')
number2 = st.number_input('Enter second number')
number3 = st.number_input('Enter third number')

if st.button('Find Largest'):
  largest = find_largest_number(number1, number2, number3)
  st.success(f'The largest number is: {largest}')
