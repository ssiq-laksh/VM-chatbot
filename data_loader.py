import pandas as pd

def load_vm_data():
    try:
        df = pd.read_csv("data/vm-data.csv", low_memory=False)
        print("Loaded VM Data")
        return df
    except Exception as e:
        print("Failed to load vm-data.csv:", e)
        return pd.DataFrame()
