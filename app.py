import streamlit as st
import joblib
import numpy as np
t_mod=joblib.load("eth_vol (1)")
st.title("ETHERIUM COIN LOW PRICE PREDICTION!!")
st.write("""This is basically a website to predict the lowest value that an etherium coin can reach based on ..\nOpen market cost and higest price recorded in a day*""")
ip1=st.number_input("MARKET OPEN PRICE (in a day)")
ip2=st.number_input("HIGEST RECORDED PRICE (in a day)")
ls1=np.append(ip1,ip2)
op=t_mod.predict([ls1])
if st.button("PREDICT"):
  st.title(op)
   
