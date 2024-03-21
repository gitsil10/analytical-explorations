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
        self.ticker: yf.Ticker = None
        self.security = {
            "info": None,
            "symbol": None,
            "history": None,
            "price": None,
            "dividends": None,
            "10k_income_statement": None,
            "10k_balance_sheet": None,
            "10k_cash_flow": None,
            "10q_income_statement": None,
            "10q_balance_sheet": None,
            "10q_cash_flow": None,
            "options": None
        }
        if symbol:
            self.set_ticker(symbol)
    
    def set_ticker(self, symbol:str = None) -> bool:
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
            self.ticker = yf.Ticker(symbol if symbol else None)
            self.security["info"] = self.ticker.info
            self.security["symbol"] = self.ticker.info["symbol"]
            self.security["history"] = self.ticker.history(period="max", interval="1d")
            self.security["price"] = self.ticker.info["currentPrice"]
            self.security["dividends"] = self.ticker.dividends
            self.security["10k_income_statement"] = self.ticker.income_stmt
            self.security["10k_balance_sheet"] = self.ticker.balance_sheet
            self.security["10k_cash_flow"] = self.ticker.cashflow
            self.security["10q_income_statement"] = self.ticker.quarterly_income_stmt
            self.security["10q_balance_sheet"] = self.ticker.quarterly_balance_sheet
            self.security["10q_cash_flow"] = self.ticker.quarterly_cashflow
            self.security["options"] = self.ticker.options
            return True
        
        except Exception as e:
            for k in self.security.keys():
                self.security[k] = None
            return False
        
    def get_info(self) -> dict:
        """
        @brief Get the information of the security
        @return (dict): The information of the security
        """
        return self.security["info"]
        
    def get_symbol(self) -> str:
        """
        @brief Get the symbol of the security
        @return (str): The symbol of the security
        """
        return self.security["symbol"]
        
    def get_history(self, start:str, end:str) -> pd.DataFrame:
        """
        @brief Get the history of the security
        @param start (str): The start date of the history
        @param end (str): The end date of the history
        @return (pd.DataFrame): The history of the security
        """
        if not self.ticker or pd.Timestamp(start) < pd.Timestamp(end):
            return pd.DataFrame()
        return self.ticker.history(start=start, end=end, interval="1d")
    
    def get_price(self) -> float:
        """
        @brief Get the price of the security
        @return (float): The price of the security
        """
        return self.security["price"]
    
    def get_dividends(self) -> pd.Series:
        """
        @brief Get the dividends of the security
        @return (pd.Series): The dividends of the security
        """
        return self.security["dividends"]
    
    def get_10k_income_statement(self) -> pd.DataFrame:
        """
        @brief Get the 10k income statement of the security
        @return (pd.DataFrame): The 10k income statement of the security
        """
        return self.security["10k_income_statement"]
    
    def get_10k_balance_sheet(self) -> pd.DataFrame:
        """
        @brief Get the 10k balance sheet of the security
        @return (pd.DataFrame): The 10k balance sheet of the security
        """
        return self.security["10k_balance_sheet"]
    
    def get_10k_cash_flow(self) -> pd.DataFrame:
        """
        @brief Get the 10k cash flow of the security
        @return (pd.DataFrame): The 10k cash flow of the security
        """
        return self.security["10k_cash_flow"]
    
    def get_10q_income_statement(self) -> pd.DataFrame:
        """
        @brief Get the 10q income statement of the security
        @return (pd.DataFrame): The 10q income statement of the security
        """
        return self.security["10q_income_statement"]
    
    def get_10q_balance_sheet(self) -> pd.DataFrame:
        """
        @brief Get the 10q balance sheet of the security
        @return (pd.DataFrame): The 10q balance sheet of the security
        """
        return self.security["10q_balance_sheet"]
    
    def get_10q_cash_flow(self) -> pd.DataFrame:
        """
        @brief Get the 10q cash flow of the security
        @return (pd.DataFrame): The 10q cash flow of the security
        """
        return self.security["10q_cash_flow"]
    
    def get_options(self) -> list:
        """
        @brief Get the options of the security
        @return (list): The options of the security
        """
        return self.security["options"]
    
    def get_option_chain(self, expiration:str) -> pd.DataFrame:
        """
        @brief Get the option chain of the security
        @param expiration (str): The expiration date of the option chain
        @return (pd.DataFrame): The option chain of the security
        """
        if not self.ticker or pd.Timestamp(expiration) > pd.Timestamp("today"):
            return pd.DataFrame()
        return self.ticker.option_chain(expiration)
    
    def get_option_chain_calls(self, expiration:str) -> pd.DataFrame:
        """
        @brief Get the option chain calls of the security
        @param expiration (str): The expiration date of the option chain
        @return (pd.DataFrame): The option chain calls of the security
        """
        if not self.ticker or pd.Timestamp(expiration) > pd.Timestamp("today"):
            return pd.DataFrame()
        return self.ticker.option_chain(expiration).calls
    
    def get_option_chain_puts(self, expiration:str) -> pd.DataFrame:
        """
        @brief Get the option chain puts of the security
        @param expiration (str): The expiration date of the option chain
        @return (pd.DataFrame): The option chain puts of the security
        """
        if not self.ticker or pd.Timestamp(expiration) > pd.Timestamp("today"):
            return pd.DataFrame()
        return self.ticker.option_chain(expiration).puts
    
    def get_option_chain_calls_strikes(self, expiration:str) -> pd.DataFrame:
        """
        @brief Get the option chain calls strikes of the security
        @param expiration (str): The expiration date of the option chain
        @return (pd.DataFrame): The option chain calls strikes of the security
        """
        if not self.ticker or pd.Timestamp(expiration) > pd.Timestamp("today"):
            return pd.DataFrame()
        return self.ticker.option_chain(expiration).calls.strike

    


    