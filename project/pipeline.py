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
dropped_cols = ["IND_ID", "IND_CODE", "IND_UUID", "IND_PER_CODE", "DIM_TIME_TYPE", "DIM_GEO_CODE_M49", "DIM_GEO_CODE_TYPE", "DIM_PUBLISH_STATE_CODE"]
output_dir = "data/"


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


def process_world_bank_data(df: pd.DataFrame, country: str) -> pd.DataFrame:
    """
    Processes the World Bank data for a specific country.

    Args:
        df (pd.DataFrame): The DataFrame containing the World Bank data.
        country (str): The country to filter the data for.

    Returns:
        pd.DataFrame: The processed data with life expectancy for the specified country.
    """
    wb_life_expectancy = df[df['Country Name'] == country].iloc[:, 4:].T # skip first 4 columns
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
    return df[df["GEO_NAME_SHORT"] == country]

def clean_columns(df: pd.DataFrame, dropped_cols: list) -> pd.DataFrame:
    """
    Cleans the DataFrame by dropping specified columns.

    Args:
        df (pd.DataFrame): The DataFrame to clean.
        dropped_cols (list): The list of columns to drop.

    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    df.drop(columns=dropped_cols, inplace=True)
    return df

def merge_dataframes(dfs: list) -> pd.DataFrame:
    """
    Merges multiple DataFrames on the 'DIM_TIME' column.

    Args:
        dfs (list): The list of DataFrames to merge.

    Returns:
        pd.DataFrame: The merged DataFrame.
    """
    merged_df = dfs[0]
    for df in dfs[1:]:
        merged_df = merged_df.merge(df, on=['DIM_TIME'], how='outer')
    return merged_df

def remove_unwanted_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Removes unwanted columns from the DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to clean.

    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    columns_to_remove = [col for col in df.columns if col.startswith('IND_NAME') or col.startswith('GEO_NAME_SHORT')]
    return df.drop(columns=columns_to_remove)

def save_to_sqlite(df: pd.DataFrame, country: str) -> None:
    """
    Saves the DataFrame to an SQLite database.

    Args:
        df (pd.DataFrame): The DataFrame to save.
        country (str): The country name to use for the database file and table.

    Returns:
        None
    """
    conn = sqlite3.connect(f"{output_dir}{country}.db")
    df.to_sql(f"{country}", conn, if_exists="replace", index=False)
    conn.close()

def main_pipeline(country: str, wb_country: str) -> None:
    """
    Main pipeline function to process and merge data for a specific country.

    Args:
        country (str): The country name to filter the data for.
        wb_country (str): The country name to filter the World Bank data for.

    Returns:
        None
    """
    life_expectancy_wb_df = download_world_bank_data(world_bank_url, specific_file, output_dir)
    wb_life_expectancy = process_world_bank_data(life_expectancy_wb_df, wb_country)

    dtp3_df = read_and_filter_csv(data_files["dtp3_immunization.csv"], country)
    hypertension_df = read_and_filter_csv(data_files["hypertension_prevalence.csv"], country)
    uhc_index_df = read_and_filter_csv(data_files["uhc_index_score.csv"], country)
    mvc2_df = read_and_filter_csv(data_files["mvc2_immunization.csv"], country)

    hypertension_df = clean_columns(hypertension_df, dropped_cols)
    dtp3_df = clean_columns(dtp3_df, dropped_cols)
    uhc_index_df = clean_columns(uhc_index_df, dropped_cols)
    mvc2_df = clean_columns(mvc2_df, dropped_cols)

    merged_df = merge_dataframes([hypertension_df, uhc_index_df, dtp3_df, mvc2_df, wb_life_expectancy])

    merged_df_cleaned = remove_unwanted_columns(merged_df)

    merged_df_cleaned = merged_df_cleaned.dropna().sort_values(by='DIM_TIME').reset_index(drop=True)
    merged_df_cleaned.to_csv(f"{output_dir}{country}.csv", index=False)
    print(f"Data for {country} merged and saved as CSV successfully.")
    
    # Save as SQLite
    save_to_sqlite(merged_df_cleaned, country)
    print(f"Data for {country} merged and saved as SQLite successfully.")

if __name__ == "__main__":
    main_pipeline("Brazil", "Brazil")
    main_pipeline("United States of America", "United States")
