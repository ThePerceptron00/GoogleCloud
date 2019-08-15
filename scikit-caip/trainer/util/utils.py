import os

import pandas as pd
from sklearn import model_selection
from sklearn.externals import joblib
import tensorflow as tf
from tensorflow import gfile

from trainer import metadata

def get_data_from_gcs(PATH_DATA):
  
    with tf.io.gfile.GFile(PATH_DATA, 'r') as my_file:
        dataset=pd.read_csv(my_file)
        print(dataset)
    return dataset

def _feature_label_split(data_df, label_column):
  
  return data_df.loc[:, data_df.columns != label_column], data_df[label_column]

def boolean_mask(columns, target_columns):
  
  target_set = set(target_columns)
  return [x in target_set for x in columns]

def data_train_test_split(data_df):
    
    label_column = metadata.LABEL
    columns_to_use = metadata.FEATURE_COLUMNS + [label_column]

    train, val = model_selection.train_test_split(data_df[columns_to_use])
    x_train, y_train = _feature_label_split(train, label_column)
    x_val, y_val = _feature_label_split(val, label_column)
    
    return x_train, y_train, x_val, y_val

def dump_object(object_to_dump, output_path):

  if not gfile.Exists(output_path):
    gfile.MakeDirs(os.path.dirname(output_path))
  
  with gfile.Open(output_path, 'w') as wf:
    joblib.dump(object_to_dump, wf)

def read_df_from_bigquery(full_table_path, project_id=None, num_samples=None):
   
  query = metadata.QUERY.format(table=full_table_path)

  data_df = pd.read_gbq(query, project_id=project_id, dialect='standard')

  return data_df