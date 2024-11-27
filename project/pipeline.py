# Imports
import os
import io
import requests
import zipfile
import pandas as pd
import sqlite3


# Initializations
data_files = {
    "mvc2_immunization.csv": "https://srhdpeuwpubsa.blob.core.windows.net/whdh/DATADOT/INDICATOR/BB4567B_ALL_LATEST.csv",
    "hypertension_prevalence.csv": "https://srhdpeuwpubsa.blob.core.windows.net/whdh/DATADOT/INDICATOR/608DE39_ALL_LATEST.csv",
    "uhc_index_score.csv": "https://srhdpeuwpubsa.blob.core.windows.net/whdh/DATADOT/INDICATOR/9A706FD_ALL_LATEST.csv",
    "dtp3_immunization.csv": "https://srhdpeuwpubsa.blob.core.windows.net/whdh/DATADOT/INDICATOR/F8E084C_ALL_LATEST.csv",
}

world_bank_url = "https://api.worldbank.org/v2/en/indicator/SP.DYN.LE00.IN?downloadformat=csv"
specific_file = 'API_SP.DYN.LE00.IN_DS2_en_csv_v2_99.csv'
UNNECESSARY_COLS = ["IND_ID", "IND_CODE", "IND_UUID", "IND_PER_CODE", "DIM_TIME_TYPE", "DIM_GEO_CODE_M49", "DIM_GEO_CODE_TYPE", "DIM_PUBLISH_STATE_CODE"]
SHEETS_ABBREVIATIONS  = ['LIFE_EXPECTANCY','HYPERTENSION', 'UHC', 'DTP3', 'MVC2']
output_dir = "data/"

#############################################
### Fetching Datasets

def download_world_bank_data(url: str, specific_file: str, output_dir: str) -> pd.DataFrame:
    """
    Downloads and extracts a specific file from a World Bank data zip file.

    Args:
        url (str): The URL to download the zip file from.
        specific_file (str): The specific file to extract from the zip file.
        output_dir (str): The directory to save the extracted file.

    Returns:
        pd.DataFrame: The extracted data as a pandas DataFrame.
    """
    response = requests.get(url)
    with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
        zip_ref.extract(specific_file, output_dir)
        original_path = os.path.join(output_dir, specific_file)
        renamed_path = os.path.join(output_dir, "life_expectancy_wb.csv")
        os.rename(original_path, renamed_path)
        df = pd.read_csv(renamed_path, delimiter=',', engine='python', skiprows=3)
        os.remove(renamed_path)
        return df


# Preprocessing
def preprocess_world_bank_data(df: pd.DataFrame, country: str) -> pd.DataFrame:
    """
    Preprocesses the World Bank data for a specific country.
    
    Args:
        df (pd.DataFrame): The DataFrame to preprocess.
        country (str): The country to filter the data for.
    
    Returns:
        pd.DataFrame: The preprocessed DataFrame.
    """
    wb_life_expectancy = df[df['Country Name'] == country].iloc[:, 4:].T  # Skip first 4 columns
    wb_life_expectancy.dropna(inplace=True)
    wb_life_expectancy.reset_index(inplace=True)
    wb_life_expectancy.columns = ["DIM_TIME", 'Life Expectancy']
    wb_life_expectancy = wb_life_expectancy.astype({'DIM_TIME': 'int64', 'Life Expectancy': 'float64'}, copy=False)
    return wb_life_expectancy

def read_and_filter_csv(url: str, country: str) -> pd.DataFrame:
    """
    Reads a CSV file from a URL and filters it for a specific country.

    Args:
        url (str): The URL of the CSV file.
        country (str): The country to filter the data for.

    Returns:
        pd.DataFrame: The filtered DataFrame.
    """
    df = pd.read_csv(url)
    country_df = df[df["GEO_NAME_SHORT"] == country]
    country_df = country_df.drop(columns=UNNECESSARY_COLS)
    return country_df

def preprocess_and_rename(df: pd.DataFrame, prefix: str) -> pd.DataFrame:
    df = df.drop(columns=['IND_NAME', 'GEO_NAME_SHORT'], errors='ignore')
    df = df.rename(columns={col: f"{prefix}_{col}" for col in df.columns if col != 'DIM_TIME'})
    return df


# Analysis
def check_duplicates_and_nulls(df: pd.DataFrame, name: str):
    """
    Checks for duplicates and null values in a DataFrame.
    """
    print(f"{name} - Null Values: {df.isnull().sum().sum()}, Duplicates: {df.duplicated().sum()}")

def show_descriptive_stats(df: pd.DataFrame, name: str):
    """
    Shows descriptive statistics for a DataFrame.
    """
    print(f"Descriptive Statistics for {name}:\n{df.describe(include='all')}")


# Cleaning
def clean_merged_data(merged_df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans a merged DataFrame by dropping rows with all missing values and sorting it by the columns.
    
    Args:
        merged_df (pd.DataFrame): The merged DataFrame to clean.
    
    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    merged_df_cleaned = merged_df.dropna(how='all', 
                                         subset=['DTP3_RATE_PER_100_N', 
                                                 'MVC2_RATE_PER_100_N', 
                                                 'HYPERTENSION_RATE_PER_100_N', 
                                                 'UHC_INDEX_N'])
    merged_df_cleaned = merged_df_cleaned.sort_values(by=list(merged_df.columns))
    return merged_df_cleaned

# Imputation
def impute_missing_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Imputes missing data in a DataFrame.
    """
    df['DTP3_RATE_PER_100_N'] = df['DTP3_RATE_PER_100_N'].interpolate(method='linear')
    df['MVC2_RATE_PER_100_N'] = df['MVC2_RATE_PER_100_N'].interpolate(method='linear')
    df['UHC_INDEX_N'] = df['UHC_INDEX_N'].interpolate(method='linear')
    df['HYPERTENSION_RATE_PER_100_N'] = df[['HYPERTENSION_RATE_PER_100_NL', 'HYPERTENSION_RATE_PER_100_NU']].mean(axis=1)
    df.fillna(method='ffill', inplace=True)
    df.fillna(method='bfill', inplace=True)
    return df


def preprocess_and_rename(df, prefix):
    """
    Preprocesses and renames a DataFrame for merging.
    
    Args:
        df (pd.DataFrame): The DataFrame to preprocess.
        prefix (str): The prefix to add to the column names.
    
    Returns:
        pd.DataFrame: The preprocessed DataFrame.
    """
    df = df.drop(columns=['IND_NAME', 'GEO_NAME_SHORT'], errors='ignore')
    df = df.rename(columns={col: f"{prefix}_{col}" for col in df.columns if col != 'DIM_TIME'})
    return df

# Transformation
def merge_dataframes(dfs) -> pd.DataFrame:
    """
    Merges multiple DataFrames on the 'DIM_TIME' column.

    Args:
        dfs (list): The list of DataFrames to merge.

    Returns:
        pd.DataFrame: The merged DataFrame.
    """
    wb_life_expectancy, *_ = dfs
    merged_df = wb_life_expectancy
    for processed_df in dfs[1:]:
        merged_df = merged_df.merge(processed_df, on=['DIM_TIME'], how='outer')

    return merged_df


def main_pipeline(country: str, wb_country: str) -> None:
    life_expectancy_wb_df = download_world_bank_data(world_bank_url, specific_file, output_dir)
    wb_life_expectancy = preprocess_world_bank_data(life_expectancy_wb_df, wb_country)

    dtp3_df = read_and_filter_csv(data_files["dtp3_immunization.csv"], country)
    hypertension_df = read_and_filter_csv(data_files["hypertension_prevalence.csv"], country)
    uhc_index_df = read_and_filter_csv(data_files["uhc_index_score.csv"], country)
    mvc2_df = read_and_filter_csv(data_files["mvc2_immunization.csv"], country)
    
    dfs = [wb_life_expectancy, hypertension_df, uhc_index_df, dtp3_df, mvc2_df]
    for i, (df, name) in enumerate(zip(dfs, SHEETS_ABBREVIATIONS)):
        if name == 'LIFE_EXPECTANCY':
            processed_df = df
        else:
            processed_df = preprocess_and_rename(df, name)
        if name == 'HYPERTENSION':
            processed_df = processed_df[~processed_df['HYPERTENSION_DIM_SEX'].isin(['MALE', 'FEMALE'])]
            processed_df = processed_df.drop(columns=['HYPERTENSION_DIM_SEX'])
        dfs[i] = processed_df
        check_duplicates_and_nulls(processed_df, name)
        show_descriptive_stats(processed_df, name)

    merged_df = merge_dataframes(dfs)
    merged_df_cleaned = clean_merged_data(merged_df)
    merged_df_imputed = impute_missing_data(merged_df_cleaned)

    # Save to CSV
    merged_df_imputed.to_csv(f"{output_dir}{country}.csv", index=False)
    print(f"Data for {country} merged and saved as CSV successfully.")


if __name__ == "__main__":
    main_pipeline("Brazil", "Brazil")
    main_pipeline("United States of America", "United States")