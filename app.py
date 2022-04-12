import streamlit as st
st.set_page_config(layout="wide")

from multiapp import MultiApp
from pages import home, user, about # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("User Upload", user.app)
app.add_app("About Project", about.app)
# The main app

app.run()