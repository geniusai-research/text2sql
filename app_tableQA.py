import streamlit as st
import pandas as pd


# install tableqa with pip/pip3 install tableqa
from tableqa.agent import Agent 
# running this for the first will start downloading of transformer models and weights
# after that they will be saved in cache and loaded from there  

st.title("Streamlit app")


path = st.text_input('File name/path:')


loaded = False

if path:

    try:
        df = pd.read_csv(path)
        st.write(df)
        loaded = True


        columns = df.columns

        for col in columns: # converting binary columns into string columns

            if df[col].nunique() < 3:
                if df[col].dtypes != 'object':

                    column = df[col]

                    new_column = []

                    for val in column:
                        if val == 1:
                            new_column.append('yes')
                        else:  
                            new_column.append('no')

                    df[col] = new_column  

        agent = Agent(df) # creating tableqa agent object with the given dataframe
    except:
        st.write("No such file found") 
        



if loaded:
    query = st.text_input('Instruction')
    if query:
        st.write("** agent response : **",agent.get_query(query))
        # currently returning the SQL query, for result use agent.query_db(query)
       