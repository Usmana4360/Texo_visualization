import pandas as pd
import numpy as np
from datetime import datetime

def generate_operations_data():
    dates = pd.date_range(end=datetime.today(), periods=7, freq="D").strftime("%Y-%m-%d")
    
    equipment_data = {
        "Date": dates,
        "Chillers": [98, 97, 99, 96, 97, 95, 99],
        "Compressors": [92, 94, 91, 95, 93, 96, 97],
        "Generators": [100, 100, 100, 100, 100, 100, 99],
        "Production Line": [95, 94, 96, 92, 93, 90, 97]
    }
    
    maintenance_data = {
        "Date": dates,
        "Completed Work Orders": [12, 15, 14, 11, 13, 10, 16],
        "Pending Work Orders": [8, 6, 7, 9, 5, 8, 4],
        "Emergency Repairs": [2, 1, 3, 2, 1, 4, 0],
        "Preventive Maintenance": [7, 8, 6, 9, 7, 5, 8]
    }
    
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

def load_data():
    # In production, replace this with real data loading
    return generate_operations_data()