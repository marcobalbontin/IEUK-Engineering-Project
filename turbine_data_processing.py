import pandas as pd

df = pd.read_csv('telemetry_data.csv') # loads csv file and stores in a dataframe

temp_anomaly = df['temperature_c'] > 85.0 # variable defined for for temperature anomalies
vibration_anomaly = df['vibration_mm_s'] > 15.0 # variable defined for vibration anomalies

anomalies = df[temp_anomaly | vibration_anomaly]

print(f"Found {len(anomalies)} anomalies out of {len(df)} records")
print(anomalies)