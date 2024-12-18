import pandas as pd

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
csv_file = '/Users/lukehsu/Desktop/biomedical-data-pipeline/data/emg_data/p1/p1_111.csv'
target_columns = ['emg0', 'emg1','emg2','emg3','emg4','emg5','emg6','emg7',]

# Calculate statistics
statistics = calculate_statistics(csv_file, target_columns)
print("Statistics:", statistics)

# Example of standardizing new data
new_data = pd.DataFrame({
    'emg0': [45,30,55],
    'emg1': [144,120,160],
    'emg2': [198,150,220],
    'emg3': [85,70,100],
    'emg4': [88,65,110],
    'emg5': [53,40,70],
    'emg6': [40,30,50],
    'emg7': [77,60,90]
})
standardized_new_data = standardize_data(new_data, statistics)
print("\nStandardized new data:")
print(standardized_new_data)
