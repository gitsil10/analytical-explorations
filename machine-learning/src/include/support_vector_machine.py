"""
@gitsil10
@version 0.1
@date 2024-03-21
@file support_vector_machine.py
@brief support vector machine

@dependencies
numpy -> np
sklearn -> svm | metrics | model_selection | preprocessing
metrics -> accuracy_score | classification_report | confusion_matrix
model_selection -> train_test_split
preprocessing -> StandardScaler

@details
Set of related algorithms for supervised learning problems
    1. supervised max-margin models
        1. input -> set of labeled training data for each category
        2. output -> categorize new text
        3. prediction -> binary classification
        4. hyperplane -> decision boundary
        5. margin -> distance between the hyperplane and the nearest data point from either category
        6. maximum-margin hyperplane -> hyperplane with the maximum margin
        7. support vectors -> data points that are closest to the hyperplane
        8. maximize the margin to minimize the generalization error
        9. memory efficient
    2. classification
        1. two-group classification problems
            1. prediction -> binary
        2. multi-class classification problems
            1. multiple binary classifiers
            2. one-versus-all -> one classifier for each category
            3. one-versus-one -> one classifier for each pair of categories
    3. regression analysis
        1. prediction -> continuous
        2. hyperplane -> best fit
        3. support vector regression
            1. minimize the margin violations
            2. minimize the sum of the differences between the predicted and actual values
    4. outlier detection
        1. identify the data points that are far from the hyperplane
    5. clustering
        1. unsupervised learning
        2. group the data points into categories
    6. density estimation
        1. estimate the probability density function of the data
    7. non-linear classification
        1. kernel trick
            1. implicit mapping inputs into high-dimensional feature spaces
    8. non-linear regression
    9. uses classification algorithms for two-group classification problems
    10. inefficient for large datasets
"""
#imports
import numpy as np
from sklearn import svm
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#class
class SupportVectorMachine:
    """
    @brief A class to perform support vector machines
    @param feature -> tuple | continuous | the independent variable
    @param response -> tuple | continuous | the dependent variable
    @param accuracy -> float | the accuracy of the model
    @param classification_report -> dict | the classification report
    @details
    """
    def __init__(self):
        self._machines:dict = {
            "feature":None,
            "response":None,
            "prediction":None,
            "accuracy":None,
            "error":None,
            "classification_report":None,
            "confusion_matrix":None
        }
        self._model = svm.SVC()

    @property
    def machines(self) -> dict:
        """
        @brief Get the support vector machines values
        @return (dict): The support vector machines values
        """
        return self._machines
    
    @property
    def feature(self) -> tuple[float]:
        """
        @brief Get the feature
        @return (tuple): The feature
        """
        return self.machines["feature"]
    
    @property
    def response(self) -> tuple[float]:
        """
        @brief Get the response
        @return (tuple): The response
        """
        return self.machines["response"]
    
    @property
    def prediction(self) -> tuple[float]:
        """
        @brief Get the prediction
        @return (tuple): The prediction
        """
        return self.machines["prediction"]
    
    @property
    def accuracy(self) -> float:
        """
        @brief Get the accuracy
        @return (float): The accuracy
        """
        return self.machines["accuracy"]
    
    @property
    def classification_report(self) -> dict:
        """
        @brief Get the classification report
        @return (dict): The classification report
        """
        return self.machines["classification_report"]
    
    @property
    def confusion_matrix(self) -> dict:
        """
        @brief Get the confusion matrix
        @return (dict): The confusion matrix
        """
        return self.machines["confusion_matrix"]
    
    @property
    def error(self) -> float:
        """
        @brief Get the error
        @return (float): The error
        """
        return self.machines["error"]
    
    @property
    def model(self) -> svm.SVC:
        """
        @brief Get the model
        @return (svm.SVC): The model
        """
        return self._model
    
    def fit(self, feature:tuple[float] = None, response:tuple[float] = None
            , test_size:float=0.2, random_state:int=0) -> bool:
        """
        @brief Fit the support vector machines
        @param feature (tuple[float]): The independent variable
        @param response (tuple[float]): The dependent variable
        @param test_size (float): The test size
        @param random_state (int): The random state
        """
        if not feature is None:
            self.machines["feature"] = feature

        if not response is None:
            self.machines["response"] = response

        if self.feature is None or self.response is None:
            return False

        #split the dataset
        X_train, X_test, y_train, y_test = train_test_split(
            self.feature, self.response, test_size=test_size, random_state=random_state
        )
        
        #scale the features
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        #fit the model
        self.model.fit(X_train, y_train)

        #process
        self.machines["prediction"] = self.model.predict(X_test)

        #evaluate
        self.machines["accuracy"] = accuracy_score(y_test, self.prediction)
        self.machines["classification_report"] = classification_report(y_test, self.prediction)
        self.machines["confusion_matrix"] = confusion_matrix(y_test, self.prediction)
        self.machines["error"] = 1 - self.accuracy
        return True
    
    def predict(self, feature:tuple[float]) -> tuple[float]:
        """
        @brief Predict the response
        @param feature (tuple[float]): The independent variable
        @return (tuple[float]): The dependent variable
        """
        return self.model.predict(feature)
    
    def score(self) -> float:
        """
        @brief Score the model
        @param feature (tuple[float]): The independent variable
        @param response (tuple[float]): The dependent variable
        @return (float): The score
        """
        return self.model.score(self.feature, self.response)
    
