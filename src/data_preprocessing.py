import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

def preprocess_data(df):
    X = df[['no_of_test_cases', 'no_of_failed_tests', 'code_changes', 'past_bugs']]
    y = df['bug_found']
    return X, y
