import pandas as pd
class Date:
    def __init__(self):
        self.current_month:int = pd.Timestamp.today().month
        self.current_year:int = pd.Timestamp.today().year
        self.today:pd.Timestamp.date = pd.Timestamp.today().date()
        self.current_month_date:pd.Timestamp.date = self.today.replace(day=1)
        self.next_month:int = (self.current_month_date + pd.DateOffset(months=1)).date()
        self.last_month:int = (self.current_month_date - pd.DateOffset(months=1)).date()
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
        return pd.Timestamp(date).date()