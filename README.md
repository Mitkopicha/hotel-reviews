# 🏨 Hotel Reviews – Python Data Project

This project analyses hotel reviews from a CSV file using Python.  
It was built for a university data assignment to show how data can be processed, filtered, and visualised directly from the command line. Built for my university’s Data Project. The focus was on practising Python scripting, data handling, and simple visualisations from real-world CSV data.

The program has a simple **text menu (TUI)** where you can:
- Filter reviews by hotel name, date or nationality  
- See average ratings and summaries  
- Create pie and bar charts using Matplotlib  
- Export results to CSV or JSON  

---

## 🔧 How It Works

Everything runs in the terminal.  
When you start the app, it loads the dataset, counts how many reviews there are, and then shows a menu like this:

************ Hotel Reviews ************
Operation: Initiating [ 0%]
There are 1031 reviews in the data set.
Operation: Completed [100%]

|| MENU ||
[1] Process Data
[2] Visualise Data
[3] Export Data
[4] Exit

You can choose options to view reviews, summaries, or open charts.

---

## 🧰 Tech Used

- **Python 3.10+**
- **Matplotlib** for graphs
- **CSV / JSON** for data handling
- **datetime** for working with review dates

---

## 📁 Project Structure
hotel-reviews/
├── data/
│ └── hotel_reviews.csv
├── src/
│ ├── main.py
│ ├── tui.py
│ ├── process.py
│ └── visual.py
├── outputs/
│ └── (exported files)
├── README.md
└── requirements.txt


📸 Screenshots
Startup and Menu
<img width="269" height="244" alt="Screenshot 2025-11-12 182754" src="https://github.com/user-attachments/assets/a231c1a7-4865-424b-b056-9e168f918172" />

Reviews by Hotel
<img width="842" height="356" alt="11" src="https://github.com/user-attachments/assets/1710198e-548c-4a19-a6f0-88e787c67ec6" />

Positive / Negative Pie Chart
<img width="808" height="332" alt="21" src="https://github.com/user-attachments/assets/b3da4060-0afc-4e60-8266-1f42a67f87ce" />

Reviews by Nationality
<img width="838" height="291" alt="22" src="https://github.com/user-attachments/assets/75123d46-95bd-4e0d-b9d4-29cac578b1fd" />

Filter Reviews by Date
<img width="538" height="225" alt="3" src="https://github.com/user-attachments/assets/25a880f2-bf87-4dbc-9327-01a155751628" />


---

## ▶️ Running the Project

### 1. Create a virtual environment
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1   # (on Windows PowerShell)
pip install -r requirements.txt
python src/main.py




