import pandas as pd
import os
from typing import List
import subprocess
import numpy as np


BRAZIL_ROW_COUNT = USA_ROW_COUNT = 33
COLS_NO = 8
COLS_NAMES = ['DIM_TIME',
              'Life Expectancy',
              'HYPERTENSION_RATE_PER_100_N',
              'HYPERTENSION_RATE_PER_100_NL',
              'HYPERTENSION_RATE_PER_100_NU',
              'UHC_INDEX_N',
              'DTP3_RATE_PER_100_N',
              'MVC2_RATE_PER_100_N']
COLS_DATATYPES = [np.dtype('int64'), np.dtype('float64'), np.dtype('float64'), np.dtype('float64'), np.dtype('float64'), np.dtype('float64'), np.dtype('float64'), np.dtype('float64')]

def test_pipeline(output_dir:str):
    # execute data pipeline, remove files later 
    try:
        subprocess.run(["python", "project/pipeline.py"], check=True)
        print("Pipeline executed successfully!")
    except subprocess.CalledProcessError as e:
        print("Error: Pipeline execution failed!")
        print(f"Command output: {e}")
        raise
    
    # check if path exists
    brazil_path = os.path.join(output_dir, "Brazil.csv")
    usa_path = os.path.join(output_dir, "United States of America.csv")

    assert os.path.exists(brazil_path), "Table of Brazil does not exist"
    assert os.path.exists(usa_path), "Table of USA does not exist"
    
    # check if the tables are not empty
    brazil_df = pd.read_csv(brazil_path)
    usa_df = pd.read_csv(usa_path)
    
    assert brazil_df.shape[0] > 0, "Table of Brazil is empty"
    assert usa_df.shape[0] > 0, "Table of USA is empty"
    
    # check if the tables have the correct shape
    assert brazil_df.shape == (BRAZIL_ROW_COUNT, COLS_NO), f"Expected shape {(BRAZIL_ROW_COUNT, COLS_NO)}, got {brazil_df.shape}"
    assert usa_df.shape == (USA_ROW_COUNT, COLS_NO), f"Expected shape {(USA_ROW_COUNT, COLS_NO)}, got {usa_df.shape}"
    
    # check column names 
    assert brazil_df.columns.tolist() == COLS_NAMES, "Table of Brazil has incorrect column names"
    assert usa_df.columns.tolist() == COLS_NAMES, "Table of USA has incorrect column names"
    
    # check nulls in the tables
    assert not brazil_df.isnull().values.any(), "Table of Brazil has null values"
    assert not usa_df.isnull().values.any(), "Table of USA has null values"
    
    # check if the tables have the correct data types
    assert brazil_df.dtypes.tolist() == COLS_DATATYPES, "Table of Brazil has incorrect data types"
    assert usa_df.dtypes.tolist() == COLS_DATATYPES, "Table of USA has incorrect data types"
    
    # check whole row duplicates
    assert not brazil_df.duplicated().any(), "Table of Brazil has duplicated rows"
    assert not usa_df.duplicated().any(), "Table of USA has duplicated rows"
    
    # check year column must be between 1990 and 2022 
    assert brazil_df['DIM_TIME'].between(1990, 2022).all(), "Table of Brazil has incorrect years"
    assert usa_df['DIM_TIME'].between(1990, 2022).all(), "Table of USA has incorrect years"
    
    # all columns must be +ve values
    assert (brazil_df.iloc[:, 1:] >= 0).all().all(), "Table of Brazil has negative values"
    assert (usa_df.iloc[:, 1:] >= 0).all().all(), "Table of USA has negative values"
    
    # remove files after testing
    os.remove(brazil_path)
    os.remove(usa_path)
    
    print("All tests passed successfully")
    

if __name__ == "__main__":
    output_dir = "data/"
    test_pipeline(output_dir)