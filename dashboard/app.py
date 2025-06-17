import streamlit as st
from components import data, status_cards, charts, summary_cards
from utils.style import apply_custom_style
from datetime import datetime

# Configure page and apply styles
st.set_page_config(layout="wide")
st.title("Daily Operations Dashboard")
apply_custom_style()

# Load data
equipment_df, maintenance_df, energy_df = data.load_data()

# Current status indicators
st.subheader("Current Operational Status")
status_cards.display_status_cards(equipment_df, maintenance_df, energy_df)

# Equipment Uptime Trends
st.markdown('<p class="section-title">Equipment Uptime Trends</p>', unsafe_allow_html=True)
equipment_chart = charts.create_equipment_uptime_chart(equipment_df)
st.plotly_chart(equipment_chart, use_container_width=True)

# Maintenance Metrics
st.markdown('<p class="section-title">Maintenance Operations</p>', unsafe_allow_html=True)
col1, col2 = st.columns([2, 1])
with col1:
    maintenance_chart = charts.create_maintenance_chart(maintenance_df)
    st.plotly_chart(maintenance_chart, use_container_width=True)
with col2:
    summary_cards.display_maintenance_summary(maintenance_df)

# Energy Consumption
st.markdown('<p class="section-title">Energy Consumption</p>', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])
with col1:
    energy_chart = charts.create_energy_consumption_chart(energy_df)
    st.plotly_chart(energy_chart, use_container_width=True)
with col2:
    gauge_chart = charts.create_energy_gauge(energy_df)
    st.plotly_chart(gauge_chart, use_container_width=True)
    summary_cards.display_energy_summary(energy_df)

# Critical Alerts
st.markdown('<p class="section-title">Critical Alerts & Action Items</p>', unsafe_allow_html=True)
summary_cards.display_alerts_table()

# Performance Summary
st.markdown('<p class="section-title">Performance Summary</p>', unsafe_allow_html=True)
summary_cards.display_performance_summary()

# Footer
st.markdown("---")
st.caption(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')} | Data refreshes every 15 minutes")