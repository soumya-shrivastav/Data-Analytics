import streamlit as st
import pandas as pd 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from streamlit_extras.metric_cards import style_metric_cards
#from query import *

#navicon and header
st.set_page_config(page_title="Dashboard", page_icon="📈", layout="wide")  

with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

#current date
from datetime import datetime
current_datetime = datetime.now()
formatted_date = current_datetime.strftime('%Y-%m-%d')
formatted_day = current_datetime.strftime('%A')
 
st.header(" MACHINE LEARNING WORKFLOW | MYSQL  ")
st.markdown(
 """
 <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
 <hr>

<div class="card mb-3">
<div class="card">
  <div class="card-body">
    <h3 class="card-title"style="color:#007710;"><strong>⏱ MULTIPLE REGRESSION ANALYSIS DASHBOARD</strong></h3>
    <p class="card-text">There are three features, InterestRate, UnemploymentRate and PriceIndex. The purpose is to check how far linear relationship  is between these variables, where InterestRate and UnemploymentRate are X features and IndexPrice is Y feature. This is a classification problem using probabilistic multiple regression analysis for the data that exists in mysql. Finnaly visualizing measure of Variations and Line of best fit</p>
    <p class="card-text"><small class="text-body-secondary"> </small></p>
  </div>
</div>
</div>
 <style>
    [data-testid=stSidebar] {
         color: white;
         text-size:24px;
    }
</style>
""",unsafe_allow_html=True
)

#uncomment line 1,3 and 3 if you use mysql database
#1. read data from mysql
#2. result = view_all_data()
#3. df = pd.DataFrame(result,columns=["id","year","month","interest_rate","unemployment_rate","index_price"])

df=pd.read_csv("advanced_regression.csv")
#logo


with st.sidebar:
 st.markdown(f"<h4 class='text-success'>{formatted_day}: {formatted_date}</h4>Analytics Dashboard V: 01/2023<hr>", unsafe_allow_html=True)
 




