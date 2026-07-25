**Retail Performance Optimization & Predictive Sales Analysis**

**Live Interactive Application:** https://aslmazrta5mpelk8fev3yr.streamlit.app

### **Strategic Business Recommendations**
* **Margin Optimization:** Re-evaluate fulfillment and discounting strategies in the Central region to fix current profit constraints ($39.7k profit vs. $501.2k sales volume).
* **Shipping SLA Alignment:** Incentivize expedited shipping (First Class / Same Day) for high-ticket orders to mitigate the systematic 5.0-day operational transit delay observed in Standard Class.
* **Category Focus:** Prioritize inventory allocation toward high-margin categories identified in the interactive breakdown to maximize net profitability.

### **Project Overview**
Interactive Streamlit web application showcasing Exploratory Data Analysis (EDA), automated anomaly detection, and machine learning profit predictions on multi-year retail operational data. The system isolates key profitability bottlenecks across regional markets, detects extreme transaction anomalies via Z-Score statistical filtering, and provides a real-time Random Forest simulator for revenue forecasting.

### **Key Application Features**
* **Real-Time Machine Learning Simulator:** Predicts transaction-level profit dynamically using an integrated Random Forest Regressor model based on sales volume, discount rates, and item quantities.
* **Automated Anomaly Detection Engine:** Utilizes Z-Score statistical thresholds to flag critical loss-making transactions automatically across regional order records.
* **Scenario Planning & Forecasting:** Includes interactive growth target sliders and region/category multi-filters for stakeholder decision-making.
* **Data Search & Executive Export:** Enables real-time order lookups by Product Name or Order ID alongside automated executive text report generation.

### **Tech Stack**
* **Language:** Python
* **Libraries:** Streamlit, Plotly, Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn
* **Tools:** Streamlit Cloud, Jupyter Notebook, GitHub

### **Core Analytical Findings**
* **Regional Profitability Bottlenecks:** Analysis revealed that while the Central region generates substantial sales volume ($501,239.89), its net profit margins are heavily constrained ($39,706.36) relative to optimized markets like the West region ($108,418.45).
* **Shipping Delay Impact Dynamics:** Quantified average logistical delays across distribution tracks, confirming that Standard Class shipping introduces a systematic 5.0-day operational lag compared to expedited First Class (2.1 days) and Same Day tracks.
* **Predictive Profit Modeling:** Engineered a Random Forest Regression model and interactive simulator to forecast expected transaction profit in real-time.

### **Local Setup & Installation**
1. Clone the repository:
   `git clone https://github.com/anshikaa120906/Retail-Performance-Optim-.git`
2. Navigate into the project directory:
   `cd Retail-Performance-Optim-`
3. Install required dependencies:
   `pip install -r requirements.txt`
4. Launch the Streamlit web app:
   `streamlit run app.py`
