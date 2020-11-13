import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.title("Streamlit App for EDA")


path = st.text_input('file name/path')


loaded = False

if path:
    try:
        df = pd.read_csv(path)       
        loaded = True
    except:
        st.write("No such file found") 
        


reps = ['Dataframe','Column Statistics','Distribution Plot','Grouped Distribution Plot','Bar Plot','Correlation Heatmap','Scatter Plot']


if loaded:

    
    
    representation = st.selectbox('Representation',list(reps))

    if representation == 'Dataframe':
        selection = st.multiselect('columns',list(df.columns),default=list(df.columns))
        st.write(df[selection])

    elif representation == 'Column Statistics':
        st.write(df.describe()) 

    elif representation == 'Distribution Plot':    
        option = st.selectbox('columns',list(df.columns))
        if option:
            fig, ax = plt.subplots()
            sns.distplot(df[option])
            st.pyplot(fig)

    elif representation == 'Grouped Distribution Plot':       
        option = st.selectbox('columns',list(df.columns))
        groupby = st.selectbox('groupby',list(df.columns))


        if option:
            if groupby:
                values = df[groupby].unique()

                if len(values) < 20:

                    fig, ax = plt.subplots()

                    for val in values:
                        sns.distplot(df[df[groupby] == val][option])

                    st.pyplot(fig)        
                else:
                    st.write('too many values for column')    

    elif representation == 'Bar Plot':       
        X = st.selectbox('X-column',list(df.columns))
        Y = st.selectbox('Y-column',list(df.columns))

        if len(df[X].unique()) < 25:

            fig, ax = plt.subplots()
            sns.barplot(x = X, y = Y, data = df)
            st.pyplot(fig)
        else:
            st.write('too many values for column') 


    elif representation == 'Correlation Heatmap':    
        fig, ax = plt.subplots()    
        sns.heatmap(df.corr(),annot=True)     
        st.pyplot(fig)



    elif representation == 'Scatter Plot':    
        X = st.selectbox('X-column',list(df.columns))
        Y = st.selectbox('Y-column',list(df.columns))
        groupby = st.selectbox('Group by',list(df.columns))
        

        fig, ax = plt.subplots()    
        sns.scatterplot(data=df, x = X, y = Y,hue = groupby)     
        st.pyplot(fig)   
