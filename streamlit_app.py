
import streamlit as st
import json
import os

st.set_page_config(page_title="Analisis Sentimen Migran", layout="wide")

st.title("Analisis Sentimen Migran Malaysia")
st.write("Sistem ini memaparkan keputusan analisis sentimen komen dari platform media sosial berkaitan warga asing di Malaysia.")

# Load JSON data
def load_json(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

# Select data source
source = st.selectbox("Pilih platform media sosial", ["YouTube", "Twitter"])
file_map = {
    "YouTube": "data/youtube_komen.json",
    "Twitter": "data/twitter_komen.json"
}

if source in file_map and os.path.exists(file_map[source]):
    data = load_json(file_map[source])
    st.metric("Jumlah Komen", len(data))

    sentiments = {"Positif": 0, "Negatif": 0, "Neutral": 0}
    for row in data:
        sentiments[row["sentimen"]] = sentiments.get(row["sentimen"], 0) + 1

    st.subheader("Ringkasan Sentimen")
    col1, col2, col3 = st.columns(3)
    col1.metric("Positif", sentiments["Positif"])
    col2.metric("Negatif", sentiments["Negatif"])
    col3.metric("Neutral", sentiments["Neutral"])

    st.subheader("Butiran Komen")
    for row in data:
        st.write(f"- **{row['sentimen']}** ({row['skor']}): {row['komen']}")

else:
    st.warning("Fail data tidak dijumpai.")
