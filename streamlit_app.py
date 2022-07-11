import streamlit
streamlit.title("My Mom's new Healthy Diner")
streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega 3 and Blueberry oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket smoothy')
streamlit.text('🐔Hard boiled free-range egg')
streamlit.text('🥑🍞Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')




import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
