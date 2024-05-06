import pickle
from pathlib import Path
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities.hasher import Hasher
import pandas

if stauth:
    print(stauth)
else:
    print("streamlit_authenticator as stauth None")

names = ["Aroosh","Shubhham"]
usernames = ["ajos","shubham"]
passwords = ["abc123", "def456"]

hashed_passwords = Hasher(passwords).generate()
file_path = Path(__file__).parent / "hashed_pw.pkl"

with file_path.open("wb") as file:
    pickle.dump(hashed_passwords,file)