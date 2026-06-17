import pandas as pd

df = pd.read_csv('telemetry_data.csv') # loads csv file and stores in a dataframe

temp_anomaly = df['temperature_c'] > 85.0 # variable holding temperature anomalies (true/false)
vibration_anomaly = df['vibration_mm_s'] > 15.0 # variable holding vibration anomalies (true/false)

anomalies = df[temp_anomaly | vibration_anomaly] # variable holding all anomalies found (either temperature or vibration anomalies) 

print(f"Found {len(anomalies)} anomalies out of {len(df)} records") # string printed using f-strings with total number of anomalies
print(anomalies) # prints the anomalies dataframe