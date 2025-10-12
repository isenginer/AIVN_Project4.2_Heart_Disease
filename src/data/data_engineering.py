import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


def data_loader(path, filenames=None):
    """
    minor function to collect train, validation and test data with error check
    :param path: path to csv file
    :param filenames: set of filenames
    :return: train, validation and test dataset
    """
    if filenames is None:
        filenames = ("", "", "")
    try:
        train_data = pd.read_csv(path + filenames[0])
        val_data = pd.read_csv(path + filenames[1])
        test_data = pd.read_csv(path + filenames[2])
        print(f"✅ Load data from {filenames} successfully")
    except FileNotFoundError:
        print("❌ Data not found, please run data_loader first")

    return (train_data.iloc[:, :-1], # X_train
            val_data.iloc[:, :-1],   # X_val
            test_data.iloc[:, :-1],  # X_test
            train_data.iloc[:, -1],  # y_train
            val_data.iloc[:, -1],    # y_val
            test_data.iloc[:, -1])   # y_test

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
        # This is method to compare subset inside a set, to check that (choice, age) is in X.columns or not
        if {"chol", "age"} <= set(X.columns):
            self.new_features_.append("chol_per_age")
        if {"trestbps", "chol"} <= set(X.columns):
            self.new_features_.append("bps_per_age")
        if {"thalach", "age"} <= set(X.columns):
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
    if {"chol", "age"} <= set(df.columns):
        df["chol_per_age"] = df["chol"] / df["age"]
    if {"trestbps", "chol"} <= set(df.columns):
        df["bps_per_age"] = df["chol"] / df["trestbps"]
    if {"thalach", "age"} <= set(df.columns):
        df["hr_ratio"] = df["chol"] / df["thalach"]
    if "age" in df.columns:
        df["age_bin"] = pd.cut(df["age"], bins=5, labels=False).astype("category")
    return df


if __name__ == "__main__":
    data = pd.read_csv("/mnt/DATA/10_AIO_VN/AIOVN_Main/Project 4.2_Heart Desease/dataset/train.csv")
    feature_add = AddNewFeatures()
    data_fit = feature_add.fit(data)
    data_transform = feature_add.transform(data)
    print(data_transform.columns)