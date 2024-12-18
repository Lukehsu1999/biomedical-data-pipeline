import pandas as pd
import pickle

statistics_file = '/Users/lukehsu/Desktop/biomedical-data-pipeline/scripts/pickles/p1_111_statistics.pkl'
with open(statistics_file, 'rb') as f:
    statistics = pickle.load(f)

def standardize_data(data):
    standardized_data = {}
    for column in data.columns:
        mean = statistics[column]['mean']
        std = statistics[column]['std']
        standardized_data[column] = (data[column] - mean) / std
    return standardized_data

# Example of standardizing new data
# new_data = pd.DataFrame({
#     'emg0': [45,30,55],
#     'emg1': [144,120,160],
#     'emg2': [198,150,220],
#     'emg3': [85,70,100],
#     'emg4': [88,65,110],
#     'emg5': [53,40,70],
#     'emg6': [40,30,50],
#     'emg7': [77,60,90]
# })
# standardized_new_data = standardize_data(new_data)
# print("\nStandardized new data:")
# print(standardized_new_data)

# test on first ten rows of p1_111.csv
csv_file = '/Users/lukehsu/Desktop/biomedical-data-pipeline/data/emg_data/p1/p1_111.csv'
data = pd.read_csv(csv_file)
data = data.head(10)

target_columns = ['emg0', 'emg1','emg2','emg3','emg4','emg5','emg6','emg7']

# only standardize the target columns
standardized_data = standardize_data(data[target_columns])
print("\nStandardized data:")
print(standardized_data)
#standardized_data = standardize_data(data)
#print("\nStandardized data:")
#print(standardized_data)