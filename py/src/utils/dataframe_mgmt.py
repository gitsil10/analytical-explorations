"""
@gitsil10
@file dataframe_mgmt.py
@brief processes dataframes

@details 
A file to processes dataframes
Groups a dataframe

@version 0.1
@date 2024-03-20

@dependencies
pandas -> pd

@todo
1. input data as a dataframe
2. describe data
    1. summary statistics
    2. column information
3. clean data
    1. drop na
    2. fill na
    3. drop duplicates
    4. fill duplicates
    5. drop outliers
    6. fill outliers
4. return group data by dates
    1. group by year as mean, std, count
    2. group by month as mean, std, count
    3. group by quarter as mean, std, count
    4. group by year, month as sum, mean, std, count
    5. group by year, quarter as sum, mean, std, count
5. return grow rate by dates
    1. grow rate by dates
    2. grow rate by year
    3. grow rate by month
    4. grow rate by quarter
    5. grow rate by year, month
6. missing values
    1. missing values by column
    2. missing values by row
    3. missing values by column and row
7. duplicate values
    1. duplicate values by column
    2. duplicate values by row
    3. duplicate values by column and row
8. outliers
    1. outliers by column
    2. outliers by row
    3. outliers by column and row
9. correlation
    1. correlation by column
    2. correlation by row
    3. correlation by column and row
10. pivot table
    1. pivot table by column
    2. pivot table by row
    3. pivot table by column and row
"""
#imports
import pandas as pd

#class
class DataframeMgmt:
    """
    @brief A class to process dataframes
    @param data (pd.DataFrame): The data from an entity
    
    @details
    describe_data -> describe the data
    info_data -> get the information of the data
    clean_drop_na -> clean the data by dropping na
    clean_fill_na -> float | clean the data by filling na
    clean_drop_duplicates -> clean the data by dropping duplicates
    clean_fill_duplicates -> float | clean the data by filling duplicates
    clean_drop_outliers -> clean the data by dropping outliers
    group_by_year -> group the data by year
    group_by_month -> group the data by month
    group_by_quarter -> group the data by quarter
    group_by_year_month -> group the data by year, month
    group_by_year_quarter -> group the data by year, quarter
    grow_rate_by_dates -> get the grow rate by dates
    grow_rate_group_by_year -> get the grow rate by year
    grow_rate_group_by_month -> get the grow rate by month
    grow_rate_group_by_quarter -> get the grow rate by quarter
    grow_rate_group_by_year_month -> get the grow rate by year, month
    grow_rate_group_by_year_quarter -> get the grow rate by year, quarter
    missing_values_by_column -> get the missing values by column
    missing_values_by_row -> get the missing values by row
    missing_values_by_column_row -> get the missing values by column and row
    duplicate_values_by_column -> get the duplicate values by column
    duplicate_values_by_row -> get the duplicate values by row
    duplicate_values_by_column_row -> get the duplicate values by column and row
    outliers_by_column -> get the outliers by column
    outliers_by_row -> get the outliers by row
    outliers_by_column_row -> get the outliers by column and row
    correlation_by_column -> get the correlation by column
    correlation_by_row -> get the correlation by row
    correlation_by_column_row -> get the correlation by column and row
    pivot_table_by_column -> get the pivot table by column
    pivot_table_by_row -> get the pivot table by row
    pivot_table_by_column_row -> get the pivot table by column and row
    """
    def __init__(self, data:pd.DataFrame = None):
        self._data:pd.DataFrame = None
        if not data is None:
            self.data = data

    @property
    def data(self) -> pd.DataFrame:
        """
        @brief Get the data of an entity
        @return (pd.DataFrame): The data of an entity
        """
        return self._data
    
    @data.setter
    def data(self, data:pd.DataFrame) -> None:
        """
        @brief Set the data of an entity
        @param data (pd.DataFrame): The data of an entity
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("The data must be a pandas dataframe")
        
        self._data = data

    def describe_data(self) -> pd.DataFrame:
        """
        @brief Describe the data
        @return (pd.DataFrame): The data described
        """
        return self._data.describe()
    
    def info_data(self) -> pd.DataFrame:
        """
        @brief Get the information of the data
        @return (pd.DataFrame): The information of the data
        """
        return self._data.info()

    def clean_drop_na(self) -> pd.DataFrame:
        """
        @brief Clean the data by dropping na
        @return (pd.DataFrame): The data cleaned by dropping na
        """
        return self._data.dropna()
    
    def clean_fill_na(self, value:float = 0) -> pd.DataFrame:
        """
        @brief Clean the data by filling na
        @param value (float): The value to fill na
        @return (pd.DataFrame): The data cleaned by filling na
        """
        return self._data.fillna(value)
    
    def clean_drop_duplicates(self) -> pd.DataFrame:
        """
        @brief Clean the data by dropping duplicates
        @return (pd.DataFrame): The data cleaned by dropping duplicates
        """
        return self._data.drop_duplicates()
    
    def clean_fill_duplicates(self, value:float = 0) -> pd.DataFrame:
        """
        @brief Clean the data by filling duplicates
        @param value (float): The value to fill duplicates
        @return (pd.DataFrame): The data cleaned by filling duplicates
        """
        return self._data.fillna(value)
    
    def clean_drop_outliers(self) -> pd.DataFrame:
        """
        @brief Clean the data by dropping outliers
        @return (pd.DataFrame): The data cleaned by dropping outliers
        """
        q1 = self._data.quantile(0.25)
        q3 = self._data.quantile(0.75)
        iqr = q3 - q1
        return self._data[~((self._data < (q1 - 1.5 * iqr)) | (self._data > (q3 + 1.5 * iqr))).any(axis=1)]

    def group_by_year(self) -> pd.DataFrame:
        """
        @brief Group the data by year
        @return (pd.DataFrame): The data grouped by year
        """
        return self._data.groupby(self._data.index.year).agg(['sum', 'mean', 'std', 'count'])
    
    def group_by_month(self) -> pd.DataFrame:
        """
        @brief Group the data by month
        @return (pd.DataFrame): The data grouped by month
        """
        return self._data.groupby(self._data.index.month).agg(['sum', 'mean', 'std', 'count'])
    
    def group_by_quarter(self) -> pd.DataFrame:
        """
        @brief Group the data by quarter
        @return (pd.DataFrame): The data grouped by quarter
        """
        return self._data.groupby(self._data.index.quarter).agg(['sum', 'mean', 'std', 'count'])
    
    def group_by_year_month(self) -> pd.DataFrame:
        """
        @brief Group the data by year, month
        @return (pd.DataFrame): The data grouped by year, month
        """
        return self._data.groupby(
            [self._data.index.year, self._data.index.month]
        ).agg(['sum', 'mean', 'std', 'count'])
    
    def group_by_year_quarter(self) -> pd.DataFrame:
        """
        @brief Group the data by year, quarter
        @return (pd.DataFrame): The data grouped by year, quarter
        """
        return self._data.groupby(
            [self._data.index.year, self._data.index.quarter]
        ).agg(['sum', 'mean', 'std', 'count'])
    
    def grow_rate_by_dates(self) -> pd.DataFrame:
        """
        @brief Get the grow rate by dates
        @return (pd.DataFrame): The grow rate by dates
        """
        return self._data.pct_change()
    
    def grow_rate_group_by_year(self) -> pd.DataFrame:
        """
        @brief Get the grow rate by year
        @return (pd.DataFrame): The grow rate by year
        """
        return self.group_by_year().pct_change()
    
    def grow_rate_group_by_month(self) -> pd.DataFrame:
        """
        @brief Get the grow rate by month
        @return (pd.DataFrame): The grow rate by month
        """
        return self.group_by_month().pct_change()
    
    def grow_rate_group_by_quarter(self) -> pd.DataFrame:
        """
        @brief Get the grow rate by quarter
        @return (pd.DataFrame): The grow rate by quarter
        """
        return self.group_by_quarter().pct_change()
    
    def grow_rate_group_by_year_month(self) -> pd.DataFrame:
        """
        @brief Get the grow rate by year, month
        @return (pd.DataFrame): The grow rate by year, month
        """
        return self.group_by_year_month().pct_change()
    
    def grow_rate_group_by_year_quarter(self) -> pd.DataFrame:
        """
        @brief Get the grow rate by year, quarter
        @return (pd.DataFrame): The grow rate by year, quarter
        """
        return self.group_by_year_quarter().pct_change()
    
    def missing_values_by_column(self) -> pd.DataFrame:
        """
        @brief Get the missing values by column
        @return (pd.DataFrame): The missing values by column
        """
        return self._data.isna().sum()
    
    def missing_values_by_row(self) -> pd.DataFrame:
        """
        @brief Get the missing values by row
        @return (pd.DataFrame): The missing values by row
        """
        return self._data.isna().sum(axis=1)
    
    def missing_values_by_column_row(self) -> pd.DataFrame:
        """
        @brief Get the missing values by column and row
        @return (pd.DataFrame): The missing values by column and row
        """
        return self._data.isna().sum().sum()
    
    def duplicate_values_by_column(self) -> pd.DataFrame:
        """
        @brief Get the duplicate values by column
        @return (pd.DataFrame): The duplicate values by column
        """
        return self._data.duplicated().sum()
    
    def duplicate_values_by_row(self) -> pd.DataFrame:
        """
        @brief Get the duplicate values by row
        @return (pd.DataFrame): The duplicate values by row
        """
        return self._data.duplicated().sum(axis=1)
    
    def duplicate_values_by_column_row(self) -> pd.DataFrame:
        """
        @brief Get the duplicate values by column and row
        @return (pd.DataFrame): The duplicate values by column and row
        """
        return self._data.duplicated().sum().sum()
    
    def outliers_by_column(self) -> pd.DataFrame:
        """
        @brief Get the outliers by column
        @return (pd.DataFrame): The outliers by column
        """
        return self._data.quantile([0.25, 0.75])
    
    def outliers_by_row(self) -> pd.DataFrame:
        """
        @brief Get the outliers by row
        @return (pd.DataFrame): The outliers by row
        """
        return self._data.quantile([0.25, 0.75], axis=1)
    
    def outliers_by_column_row(self) -> pd.DataFrame:
        """
        @brief Get the outliers by column and row
        @return (pd.DataFrame): The outliers by column and row
        """
        return self._data.quantile([0.25, 0.75]).quantile([0.25, 0.75], axis=1)
    
    def correlation_by_column(self) -> pd.DataFrame:
        """
        @brief Get the correlation by column
        @return (pd.DataFrame): The correlation by column
        """
        return self._data.corr()
    
    def correlation_by_row(self) -> pd.DataFrame:
        """
        @brief Get the correlation by row
        @return (pd.DataFrame): The correlation by row
        """
        return self._data.corrwith(self._data)
    
    def correlation_by_column_row(self) -> pd.DataFrame:
        """
        @brief Get the correlation by column and row
        @return (pd.DataFrame): The correlation by column and row
        """
        return self._data.corr().corrwith(self._data.corrwith(self._data))
    
    def pivot_table_by_column(self, index:str, columns:str, values:str, aggfunc:str) -> pd.DataFrame:
        """
        @brief Get the pivot table by column
        @param index (str): The index of the pivot table
        @param columns (str): The columns of the pivot table
        @param values (str): The values of the pivot table
        @param aggfunc (str): The function to aggregate the pivot table
        @return (pd.DataFrame): The pivot table by column
        """
        return pd.pivot_table(self._data, index=index, columns=columns, values=values, aggfunc=aggfunc)
    
    def pivot_table_by_row(self, index:str, columns:str, values:str, aggfunc:str) -> pd.DataFrame:
        """
        @brief Get the pivot table by row
        @param index (str): The index of the pivot table
        @param columns (str): The columns of the pivot table
        @param values (str): The values of the pivot table
        @param aggfunc (str): The function to aggregate the pivot table
        @return (pd.DataFrame): The pivot table by row
        """
        return pd.pivot_table(self._data, index=index, columns=columns, values=values, aggfunc=aggfunc, axis=1)
    
    def pivot_table_by_column_row(self, index:str, columns:str, values:str, aggfunc:str) -> pd.DataFrame:
        """
        @brief Get the pivot table by column and row
        @param index (str): The index of the pivot table
        @param columns (str): The columns of the pivot table
        @param values (str): The values of the pivot table
        @param aggfunc (str): The function to aggregate the pivot table
        @return (pd.DataFrame): The pivot table by column and row
        """
        return pd.pivot_table(
            self._data, index=index, columns=columns, values=values, aggfunc=aggfunc
        ).pivot_table(index=index, columns=columns, values=values, aggfunc=aggfunc, axis=1)