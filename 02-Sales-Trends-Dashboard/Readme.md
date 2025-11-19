<h1 align="center">📈 Sales Performance Dashboard — Power BI</h1>

<p align="center">
  <img src="banner.png" width="750"/>
</p>

---

## 🟦 Overview
This dashboard analyzes sales performance using the **Superstore Sales (Kaggle)** dataset.  
It evaluates revenue trends, product performance, regional contribution, and customer purchasing behavior.

---

## 🟩 Objectives
- Understand sales trends and growth  
- Identify top-performing categories & products  
- Compare regional performance  
- Evaluate customer purchasing patterns  
- Provide sales insights for decision-making  

---

## 🟨 Dataset
**Source:** Kaggle – *Superstore Sales Dataset*  
Includes:  
- Orders  
- Sales & Profit  
- Category & Sub-category  
- Regions & Segments  
- Customer information  

---

## 🟧 Key KPIs
### 📌 Primary Sales KPIs
- Total Sales  
- Total Revenue  
- Total Orders  
- Average Order Value (AOV)  
- Units Sold  
- Discount Rate  
- Sales Growth % (MoM)

### 📈 Trend Analysis
- Monthly Sales Trend  
- Sales YoY Comparison  
- Profit vs Sales Trend  

### 🗂 Performance Breakdown
- Sales by Region  
- Sales by Segment  
- Sales by Category / Sub-category  
- Top 10 Products  
- Bottom 10 Products  

---

## 🟪 Dashboard Preview
<p align="center">
  <img src="dashboard_screenshot.png" width="750"/>
</p>

---

## 🟫 Skills Used
- Power BI Desktop  
- Data Cleaning (Power Query)  
- DAX Calculations  
- Data Modelling  
- Data Visualization  
- Sales Trend Analysis  
- Business Reporting  

---

## 🔵 DAX Measures
```DAX
Total Sales = SUM('Orders'[Sales])

Total Orders = DISTINCTCOUNT('Orders'[Order ID])

Units Sold = SUM('Orders'[Quantity])

AOV = DIVIDE([Total Sales], [Total Orders], 0)

Sales Growth % = 
VAR ThisMonth = [Total Sales]
VAR LastMonth = CALCULATE([Total Sales], DATEADD('Orders'[Order Date], -1, MONTH))
RETURN DIVIDE(ThisMonth - LastMonth, LastMonth, 0)

