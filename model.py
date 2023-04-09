import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

stocks = pd.read_csv('C:/Users/prath/Demo/nifty_500_data.csv')
stocks.rename(columns={'market_cap': 'MarketCapture', 'stock_PE': 'PERatio', 'Dividend_Yield': 'Dividend',
                       'ROE': 'ROE', 'promoters_t': 'PromoterHoldings', 'compounded_profit_growth': 'ProfitGrowth',
                       'compounded_sales_growth': 'SalesGrowth', 'ROCE': 'ROCE'}, inplace=True)
stocks = stocks[['MarketCapture', 'PERatio', 'Dividend', 'ROE', 'PromoterHoldings', 'ProfitGrowth', 'SalesGrowth', 'ROCE']]

# separate the data and label
x = stocks.drop('ROE', axis=1)
y = stocks['ROE'].apply(lambda y_value: 1 if y_value >= 16 else 0)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2)

def predict_stock(MarketCapture, PERatio, Dividend, PromoterHoldings, ProfitGrowth, SalesGrowth, ROCE):
    stocks = pd.DataFrame({
        'MarketCapture': [MarketCapture],
        'PERatio': [PERatio],
        'Dividend': [Dividend],
        'PromoterHoldings': [PromoterHoldings],
        'ProfitGrowth': [ProfitGrowth],
        'SalesGrowth': [SalesGrowth],
        'ROCE': [ROCE]
    })

    model = RandomForestClassifier()
    model.fit(x_train, y_train)

    return model.predict(stocks)
