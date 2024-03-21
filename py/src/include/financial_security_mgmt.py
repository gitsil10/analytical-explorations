"""
@gitsil10
@file financial_security_mgmt.py
@brief security management
@details A file to manage financial security
@version 0.1
@date 2024-03-20

@dependencies
yfinance -> yt
"""
# imports
import yfinance as yf
import pandas as pd

# class
class FinancialSecurityMgmt:
    """
    @brief A class to manage financial security
    @param symbol (str): The symbol of the security
    """
    def __init__(self, symbol:str = None):
        self._ticker: yf.Ticker = None
        self._security = {
            "info": None,
            "symbol": None,
            "history": None,
            "price": None,
            "dividends": None,
            "income_statement_10k": None,
            "balance_sheet_10k": None,
            "cash_flow_10k": None,
            "income_statement_10q": None,
            "balance_sheet_10q": None,
            "cash_flow_10q": None,
            "options": None
        }
        if symbol:
            self.ticker = symbol

    @property
    def ticker(self) -> yf.Ticker:
        return self._ticker
    
    @property
    def security(self) -> dict:
        return self._security
    
    @property
    def info(self) -> dict:
        """
        @brief Get the information of the security
        @return (dict): The information of the security
        """
        return self._security["info"]
        
    @property
    def symbol(self) -> str:
        """
        @brief Get the symbol of the security
        @return (str): The symbol of the security
        """
        return self._security["symbol"]
    
    @property
    def price(self) -> float:
        """
        @brief Get the price of the security
        @return (float): The price of the security
        """
        return self._security["price"]
    
    @property
    def dividends(self) -> pd.Series:
        """
        @brief Get the dividends of the security
        @return (pd.Series): The dividends of the security
        """
        return self._security["dividends"]
    
    @property
    def income_statement_10k(self) -> pd.DataFrame:
        """
        @brief Get the 10k income statement of the security
        @return (pd.DataFrame): The 10k income statement of the security
        """
        return self._security["income_statement_10k"]
    
    @property
    def balance_sheet_10k(self) -> pd.DataFrame:
        """
        @brief Get the 10k balance sheet of the security
        @return (pd.DataFrame): The 10k balance sheet of the security
        """
        return self._security["balance_sheet_10k"]
    
    @property
    def cash_flow_10k(self) -> pd.DataFrame:
        """
        @brief Get the 10k cash flow of the security
        @return (pd.DataFrame): The 10k cash flow of the security
        """
        return self._security["cash_flow_10k"]
    
    @property
    def income_statement_10q(self) -> pd.DataFrame:
        """
        @brief Get the 10q income statement of the security
        @return (pd.DataFrame): The 10q income statement of the security
        """
        return self._security["income_statement_10q"]
    
    @property
    def balance_sheet_10q(self) -> pd.DataFrame:
        """
        @brief Get the 10q balance sheet of the security
        @return (pd.DataFrame): The 10q balance sheet of the security
        """
        return self._security["balance_sheet_10q"]
    
    @property
    def cash_flow_10q(self) -> pd.DataFrame:
        """
        @brief Get the 10q cash flow of the security
        @return (pd.DataFrame): The 10q cash flow of the security
        """
        return self._security["cash_flow_10q"]
    
    def get_options(self) -> list:
        """
        @brief Get the options of the security
        @return (list): The options of the security
        """
        return self._security["options"]
    
    @ticker.setter
    def ticker(self, symbol:str = None) -> bool:
        """
        @brief Set the ticker of the security
        @param symbol (str): The symbol of the security
        @return (bool): True if the ticker was set, False otherwise

        @details
        The ticker is the object that contains all the information of the security
        From the ticker, we can get the information, history, price, dividends, 10k and 10q financial statements, and options

        If the ticker is not set, then all the information of the security will be set to None
        """
        try:
            self._ticker = yf.Ticker(symbol if symbol else None)
            self._security["info"] = self._ticker.info
            self._security["symbol"] = self._ticker.info["symbol"]
            self._security["history"] = self._ticker.history(period="max", interval="1d")
            self._security["price"] = self._ticker.info["currentPrice"]
            self._security["dividends"] = self._ticker.dividends
            self._security["income_statement_10k"] = self._ticker.income_stmt
            self._security["balance_sheet_10k"] = self._ticker.balance_sheet
            self._security["cash_flow_10k"] = self._ticker.cashflow
            self._security["income_statement_10q"] = self._ticker.quarterly_income_stmt
            self._security["balance_sheet_10q"] = self._ticker.quarterly_balance_sheet
            self._security["cash_flow_10q"] = self._ticker.quarterly_cashflow
            self._security["options"] = self._ticker.options
            return True
        
        except Exception as e:
            for k in self._security.keys():
                self._security[k] = None
            return False
             
    def get_history(self, start:str, end:str) -> pd.DataFrame:
        """
        @brief Get the history of the security
        @param start (str): The start date of the history
        @param end (str): The end date of the history
        @return (pd.DataFrame): The history of the security
        """
        if not self._ticker or pd.Timestamp(start) < pd.Timestamp(end):
            return pd.DataFrame()
        return self._ticker.history(start=start, end=end, interval="1d")
    
    def get_option_chain(self, expiration:str) -> pd.DataFrame:
        """
        @brief Get the option chain of the security
        @param expiration (str): The expiration date of the option chain
        @return (pd.DataFrame): The option chain of the security
        """
        if not self._ticker or pd.Timestamp(expiration) > pd.Timestamp("today"):
            return pd.DataFrame()
        return self._ticker.option_chain(expiration)
    
    def get_option_chain_calls(self, expiration:str) -> pd.DataFrame:
        """
        @brief Get the option chain calls of the security
        @param expiration (str): The expiration date of the option chain
        @return (pd.DataFrame): The option chain calls of the security
        """
        if not self._ticker or pd.Timestamp(expiration) > pd.Timestamp("today"):
            return pd.DataFrame()
        return self._ticker.option_chain(expiration).calls
    
    def get_option_chain_puts(self, expiration:str) -> pd.DataFrame:
        """
        @brief Get the option chain puts of the security
        @param expiration (str): The expiration date of the option chain
        @return (pd.DataFrame): The option chain puts of the security
        """
        if not self._ticker or pd.Timestamp(expiration) > pd.Timestamp("today"):
            return pd.DataFrame()
        return self._ticker.option_chain(expiration).puts
    
    def get_option_chain_calls_strikes(self, expiration:str) -> pd.DataFrame:
        """
        @brief Get the option chain calls strikes of the security
        @param expiration (str): The expiration date of the option chain
        @return (pd.DataFrame): The option chain calls strikes of the security
        """
        if not self._ticker or pd.Timestamp(expiration) > pd.Timestamp("today"):
            return pd.DataFrame()
        return self._ticker.option_chain(expiration).calls.strike

    


    