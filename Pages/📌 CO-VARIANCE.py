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


def load_data():
    return pd.read_excel('regression.xlsx')
df = load_data()
selected_column = st.selectbox('SELECT INPUT X FEATURE', df.select_dtypes("number").columns)
X = sm.add_constant(df[selected_column])  # Adding a constant for intercept

# Fitting the model
model = sm.OLS(df['Projects'],X).fit()


c1,c2,c3,c4=st.columns(4)
# Printing general intercept
c1.metric("INTERCEPT:",f"{model.params[0]:,.4f}")

# Printing R-squared
c2.metric("R SQUARED",f"{model.rsquared:,.2f}",delta="is it strong relationship ?")

# Printing adjusted R-squared
c3.metric("ADJUSTED R",f"{model.rsquared_adj:,.3f}",)

# Printing standard error
c4.metric("STANDARD ERROR",f"{model.bse[0]:,.4f}")

# Printing correlation coefficient
 

style_metric_cards(background_color="#FFFFFF",border_left_color="#686664")

b1,b2=st.columns(2)
# Printing predicted values
data = {
    'X feature':selected_column,
    'Prediction': model.predict(X),
    'Residuals':model.resid
}
