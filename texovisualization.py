import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Configure page
st.set_page_config(layout="wide")
st.title("Daily Operations Dashboard")
st.markdown("""
<style>
    .summary-card {background: white; border-radius: 10px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 20px;}
    .metric-value {font-size: 2.2rem; font-weight: 700; text-align: center; color: #1e3a8a;}
    .metric-label {text-align: center; font-size: 1rem; color: #4b5563; margin-top: 5px;}
    .critical {color: #ef4444 !important;}
    .warning {color: #f59e0b !important;}
    .normal {color: #10b981 !important;}
    .section-title {color: #1e3a8a; border-bottom: 2px solid #dbeafe; padding-bottom: 8px; margin-top: 25px;}
    .alert-table th {background-color: #1e3a8a !important; color: white !important;}
</style>
""", unsafe_allow_html=True)

# Generate sample data for demonstration
def generate_operations_data():
    # Create date range for last 7 days
    dates = pd.date_range(end=datetime.today(), periods=7, freq="D").strftime("%Y-%m-%d")
    
    # Equipment status data
    equipment_data = {
        "Date": dates,
        "Chillers": [98, 97, 99, 96, 97, 95, 99],
        "Compressors": [92, 94, 91, 95, 93, 96, 97],
        "Generators": [100, 100, 100, 100, 100, 100, 99],
        "Production Line": [95, 94, 96, 92, 93, 90, 97]
    }
    
    # Maintenance metrics
    maintenance_data = {
        "Date": dates,
        "Completed Work Orders": [12, 15, 14, 11, 13, 10, 16],
        "Pending Work Orders": [8, 6, 7, 9, 5, 8, 4],
        "Emergency Repairs": [2, 1, 3, 2, 1, 4, 0],
        "Preventive Maintenance": [7, 8, 6, 9, 7, 5, 8]
    }
    
    # Energy consumption
    energy_data = {
        "Date": dates,
        "Chillers (kWh)": [4200, 4350, 4100, 4450, 4300, 4600, 4000],
        "Compressors (kWh)": [3800, 3950, 3700, 4000, 3850, 4150, 3600],
        "Lighting (kWh)": [1200, 1200, 1200, 1200, 1200, 1200, 1200],
        "Total (kWh)": [9200, 9500, 9000, 9650, 9350, 9950, 8800]
    }
    
    return (
        pd.DataFrame(equipment_data),
        pd.DataFrame(maintenance_data),
        pd.DataFrame(energy_data)
    )

# Generate data
equipment_df, maintenance_df, energy_df = generate_operations_data()

# Current status indicators
st.subheader("Current Operational Status")
col1, col2, col3, col4 = st.columns(4)

with col1:
    status = "normal" if equipment_df["Chillers"].iloc[-1] >= 95 else "warning" if equipment_df["Chillers"].iloc[-1] >= 90 else "critical"
    st.markdown(f"""
    <div class="summary-card">
        <div class="metric-value {status}">{equipment_df["Chillers"].iloc[-1]}%</div>
        <div class="metric-label">Chiller Uptime</div>
        <div style="text-align: center; margin-top: 10px;">
            <small>Target: >95%</small>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    status = "normal" if equipment_df["Compressors"].iloc[-1] >= 95 else "warning" if equipment_df["Compressors"].iloc[-1] >= 90 else "critical"
    st.markdown(f"""
    <div class="summary-card">
        <div class="metric-value {status}">{equipment_df["Compressors"].iloc[-1]}%</div>
        <div class="metric-label">Compressor Uptime</div>
        <div style="text-align: center; margin-top: 10px;">
            <small>Target: >95%</small>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    status = "normal" if maintenance_df["Emergency Repairs"].iloc[-1] <= 1 else "warning" if maintenance_df["Emergency Repairs"].iloc[-1] <= 3 else "critical"
    st.markdown(f"""
    <div class="summary-card">
        <div class="metric-value {status}">{maintenance_df["Emergency Repairs"].iloc[-1]}</div>
        <div class="metric-label">Emergency Repairs</div>
        <div style="text-align: center; margin-top: 10px;">
            <small>Target: <2/day</small>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    status = "normal" if energy_df["Total (kWh)"].iloc[-1] <= 9500 else "warning" if energy_df["Total (kWh)"].iloc[-1] <= 10000 else "critical"
    st.markdown(f"""
    <div class="summary-card">
        <div class="metric-value {status}">{energy_df["Total (kWh)"].iloc[-1]:,}</div>
        <div class="metric-label">Daily Energy Usage</div>
        <div style="text-align: center; margin-top: 10px;">
            <small>Target: <9,500 kWh</small>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Equipment Uptime Trends
st.markdown('<p class="section-title">Equipment Uptime Trends</p>', unsafe_allow_html=True)
fig1 = go.Figure()

# Add traces for each equipment type
fig1.add_trace(go.Scatter(
    x=equipment_df["Date"], 
    y=equipment_df["Chillers"],
    name="Chillers",
    line=dict(color="#3b82f6", width=3),
    mode="lines+markers"
))

fig1.add_trace(go.Scatter(
    x=equipment_df["Date"], 
    y=equipment_df["Compressors"],
    name="Compressors",
    line=dict(color="#ef4444", width=3),
    mode="lines+markers"
))

fig1.add_trace(go.Scatter(
    x=equipment_df["Date"], 
    y=equipment_df["Generators"],
    name="Generators",
    line=dict(color="#10b981", width=3),
    mode="lines+markers"
))

fig1.add_trace(go.Scatter(
    x=equipment_df["Date"], 
    y=equipment_df["Production Line"],
    name="Production Line",
    line=dict(color="#f59e0b", width=3),
    mode="lines+markers"
))

# Add target line
fig1.add_hline(y=95, line_dash="dash", line_color="green", annotation_text="Target: 95%")

# Update layout
fig1.update_layout(
    title="Equipment Uptime - Last 7 Days",
    yaxis_title="Uptime (%)",
    xaxis_title="Date",
    height=400,
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
)

st.plotly_chart(fig1, use_container_width=True)

# Maintenance Metrics
st.markdown('<p class="section-title">Maintenance Operations</p>', unsafe_allow_html=True)
col1, col2 = st.columns([2, 1])

with col1:
    # Maintenance activities chart
    fig2 = go.Figure()
    
    fig2.add_trace(go.Bar(
        x=maintenance_df["Date"],
        y=maintenance_df["Completed Work Orders"],
        name="Completed",
        marker_color="#10b981"
    ))
    
    fig2.add_trace(go.Bar(
        x=maintenance_df["Date"],
        y=maintenance_df["Pending Work Orders"],
        name="Pending",
        marker_color="#f59e0b"
    ))
    
    fig2.add_trace(go.Bar(
        x=maintenance_df["Date"],
        y=maintenance_df["Emergency Repairs"],
        name="Emergency",
        marker_color="#ef4444"
    ))
    
    fig2.update_layout(
        title="Work Order Status - Last 7 Days",
        barmode="stack",
        height=400,
        yaxis_title="Number of Work Orders"
    )
    
    st.plotly_chart(fig2, use_container_width=True)

with col2:
    # Maintenance efficiency metrics
    completed = maintenance_df["Completed Work Orders"].sum()
    pending = maintenance_df["Pending Work Orders"].sum()
    emergency = maintenance_df["Emergency Repairs"].sum()
    preventive = maintenance_df["Preventive Maintenance"].sum()
    efficiency = round((completed - emergency) / completed * 100) if completed > 0 else 0
    status_class = "normal" if efficiency >= 80 else "warning" if efficiency >= 70 else "critical"
    
    # Build HTML as a single string without line breaks
    html_content = (
        f'<div class="summary-card">'
        f'<div style="font-size: 1.2rem; text-align: center; font-weight: bold; margin-bottom: 15px;">'
        f'Weekly Maintenance Summary'
        f'</div>'
        f'<div style="display: flex; justify-content: space-between; margin-bottom: 10px;">'
        f'<span>Completed:</span>'
        f'<span style="font-weight: bold;">{completed}</span>'
        f'</div>'
        f'<div style="display: flex; justify-content: space-between; margin-bottom: 10px;">'
        f'<span>Pending:</span>'
        f'<span style="font-weight: bold;">{pending}</span>'
        f'</div>'
        f'<div style="display: flex; justify-content: space-between; margin-bottom: 10px;">'
        f'<span>Emergency:</span>'
        f'<span style="font-weight: bold; color: #ef4444;">{emergency}</span>'
        f'</div>'
        f'<div style="display: flex; justify-content: space-between; margin-bottom: 10px;">'
        f'<span>Preventive:</span>'
        f'<span style="font-weight: bold;">{preventive}</span>'
        f'</div>'
        f'<div style="margin-top: 20px; text-align: center;">'
        f'<div class="metric-value {status_class}">{efficiency}%</div>'
        f'<div class="metric-label">Planned Maintenance Efficiency</div>'
        f'<div style="text-align: center; margin-top: 10px;">'
        f'<small>Target: >80%</small>'
        f'</div>'
        f'</div>'
        f'</div>'
    )
    
    st.markdown(html_content, unsafe_allow_html=True)

# Energy Consumption
st.markdown('<p class="section-title">Energy Consumption</p>', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])

with col1:
    # Energy consumption by equipment - FIXED
    fig3 = px.bar(
        energy_df.melt(id_vars="Date", 
                      value_vars=["Chillers (kWh)", "Compressors (kWh)", "Lighting (kWh)"],
                      var_name="Equipment", 
                      value_name="kWh"),
        x="Date", 
        y="kWh",
        color="Equipment",
        title="Energy Consumption by Equipment",
        labels={"kWh": "Energy Consumption (kWh)"},
        color_discrete_map={
            "Chillers (kWh)": "#3b82f6",
            "Compressors (kWh)": "#ef4444",
            "Lighting (kWh)": "#f59e0b"
        }
    )
    
    fig3.update_layout(
        barmode="stack",
        height=400,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    # Energy efficiency metrics
    avg_energy = energy_df["Total (kWh)"].mean()
    target_energy = 9500
    efficiency = round((target_energy - avg_energy) / target_energy * 100, 1)
    
    # Energy cost savings
    cost_per_kwh = 0.12  # $0.12 per kWh
    daily_savings = (target_energy - avg_energy) * cost_per_kwh if avg_energy < target_energy else 0
    
    # Create energy efficiency gauge chart
    fig4 = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = avg_energy,
        number = {'suffix': " kWh"},
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Average Daily Energy", 'font': {'size': 16}},
        gauge = {
            'axis': {'range': [None, 11000], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "#3b82f6"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 9500], 'color': '#10b981'},
                {'range': [9500, 10000], 'color': '#f59e0b'},
                {'range': [10000, 11000], 'color': '#ef4444'}],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': target_energy}}))
    
    fig4.update_layout(
        height=350,
        margin=dict(t=50, b=10, l=20, r=20)
    )
    
    st.plotly_chart(fig4, use_container_width=True)
    
    # Savings summary - FIXED HTML RENDERING
    st.markdown(
        f'<div class="summary-card" style="margin-top: 20px;">'
        f'<div style="display: flex; justify-content: space-between; margin-bottom: 10px;">'
        f'<span>Target Daily Usage:</span>'
        f'<span style="font-weight: bold;">{target_energy:,.0f} kWh</span>'
        f'</div>'
        f'<div style="display: flex; justify-content: space-between; margin-bottom: 10px;">'
        f'<span>Avg. Daily Usage:</span>'
        f'<span style="font-weight: bold;">{avg_energy:,.0f} kWh</span>'
        f'</div>'
        f'<div style="margin-top: 15px; background: #dcfce7; padding: 15px; border-radius: 8px; text-align: center;">'
        f'<div style="font-size: 1.5rem; font-weight: bold;">${daily_savings:,.2f}</div>'
        f'<div>Estimated Daily Savings</div>'
        f'<div style="font-size: 0.8rem; margin-top: 5px;">Based on ${cost_per_kwh}/kWh</div>'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True
    )

## Critical Alerts
st.markdown('<p class="section-title">Critical Alerts & Action Items</p>', unsafe_allow_html=True)

# Sample alerts data
alerts = [
    {"equipment": "Compressor #7", "issue": "Temperature exceeding threshold", "status": "High", "duration": "4 hours", "action": "Inspect cooling system"},
    {"equipment": "Chiller #3", "issue": "Low refrigerant pressure", "status": "Medium", "duration": "8 hours", "action": "Check for leaks"},
    {"equipment": "Generator #2", "issue": "Battery voltage low", "status": "Medium", "duration": "12 hours", "action": "Test and replace battery"},
    {"equipment": "Production Line B", "issue": "Vibration levels increasing", "status": "High", "duration": "2 days", "action": "Schedule bearing inspection"}
]

# Create alerts table as a single HTML string
table_html = (
    '<table class="alert-table">'
    '<thead>'
    '<tr>'
    '<th>Equipment</th>'
    '<th>Issue</th>'
    '<th>Status</th>'
    '<th>Duration</th>'
    '<th>Action Required</th>'
    '</tr>'
    '</thead>'
    '<tbody>'
)

# Add table rows
for alert in alerts:
    status_class = "status-high" if alert["status"] == "High" else "status-medium"
    table_html += (
        f'<tr>'
        f'<td><strong>{alert["equipment"]}</strong></td>'
        f'<td>{alert["issue"]}</td>'
        f'<td class="{status_class}">{alert["status"]}</td>'
        f'<td>{alert["duration"]}</td>'
        f'<td>{alert["action"]}</td>'
        f'</tr>'
    )

# Close table
table_html += '</tbody></table>'

# Display the table
st.markdown(table_html, unsafe_allow_html=True)

# Performance Summary
st.markdown('<p class="section-title">Performance Summary</p>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="summary-card">
        <div style="text-align: center; font-weight: bold; margin-bottom: 15px;">
            ✅ Positive Trends
        </div>
        <ul>
            <li>Generator uptime at 100% for 6 days</li>
            <li>Emergency repairs reduced by 33% this week</li>
            <li>Energy consumption 7% below target yesterday</li>
            <li>Preventive maintenance compliance at 98%</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="summary-card">
        <div style="text-align: center; font-weight: bold; margin-bottom: 15px; color: #f59e0b;">
            ⚠ Watch Areas
        </div>
        <ul>
            <li>Compressor #7 running hot (needs inspection)</li>
            <li>Chiller #3 refrigerant pressure low</li>
            <li>Production Line B vibration increasing</li>
            <li>Pending work orders increased by 20%</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="summary-card">
        <div style="text-align: center; font-weight: bold; margin-bottom: 15px;">
            📅 Upcoming Priorities
        </div>
        <ul>
            <li>Monthly maintenance on Generator #1 (Tomorrow)</li>
            <li>Quarterly inspection of all chillers (Next Week)</li>
            <li>Compressor efficiency audit (Friday)</li>
            <li>Energy optimization review meeting (Tomorrow 10AM)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')} | Data refreshes every 15 minutes")
