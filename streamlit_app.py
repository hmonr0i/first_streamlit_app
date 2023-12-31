import streamlit
import pandas 
import requests
import snowflake.connector
import requests
from urllib.error import URLError

streamlit.title('My Mom´s New Healthy Diner')

streamlit.text('🥣  Omega 3 y avena con arándanos')
streamlit.text('🥗 Batido de col rizada, espinacas y rúcula')
streamlit.text('🐔 Huevo duro de gallinas camperas')
streamlit.text('🥑🍞 Totada de Aguacate')

streamlit.header('🍌🥭 Prepara tu propio batido de frutas 🥝🍇')



my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fuits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show )

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

streamlit.header('Fruityvice Fruit Advice!')

try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')

    if not fruit_choice:
        streamlit.error("Please select a fruit to get information.")
    else:
        back_from_function = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)
except URLError as e:
    streamlit.error("There was an error with the URL.")
        

#streamlit.stop()
streamlit.header("The fruit load list contains:")
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("SELECT * FROM fruit_load_list")
         return my_cur.fetchall()


if streamlit.button('Get Fruit Load List'):
     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
     my_data_rows = get_fruit_load_list()
     streamlit.dataframe(my_data_rows)





def insert_row_snowflake(new_fruit,connection):
    with connection.cursor() as my_cur:
         my_cur.execute("insert into fruit_load_list values('"+ new_fruit +"')")
         return "Thanks for adding " + new_fruit
        
add_my_fruit = streamlit.text_input('What fruit would you like to add?')        
if streamlit.button('Add a Fruit to the list'):
     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])   
     back_from_function = insert_row_snowflake(add_my_fruit, my_cnx) 
     streamlit.text(back_from_function)

streamlit.write('Thanks for adding ', add_my_fruit)


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
