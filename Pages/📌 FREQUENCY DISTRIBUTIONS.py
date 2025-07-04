import streamlit as st
import pandas as pd 
import plotly.express as px

#config page layout to wide
st.set_page_config(page_title="Home",page_icon="",layout="wide")

st.success("**FREQUENCY DISTRIBUTION TABLE**")

#load css
theme_plotly = None 

# load Style css
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

#load dataframe
df=pd.read_csv("sales.csv")

with st.expander("🔎 VIEW ORIGINAL DATASET"):
 showData=st.multiselect("",df.columns,default=["OrderDate","Region","City","Category","Product","Quantity","UnitPrice","TotalPrice"]) 
 st.dataframe(df[showData],use_container_width=True)

#side navigation 
st.sidebar.image("data/logo1.png")

#calculate a frequency
frequency=df.UnitPrice.value_counts().sort_index()

#calculate percentage frequency %
percentage_frequency=frequency/len(df.UnitPrice)*100

#calculate cumulative frequency
cumulative_frequency=frequency.cumsum()

#relative frequency
relative_frequency=frequency/len(df.UnitPrice)

#cumulative relative frequency
cumulative_relative_frequency=relative_frequency.cumsum()


