import pandas as pd
from datetime import datetime, timedelta

today = datetime.today()
due_date = today + timedelta(days=30)

df = pd.read_csv('vendors.csv')
df['next_review_date'] = pd.to_datetime(df['next_review_date'])
due = df[df['next_review_date'] <= due_date]

print(f"Vendors due in next 30 days: {len(due)}")
for _, row in due.iterrows():
    print(f"{row['name']} | {row['risk_tier']} | {row['next_review_date'].strftime('%d-%b')}")
