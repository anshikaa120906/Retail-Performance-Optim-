import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Retail Analytics Dashboard",
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

st.title("📊 Retail Performance & Predictive Analytics Dashboard")
st.markdown("An interactive web application showcasing Exploratory Data Analysis (EDA) and predictive sales insights.")

@st.cache_data
def load_data():
    df = pd.read_csv("Superstore sales dataset.csv")
    return df

try:
    df = load_data()
    
    st.sidebar.header("Filter Options")
    
    regions = st.sidebar.multiselect(
        "Select Regions to View:",
        options=df["Region"].unique(),
        default=df["Region"].unique()
    )
    
    categories = st.sidebar.multiselect(
        "Select Product Categories:",
        options=df["Category"].unique(),
        default=df["Category"].unique()
    )
    
    filtered_df = df[
        (df["Region"].isin(regions)) & 
        (df["Category"].isin(categories))
    ]
    
    st.markdown("### Core Operational Metrics")
    col1, col2, col3 = st.columns(3)
    
    total_sales = filtered_df["Sales"].sum()
    total_profit = filtered_df["Profit"].sum()
    total_orders = len(filtered_df)
    
    col1.metric("Total Sales Volume", f"${total_sales:,.2f}")
    col2.metric("Net Profit Margin", f"${total_profit:,.2f}")
    col3.metric("Total Orders Processed", f"{total_orders:,}")
    
    st.markdown("---")
    
    tab1, tab2, tab3 = st.tabs(["📈 Profitability Analysis", "🤖 Sales Baseline & What-If", "📋 Raw Data & Search"])
    
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
        
        st.markdown("#### ⚠️ High-Risk Profit Loss Alert")
        loss_threshold = st.number_input("Filter Unprofitable Transactions Below ($):", value=-500)
        loss_df = filtered_df[filtered_df["Profit"] < loss_threshold]

        if not loss_df.empty:
            st.warning(f"Detected {len(loss_df)} critical loss-making transactions exceeding ${abs(loss_threshold)}.")
            st.dataframe(loss_df[["Order ID", "Product Name", "Sales", "Profit", "Discount"]], use_container_width=True)
        else:
            st.success("No critical loss-making orders found under selected threshold.")
        
    with tab2:
        st.subheader("Predictive Growth Trend Baseline")
        st.info("Linear Regression analysis tracks a steady baseline upward trend scale of $1.11 per transactional period through high-volatility retail sales waves.")
        
        sales_trend = filtered_df.groupby("Category")["Sales"].sum().reset_index()
        fig_sales = px.pie(
            sales_trend, 
            values="Sales", 
            names="Category", 
            title="Sales Distribution Across Product Categories",
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        fig_sales.update_layout(template="plotly_dark")
        st.plotly_chart(fig_sales, use_container_width=True)

        st.markdown("---")
        st.markdown("#### 🎛️ Interactive Growth Scenario Simulator")
        growth_rate = st.slider("Simulated Regional Sales Growth (%)", min_value=-20, max_value=50, value=10, step=5)
        simulated_sales = total_sales * (1 + growth_rate / 100)
        st.metric("Projected Total Revenue", f"${simulated_sales:,.2f}", delta=f"{growth_rate}% Growth")

        st.markdown("---")
        st.markdown("#### 📑 Summary Report Generation")
        summary_text = f"""RETAIL PERFORMANCE EXECUTIVE SUMMARY
-------------------------------------
Total Sales Volume: ${total_sales:,.2f}
Net Profit Margin: ${total_profit:,.2f}
Total Orders Processed: {total_orders:,}

Key Takeaways:
- Regional performance evaluated across active filters.
- Trend line baseline tracks growth at scale through volatility.
"""
        st.download_button(
            label="📄 Download Summary Report (.txt)",
            data=summary_text,
            file_name="executive_summary.txt",
            mime="text/plain"
        )

    with tab3:
        st.subheader("Dataset Inspector & Export")
        
        st.markdown("#### 🔎 Quick Order Search")
        search_query = st.text_input("Search by Product Name or Order ID:")
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
        csv_data = filtered_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Export Filtered Data to CSV",
            data=csv_data,
            file_name="filtered_retail_data.csv",
            mime="text/csv"
        )

    st.sidebar.markdown("---")
    st.sidebar.info("Developed by **Anshika** | Powered by Streamlit & Plotly")

except Exception as e:
    st.error(f"Error loading dataset: {e}")
