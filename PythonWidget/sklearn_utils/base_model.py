
import warnings

from numbers import Number

import numpy as np
import pandas as pd

from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler, Normalizer, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import precision_score, recall_score

warnings.filterwarnings("ignore")

def load_data(path):
    if path.endswith("xls") or path.endswith("xlsx"):
        data = pd.read_excel(path)
    elif path.endswith("csv"):
        data = pd.read_csv(path)
    else:
        raise ValueError("data type does not support")
    return data


class BaseModel(object):
    """base_model
    
    [description]
    自动补入nan值
    提供基准模型
    """
    def __init__(self, estimator,
                       fill_num_na_value=0,
                       fill_cat_na_strategy="most_frequent",
                       num_columns=None,
                       cat_columns=None,
                       data=None):
        self.estimator = estimator
        self.fill_num_na_value = fill_num_na_value
        self.fill_cat_na_strategy = fill_cat_na_strategy
        self.num_columns = num_columns
        self.cat_columns = cat_columns
        self.data = data
        if self.data is not None:
            ret = self.auto_search_cat_and_nums()
            if self.num_columns is None:
                self.num_columns = ret["num_columns"]
            if self.cat_columns is None:
                self.cat_columns = ret["cat_columns"]

    def auto_search_cat_and_nums(self):
        num_columns = []
        cat_columns = []
        for column in self.data.columns:
            if self.data[column].dtype == "object":
                cat_columns.append(column)
            else:
                num_columns.append(column)
        ret = {}
        ret["cat_columns"] = cat_columns
        ret["num_columns"] = num_columns
        return ret

    @property
    def fill_na_num(self):
        return SimpleImputer(strategy="constant", 
                             fill_value=self.fill_num_na_value)

    @property
    def fill_na_cat(self):
        pipe = Pipeline(
                steps=[("impute", SimpleImputer(strategy=self.fill_cat_na_strategy)),
                       ("onehot", OneHotEncoder(handle_unknown="ignore")),
                       ])
        return pipe

    def data_pipe(self):
        transformers=[
                        ("num", self.fill_na_num, self.num_columns),
                        ("cat", self.fill_na_cat, self.cat_columns),
                    ]
        pipe = ColumnTransformer(
                   transformers=transformers,
            )
        return pipe

    def pipe(self):
        pipe = Pipeline([
                ("data_pipe", self.data_pipe()),
                ("estimator", self.estimator)
            ])
        return pipe

    def api(self):
        return self.pipe()

    def __call__(self):
        return self.api()


class ResetThresholdForBinaryClassification(object):
    def __init__(self, estimator, 
                       train_data, 
                       threshold=0.5):
        self.estimator = estimator
        self.train_data = train_data
        self.threshold = threshold


    def postprocess(self):
        prediction_proba = self.estimator.predict_proba(self.train_data)
        new_prediction = np.zeros(len(self.train_data))
        
        for index, prob in enumerate(prediction_proba[:, 1]):
            if prob >= self.threshold:
                new_prediction[index] = 1
        return new_prediction

    def api(self):
        ret = self.postprocess()
        return ret

    def __call__(self):
        return self.api()
