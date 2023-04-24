import pandas as pd

data_path = 'data/scraped_data.csv'
cleaned_data = 'data/cleaned_scraped_data.csv'
transformed_data = 'data/transformed_data.csv'

def load_data(filepath):
    return pd.read_csv(filepath, index_col=0)

def clean_name(df):
    df['name'] = df['name'].map(lambda x: x.replace('†', '').strip())
    df['name'] = df['name'].map(lambda x: x.replace('(c)', '').strip())

def batted_out_bool(df):
    df['batted_out'] = df['batted_out'].map(lambda x: 'no' if 'not out' in x else 'yes')

def get_raw_cleaned_data():
    df = load_data(data_path)
    clean_name(df)
    batted_out_bool(df)
    df.to_csv(cleaned_data)
    return df

def get_games_played_count(df):
    return df['name'].value_counts().rename('count')

def get_total_stats(df):
    return df.groupby('name')[['runs', 'balls_faced', 'fours', 'sixes']].sum().reset_index()

def join_total_stats_with_games_count(stats_df, counts_df):
    return stats_df.merge(counts_df, how='left', on='name').sort_values(by='runs', ascending=False)

def get_transformed_data():
    df = pd.read_csv(cleaned_data)
    total_stats = get_total_stats(df)
    games_played_count = get_games_played_count(df)
    df = join_total_stats_with_games_count(total_stats, games_played_count)
    df.to_csv(transformed_data)
    return df

"""RUN SCRIPT"""
print(get_raw_cleaned_data())
print(get_transformed_data())

