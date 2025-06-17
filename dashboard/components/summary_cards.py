import streamlit as st
import pandas as pd

def display_maintenance_summary(maintenance_df):
    completed = maintenance_df["Completed Work Orders"].sum()
    pending = maintenance_df["Pending Work Orders"].sum()
    emergency = maintenance_df["Emergency Repairs"].sum()
    preventive = maintenance_df["Preventive Maintenance"].sum()
    efficiency = round((completed - emergency) / completed * 100) if completed > 0 else 0
    
    status_class = "normal" if efficiency >= 80 else "warning" if efficiency >= 70 else "critical"
    
    html_content = f"""
    <div class="summary-card">
        <div style="font-size: 1.2rem; text-align: center; font-weight: bold; margin-bottom: 15px;">
            Weekly Maintenance Summary
        </div>
        <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
            <span>Completed:</span>
            <span style="font-weight: bold;">{completed}</span>
        </div>
        <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
            <span>Pending:</span>
            <span style="font-weight: bold;">{pending}</span>
        </div>
        <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
            <span>Emergency:</span>
            <span style="font-weight: bold; color: #ef4444;">{emergency}</span>
        </div>
        <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
            <span>Preventive:</span>
            <span style="font-weight: bold;">{preventive}</span>
        </div>
        <div style="margin-top: 20px; text-align: center;">
            <div class="metric-value {status_class}">{efficiency}%</div>
            <div class="metric-label">Planned Maintenance Efficiency</div>
            <div style="text-align: center; margin-top: 10px;">
                <small>Target: >80%</small>
            </div>
        </div>
    </div>
    """
    
    st.markdown(html_content, unsafe_allow_html=True)

def display_energy_summary(energy_df):
    avg_energy = energy_df["Total (kWh)"].mean()
    target_energy = 9500
    cost_per_kwh = 0.12
    daily_savings = (target_energy - avg_energy) * cost_per_kwh if avg_energy < target_energy else 0
    
    html_content = f"""
    <div class="summary-card" style="margin-top: 20px;">
        <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
            <span>Target Daily Usage:</span>
            <span style="font-weight: bold;">{target_energy:,.0f} kWh</span>
        </div>
        <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
            <span>Avg. Daily Usage:</span>
            <span style="font-weight: bold;">{avg_energy:,.0f} kWh</span>
        </div>
        <div style="margin-top: 15px; background: #dcfce7; padding: 15px; border-radius: 8px; text-align: center;">
            <div style="font-size: 1.5rem; font-weight: bold;">${daily_savings:,.2f}</div>
            <div>Estimated Daily Savings</div>
            <div style="font-size: 0.8rem; margin-top: 5px;">Based on ${cost_per_kwh}/kWh</div>
        </div>
    </div>
    """
    
    st.markdown(html_content, unsafe_allow_html=True)

def display_alerts_table():
    alerts = [
        {"equipment": "Compressor #7", "issue": "Temperature exceeding threshold", 
         "status": "High", "duration": "4 hours", "action": "Inspect cooling system"},
        {"equipment": "Chiller #3", "issue": "Low refrigerant pressure", 
         "status": "Medium", "duration": "8 hours", "action": "Check for leaks"},
        {"equipment": "Generator #2", "issue": "Battery voltage low", 
         "status": "Medium", "duration": "12 hours", "action": "Test and replace battery"},
        {"equipment": "Production Line B", "issue": "Vibration levels increasing", 
         "status": "High", "duration": "2 days", "action": "Schedule bearing inspection"}
    ]
    
    # Build the entire table HTML as a single concatenated string without line breaks
    table_html = '<table class="alert-table"><thead><tr><th>Equipment</th><th>Issue</th><th>Status</th><th>Duration</th><th>Action Required</th></tr></thead><tbody>'
    
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
    
    table_html += '</tbody></table>'
    st.markdown(table_html, unsafe_allow_html=True)

def display_performance_summary():
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