import pandas as pd
import pickle

file_name = 'p1_111'
def calculate_statistics(csv_file, target_columns):
    # Read the CSV file
    data = pd.read_csv(csv_file)
    
    # Calculate mean and standard deviation for target columns
    stats = {}
    for column in target_columns:
        mean = data[column].mean()
        std = data[column].std()
        stats[column] = {'mean': mean, 'std': std}
    
    return stats

def standardize_data(data, stats):
    standardized_data = data.copy()
    for column, values in stats.items():
        mean = values['mean']
        std = values['std']
        standardized_data[column] = (data[column] - mean) / std
    return standardized_data

# Example usage
csv_file = '/Users/lukehsu/Desktop/biomedical-data-pipeline/data/emg_data/p1/'+file_name+'.csv'
target_columns = ['emg0', 'emg1','emg2','emg3','emg4','emg5','emg6','emg7',]

# Calculate statistics
statistics = calculate_statistics(csv_file, target_columns)
print("Statistics:", statistics)

# Save statistics to a file
with open('/Users/lukehsu/Desktop/biomedical-data-pipeline/scripts/pickles/'+file_name+'_statistics.pkl', 'wb') as f:
    pickle.dump(statistics, f)


