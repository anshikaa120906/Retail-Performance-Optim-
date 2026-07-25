**Retail Performance Optimization & Predictive Sales Analysis**

**Live Project Website:** https://aslmazrta5mpelk8fev3yr.streamlit.app

Strategic Business Recommendations
Margin Optimization: Re-evaluate fulfillment and discounting strategies in the Central region to fix current profit constraints ($39.7k profit vs. $501.2k sales volume).

Shipping SLA Alignment: Incentivize expedited shipping (First Class / Same Day) for high-ticket orders to mitigate the systematic 5.0-day operational transit delay observed in Standard Class.

Category Focus: Prioritize inventory allocation toward high-margin categories identified in the interactive breakdown to maximize net profitability.

Project Overview
An interactive Streamlit web application showcasing Exploratory Data Analysis (EDA), automated anomaly detection, and machine learning profit predictions on multi-year retail operational data. The system isolates key profitability bottlenecks across regional markets, detects extreme transaction anomalies via Z-Score filtering, and provides a real-time Random Forest simulator for revenue forecasting.

Tech Stack
Language: Python

Libraries: Streamlit, Plotly, Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn

Tools: Streamlit Cloud, Jupyter Notebook, GitHub

Core Analytical Findings
Regional Profitability Bottlenecks: Analysis revealed that while the Central region generates substantial sales volume ($501,239.89), its net profit margins are heavily constrained ($39,706.36) relative to optimized markets like the West region ($108,418.45).

Shipping Delay Impact Dynamics: Quantified average logistical delays across distribution tracks, confirming that Standard Class shipping introduces a systematic 5.0-day operational lag compared to expedited First Class (2.1 days) and Same Day tracks.

Predictive Profit Modeling: Engineered a Random Forest Regression model and interactive simulator to forecast expected transaction profit in real-time based on sales volume, applied discounts, and item quantity.

Automated Anomaly Detection: Integrated dynamic Z-Score statistical filtering to flag high-risk transaction losses automatically.
