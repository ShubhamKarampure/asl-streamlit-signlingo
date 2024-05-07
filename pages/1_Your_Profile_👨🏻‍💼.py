import streamlit as st
import sqlite3
import pandas as pd

# Check if 'page' exists in session state, if not, initialize it
if "page" not in st.session_state:
    st.session_state["page"] = "profilepage"

# Connect to the SQLite database
conn = sqlite3.connect("signlingo.db")

# Create a cursor object
cursor = conn.cursor()

# Retrieve current user information from session state
current_user = st.session_state["current_user"]

# Execute SQL queries to fetch profile data, letters learnt, and words learnt
cursor.execute(f"SELECT * FROM profile WHERE username = '{current_user['username']}'")
profiledata = cursor.fetchall()
profile_columns = [i[0] for i in cursor.description]

cursor.execute(
    f"SELECT * FROM learntletter WHERE username = '{current_user['username']}'"
)
letterslearnt = cursor.fetchall()
ll_columns = [i[0] for i in cursor.description]

cursor.execute(
    f"SELECT * FROM learntword WHERE username = '{current_user['username']}'"
)
wordslearnt = cursor.fetchall()
wl_columns = [i[0] for i in cursor.description]

# Convert fetched data into pandas DataFrame for easier manipulation
df_profile = pd.DataFrame(profiledata, columns=profile_columns)
df_letters_learnt = pd.DataFrame(letterslearnt, columns=ll_columns)
df_words_learnt = pd.DataFrame(wordslearnt, columns=wl_columns)

# Display the data in Streamlit
st.write("Profile Data:")
st.write(df_profile)

st.write("Words Learnt:")
st.write(df_words_learnt)

st.write("Letters Learnt:")
st.write(df_letters_learnt)

# Close the database connection
conn.close()

# Update the page in session state
st.session_state["page"] = "profilepage"
