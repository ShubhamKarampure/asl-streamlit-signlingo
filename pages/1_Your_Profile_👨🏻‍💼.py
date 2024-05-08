import streamlit as st
import sqlite3
import math
from styles import profile,letterprogress

st.markdown(profile(), unsafe_allow_html=True)
st.markdown(letterprogress(), unsafe_allow_html=True)
# Check if 'page' exists in session state, if not, initialize it
if "page" not in st.session_state:
    st.session_state["page"] = "profilepage"

st.session_state["page"] = "profilepage"

# Connect to the SQLite database
conn = sqlite3.connect("signlingo.db")

# Create a cursor object
cursor = conn.cursor()

# Retrieve current user information from session state
current_user = st.session_state["current_user"]


title = f"""
<div class="welcome-content">Hello {current_user['name'].title()}, Welcome Back!</div>
<div class="my_course_title">
    <h1>My Progress</h1>
</div>
"""
st.markdown(title,unsafe_allow_html=True)

col1,col2 = st.columns([0.5,0.5])


cursor.execute(f"SELECT * FROM Alphabet WHERE Username = '{current_user['username']}'")
rows = cursor.fetchall()  
number_of_rows = len(rows)
print(number_of_rows)

circumference = 2*math.pi*24
progress = (number_of_rows/24)*100
progress_offset = circumference - ((progress / 100) * circumference)

letter_progress = f"""
<div class="my_course_details">
  <div class="course-container letter">
    <h5>Letters</h5>
    <h3>No.of letters</h3>
    <div class="circular-progress-container">
      <svg class="circle" viewBox="0 0 52 52">
        <circle cx="26" cy="26" r="24" stroke="#006ED3" stroke-opacity="0.4" stroke-width="4" fill="none"></circle>
      </svg>
      <svg class="letter" viewBox="0  0 52 52">
        <circle cx="26" cy="26" r="24" stroke="white" stroke-width="4" stroke-linecap="round" fill="none";></circle>
      </svg>
      <span class="course-completed-no progress-text">{number_of_rows}</span>
    </div>
  </div>
</div>
<style>
.circular-progress-container .letter {{
  stroke-dasharray: {circumference}px;
  stroke-dashoffset: {progress_offset}px;
  }}
</style>
"""

with col1:
    st.markdown(letter_progress, unsafe_allow_html=True)

cursor.execute(f"SELECT * FROM Words WHERE Username = '{current_user['username']}'")
rows = cursor.fetchall()
number_of_rows = len(rows)
progress = (number_of_rows / 5) * 100
progress_offset = circumference - ((progress / 100) * circumference)

words_progress = f"""
<div class="my_course_details">
  <div class="course-container words">
    <h5>Words</h5>
    <h3>No.of Words</h3>
    <div class="circular-progress-container">
      <svg class="circle" viewBox="0 0 52 52">
        <circle cx="26" cy="26" r="24" stroke="#006ED3" stroke-opacity="0.4" stroke-width="4" fill="none"></circle>
      </svg>
      <svg class="word" viewBox="0 0 52 52">
        <circle cx="26" cy="26" r="24" stroke="white" stroke-width="4" stroke-linecap="round" fill="none";></circle>
      </svg>
      <span class="course-completed-no progress-text">{number_of_rows}</span>
    </div>
  </div>
</div>
<style>
.circular-progress-container .word {{
  stroke-dasharray: {circumference}px;
  stroke-dashoffset: {progress_offset}px;
  }}
</style>
"""

with col2:
    st.markdown(words_progress, unsafe_allow_html=True)
