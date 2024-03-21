"""
@gitsil10
@file finance_model.py
@brief financial security entity
@details A file to manage financial security
@version 0.1
@date 2024-03-20
@dependencies
"""
#imports


#class
class Finance:
    """
    @brief A class to manage financial security
    @param revenue (float): The income from an entity
    @param expense (float): The costs from an entity
    @param asset (float): The financial resources of an entity
    @param liability (float): The financial obligations of an entity
    """
    def __init__(self):
        self._revenue:list[float] = None
        self._expense:list[float] = None
        self._asset:list[float] = None
        self._liability:list[float] = None
    
    @property
    def revenue(self) -> list[float]:
        """
        @brief Get the revenue of an entity
        @return (float): The revenue of an entity
        """
        return self._revenue
    
    @property
    def expense(self) -> list[float]:
        """
        @brief Get the expense of an entity
        @return (float): The expense of an entity
        """
        return self._expense
    
    @property
    def asset(self) -> list[float]:
        """
        @brief Get the asset of an entity
        @return (float): The asset of an entity
        """
        return self._asset
    
    @property
    def liability(self) -> list[float]:
        """
        @brief Get the liability of an entity
        @return (float): The liability of an entity
        """
        return self._liability
    
    @property
    def net_income(self) -> list[float]:
        """
        @brief Get the net income of an entity
        @return (float): The net income of an entity
        """
        return self._revenue - self._expense
    
    @property
    def equity(self) -> list[float]:
        """
        @brief Get the equity of an entity
        @return (float): The equity of an entity
        """
        return self._asset - self._liability
    
    @revenue.setter
    def revenue(self, revenue:list[float]) -> None:
        """
        @brief Set the revenue of an entity
        @param revenue (float): The revenue of an entity
        """
        self._revenue = revenue

    @expense.setter
    def expense(self, expense:list[float]) -> None:
        """
        @brief Set the expense of an entity
        @param expense (float): The expense of an entity
        """
        self._expense = expense

    @asset.setter
    def asset(self, asset:list[float]) -> None:
        """
        @brief Set the asset of an entity
        @param asset (float): The asset of an entity
        """
        self._asset = asset

    @liability.setter
    def liability(self, liability:list[float]) -> None:
        """
        @brief Set the liability of an entity
        @param liability (float): The liability of an entity
        """
        self._liability = liability
