import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

channels = ['Tmall', 'JD.com', 'Douyin', 'WeChat Mini', 'Offline Store']
categories = ['MLB Cap', 'MLB Apparel', 'MLB Bag', 'Discovery Apparel', 'Discovery Shoes']

rows = []
base_date = datetime(2026, 5, 5)

for day_offset in range(7):  # 1주일치
    date = base_date + timedelta(days=day_offset)
    for ch in channels:
        for cat in categories:
            base_sales = {
                'Tmall': 800, 'JD.com': 600, 'Douyin': 500,
                'WeChat Mini': 300, 'Offline Store': 400
            }[ch]
            cat_mult = {
                'MLB Cap': 1.3, 'MLB Apparel': 1.1, 'MLB Bag': 0.9,
                'Discovery Apparel': 0.8, 'Discovery Shoes': 0.7
            }[cat]

            qty = int(np.random.normal(base_sales * cat_mult, base_sales * 0.15))
            avg_price = np.random.uniform(150, 650)
            revenue = round(qty * avg_price, 2)
            cost = round(revenue * np.random.uniform(0.35, 0.50), 2)
            gross_profit = round(revenue - cost, 2)

            rows.append({
                'Date': date.strftime('%Y-%m-%d'),
                'Channel': ch,
                'Category': cat,
                'Quantity': max(qty, 0),
                'Avg_Price_CNY': round(avg_price, 2),
                'Revenue_CNY': max(revenue, 0),
                'Cost_CNY': max(cost, 0),
                'Gross_Profit_CNY': max(gross_profit, 0),
            })

df = pd.DataFrame(rows)
filename = f"sample_data/FF_China_Weekly_{base_date.strftime('%Y%m%d')}_{(base_date+timedelta(days=6)).strftime('%Y%m%d')}.xlsx"
df.to_excel(filename, index=False, sheet_name='Weekly Sales')
print(f"Created: {filename}")
print(f"Rows: {len(df)}, Columns: {list(df.columns)}")
print(df.head())
