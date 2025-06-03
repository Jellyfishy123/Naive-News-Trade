# 📰 Naive News-Based Trading Strategy – `demo_NewsTrade`

This repository demonstrates a **simple news-driven trading strategy** using the AlgoAPI framework. The strategy places a buy order for **SP500 (SPXUSD)** whenever specific keywords are detected in **news articles related to the Americas region**.

---

## 📘 Strategy Overview

News parsing was traditionally a domain of computational linguistics. With the rise of **machine learning**, **natural language processing (NLP)**, and **AI**, financial applications have begun integrating news sentiment and keyword detection into trading logic.

This strategy serves as an **introductory example** to help developers understand how to use **news data feeds** in backtesting and real-time trading.

---

## 🧠 Strategy Logic

The algorithm listens for incoming news articles and looks for:

- Language: **English**
- Region: **"AMERICAS"**
- Keywords: `"increase"`, `"up"`, and `"improve"`  
- All keywords must appear **within the same article**

If a news article satisfies all of the above, the algorithm immediately sends a **market buy order** for **SPXUSD**.

While basic in logic, this implementation demonstrates:

- How to access and parse news feeds in AlgoAPI
- How to incorporate textual data into trading decisions
- The use of simple keyword filtering for event-based trading

---

## ⚙️ Backtest Configuration

| Setting               | Value           |
|-----------------------|-----------------|
| Strategy Name         | `demo_NewsTrade` |
| Instruments           | `['SPXUSD']`     |
| Backtest Period       | January to March 2019 |
| Data Interval         | Tick             |
| Initial Capital       | USD 1,000,000     |
| Base Currency         | USD              |
| Leverage              | 1                |
| Transaction Cost      | 0                |
| Allow Short Selling   | Yes              |
| News Feed             | **Enabled** ✅     |

