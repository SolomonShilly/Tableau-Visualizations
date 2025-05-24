import yfinance
import pandas as pd
from datetime import datetime, timedelta

def stock_retriever(tickers, end, start):
    for ticker in tickers:
        data = yfinance.download(ticker,start=start, end=end, interval='1mo')
        data.reset_index(inplace=True)

        data['Ticker'] = ticker
        file = f'{ticker}Data.xlsx'
        data.to_excel(file, sheet_name=ticker)

    print('Files saved')

tickers = ['TJX', 'KSS']
end = datetime.today().date()
start = end - timedelta(days=365*10)
stock_retriever(tickers, end, start)