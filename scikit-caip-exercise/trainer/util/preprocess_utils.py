import functools

import numpy as np
from sklearn import compose
from sklearn import impute
from sklearn import pipeline
from sklearn import preprocessing
from trainer import metadata

from trainer.util import utils

def get_preprocess_pipeline(feature_columns, categorical_names, numerical_names):

    numeric_transformer = pipeline.Pipeline([
        ('imputer', impute.SimpleImputer(strategy='median')),
        ('scaler', preprocessing.StandardScaler()),
        ])

    categorical_transformer = pipeline.Pipeline([
        ('onehot', preprocessing.OneHotEncoder(
            handle_unknown='ignore', sparse=False)),
        ])

    feature_columns = metadata.FEATURE_COLUMNS
    numerical_names = metadata.NUMERIC_FEATURES
    categorical_names = metadata.CATEGORICAL_FEATURES

    boolean_mask = functools.partial(utils.boolean_mask, feature_columns)
    numerical_boolean = boolean_mask(numerical_names)
    categorical_boolean = boolean_mask(categorical_names)

    print(numerical_boolean)
    print(categorical_boolean)

    transform_list = []

    if any(numerical_boolean):
             transform_list.extend([('numeric', numeric_transformer, numerical_boolean),
             ])

    if any(categorical_boolean):
            transform_list.extend([
            ('categorical', categorical_transformer, categorical_boolean),
            ])

    preprocessor = compose.ColumnTransformer(transform_list)

    return preprocessor

