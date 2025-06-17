import streamlit as st

def get_status_class(value, thresholds, reverse=False):
    if reverse:
        if value <= thresholds["normal"]:
            return "normal"
        elif value <= thresholds["warning"]:
            return "warning"
        else:
            return "critical"
    else:
        if value >= thresholds["normal"]:
            return "normal"
        elif value >= thresholds["warning"]:
            return "warning"
        else:
            return "critical"

def create_status_card(value, label, target, thresholds, reverse=False):
    status_class = get_status_class(value, thresholds, reverse)
    return f"""
    <div class="summary-card">
        <div class="metric-value {status_class}">{value}{'%' if '%' in label else ''}</div>
        <div class="metric-label">{label}</div>
        <div style="text-align: center; margin-top: 10px;">
            <small>Target: {target}</small>
        </div>
    </div>
    """

def display_status_cards(equipment_df, maintenance_df, energy_df):
    col1, col2, col3, col4 = st.columns(4)
    
    # Define thresholds for each card
    thresholds = {
        "chillers": {"normal": 95, "warning": 90},
        "compressors": {"normal": 95, "warning": 90},
        "emergency": {"normal": 1, "warning": 3},
        "energy": {"normal": 9500, "warning": 10000}
    }
    
    with col1:
        value = equipment_df["Chillers"].iloc[-1]
        st.markdown(create_status_card(
            value, "Chiller Uptime", ">95%", thresholds["chillers"]
        ), unsafe_allow_html=True)
    
    with col2:
        value = equipment_df["Compressors"].iloc[-1]
        st.markdown(create_status_card(
            value, "Compressor Uptime", ">95%", thresholds["compressors"]
        ), unsafe_allow_html=True)
    
    with col3:
        value = maintenance_df["Emergency Repairs"].iloc[-1]
        st.markdown(create_status_card(
            value, "Emergency Repairs", "<2/day", thresholds["emergency"], reverse=True
        ), unsafe_allow_html=True)
    
    with col4:
        value = energy_df["Total (kWh)"].iloc[-1]
        st.markdown(create_status_card(
            value, "Daily Energy Usage", "<9,500 kWh", thresholds["energy"], reverse=True
        ), unsafe_allow_html=True)