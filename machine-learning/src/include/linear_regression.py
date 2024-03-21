"""
@gitsil10
@version 0.1
@date 2024-03-21
@file linear_regression.py
@brief linear regression

@dependencies
numpy -> np
scipy -> stats | st

sklearn -> linear_model | metrics | model_selection | preprocessing
linear_model -> LinearRegression
metrics -> mean_squared_error | r2_score
model_selection -> train_test_split
preprocessing -> StandardScaler

@details 
A file to perform linear regression

Modeling the relationship between a dependent variable and independent variables
        1. independent variables -> explanatory | feature | continuous | quantitative | predictor | input
            1. one variable -> simple linear regression
            2. more than one variable -> multiple linear regression
        2. dependent variables -> response | continuous | quantitative | output | outcome
            1. continuous -> linear regression
            2. categorical -> logistic regression
        3. regression line -> y = mx + b | y = b0 + b1x
            1. y -> dependent variable
            2. x -> independent variable
            3. m -> b1 | slope | the change in y for a one-unit change in x
            4. b -> b0 | intercept | value of y when x = 0
            5. best fit line
            6. minimizes the sum of the squared differences between the observed and predicted values
        4. coefficient of determination -> r^2 | r-squared | the proportion of the variance in the dependent variable that is predictable from the independent variable
        5. p-value -> the probability of observing a test statistic at least as extreme in a statistical test
        6. standard error -> the standard deviation of the sampling distribution of a statistic
        7. residuals -> the difference between the observed and predicted values
        8. assumptions
            1. linearity
            2. independence
            3. homoscedasticity
            4. normality
"""
#imports
import numpy as np
import scipy.stats as st
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
#class
class Regression:
    """
    @brief A class to perform regression
    @param regression -> dict | the regression values
    @param feature -> tuple | continuous | the independent variable
    @param response -> tuple | continuous | the dependent variable
    @param slope -> float | the slope of the regression line
    @param intercept -> float | the intercept of the regression line
    @param r_squared -> float | the coefficient of determination
    @param p_value -> float | the p-value of the regression
    @param std_err -> float | the standard error of the regression
    @param residuals -> tuple | the difference between the observed and predicted values

    @details
    Modeling the relationship between a dependent variable and independent variables
    """
    def __init__(self):
        self._regression:dict = {
            "feature":None,
            "response":None,
            "slope":None,
            "intercept":None,
            "r_squared":None,
            "p_value":None,
            "std_err":None,
            "residuals":None
        }
        
        self._model = LinearRegression()

    @property
    def regression(self) -> dict:
        """
        @brief Get the regression values
        @return (dict): The regression values
        """
        return self._regression

    @property
    def feature(self) -> tuple[float]:
        """
        @brief Get the independent variable
        @return (tuple[float]): The independent variable
        """
        return self.regression["feature"]
    
    @property
    def response(self) -> tuple[float]:
        """
        @brief Get the dependent variable
        @return (tuple[float]): The dependent variable
        """
        return self.regression["response"]
    
    @property
    def predictions(self) -> tuple[float]:
        """
        @brief Get the predicted values
        @return (tuple[float]): The predicted values
        """
        return tuple(self.regression["predictions"])
    
    @property
    def slope(self) -> float:
        """
        @brief Get the slope of the regression line
        @return (float): The slope of the regression line
        """
        return self.regression["slope"]
    
    @property
    def intercept(self) -> float:
        """
        @brief Get the intercept of the regression line
        @return (float): The intercept of the regression line
        """
        return self.regression["intercept"]
    
    @property
    def mean_squared_error(self) -> float:
        """
        @brief Get the mean squared error
        @return (float): The mean squared error
        """
        return self.regression["mean_squared_error"]
    
    @property
    def r_squared(self) -> float:
        """
        @brief Get the coefficient of determination
        @return (float): The coefficient of determination
        """
        return self.regression["r_squared"]
    
    @property
    def p_value(self) -> float:
        """
        @brief Get the p-value of the regression
        @return (float): The p-value of the regression
        """
        return self.regression["p_value"]
    
    @property
    def std_err(self) -> float:
        """
        @brief Get the standard error of the regression
        @return (float): The standard error of the regression
        """
        return self.regression["std_err"]
    
    @property
    def residuals(self) -> tuple[float]:
        """
        @brief Get the difference between the observed and predicted values
        @return (tuple[float]): The difference between the observed and predicted values
        """
        return self.regression["residuals"]
    
    @property
    def model(self) -> LinearRegression:
        """
        @brief Get the linear regression model
        @return (LinearRegression): The linear regression model
        """
        return self._model

    def fit(self, feature:tuple[float] = None, response:tuple[float] = None) -> bool:
        """
        @brief Fit the linear regression model
        @param feature -> tuple[float] | None | continuous | the independent variable
        @param response -> tuple[float] | None | continuous | the dependent variable
        @return (None)
        """
        #feature is set
        if not feature is None:
            self.regression["feature"] = feature

        #response is set
        if not response is None:
            self.regression["response"] = response

        #ignore if feature is not set
        if not self.regression["feature"] is None and not self.regression["response"] is None:
            #simple random sampling
            X_train, X_test, y_train, y_test = train_test_split(
                np.array(self.feature).reshape(-1, 1), 
                np.array(self.response).reshape(-1, 1), 
                test_size=0.2, 
                random_state=0
            )

            #normalize
            scaler = StandardScaler()
            X_train, X_test = scaler.fit_transform(X_train), scaler.transform(X_test)
            
            #model fitting
            self.model.fit(X_train, y_train)

            #model evaluation
            self.regression["slope"] = self.model.coef_[0][0]
            self.regression["intercept"] = self.model.intercept_[0]
            self.regression["predictions"] = self.model.predict(X_test)
            self.regression["mean_squared_error"] = mean_squared_error(y_test, self.predictions)
            self.regression["r_squared"] = r2_score(y_test, self.predictions)
            self.regression["p_value"] = st.linregress(self.feature, self.response).pvalue
            self.regression["std_err"] = st.linregress(self.feature, self.response).stderr
            self.regression["residuals"] = y_test - self.predictions
            return True
    
        return False
        
    def prediction(self, feature:tuple[float]) -> float:
        """
        @brief Predict the dependent variable
        @param feature -> tuple[float] | continuous | the independent variable
        @return (float): The predicted dependent variable
        """
        return self.model.predict(np.array(self.feature).reshape(-1, 1))[0][0]
    
