import functools

import numpy as np
from sklearn import compose
from sklearn import ensemble
from sklearn import impute
from sklearn import pipeline
from sklearn import preprocessing
from trainer import metadata
import tensorflow as tf
import pandas as pd
from trainer.util import utils
from trainer.util import preprocess_utils

from trainer import metadata

def get_estimator():

    classifier = ensemble.RandomForestClassifier(
        n_estimators=20)

    return classifier

def get_pipeline():

    classifier = get_estimator()


    feature_columns = metadata.FEATURE_COLUMNS
    numerical_names = metadata.NUMERIC_FEATURES
    categorical_names = metadata.CATEGORICAL_FEATURES

    preprocessor = preprocess_utils.get_preprocess_pipeline(
                                  feature_columns=feature_columns,
                                  numerical_names=numerical_names,
                                  categorical_names=categorical_names
                                  )

    estimator = pipeline.Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', classifier),
        ])

    return estimator




