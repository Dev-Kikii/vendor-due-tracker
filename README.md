##Vendor Due-Date Tracker (v0.2)

A lightweight Python utility that turns static vendor data into an actionable risk signal.

This tool identifies third-party vendors due for reassessment within the next 30 days and surfaces them immediately via terminal output or Slack notification. It is intentionally simple, readable, and extensible — designed to support timely risk decisions without dashboards, spreadsheets, or manual tracking.

Built as a practical GRC automation project. Terraform drift checks planned for v0.3.


## Quick Start
	1.	Clone or download this repository
	2.	Install dependencies: pip install pandas
	3.	Run: python3 tracker.py


## What It Does (v0.2)
- Reads `vendors.csv` (name, risk_tier, next_review_date)  
- Filters due ≤ 30 days  
- **ANSI colour tiers** (High=red, Medium=yellow, Low=green)  
- **Generates Slack-ready JSON payloads for webhook integration 
- 12 seconds to notification


Sample Output
Vendors due in next 30 days: 4
Acme Cloud | High | 01-May
Beta SaaS | Medium | 15-Jun


## Next (open to PRs)
Roadmap
	•	Risk-tier colour enhancements (v0.2 ✔)
	•	Slack webhook integration (v0.2 ✔)
	•	Planned: Explore Terraform state drift checks as a future GRC automation enhancement.

Open an issue or submit a PR — the aim is to build practical, composable tools that make TPRM less manual and more reliable.


## Licence
MIT — free to use, adapt, and extend. Attribution appreciated.
