import os
import pandas as pd

def get_WH_data_for_given_year(data_path: str, year: int) -> pd.DataFrame:
    ''' Extract World Happiness data for a given year
    
        Parameters
        ----------
        data_path
            path to the CSV data file
        year
            year for which to select the data

        Returns
        -------
        df_for_given_year
            A new dataframe with only data for the year selected
    '''
    WH_df = pd.read_csv(data_path)
    selected_rows = WH_df["Year"]==year
    selected_columns = WH_df.columns[2:9]
    WH_year_df = WH_df.loc[selected_rows, selected_columns]
    return WH_year_df

