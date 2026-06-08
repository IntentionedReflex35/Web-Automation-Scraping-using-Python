# Web Automation & Scraping using Python

![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-4.15.0-orange)
![Selenium](https://img.shields.io/badge/Selenium-4.44.0-green?logo=selenium&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-3.0.3-150458?logo=pandas&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-brightgreen)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

> A structured, hands-on learning journey through web scraping and browser automation with Python — built alongside a Udemy course, extended with real-world projects.

---

## 📖 About This Repository

This repository documents my self-directed learning of web scraping and browser automation using Python. It is organized into two sections:

- **Lessons** — Core concepts and techniques covered through guided course material
- **Projects** — Independent, real-world scraping projects that apply and extend those concepts

The goal is to build both a strong conceptual foundation and a practical portfolio of applied scraping work.

---

## 🗂️ Project Structure

```
Web Automation&Scraping using Python/
│
├── .venv/                        # Virtual environment (not tracked)
│
├── Lessons/                      # Guided course lessons
│   ├── intro.py                  # BeautifulSoup fundamentals
│   ├── lecture_selenium.py       # Selenium basics & browser control
│   ├── lecture_selenium1.py      # Cookie saving with pickle
│   └── lecture_selenium2.py     # Executing JavaScript via Selenium
│
├── Projects/                     # Applied real-world scraping projects
│   ├── Project1_ConsumerReportsWebsite.py
│   └── Project2_CraigslistWebsite.py
│
├── data/                         # Output data files (CSV, etc.)
│   └── accra_craigslist.csv
│
├── cookies.pkl                   # Saved browser session (generated at runtime)
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 📚 Lessons Overview

### `intro.py` — BeautifulSoup Fundamentals
**Concepts:** `requests`, `html5lib`, `BeautifulSoup`

Scrapes the **Wikipedia page on Logical Fallacies** and extracts the table of contents. Demonstrates:
- Making HTTP GET requests with custom headers to mimic a real browser
- Parsing raw HTML with the `html5lib` parser
- Navigating the DOM with `.find()` and `.find_all()`
- Cleaning and formatting extracted text

---

### `lecture_selenium.py` — Selenium Basics & Browser Control
**Concepts:** `webdriver`, `ChromeDriverManager`, element interaction

Opens a real Chrome browser, navigates to **Wikipedia**, and performs a live search for *Bayern Munich*. Demonstrates:
- Launching a Chrome browser session with Selenium
- Auto-managing ChromeDriver with `webdriver-manager`
- Finding elements by `ID` and `XPATH`
- Simulating user input (`.send_keys()`) and clicks (`.click()`)

---

### `lecture_selenium1.py` — Saving Browser Sessions as Cookies
**Concepts:** Session persistence, `pickle`

Logs into a **practice test login page** and saves the authenticated browser session to a `.pkl` file. Demonstrates:
- Filling and submitting login forms via Selenium
- Capturing and persisting cookies with Python's `pickle` module
- The concept of reusable authenticated sessions (to avoid repeated logins)

---

### `lecture_selenium2.py` — Executing JavaScript via Selenium
**Concepts:** `execute_script()`, browser-side JavaScript

Navigates to Google and runs a raw JavaScript snippet directly in the browser. Demonstrates:
- Using `driver.execute_script()` to interact with page elements at the JS level
- Why JS execution is useful when standard Selenium selectors fall short on dynamic pages

---

## 🚀 Projects

### Project 1 — Consumer Reports Website
**File:** `Projects/Project1_ConsumerReportsWebsite.py`
**Libraries:** `requests`, `BeautifulSoup`, `pandas`

Scrapes article cards from **[consumerreports.org](https://www.consumerreports.org/)** and follows each article link to extract its *"In This Article"* section items.

**What it does:**
- Fetches the Consumer Reports homepage and identifies article cards
- Extracts article titles and their full URLs
- Crawls each article page to extract its sub-topic links and anchor text
- Stores the aggregated data in a `pandas` DataFrame

**Key techniques:** multi-page crawling, link resolution, dictionary aggregation, DataFrame output

> ⚠️ **Note:** Consumer Reports is a dynamic (JavaScript-rendered) site. Some content may not be fully accessible via static `requests`-based scraping. This project intentionally explores the limits of static scraping on modern websites.

---

### Project 2 — Accra Craigslist Real Estate Listings
**File:** `Projects/Project2_CraigslistWebsite.py`
**Libraries:** `requests`, `BeautifulSoup`, `pandas`, `pathlib`

Scrapes real estate listings from the **Accra section of Craigslist** and exports a clean dataset as a CSV file.

**What it does:**
- Fetches gallery-view listing results from `accra.craigslist.org`
- Extracts listing **title**, **price**, **location**, and **direct link** for each result
- Saves the structured data to `data/accra_craigslist.csv` using `pathlib` for cross-platform path resolution

**Key techniques:** structured data extraction, multi-field parsing, CSV export, `Path(__file__).resolve()` for portable paths

**Sample output:**

| Name            | Link                             | Location   | Price    |
|-----------------|----------------------------------|------------|----------|
| 3 Bedroom House | https://accra.craigslist.org/... | East Legon | GH₵3,500 |
| ...             | ...                              | ...        | ...      |

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.11 or higher
- Google Chrome browser installed
- Git

### 1. Clone the repository
```bash
git clone https://github.com/IntentionedReflex35/Web-Automation-Scraping-using-Python.git
cd Web-Automation-Scraping-using-Python
```

### 2. Create and activate a virtual environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

> `webdriver-manager` automatically downloads and manages the correct ChromeDriver version for your installed Chrome browser — no manual setup needed.

---

## ▶️ Running the Scripts

```bash
# Run a lesson
python Lessons/intro.py

# Run a project
python Projects/Project2_CraigslistWebsite.py
```

Output CSV files are saved to the `data/` directory.

---

## 🛠️ Tech Stack

| Tool                | Purpose                                            |
|---------------------|----------------------------------------------------|
| `requests`          | HTTP requests for static page content              |
| `html5lib`          | Lenient HTML parser (handles malformed HTML well)  |
| `BeautifulSoup4`    | HTML parsing and DOM navigation                    |
| `selenium`          | Browser automation and dynamic content interaction |
| `webdriver-manager` | Automatic ChromeDriver version management          |
| `pandas`            | Data structuring and CSV export                    |
| `pickle`            | Serializing and saving browser session cookies     |
| `pathlib`           | Cross-platform file path management                |

---

## 🧠 Concepts Covered

- [x] HTTP requests and response handling
- [x] Static HTML parsing with BeautifulSoup
- [x] Custom request headers to avoid bot detection
- [x] DOM traversal (`.find()`, `.find_all()`, `.get_text()`)
- [x] Browser automation with Selenium WebDriver
- [x] Locating elements by ID, Name, and XPATH
- [x] Simulating user interactions (typing, clicking)
- [x] Cookie persistence with `pickle`
- [x] JavaScript execution in the browser
- [x] Multi-page crawling
- [x] Structured data extraction and CSV export
- [x] Virtual environment setup and dependency management
- [ ] Handling dynamic/JavaScript-rendered pages (Selenium + scraping combined) — *upcoming*
- [ ] Pagination and infinite scroll — *upcoming*
- [ ] Proxy rotation and rate limiting — *upcoming*
- [ ] Scrapy framework — *upcoming*

---

## ⚠️ Disclaimer

This repository is for **educational purposes only**. All scraping is performed on publicly accessible pages. Always review and comply with a website's `robots.txt` file and Terms of Service before scraping. The author is not responsible for any misuse of the techniques demonstrated here.

---

## 📄 License

MIT License — © 2026 Jeshurun Nana Kojo Ansah

Permission is hereby granted, free of charge, to any person obtaining a copy of this repository and its associated files, to use, copy, modify, merge, publish, distribute, and/or sublicense them, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the software.

> This project is provided **as-is**, without warranty of any kind. The author is not liable for any damages or misuse arising from its use.

---

## 👤 Author

**Jeshurun Nana Kojo Ansah** — Geomatic Engineering student | Aspiring Data Analyst  
🔗 [GitHub: IntentionedReflex35](https://github.com/IntentionedReflex35)

> *"Move stealthy, execute in silence."*
