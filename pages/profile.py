import streamlit as st
import mysql.connector
import pandas as pd
from Signlingo import current_user, conn

if "page" not in st.session_state:
    st.session_state["page"] = "profilepage"
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="aj19@SQL",
    database="signlingo"
     )

    # Create a cursor object
    cursor = conn.cursor()

    # Execute a SQL query
    # print({st.session_state['current_user']['username']})
    cursor.execute(f"SELECT * FROM profile where username = '{current_user['username']}'")
    
    profiledata = cursor.fetchall()
    columns = [i[0] for i in cursor.description]

    cursor.execute(f"SELECT * FROM learntletter where username = '{current_user['username']}'")
    
    letterslearnt = cursor.fetchall()
    llcolumns = [i[0] for i in cursor.description]

    cursor.execute(f"SELECT * FROM learntword where username = '{current_user['username']}'")
    wordslearnt = cursor.fetchall()
    wlcolumns = [i[0] for i in cursor.description]

   
    


    df = pd.DataFrame(profiledata, columns=columns) 
    lettersLearnt = pd.DataFrame(letterslearnt, columns= llcolumns) 

    wordsLearnt = pd.DataFrame(wordslearnt,columns=wlcolumns )
    
    

    # Display the data in Streamlit
    st.write(df)
  
    st.write(wordsLearnt)
    
    st.write(lettersLearnt)
    
    
    conn.close()

st.session_state["page"] = "profilepage"