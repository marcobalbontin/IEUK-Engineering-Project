import pandas as pd

df = pd.read_csv('telemetry_data.csv') # loads csv file and stores in a dataframe

temp_anomaly = df['temperature_c'] > 85.0 # variable holding temperature anomalies (true/false)
vibration_anomaly = df['vibration_mm_s'] > 15.0 # variable holding vibration anomalies (true/false)

anomalies = df[temp_anomaly | vibration_anomaly] # variable holding all anomalies found (either temperature or vibration anomalies) 

print(f"Found {len(anomalies)} anomalies out of {len(df)} records") # string printed using f-strings with total number of anomalies
print(anomalies) # prints the anomalies dataframe

print("")
print("First anomalies in faulty turbines:")
first_anomaly_per_turbine = anomalies.drop_duplicates(subset='turbine_id') # identifies the first anomaly for each faulty turbine
print(first_anomaly_per_turbine)

print("")
print("Number of anomalies per each turbine:")
turbine_counts = anomalies['turbine_id'].value_counts() # returns the turbine ID with count of faults
print(turbine_counts)