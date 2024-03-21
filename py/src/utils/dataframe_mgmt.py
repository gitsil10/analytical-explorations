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
"""
#imports
import pandas as pd

#class
class DataframeMgmt:
    """
    @brief A class to process dataframes
    @param data (pd.DataFrame): The data from an entity
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
    