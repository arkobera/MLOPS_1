import pandas as pd
import numpy as np

def generate_data(num_rows=100):
    data = {
        "feature1": np.random.rand(num_rows),
        "feature2": np.random.rand(num_rows),
        "label": np.random.randint(0, 2, num_rows)
    }
    return pd.DataFrame(data)

import os
def save_data(df, filename="data.csv"):
    data_dir = "DATA"
    os.makedirs(data_dir, exist_ok=True)
    filepath = os.path.join(data_dir, filename)
    df.to_csv(filepath, index=False)
    print(f"Data saved to {filepath}")

if __name__ == "__main__":
    df = generate_data(100)
    save_data(df, "data.csv")
    print("Data generation complete.")