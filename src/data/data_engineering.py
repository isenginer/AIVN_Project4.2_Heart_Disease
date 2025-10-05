import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class AddNewFeatures(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        """
        Class to fit the transformer and return self
        :param X: DataFrame
        :param y:
        :return:
        """
        self.columns_ = X.columns
        self.new_features_ = []
        if ("chol", "age") <= set(X.columns):
            self.new_features_.append("chol_per_age")
        if ("trestbps", "chol") <= set(X.columns):
            self.new_features_.append("bps_per_age")
        if ("thalach", "age") <= set(X.columns):
            self.new_features_.append("hr_ratio")
        if "age" in X.columns:
            self.new_features_.append("age_bin")
        return self

    def transform(self, X):
        return add_new_features(X)

    def get_new_feature_names_out(self, input_features=None):
        return list(self.columns_) + self.new_features_

# This function could not be provided in class
def add_new_features(df):
    df = df.copy()
    if ("chol", "age") <= set(df.columns):
        df["chol_per_age"] = df["chol"] / df["age"]
    if ("trestbps", "chol") <= set(df.columns):
        df["bps_per_age"] = df["chol"] / df["trestbps"]
    if (("thalach", "age") <= set(df.columns)):
        df["hr_ratio"] = df["chol"] / df["thalach"]
    if "age" in df.columns:
        df["age_bin"] = pd.cut(df["age"], bins=5, labels=False).astype("category")
    return df