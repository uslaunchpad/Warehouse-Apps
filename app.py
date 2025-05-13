import streamlit as st
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1PwvyTVq947Bho9FfpJdzMBM94HMzFRwx4sYWmiE3p8o/edit").sheet1

# UI
st.title("Warehouse Delivery Recorder")

clients = [
    "Aegles", "Art on Scarves", "Away That Day", "By Sarah", "Cloudcha", "Doddl", "Faune", "Foldimats",
    "Gilded Bird", "GNGR Bees", "Isla & Fraser", "Made by Coopers", "Moussse", "Mustard Made", "OEST London",
    "Oxygen Boutique", "Sophie Home", "Stelar", "Thandana", "The Balcony Garden", "The Positive Planner", "Tilbea"
]

st.markdown("### Select Client:")
client_selected = st.radio("", clients)

delivery_type = st.radio("Delivery Type", ["Box", "Pallet"])

quantity = st.number_input("Quantity", min_value=1, step=1)

if st.button("Submit"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([timestamp, client_selected, delivery_type, quantity])
    st.success("Delivery recorded!")
