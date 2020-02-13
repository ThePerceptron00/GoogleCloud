import functools

import numpy as np
import sklearn
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

def get_estimator(numberestimators):

    classifier = ensemble.RandomForestClassifier(n_estimators=numberestimators)

    return classifier

def get_pipeline(numberestimators):

    classifier = get_estimator(numberestimators)


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




