    # __author__ = 'R. Sengupta | r_xn'
# __copyright__ = 'Copyright 2023, Ledgr | www.alphaLedgr.com'
# __credits__ = ['r_xn, s.sengupta, adasgupta@gmail.com']
# __license__ = 'Ledgr | alphaledgr.com'
# __version__ = '01.02.04'
# __maintainer__ = 'r_xn@alphaledgr.com'
# __emails__ = 'r_xn@alphaledgr.com / outreach@alphaledgr.com'
# __status__ = 'In active development'

# Imports #####################################################################

import numpy as np
import pandas as pd
import datetime as dt
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import yfinance as yf
# import matplotlib as plt
# import seaborn as sns
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
import os
# Page Setup ##################################################################
st.set_page_config(page_title='Ledgr | Forecasting Engine',
                   layout="wide", initial_sidebar_state="expanded")
direc = os.getcwd()

# direc = f'{direc}/Documents/Ledgr'
logofile = f'{direc}/pages/appdata/imgs/Ledgr_Logo_F2.png'

with st.sidebar:
    st.image(logofile, use_container_width=True)
    st.caption("Select a stock, train the algorithm and predict scenarios.")
# Variables & Declarations ####################################################
start_date = dt.datetime(2020, 1, 1)
end_date = dt.datetime.today()
pathtkr = f"{direc}/pages/appdata/tickerlist_y.csv"

tickerdb = pd.read_csv(pathtkr)
tickerlist = tickerdb["SYMBOL"]

# Functions & Cached Resources ################################################
@st.cache_data
def getdata(stock):
    stock = yf.Ticker(stock)
    df = stock.history(period='max')['Close']
    return df


# Icons and Links ###########################

ytube = f"{direc}/pages/appdata/imgs/ytube.svg"
fbook = f"{direc}/pages/appdata/imgs/fbook.svg"
insta = f"{direc}/pages/appdata/imgs/insta.svg"
linkedin = f"{direc}/pages/appdata/imgs/linkedin.svg"
ledgrblog = f"{direc}/pages/appdata/imgs/Ledgr_Logo_F1.png"
fc1, fc2 = st.columns(2)
with fc1:
    st.title(":Forecast Engine:")
    st.write("Train Ledgr's AI Engines. Forecast Asset Prices.")
    st.info("Chart behaviour, predict price-ranges, observe trajectories.")
with fc2:
    st.video('https://youtu.be/tqOWAGEnKKQ?si=yW1nz3AVFKvUxGjA')
st.write("    -----------------------------------------------------------    ")
st.header("This page is under the works and shall be open soon!")



st.write("  ---------------------------------------------------------------  ")
url_ytube = "https://www.youtube.com/@LedgrInc"
url_fb = "https://www.facebook.com/share/1BnXaYvRzV/"
url_insta ='https://www.instagram.com/alphaledgr/'
url_blog = 'https://www.alphaledgr.com/Blog'
url_linkedin = "https://www.linkedin.com/company/ledgrapp/"
st.write("  ---------------------------------------------------------------  ")
column1, column2, column3, column4, column5 = st.columns([1, 1, 1, 2 , 1])
with column1:
    st.image(ytube, '[Ledgr\'s YouTube Channel](%s)' % url_ytube)
with column2:
    st.image(fbook, '[Ledgr\'s FaceBook Page ](%s)' % url_fb)
with column3:
    st.image(linkedin,  '[Our LinkedIn Page ](%s)' % url_linkedin)
with column4:
    st.write(" ")
    st.image(ledgrblog,  '[Ledgr\'s Blog ](%s)' % url_blog)
    st.write(" ")
with column5:
    st.image(insta,  '[Ledgr\'s @ Instagram ](%s)' % url_insta)
# # ###################################################################
with st.container():
    f9, f10, f11 = st.columns([1, 5, 1])
    with f9:
        st.write(" ")
    with f10:
        st.caption(": | 2025 - 2026 | All Rights Resrved  ©  Ledgr Inc. | www.alphaLedgr.com | alphaLedgr Technologies Ltd. :")
    with f11:
        st.write(" ")
