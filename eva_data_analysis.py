import json
import csv
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt

# Data source: https://data.nasa.gov/resource/eva.json (with modifications)
input_file = open('./eva-data.json', 'r')
output_file = open('./eva-data.csv', 'w')
graph_file = './cumulative_eva_graph.png'

# Read the data from JSON file
eva_data = read_json_to_dataframe(input_file)

# Convert and export data to CSV file
write_dataframe_to_csv(eva_data, output_file)

print(f'Plotting cumulative spacewalk duration and saving to {graph_file}')

# Plot cumulative time spent in space over years
eva_df['duration_hours'] = eva_df['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
eva_df['cumulative_time'] = eva_df['duration_hours'].cumsum()
plt.plot(eva_df['date'], eva_df['cumulative_time'], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(graph_file)
plt.show()


print("--END--")


