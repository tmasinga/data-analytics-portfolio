
---

# ✅ **README for Sales Dashboard**

```markdown
# 📈 Superstore Sales Dashboard – Power BI

This folder contains the **Sales Performance Dashboard** developed using the Sample Superstore dataset.  
The dashboard provides a detailed view of company revenue, profit, and product performance across different regions and segments.

---

## 🎯 Dashboard Purpose
To provide insights into:

- Sales performance trends
- Profitability over time
- Product & category contribution
- Regional business performance
- High-level business health KPIs

---

## 🔑 Key KPIs Included
- Total Sales  
- Total Profit  
- Total Quantity  
- Profit Margin  
- Sales YoY Growth  
- Profit YoY Growth  

---

## 📊 Visuals Included
- Line Chart – Sales Over Time  
- Map – Sales by State  
- Bar Chart – Category & Sub-Category Performance  
- Profit by Segment  
- Top 10 Products by Sales  
- Bottom 10 Products by Profit  
- KPI Cards for Sales, Profit, Quantity  

---

## 🧠 DAX Logic Highlights
```DAX
Total Sales = SUM(Orders[Sales])

Total Profit = SUM(Orders[Profit])

Total Quantity = SUM(Orders[Quantity])

Profit Margin = 
DIVIDE([Total Profit], [Total Sales])
