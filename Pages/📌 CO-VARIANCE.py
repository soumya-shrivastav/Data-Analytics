import streamlit as st
import pandas as pd 
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_extras.metric_cards import style_metric_cards 
 
#navicon and header
st.set_page_config(page_title="Dashboard", page_icon="📈", layout="wide")  

st.header("COVARIANCE FOR TWO RONDOM VARIABLES")
st.success("The main objective is to measure if Number of family dependents or Wives may influence a person to supervise many projects")
 
# load CSS Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)



