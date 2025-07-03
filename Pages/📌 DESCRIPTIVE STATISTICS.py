import streamlit as st
import pandas as pd 
import plotly.express as px
import numpy as np
from streamlit_extras.metric_cards import style_metric_cards 

st.set_page_config(page_title="Dashboard ", page_icon="📈", layout="wide")  
st.header("PERCENTILES, NUMBER SUMMARY FOR CATEGORICAL DATA")
st.markdown("##")
 
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
     
df=pd.read_excel('descriptive_statistics.xlsx', sheet_name='Sheet1')

tab1, tab2 = st.tabs(["DATASET","SALES BY PERCENTILES"])

with tab1:
 with st.expander("Show Workbook"):
  #st.dataframe(df_selection,use_container_width=True)
  shwdata = st.multiselect('Filter :', df.columns, default=["SALES","ORDERDATE","STATUS","YEAR_ID","PRODUCTLINE","CUSTOMERNAME","CITY","COUNTRY"])
  st.dataframe(df[shwdata],use_container_width=True
  )

with tab2.caption("SALES BY PERCENTILES"):
 c1,c2,c3,c4,c5=st.columns(5)
 with c1:
   st.info('Percentile 25 %', icon="⏱")
   st.metric(label='USD', value=f"{np.percentile(df['SALES'], 25):,.2f}")
 with c2:
   st.info('Percentile 50 %', icon="⏱")
   st.metric(label='USD', value=f"{np.percentile(df['SALES'], 50):,.2f}")
 with c3:
   st.info('Percentile 75 %', icon="⏱")
   st.metric(label='USD', value=f"{np.percentile(df['SALES'], 75):,.2f}")
 with c4:
   st.info('Percentile 100 %', icon="⏱")
   st.metric(label='USD', value=f"{np.percentile(df['SALES'], 100):,.2f}")
 with c5:
   st.info('Percentile 0 %', icon="⏱")
   st.metric(label='USD', value=f"{np.percentile(df['SALES'], 0):,.2f}")

