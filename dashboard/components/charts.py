import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

def create_equipment_uptime_chart(equipment_df):
    fig = go.Figure()
    
    # Add traces for each equipment type
    colors = {
        "Chillers": "#3b82f6",
        "Compressors": "#ef4444",
        "Generators": "#10b981",
        "Production Line": "#f59e0b"
    }
    
    for column in ["Chillers", "Compressors", "Generators", "Production Line"]:
        fig.add_trace(go.Scatter(
            x=equipment_df["Date"], 
            y=equipment_df[column],
            name=column,
            line=dict(color=colors[column], width=3),
            mode="lines+markers"
        ))
    
    # Add target line
    fig.add_hline(y=95, line_dash="dash", line_color="green", annotation_text="Target: 95%")
    
    # Update layout
    fig.update_layout(
        title="Equipment Uptime - Last 7 Days",
        yaxis_title="Uptime (%)",
        xaxis_title="Date",
        height=400,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    return fig

def create_maintenance_chart(maintenance_df):
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=maintenance_df["Date"],
        y=maintenance_df["Completed Work Orders"],
        name="Completed",
        marker_color="#10b981"
    ))
    
    fig.add_trace(go.Bar(
        x=maintenance_df["Date"],
        y=maintenance_df["Pending Work Orders"],
        name="Pending",
        marker_color="#f59e0b"
    ))
    
    fig.add_trace(go.Bar(
        x=maintenance_df["Date"],
        y=maintenance_df["Emergency Repairs"],
        name="Emergency",
        marker_color="#ef4444"
    ))
    
    fig.update_layout(
        title="Work Order Status - Last 7 Days",
        barmode="stack",
        height=400,
        yaxis_title="Number of Work Orders"
    )
    
    return fig

def create_energy_consumption_chart(energy_df):
    melted_df = energy_df.melt(
        id_vars="Date", 
        value_vars=["Chillers (kWh)", "Compressors (kWh)", "Lighting (kWh)"],
        var_name="Equipment", 
        value_name="kWh"
    )
    
    fig = px.bar(
        melted_df,
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
    
    fig.update_layout(
        barmode="stack",
        height=400,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    return fig

def create_energy_gauge(energy_df):
    avg_energy = energy_df["Total (kWh)"].mean()
    target_energy = 9500
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=avg_energy,
        number={"suffix": " kWh"},
        domain={"x": [0, 1], "y": [0, 1]},
        title={"text": "Average Daily Energy", "font": {"size": 16}},
        gauge={
            "axis": {"range": [None, 11000], "tickwidth": 1, "tickcolor": "darkblue"},
            "bar": {"color": "#3b82f6"},
            "bgcolor": "white",
            "borderwidth": 2,
            "bordercolor": "gray",
            "steps": [
                {"range": [0, 9500], "color": "#10b981"},
                {"range": [9500, 10000], "color": "#f59e0b"},
                {"range": [10000, 11000], "color": "#ef4444"}],
            "threshold": {
                "line": {"color": "black", "width": 4},
                "thickness": 0.75,
                "value": target_energy
            }
        }
    ))
    
    fig.update_layout(height=350, margin=dict(t=50, b=10, l=20, r=20))
    return fig