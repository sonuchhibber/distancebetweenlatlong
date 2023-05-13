from geopy.distance import geodesic
import streamlit as st
from io import StringIO
import csv
import pandas as pd

c=[]
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    c=dataframe.values.tolist()
else:
    st.write("Upload file")

i=1
while i<len(c):
    st.write(geodesic(eval(c[i][0]),eval(c[i][1])).km)
    i+=1
    
