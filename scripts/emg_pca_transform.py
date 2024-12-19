import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

file_name = 'p1_111'

def create_pca_transform(csv_file, target_columns, n_components=None):
    # Read the CSV file
    data = pd.read_csv(csv_file)
    
    # Extract target columns
    X = data[target_columns]
    
    # Initialize and fit StandardScaler
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Initialize and fit PCA
    pca = PCA(n_components=n_components)
    pca.fit(X_scaled)
    
    # Create transformation dictionary
    transform_dict = {
        'scaler': scaler,
        'pca': pca
    }
    
    return transform_dict

def apply_pca_transform(data, transform_dict, target_columns):
    # Extract only target columns
    X = data[target_columns]
    
    # Apply scaling
    X_scaled = transform_dict['scaler'].transform(X)
    
    # Apply PCA transformation
    X_pca = transform_dict['pca'].transform(X_scaled)
    
    return X_pca


# File paths
csv_file = '/Users/lukehsu/Desktop/biomedical-data-pipeline/data/emg_data/p1/'+file_name+'.csv'
target_columns = ['emg0', 'emg1', 'emg2', 'emg3', 'emg4', 'emg5', 'emg6', 'emg7']

# Part 1: create PCA transformation
# Create PCA transformation
def test_transformation_creation():
    transform_dict = create_pca_transform(csv_file, target_columns, 3)

    # Save transformation to pickle file
    with open('/Users/lukehsu/Desktop/biomedical-data-pipeline/scripts/pickles/'+file_name+'_pca_transform.pkl', 'wb') as f:
        pickle.dump(transform_dict, f)

    # Print explained variance ratio
    print("Explained variance ratio:", transform_dict['pca'].explained_variance_ratio_)

# Part 2: apply PCA transformation
def test_applying_transformation():
    transform_dict = pickle.load(open('/Users/lukehsu/Desktop/biomedical-data-pipeline/scripts/pickles/'+file_name+'_pca_transform.pkl', 'rb'))
    data = pd.read_csv(csv_file)
    transformed_data = apply_pca_transform(data, transform_dict, target_columns)
    print(transformed_data[:10])

test_applying_transformation()

