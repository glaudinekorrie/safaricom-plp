import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title='Sales Dashboard', layout='wide')

st.title('📊 Sales Dashboard MVP')

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, parse_dates=['date'])

    # Sidebar filters
    st.sidebar.header("Filters")
    product_filter = st.sidebar.multiselect("Product", options=df['product'].unique(), default=df['product'].unique())
    region_filter = st.sidebar.multiselect("Region", options=df['region'].unique(), default=df['region'].unique())
    rep_filter = st.sidebar.multiselect("Sales Rep", options=df['sales_rep'].unique(), default=df['sales_rep'].unique())

    # Apply filters
    filtered_df = df[
        (df['product'].isin(product_filter)) &
        (df['region'].isin(region_filter)) &
        (df['sales_rep'].isin(rep_filter))
    ]

    # KPIs
    st.subheader("🔢 Key Metrics")
    total_sales = filtered_df['total_sales'].sum()
    avg_conversion = filtered_df['conversion_rate'].mean()
    st.metric("Total Sales", f"Ksh {total_sales:,.0f}")
    st.metric("Avg. Conversion Rate", f"{avg_conversion:.2%}")

    # Line chart: Sales over time
    st.subheader("📈 Sales Over Time")
    line_data = filtered_df.groupby('date')['total_sales'].sum().reset_index()
    fig1, ax1 = plt.subplots()
    sns.lineplot(data=line_data, x='date', y='total_sales', marker='o', ax=ax1)
    ax1.set_ylabel("Total Sales")
    ax1.set_xlabel("Date")
    st.pyplot(fig1)

    # Bar chart: Sales by Product
    st.subheader("📊 Sales by Product")
    bar_data = filtered_df.groupby('product')['total_sales'].sum().reset_index()
    fig2, ax2 = plt.subplots()
    sns.barplot(data=bar_data, x='product', y='total_sales', ax=ax2)
    ax2.set_ylabel("Total Sales")
    ax2.set_xlabel("Product")
    st.pyplot(fig2)

else:
    st.info("Please upload a CSV file to start.")
