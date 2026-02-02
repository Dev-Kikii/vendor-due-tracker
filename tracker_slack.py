import pandas as pd
import requests, json, os
from datetime import datetime, timedelta

WEBHOOK = os.getenv("SLACK_WEBHOOK")
today = datetime.today()
due_date = today + timedelta(days=30)

df = pd.read_csv('vendors.csv')
df['next_review_date'] = pd.to_datetime(df['next_review_date'])
due = df[df['next_review_date'] <= due_date]

# Slack colour blocks
colour = {"High": "#d32f2f", "Medium": "#f57c00", "Low": "#388e3c"}
blocks = [{
    "type": "section",
    "text": {"type": "mrkdwn", "text": f"*Vendors due ≤ 30 days:* {len(due)}"}
}]
for _, r in due.iterrows():
    blocks.append({
        "type": "section",
        "text": {"type": "mrkdwn", "text": f"{r['name']}  |  {r['risk_tier']}  |  {r['next_review_date'].strftime('%d-%b')}"}
    })

payload = {"blocks": blocks}
print("Blocks sent:", json.dumps(payload, indent=2))
requests.post(WEBHOOK, data=json.dumps(payload))
print("Slack ping sent ✅")

# Terminal colour pop
COLOUR = {"High": "\033[91m", "Medium": "\033[93m", "Low": "\033[92m", "RESET": "\033[0m"}
print("\nTerminal preview:")
for _, r in due.iterrows():
    print(f"{COLOUR[r['risk_tier']]}{r['name']} | {r['risk_tier']} | {r['next_review_date'].strftime('%d-%b')}{COLOUR['RESET']}")

