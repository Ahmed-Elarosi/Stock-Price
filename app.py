import yfinance as yf
import streamlit as st


st.write(
    """
# Simple Stock Price App.


Shown are the stock closing price, volume, and value of Google.


"""
)

tickerSymbol = "GOOGL"
tickerData = yf.Ticker(tickerSymbol)

tickerDF = tickerData.history(period="1d", start="2010-5-31", end="2022-5-31")

st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)
st.area_chart(tickerDF.values)
