"""
@gitsil10
@version 0.1
@date 2024-03-20
@file statistics_mgmt.py
@brief statistics management

@dependencies
scipy.stats -> st

@details
A file to manage statistics
1. standard error
2. normalize
3. confidence intervals
4. hypothesis test
5. probability
    1. normal distribution
    2. binomial distribution
    3. poisson distribution
    4. exponential distribution
    5. uniform distribution
    6. bernoulli distribution
    7. geometric distribution
    8. hypergeometric distribution
    9. negative binomial distribution
    10. chi-square distribution
    11. student's t-distribution
    12. f-distribution
    13. gamma distribution
    14. weibull distribution
    15. t-distribution
"""
#imports
import scipy.stats as st

#class
class StatisticsMgmt:
    def __init__(self):
        self._data: tuple[float] = None
        self._mean: float = None
        self._std_dev: float = None
        self._count: int = None

    @property
    def data(self):
        return self._data
    
    @property
    def mean(self):
        return self._mean
    
    @property
    def std_dev(self):
        return self._std_dev
    
    @property
    def count(self):
        return self._count
    
    @property
    def standard_error(self):
        if self.data is None:
            raise ValueError("Data must be set")
        return st.sem(self.data)
    
    @data.setter
    def data(self, data: list[float] = None):
        if data is None or not isinstance(data, list[float]):
            raise ValueError("Data must be list of floats")
        
        self._data = tuple(data)

    @mean.setter
    def mean(self, mean: float = None):
        if mean is None or not isinstance(mean, float):
            raise ValueError("Mean must be float")
        
        self._mean = mean

    @std_dev.setter
    def std_dev(self, std_dev: float = None):
        if std_dev is None or not isinstance(std_dev, float):
            raise ValueError("Standard deviation must be float")
        
        self._std_dev = std_dev

    @count.setter
    def count(self, count: int = None):
        if count is None or not isinstance(count, int):
            raise ValueError("Count must be int")
        
        self._count = count

    def normalize(self) -> tuple:
        """
        @brief sets data relative to mean of zero and standard deviation of one
        @return tuple

        @details
        A method to calculate z-score
        z = (x - mean) / std_dev
        """
        if self.mean is None or self.std_dev is None:
            raise ValueError("Mean and standard deviation must be set")
        
        return st.zscore(self.data)

    def conf_interval(self, alpha: float = 0.05) -> tuple:
        """
        @brief confidence interval
        @param alpha -> float | 0.05 | significance level
        @return tuple -> (float, float) | (lower, upper) | range of values that is likely to contain the population parameter

        @details
        A method to calculate confidence interval
            1. mean +- (z * (std_dev / sqrt(n)))
            2. purpose is to estimate the population parameter   
        """
        if self.mean is None or self.std_dev is None or self.count is None or alpha < 0 or alpha > 1:
            raise ValueError("Mean, standard deviation, and count must be set")
        
        return st.t.interval(1 - alpha, self.count -1 , loc = self.mean, scale=self.standard_error)
        
    def hypothesis_test(self, mu: float = 0, alpha: float = 0.05, alternative: str = "two-sided") -> tuple:
        """
        @brief hypothesis test
        @param mu -> float | mean of the population
        @param alpha -> float | 0.05 | significance level
        @param alternative -> str | "two-sided" | "less" | "greater" | alternative hypothesis | test type
        @return tuple -> (float, float) | (t-statistic, p-value) | test statistic and p-value | test result

        @details
        A method to perform hypothesis test
            1. null hypothesis -> H0: mu = mu0
            2. alternative hypothesis -> H1: mu != mu0 | H1: mu < mu0 | H1: mu > mu0
            3. t-statistic = (mean - mu) / (std_dev / sqrt(n))
            4. p-value = P(t > |t-statistic|) | P(t < |t-statistic|) | P(t > |t-statistic|)
            5. if p-value < alpha, reject null hypothesis
            6. if p-value > alpha, fail to reject null hypothesis
            7. purpose is to determine if there is enough evidence to reject the null hypothesis
        """
        if self.mean is None or self.std_dev is None or self.count is None or alpha < 0 or alpha > 1:
            raise ValueError("Mean, standard deviation, and count must be set")
        
        return st.ttest_1samp(self.data, mu, alternative=alternative, nan_policy="omit")
    
    #probability
    def normal_prob(self, x: float = 0, mu: float = 0, sigma: float = 1) -> float:
        """
        @brief normal distribution
        @param x -> float | random variable
        @param mu -> float | mean of the distribution | center of the peak
        @param sigma -> float | standard deviation | spread of the distribution
        @return float

        @details
        A method to calculate normal distribution
            1. f(x) = (1 / (sigma * sqrt(2 * pi))) * e^(-1/2 * ((x - mu) / sigma)^2)
            2. the normal distribution is a continuous probability distribution
            3. symmetric about the mean
            4. mean = median = mode
            5. 68% of the data falls within 1 standard deviation of the mean
            6. 95% of the data falls within 2 standard deviations of the mean
            7. 99.7% of the data falls within 3 standard deviations of the mean
        """
        return st.norm.pdf(x, mu, sigma)
    
    def binomial_prob(self, x: int = 0, n: int = 0, p: float = 0) -> float:
        """
        @brief binomial distribution
        @param x -> int | number of successes
        @param n -> int | number of trials
        @param p -> float | probability of success
        @return float

        @details
        A method to calculate binomial distribution
            1. f(x) = (n choose x) * p^x * (1 - p)^(n - x)
            2. the binomial distribution is a discrete probability distribution
            3. purpose is to determine the probability of a given number of successes in a fixed number of trials
        """
        return st.binom.pmf(x, n, p)
    
    def poisson_prob(self, x: int = 0, mu: float = 0) -> float:
        """
        @brief poisson distribution
        @param x -> int | number of events
        @param mu -> float | average number of events
        @return float

        @details
        A method to calculate poisson distribution
            1. the poisson distribution is a discrete probability distribution
            2. f(x) = (e^(-mu) * mu^x) / x!
            3. purpose is to determine the probability of a given number of events in a fixed interval of time
        """
        return st.poisson.pmf(x, mu)
    
    def exponential_prob(self, x: float = 0, mu: float = 0) -> float:
        """
        @brief exponential distribution
        @param x -> float | random variable
        @param mu -> float | average time between events
        @return float

        @details
        A method to calculate exponential distribution
            1. the exponential distribution is a continuous probability distribution
            2. f(x) = (1 / mu) * e^(-x / mu)
            3. purpose is to determine the probability of a given time between events
        """
        return st.expon.pdf(x, mu)
    
    def uniform_prob(self, x: float = 0, a: float = 0, b: float = 1) -> float:
        """
        @brief uniform distribution
        @param x -> float | random variable
        @param a -> float | lower bound
        @param b -> float | upper bound
        @return float

        @details
        A method to calculate uniform distribution
            1. the uniform distribution is a continuous probability distribution
            2. f(x) = 1 / (b - a)
            3. purpose is to determine the probability of a given value within a range
        """
        return st.uniform.pdf(x, a, b)
    
    def bernoulli_prob(self, x: int = 0, p: float = 0) -> float:
        """
        @brief bernoulli distribution
        @param x -> int | number of successes
        @param p -> float | probability of success
        @return float

        @details
        A method to calculate bernoulli distribution
            1. the bernoulli distribution is a discrete probability distribution
            2. f(x) = p^x * (1 - p)^(1 - x)
            3. purpose is to determine the probability of a given number of successes in a single trial
        """
        return st.bernoulli.pmf(x, p)
    
    def geometric_prob(self, x: int = 0, p: float = 0) -> float:
        """
        @brief geometric distribution
        @param x -> int | number of trials until success
        @param p -> float | probability of success
        @return float

        @details
        A method to calculate geometric distribution
            1. the geometric distribution is a discrete probability distribution
            2. f(x) = (1 - p)^(x - 1) * p
            3. purpose is to determine the probability of a given number of trials until success
        """
        return st.geom.pmf(x, p)
    
    def hypergeometric_prob(self, x: int = 0, M: int = 0, n: int = 0, N: int = 0) -> float:
        """
        @brief hypergeometric distribution
        @param x -> int | number of successes
        @param M -> int | population size
        @param n -> int | number of successes in population
        @param N -> int | number of draws
        @return float

        @details
        A method to calculate hypergeometric distribution
            1. the hypergeometric distribution is a discrete probability distribution
            2. f(x) = (n choose x) * ((M - n) choose (N - x)) / (M choose N)
            3. purpose is to determine the probability of a given number of successes in a fixed number of draws without replacement
        """
        return st.hypergeom.pmf(x, M, n, N)
    
    def negative_binomial_prob(self, x: int = 0, n: int = 0, p: float = 0) -> float:
        """
        @brief negative binomial distribution
        @param x -> int | number of successes
        @param n -> int | number of trials
        @param p -> float | probability of success
        @return float

        @details
        A method to calculate negative binomial distribution
            1. the negative binomial distribution is a discrete probability distribution
            2. f(x) = (x + n - 1 choose x) * p^n * (1 - p)^x
            3. purpose is to determine the probability of a given number of trials until a given number of successes
        """
        return st.nbinom.pmf(x, n, p)
    
    def chi_square_prob(self, x: float = 0, df: int = 1) -> float:
        """
        @brief chi-square distribution
        @param x -> float | random variable
        @param df -> int | degrees of freedom
        @return float

        @details
        A method to calculate chi-square distribution
            1. the chi-square distribution is a continuous probability distribution
            2. f(x) = (1 / (2^(k/2) * gamma(k/2))) * x^(k/2 - 1) * e^(-x/2)
            3. purpose is to determine the probability of a given value within a range
            4. used to compare the variance of a sample to the variance of a population
        """
        return st.chi2.pdf(x, df)
    
    def student_t_prob(self, x: float = 0, df: int = 1) -> float:
        """
        @brief student's t-distribution
        @param x -> float | random variable
        @param df -> int | degrees of freedom
        @return float

        @details
        A method to calculate student's t-distribution
            1. the student's t-distribution is a continuous probability distribution
            2. f(x) = (1 / (sqrt(df) * beta(1/2, df/2))) * (1 + (x^2 / df))^(-1/2 * (df + 1))
            3. purpose is to determine the probability of a given value within a range
            4. used to estimate the population mean when the population standard deviation is unknown
        """
        return st.t.pdf(x, df)
    
    def f_prob(self, x: float = 0, dfn: int = 1, dfd: int = 1) -> float:
        """
        @brief f-distribution
        @param x -> float | random variable
        @param dfn -> int | degrees of freedom numerator
        @param dfd -> int | degrees of freedom denominator
        @return float

        @details
        A method to calculate f-distribution
            1. the f-distribution is a continuous probability distribution
            2. f(x) = (1 / (beta(dfn/2, dfd/2) * dfn/dfd^(dfn/2))) * x^((dfn/2) - 1) * (1 + (dfn/dfd * x))^(-1 * (dfn + dfd)/2)
            3. purpose is to determine the probability of a given value within a range
            4. used to compare the variances of two populations
        """
        return st.f.pdf(x, dfn, dfd)
    
    def gamma_prob(self, x: float = 0, a: float = 1, scale: float = 1) -> float:
        """
        @brief gamma distribution
        @param x -> float | random variable
        @param a -> float | shape parameter
        @param scale -> float | scale parameter
        @return float

        @details
        A method to calculate gamma distribution
            1. the gamma distribution is a continuous probability distribution
            2. f(x) = (1 / (gamma(a) * scale^a)) * x^(a - 1) * e^(-x/scale)
            3. purpose is to determine the probability of a given value within a range
            4. used to model the time until an event occurs in a fixed interval of time
        """
        return st.gamma.pdf(x, a, scale)
    
    def weibull_prob(self, x: float = 0, c: float = 1, scale: float = 1) -> float:
        """
        @brief weibull distribution
        @param x -> float | random variable
        @param c -> float | shape parameter
        @param scale -> float | scale parameter
        @return float

        @details
        A method to calculate weibull distribution
            1. the weibull distribution is a continuous probability distribution
            2. f(x) = (c / scale) * (x / scale)^(c - 1) * e^(-1 * (x / scale)^c)
            3. purpose is to determine the probability of a given value within a range
            4. used to model the time until an event occurs in a fixed interval of time
        """
        return st.weibull_min.pdf(x, c, scale)
    
    def t_prob(self, x: float = 0, df: int = 1) -> float:
        """
        @brief t-distribution
        @param x -> float | random variable
        @param df -> int | degrees of freedom
        @return float

        @details
        A method to calculate t-distribution
            1. the t-distribution is a continuous probability distribution
            2. f(x) = (1 / (sqrt(df) * beta(1/2, df/2))) * (1 + (x^2 / df))^(-1/2 * (df + 1))
            3. purpose is to determine the probability of a given value within a range
            4. used to estimate the population mean when the population standard deviation is unknown
        """
        return st.t.pdf(x, df)
    
    


    