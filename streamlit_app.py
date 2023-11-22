import streamlit
streamlit.title('My Mom´s New Healthy Diner')

streamlit.text('🥣  Omega 3 y avena con arándanos')
streamlit.text('🥗 Batido de col rizada, espinacas y rúcula')
streamlit.text('🐔 Huevo duro de gallinas camperas')
streamlit.text('🥑🍞 Totada de Aguacate')

streamlit.header('🍌🥭 Prepara tu propio batido de frutas 🥝🍇')


import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
