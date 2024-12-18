import pandas as pd
import pickle
import sys

try:
    # Set up - use absolute path for pickle file
    statistics_file = '/Users/lukehsu/Desktop/biomedical-data-pipeline/scripts/pickles/p1_111_statistics.pkl'
    with open(statistics_file, 'rb') as f:
        statistics = pickle.load(f)

    target_columns = ['emg0', 'emg1', 'emg2', 'emg3', 'emg4', 'emg5', 'emg6', 'emg7']

    # Read input from stdin
    df = pd.read_csv(sys.stdin)

    # Standardize data and add new columns
    for column in target_columns:
        mean = statistics[column]['mean']
        std = statistics[column]['std']
        # Create new standardized column
        df[f'{column}_standardized'] = (df[column] - mean) / std

    # Write to stdout and ensure proper flushing
    df.to_csv(sys.stdout, index=False)
    sys.stdout.flush()
    sys.exit(0)

except Exception as e:
    print(str(e), file=sys.stderr)
    sys.stderr.flush()
    sys.exit(1)
