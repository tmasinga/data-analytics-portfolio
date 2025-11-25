# 📊 Customer KPI Dashboard – Superstore Dataset

This folder contains the **Customer KPI Dashboard** built using the Sample Superstore dataset.  
The dashboard focuses on customer performance, segmentation, and business-driving KPIs using advanced DAX calculations.

---

## 🎯 Dashboard Purpose
To understand customer value, purchasing patterns, and business health using:

- RFM Analysis (Recency, Frequency, Monetary)
- Customer Loyalty & Retention Metrics
- Customer Spend Patterns
- Profitability per Customer
- Behaviour Segmentation

---

## 🔑 Key KPIs Included
- **Total Customers**
- **New Customers**
- **Returning Customers**
- **Churned Customers**
- **Average Sales per Customer**
- **Average Profit per Customer**
- **Days Since Last Purchase**
- **RFM Score & Segmentation**

---

## 🧠 DAX Logic Highlights
Some of the core DAX measures used:

```DAX
Customer Count = DISTINCTCOUNT(Orders[Customer Name])

Sales per Customer = 
DIVIDE([Total Sales], [Customer Count])

R = DATEDIFF(
    CALCULATE(MAX(Orders[Order Date]), ALLEXCEPT(Orders, Orders[Customer Name])),
    TODAY(),
    DAY
)

F = CALCULATE(
    DISTINCTCOUNT(Orders[Order ID]),
    ALLEXCEPT(Orders, Orders[Customer Name])
)

M = CALCULATE(
    SUM(Orders[Sales]),
    ALLEXCEPT(Orders, Orders[Customer Name])
)

