
import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from numerize.numerize import numerize
import time
from streamlit_extras.metric_cards import style_metric_cards
import plotly.graph_objs as go


#uncomment this line if you use mysql
#from query import *

st.set_page_config(page_title="Dashboard",page_icon="🌍",layout="wide")
st.header("ANALYTICAL PROCESSING, KPI, TRENDS & PREDICTIONS")

#all graphs we use custom css not streamlit 
theme_plotly = None 


# load Style css
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

#uncomment these two lines if you fetch data from mysql
#result = view_all_data()
#df=pd.DataFrame(result,columns=["Policy","Expiry","Location","State","Region","Investment","Construction","BusinessType","Earthquake","Flood","Rating","id"])

#load excel file | comment this line when  you fetch data from mysql
df=pd.read_excel('data.xlsx', sheet_name='Sheet1')

#side bar logo


#switcher

region=st.sidebar.multiselect(
    "SELECT REGION",
     options=df["Region"].unique(),
     default=df["Region"].unique(),
)
location=st.sidebar.multiselect(
    "SELECT LOCATION",
     options=df["Location"].unique(),
     default=df["Location"].unique(),
)
construction=st.sidebar.multiselect(
    "SELECT CONSTRUCTION",
     options=df["Construction"].unique(),
     default=df["Construction"].unique(),
)

df_selection=df.query(
    "Region==@region & Location==@location & Construction ==@construction"
)

#this function performs basic descriptive analytics like Mean,Mode,Sum  etc
def Home():
    with st.expander("VIEW EXCEL DATASET"):
        showData=st.multiselect('Filter: ',df_selection.columns,default=["Policy","Expiry","Location","State","Region","Investment","Construction","BusinessType","Earthquake","Flood","Rating"])
        st.dataframe(df_selection[showData],use_container_width=True)
    #compute top analytics
    total_investment = float(pd.Series(df_selection['Investment']).sum())
    investment_mode = float(pd.Series(df_selection['Investment']).mode())
    investment_mean = float(pd.Series(df_selection['Investment']).mean())
    investment_median= float(pd.Series(df_selection['Investment']).median()) 
    rating = float(pd.Series(df_selection['Rating']).sum())


    total1,total2,total3,total4,total5=st.columns(5,gap='small')
    with total1:
        st.info('Sum Investment',icon="💰")
        st.metric(label="Sum TZS",value=f"{total_investment:,.0f}")

    with total2:
        st.info('Most Investment',icon="💰")
        st.metric(label="Mode TZS",value=f"{investment_mode:,.0f}")

    with total3:
        st.info('Average',icon="💰")
        st.metric(label="Average TZS",value=f"{investment_mean:,.0f}")

    with total4:
        st.info('Central Earnings',icon="💰")
        st.metric(label="Median TZS",value=f"{investment_median:,.0f}")

    with total5:
        st.info('Ratings',icon="💰")
        st.metric(label="Rating",value=numerize(rating),help=f""" Total Rating: {rating} """)
    style_metric_cards(background_color="#FFFFFF",border_left_color="#686664",border_color="#000000",box_shadow="#F71938")

    #variable distribution Histogram
    with st.expander("DISTRIBUTIONS BY FREQUENCY"):
     df.hist(figsize=(16,8),color='#898784', zorder=2, rwidth=0.9,legend = ['Investment']);
     st.pyplot()

