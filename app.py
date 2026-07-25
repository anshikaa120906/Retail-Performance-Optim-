import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.ensemble import RandomForestRegressor

st.set_page_config(
    page_title="Retail Performance & Predictive Analytics Engine",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
    <style>
    div[data-testid="stMetric"] {
        background-color: #1E222D;
        border: 1px solid #2B303C;
        padding: 15px;
        border-radius: 10px;
    }
    button[data-baseweb="tab"] {
        font-size: 16px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Retail Performance & Predictive Analytics Engine")
st.markdown("An advanced analytics platform featuring automated anomaly detection, live ML prediction, and business performance metrics.")

@st.cache_data
def load_data():
    df = pd.read_csv("Superstore sales dataset.csv")
    return df

@st.cache_resource
def train_model(df):
    clean_df = df.dropna(subset=["Sales", "Discount", "Quantity", "Profit"])
    X = clean_df[["Sales", "Discount", "Quantity"]]
    y = clean_df["Profit"]
    model = RandomForestRegressor(n_estimators=50, random_state=42)
    model.fit(X, y)
    return model

try:
    df = load_data()
    ml_model = train_model(df)
    
    st.sidebar.header("Filter Options")
    
    regions = st.sidebar.multiselect(
        "Select Regions:",
        options=df["Region"].unique(),
        default=df["Region"].unique()
    )
    
    categories = st.sidebar.multiselect(
        "Select Categories:",
        options=df["Category"].unique(),
        default=df["Category"].unique()
    )
    
    filtered_df = df[
        (df["Region"].isin(regions)) & 
        (df["Category"].isin(categories))
    ]
    
    st.markdown("### Core Operational Metrics")
    col1, col2, col3, col4 = st.columns(4)
    
    total_sales = filtered_df["Sales"].sum()
    total_profit = filtered_df["Profit"].sum()
    total_orders = len(filtered_df)
    avg_discount = filtered_df["Discount"].mean() * 100
    
    col1.metric("Total Sales Volume", f"${total_sales:,.2f}")
    col2.metric("Net Profit Margin", f"${total_profit:,.2f}")
    col3.metric("Total Orders Processed", f"{total_orders:,}")
    col4.metric("Average Discount Rate", f"{avg_discount:.1f}%")
    
    st.markdown("---")
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "📈 Regional & Segment Performance", 
        "🤖 Real-Time ML Profit Predictor", 
        "🚨 Anomaly Detection Engine", 
        "📋 Data Inspector & Export"
    ])
    
    with tab1:
        st.subheader("Regional Profitability Breakdown")
        regional_profit = filtered_df.groupby("Region")["Profit"].sum().reset_index()
        fig_profit = px.bar(
            regional_profit, 
            x="Region", 
            y="Profit", 
            color="Region",
            title="Total Profit by Region ($)",
            color_discrete_sequence=px.colors.qualitative.Set2,
            text_auto='.2s'
        )
        fig_profit.update_layout(template="plotly_dark", showlegend=False)
        st.plotly_chart(fig_profit, use_container_width=True)
        
        st.markdown("#### 🚚 Profitability by Category & Segment")
        segment_profit = filtered_df.groupby(["Category", "Segment"])["Profit"].sum().reset_index()
        fig_segment = px.bar(
            segment_profit,
            x="Category",
            y="Profit",
            color="Segment",
            barmode="group",
            title="Segment Profit Distribution Across Categories",
            color_discrete_sequence=px.colors.qualitative.Bold
        )
        fig_segment.update_layout(template="plotly_dark")
        st.plotly_chart(fig_segment, use_container_width=True)
        
    with tab2:
        st.subheader("🔮 Live Random Forest Profit Simulator")
        st.info("Interactive Machine Learning Model: Adjust order parameters below to predict expected profit in real time.")
        
        col_input1, col_input2, col_input3 = st.columns(3)
        input_sales = col_input1.number_input("Estimated Sales Value ($):", min_value=1.0, max_value=20000.0, value=500.0)
        input_discount = col_input2.slider("Discount Applied (%):", min_value=0.0, max_value=80.0, value=10.0) / 100.0
        input_qty = col_input3.slider("Item Quantity:", min_value=1, max_value=20, value=3)
        
        predicted_profit = ml_model.predict([[input_sales, input_discount, input_qty]])[0]
        
        st.markdown("### Model Result Prediction")
        if predicted_profit >= 0:
            st.success(f"Estimated Profit: **${predicted_profit:,.2f}**")
        else:
            st.error(f"Estimated Loss: **${predicted_profit:,.2f}** (High Risk Order)")
            
        st.markdown("---")
        st.markdown("#### 🎛️ Regional Growth Scenario Simulator")
        growth_rate = st.slider("Simulated Regional Sales Growth (%)", min_value=-20, max_value=50, value=10, step=5)
        simulated_sales = total_sales * (1 + growth_rate / 100)
        st.metric("Projected Total Revenue", f"${simulated_sales:,.2f}", delta=f"{growth_rate}% Target")

    with tab3:
        st.subheader("🚨 Automated Outlier & Anomaly Detection")
        st.info("Z-Score statistical filtering to flag severe profit loss anomalies across transactional records.")
        
        filtered_df["Profit_ZScore"] = (filtered_df["Profit"] - filtered_df["Profit"].mean()) / filtered_df["Profit"].std()
        anomalies = filtered_df[filtered_df["Profit_ZScore"] < -2.0]
        
        st.warning(f"Detected **{len(anomalies)}** anomalous loss transactions (Z-Score < -2.0).")
        st.dataframe(
            anomalies[["Order ID", "Product Name", "Sales", "Profit", "Discount", "Region"]], 
            use_container_width=True
        )

    with tab4:
        st.subheader("Dataset Inspector & Executive Export")
        
        st.markdown("#### 🔎 Dynamic Order Search")
        search_query = st.text_input("Search orders by Product Name or Order ID:")
        if search_query:
            search_results = filtered_df[
                filtered_df["Product Name"].astype(str).str.contains(search_query, case=False) |
                filtered_df["Order ID"].astype(str).str.contains(search_query, case=False)
            ]
            st.dataframe(search_results, use_container_width=True)
        else:
            st.dataframe(filtered_df.head(100), use_container_width=True)
            st.caption("Showing first 100 rows based on active filters.")

        st.markdown("---")
        col_exp1, col_exp2 = st.columns(2)
        
        csv_data = filtered_df.to_csv(index=False).encode('utf-8')
        col_exp1.download_button(
            label="📥 Export Filtered Data to CSV",
            data=csv_data,
            file_name="filtered_retail_data.csv",
            mime="text/csv"
        )
        
        summary_text = f"""RETAIL PERFORMANCE EXECUTIVE REPORT
-----------------------------------------
Total Revenue: ${total_sales:,.2f}
Net Profit: ${total_profit:,.2f}
Total Orders: {total_orders:,}
Average Discount: {avg_discount:.1f}%

ANOMALY AUDIT:
Critical Loss Anomalies Detected: {len(anomalies)}
"""
        col_exp2.download_button(
            label="📄 Export Executive Summary (.txt)",
            data=summary_text,
            file_name="executive_report.txt",
            mime="text/plain"
        )

    st.sidebar.markdown("---")
    st.sidebar.caption("Developed by Anshika Mishra")

except Exception as e:
    st.error(f"Error executing dashboard: {e}")
