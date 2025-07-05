import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from scipy.stats import norm
from streamlit_extras.metric_cards import style_metric_cards


st.set_page_config(page_title="Dashboard", page_icon="📈", layout="wide")
st.header("STANDARD NORMAL DISTRIBUTION  Z~(0,1)")  
st.write("RANDOM VARIABLE & PROBABILITY DISTRIBUTIONS")

theme_plotly = None 

#sidebar
html_code = '''
<iframe src="https://free.timeanddate.com/clock/i95di01a/n71/szw160/szh160/hocfff/hbw6/cf100/hgr0/hcw2/hcd88/fan2/fas20/fdi70/mqc000/mqs3/mql13/mqw4/mqd94/mhc000/mhs3/mhl13/mhw4/mhd94/mmc000/mml5/mmw1/mmd94/hwm2/hhs2/hhb18/hms2/hml80/hmb18/hmr7/hscf09/hss1/hsl90/hsr5" frameborder="0" width="160" height="160"></iframe>

'''
st.sidebar.markdown(html_code, unsafe_allow_html=True)

# load Style css
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

