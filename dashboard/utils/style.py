import streamlit as st
def apply_custom_style():
    st.markdown("""
    <style>
        .summary-card {background: white; border-radius: 10px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 20px;}
        .metric-value {font-size: 2.2rem; font-weight: 700; text-align: center; color: #1e3a8a;}
        .metric-label {text-align: center; font-size: 1rem; color: #4b5563; margin-top: 5px;}
        .critical {color: #ef4444 !important;}
        .warning {color: #f59e0b !important;}
        .normal {color: #10b981 !important;}
        .section-title {color: #1e3a8a; border-bottom: 2px solid #dbeafe; padding-bottom: 8px; margin-top: 25px;}
        
        /* Add table styling */
        .alert-table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }
        .alert-table th, .alert-table td {
            border: 1px solid #e5e7eb;
            padding: 12px;
            text-align: left;
        }
        .alert-table th {
            background-color: #1e3a8a;
            color: white;
            font-weight: bold;
        }
        .alert-table tr:nth-child(even) {
            background-color: #f9fafb;
        }
        .status-high {
            color: #ef4444;
            font-weight: bold;
        }
        .status-medium {
            color: #f59e0b;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True)