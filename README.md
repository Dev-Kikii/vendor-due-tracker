# Vendor Due-Date Tracker (v0.1)
38-line Python CLI that reads a CSV and lists vendors due ≤ 30 days.  
Ugly, working, mine—colours and Slack coming in v0.2.

## Quick Start
1. Clone or download this repo  
2. `pip install pandas`  
3. `python3 tracker.py`

## What It Does
- Reads `vendors.csv` (name, risk_tier, next_review_date)  
- Filters due ≤ 30 days  
- Prints to terminal in 12 seconds

Sample Output
Vendors due in next 30 days: 4
Acme Cloud | High | 01-May
Beta SaaS | Medium | 15-Jun


## Next (open to PRs)
- Risk-tier colours (v0.2)  
- Slack webhook (v0.2)  
- Terraform state drift (v0.3)

Open an issue or fork & PR—let’s build the least-boring TPRM toolkit together.

## Licence
MIT - do what you want, just point back here.
