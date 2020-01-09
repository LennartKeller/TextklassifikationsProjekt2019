from typing import Union, List

import numpy as np
from scipy.sparse import csr_matrix
from sklearn.base import BaseEstimator
from sklearn.exceptions import NotFittedError
from sklearn.metrics import f1_score
from tqdm import tqdm


class PeriodEstimatorWrapper(BaseEstimator):

    def __init__(self, clf: BaseEstimator, **params):
        self.clf = clf(**params)
        if params.get('verbose'):
            self.verbose = params['verbose']

    def fit(self, X_train: Union[csr_matrix, np.ndarray], y_train: np.array):
        """
        Fits the estimator.

        :param X_train: normal feature matrix e.g. shape (n_samples, n_features)
        :param y_train: label vector shape (n_samples,)
        :return: fitted instance of itself
        """

        self.clf.fit(X_train, y_train)
        self.fitted_ = True

        return self

    def predict(self, X_test: List[Union[csr_matrix, np.ndarray]]):
        """
        Predicts classes for n periods
        :param X_test: list of feature matrices (n_samples, n_features) to predict (one for each period)
        :return: list of predicted label vectors
        """

        if not self.fitted_:
            raise NotFittedError

        result = []
        if self.verbose:
            iterator = tqdm(X_test, desc='Predicting classes for periods')
        else:
            iterator = X_test

        for X in iterator:
            result.append(self.clf.predict(X))

        return result

    def predict_proba(self, X_test: List[Union[csr_matrix, np.ndarray]]):
        """
        Predicts probabilities for n periods
        :param X_test: list of feature matrices (n_samples, n_features) to predict (one for each period)
        :return: list of predicted label vectors
        """
        if not hasattr(self.clf, 'predict_proba'):
            raise Exception(f"Method predict_proba is not implemented in {self.clf.__class__.__name__}")

        if not self.fitted_:
            raise NotFittedError

        result = []
        if self.verbose:
            iterator = tqdm(X_test, desc='Predicting classes for periods')
        else:
            iterator = X_test

        for X in iterator:
            result.append(self.clf.predict_proba(X))

        return result

    def decision_function(self, X_test: List[Union[csr_matrix, np.ndarray]]):
        """
        Predicts decision scores for n periods
        :param X_test: list of feature matrices (n_samples, n_features) to predict (one for each period)
        :return: list of predicted label vectors
        """
        if not hasattr(self.clf, 'decision_function'):
            raise Exception(f"Method decision_function is not implemented in {self.clf.__class__.__name__}")

        if not self.fitted_:
            raise NotFittedError

        result = []
        if self.verbose:
            iterator = tqdm(X_test, desc='Predicting classes for periods')
        else:
            iterator = X_test

        for X in iterator:
            result.append(self.clf.predict_proba(X))

        return result

    def score(self,
              X_test: List[Union[csr_matrix, np.ndarray]],
              y_true: List[np.array],
              scoring_func: callable = lambda y_true, y_pred: f1_score(y_true, y_pred, average='macro'),
              pooling_func: callable = np.mean,
              pooling: bool = True):

        if not self.fitted_:
            raise NotFittedError

        scores = []
        for X, y in zip(X_test, y_true):
            y_pred = self.clf.predict(X)
            score = scoring_func(y, y_pred)
            scores.append(score)

        if pooling:
            return pooling_func(scores)
        else:
            return scores
