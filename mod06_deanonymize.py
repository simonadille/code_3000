import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df, aux_df):
    """
    Attempt to link anonymized records to auxiliary records
    using exact matching on quasi-identifiers.

    Returns a DataFrame with columns:
      anon_id, matched_name
    containing ONLY uniquely matched records.
    """
    # Merge the datasets on the quasi-identifiers (age, gender, zip3)
    merged = pd.merge(
        anon_df, 
        aux_df, 
        on=['age', 'gender', 'zip3'], 
        how='inner',
        suffixes=('_anon', '_aux')
    )
    
    # Identify records that match to a single unique name
    # Group by the anonymized record identifier and count unique names
    unique_matches = merged.groupby('anon_id').agg(
        unique_names=pd.NamedAgg(column='name', aggfunc='nunique'),
        matched_name=pd.NamedAgg(column='name', aggfunc='first')
    ).reset_index()
    
    # Keep only records with exactly one unique name match
    unique_matches = unique_matches[unique_matches['unique_names'] == 1]
    
    # Return only the required columns
    return unique_matches[['anon_id', 'matched_name']]


def deanonymization_rate(matches_df, anon_df):
    """
    Compute the fraction of anonymized records
    that were uniquely re-identified.
    """
    # Count the number of successfully matched records
    num_matched = len(matches_df)
    
    # Count the total number of anonymized records
    total_records = len(anon_df)
    
    # Calculate the rate
    if total_records > 0:
        rate = num_matched / total_records
    else:
        rate = 0.0
    
    return rate