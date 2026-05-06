import pandas as pd

def load_behaviour_data(path):
    """Load behavioural dataset from a CSV file."""
    return pd.read_csv(path)

def compute_activity_budget(df, behaviour_column):
    """
    Compute the proportion of time spent in each behaviour.
    df: pandas DataFrame
    behaviour_column: name of the column with behaviour labels
    """
    return df[behaviour_column].value_counts(normalize=True)

def filter_individual(df, individual_id, id_column="id"):
    """Return data for a single individual."""
    return df[df[id_column] == individual_id]
