from src.etl.transform import *

def test_cleaned_data_columns():
    df = load_data(cleaned_data_path)
    cols = ["name", "runs", "balls_faced", "fours", "sixes", "batted_out", "date"]
    assert all(col in df.columns for col in cols)

def test_transformed_data_columns():
    df = load_data(transformed_data_path)
    print(df)
    cols = ["name", "runs", "balls_faced", "fours", "sixes", "count"]
    assert all(col in df.columns for col in cols)
    
def test_cleaned_data_expected_column_datatypes():
    df = load_data(cleaned_data_path)
    expected_data_types = {'name': 'object', 
                           'runs': 'int64', 
                           'balls_faced': 'int64',
                           'fours': 'int64', 
                           'sixes': 'int64', 
                           'date': 'object'}
    for col_name, expected_type in expected_data_types.items():
        assert str(df[col_name].dtype) == expected_type

def test_cleaned_names():
    df = load_data(cleaned_data_path)
    assert not df['name'].str.contains('†').any(), "'†' character found"
    assert not df['name'].str.contains('(c)', regex=False).any(), "'(c)' character found"


def test_batted_out_bool():
    df = load_data(cleaned_data_path)
    assert df['batted_out'].isin(['yes', 'no']).all()

def test_transformed_data():
    df = load_data(transformed_data_path)
    assert df['runs'].max() == 405