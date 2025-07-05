import pandas as pd
import numpy as np
from scipy import stats
import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards
import plotly.graph_objects as go
fig = go.Figure()
 
st.set_page_config(page_title="Dashboard",page_icon="🌍",layout="wide")

st.header("**HYPOTHESIS  TESTING** UNDER T-STUDENT DISTRIBUTION CURVE, TWO TAILED TEST")  
theme_plotly = None 

st.subheader("𝑡=(𝑋 ̅−𝜇)/(𝑆⁄√𝑛)~𝑡(𝑛−1)")
# load Style css
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

#Logo
st.sidebar.image("data/logo1.png")

#read dataset
df=pd.read_excel("hypothesis.xlsx")

#drop unnecessary field
df.drop(columns=["Date"],axis=1,inplace=True)

# Steps for hypothesis testing
# 1. Formulate null and alternative hypothesis
st.info("**Null hypothesis: The average Revenue of Group A and Group B are the same.**")
st.info("**Alternative hypothesis: The average Revenue  of Group A and Group B are different.**")

# 2. Determine confidence level
confidence_level = 0.95  

# 3. Determine test statistic
# Assuming the sample size is small (<30), we'll use a t-test for independent samples.
t_stat, p_value = stats.ttest_ind(df['GroupA'], df['GroupB'])

# Basic statistics from the DataFrame
sample_mean = df.mean()
sample_std = df.std()
sample_size = df.shape[0]


import sys
if sample_size >=30 :
    st.error(f" ERROR: T student is for sample size less than 30. unable to solve for **{sample_size}** sample size")
    sys.exit()


# 4. Normal distribution and critical value
alpha = 1 - confidence_level
critical_value = stats.t.ppf(1 - alpha / 2, df=sample_size - 1)  # Two-tailed test

# Generate x values for the normal distribution curve
x = np.linspace(-4, 4, 1000)
# Generate the normal distribution curve
y = stats.t.pdf(x, df=sample_size - 1)

# 5. Compute actual value
# The t-statistic is our computed value

