# src/user_analysis.py
def aggregate_user_behavior(df):
    """Aggregate user behavior metrics."""
    df['total_data'] = df['download'] + df['upload']
    aggregated = df.groupby('user_id').agg({
        'session_count': 'sum',
        'session_duration': 'sum',
        'download': 'sum',
        'upload': 'sum',
        'total_data': 'sum'
    }).reset_index()
    return aggregated
