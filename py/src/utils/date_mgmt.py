<<<<<<< HEAD
import pandas as pd
class Date:
=======
"""
@gitsil10
@file date_mgmt.py
@brief A class to manage dates
@details A class to manage dates
@version 0.1
@date 2024-03-20

@dependencies
pandas -> pd
"""
#imports
import pandas as pd

#class
class DateMgmt:
    """
    @brief A class to manage dates
    @param current_month (int): The current month
    @param current_year (int): The current year
    @param today (pd.Timestamp.date): The current date
    @param current_month_date (pd.Timestamp.date): The current month date
    @param next_month (int): The next month
    @param last_month (int): The last month
    @return (Date): The Date object
    """
>>>>>>> feat/python/analytics
    def __init__(self):
        self.current_month:int = pd.Timestamp.today().month
        self.current_year:int = pd.Timestamp.today().year
        self.today:pd.Timestamp.date = pd.Timestamp.today().date()
        self.current_month_date:pd.Timestamp.date = self.today.replace(day=1)
        self.next_month:int = (self.current_month_date + pd.DateOffset(months=1)).date()
        self.last_month:int = (self.current_month_date - pd.DateOffset(months=1)).date()
<<<<<<< HEAD
    def get_current_month(self) -> int:
        return self.current_month
    def get_next_month(self) -> int:
        return self.next_month
    def get_last_month(self) -> int:
        return self.last_month
    def get_current_year(self) -> int:
        return self.current_year
    def get_last_year(self) -> int:
        return self.current_year - 1
    def get_current_month_date(self) -> pd.Timestamp.date:
        return self.current_month_date
    def get_today(self) -> pd.Timestamp.date:
        return self.today
    def get_last_year_date(self) -> pd.Timestamp.date:
        return self.current_month_date - pd.DateOffset(years=1)
    def get_previous_date(self, months:int) -> pd.Timestamp:
        return self.current_month_date - pd.DateOffset(months=months)
    def get_date(self, date:str) -> pd.Timestamp.date:
=======

    def get_current_month(self) -> int:
        """
        @brief Get the current month
        @return (int): The current month

        @details
        Return the current month

        @note
        Time: O(1)
        Space: O(1)
        """
        return self.current_month
    
    def get_next_month(self) -> int:
        """
        @brief Get the next month
        @return (int): The next month

        @details
        Return the next month

        @note
        Time: O(1)
        Space: O(1)
        """
        return self.next_month
    
    def get_last_month(self) -> int:
        """
        @brief Get the last month
        @return (int): The last month

        @details
        Return the last month

        @note
        Time: O(1)
        Space: O(1)
        """
        return self.last_month
    
    def get_current_year(self) -> int:
        """
        @brief Get the current year
        @return (int): The current year

        @details
        Return the current year

        @note
        Time: O(1)
        Space: O(1)
        """
        return self.current_year
    
    def get_last_year(self) -> int:
        """
        @brief Get the last year
        @return (int): The last year

        @details
        Return the last year

        @note
        Time: O(1)
        Space: O(1)
        """
        return self.current_year - 1
    
    def get_current_month_date(self) -> pd.Timestamp.date:
        """
        @brief Get the current month date
        @return (pd.Timestamp.date): The current month date

        @details
        Return the current month date

        @note
        Time: O(1)
        Space: O(1)
        """
        return self.current_month_date
    
    def get_today(self) -> pd.Timestamp.date:
        """
        @brief Get the current date
        @return (pd.Timestamp.date): The current date

        @details
        Return the current date

        @note
        Time: O(1)
        Space: O(1)
        """
        return self.today
    
    def get_last_year_date(self) -> pd.Timestamp.date:
        """
        @brief Get the last year date
        @return (pd.Timestamp.date): The last year date

        @details
        Return the last year date

        @note
        Time: O(1)
        Space: O(1)
        """
        return self.current_month_date - pd.DateOffset(years=1)
    
    def get_previous_date(self, months:int) -> pd.Timestamp.date:
        """
        @brief Get the previous date
        @param months (int): The number of months to go back
        @return (pd.Timestamp): The previous date

        @details
        Return the previous date

        @note
        Time: O(1)
        Space: O(1)
        """
        return self.current_month_date - pd.DateOffset(months=months)
    
    def get_date(self, date:str) -> pd.Timestamp.date:
        """
        @brief Get the date
        @param date (str): The date
        @return (pd.Timestamp.date): The date

        @details
        Return the date

        @note
        Time: O(1)
        Space: O(1)
        """
>>>>>>> feat/python/analytics
        return pd.Timestamp(date).date()