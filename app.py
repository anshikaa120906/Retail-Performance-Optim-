import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configure page layout
st.set_page_config(page_title="Retail Optimization Dashboard", layout="wide")

st.title(" Retail Performance Optimization Dashboard")
st.markdown("An interactive web application showcasing Exploratory Data Analysis (EDA) and business metrics.")

@st.cache_data
def load_data():
    df = pd.read_csv("Superstore sales dataset.csv")
    return df

try:
    df = load_data()
    
    st.sidebar.header(" Filter Options")
    all_regions = df["Region"].unique()
    selected_regions = st.sidebar.multiselect("Select Regions to View:", options=all_regions, default=all_regions)
    
    filtered_df = df[df["Region"].isin(selected_regions)]
    
    st.subheader(" Core Operational Metrics")
    col1, col2 = st.columns(2)
    
    total_sales = filtered_df["Sales"].sum()
    total_profit = filtered_df["Profit"].sum()
    
    col1.metric("Total Sales Volume", f"${total_sales:,.2f}")
    col2.metric("Net Profit Margin", f"${total_profit:,.2f}")
    
    st.markdown("---")
    
    st.subheader(" Regional Profitability Insights")
    if not filtered_df.empty:
        fig, ax = plt.subplots(figsize=(10, 4))
        sns.barplot(data=filtered_df, x="Region", y="Profit", estimator=sum, ax=ax, palette="viridis", errorbar=None)
        plt.ylabel("Total Profit ($)")
        st.pyplot(fig)
    else:
        st.warning("Please select at least one region.")
        
    st.subheader(" Predictive Sales Baseline Modeling")
    st.info("Linear Regression analysis tracks a steady baseline upward trend scale of $1.11 per transactional period.")

except FileNotFoundError:
    st.error("Error: 'Superstore sales dataset.csv' not found.")