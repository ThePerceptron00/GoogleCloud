import logging
import os
import sys

import argparse
from trainer import model
from trainer.util import utils
from trainer import metadata
import time
import os
from sklearn import model_selection
import hypertune

def get_args():
    
    parser = argparse.ArgumentParser(
        description="ArgeParser"
        )

    parser.add_argument('--pathdata', 
                        help="Path to raw data",
                        type=str,
                        required=True,
                        default=1
                        )

    parser.add_argument('--pathoutput', 
                        help="GCS Bucket to output model.joblib",
                        required=True,
                        type=str,
                        default=1
                        )

    parser.add_argument('--storage', 
                        help="Where your data is stored: BQ or GCS",
                        type=str,
                        required=True,
                        default=1
                        )

    parser.add_argument('--bqtable', 
                        help="full path to the BigQuery table: yourproject.dataset.table",
                        type=str,
                        required=False,
                        default=1
                        )

    parser.add_argument('--numberestimators', 
                        help="Int for the number of estimators. Default is 20",
                        type=int,
                        required=False,
                        default=20
                        )

    arguments = parser.parse_args()

    return arguments

def main():

    args = get_args()

    path_data = args.pathdata

    output_bucket = args.pathoutput

    storage = args.storage
    
    numberestimators = args.numberestimators

    full_table_path = args.bqtable

    if storage in ['BQ', 'bq' 'bigquery', 'BigQuery']:
      dataset = utils.read_df_from_bigquery(full_table_path)
    else:
      dataset = utils.get_data_from_gcs(path_data)

    x_train, y_train, x_val, y_val = utils.data_train_test_split(dataset)

    pipeline = model.get_pipeline(numberestimators)
   
    pipeline.fit(x_train, y_train)

    scores = model_selection.cross_val_score(pipeline, x_val, y_val, cv=3)

    model_output_path = os.path.join(
      output_bucket, 'model', metadata.MODEL_FILE_NAME)

    metric_output_path = os.path.join(
      output_bucket, 'experiment', metadata.METRIC_FILE_NAME)

    utils.dump_object(pipeline, model_output_path)
    utils.dump_object(scores, metric_output_path)

    accuracy = pipeline.score(x_val, y_val)

    hpt = hypertune.HyperTune()
    hpt.report_hyperparameter_tuning_metric(
      hyperparameter_metric_tag='accuracy',
      metric_value=accuracy,
      global_step=1000
      )
    
    print("model score: %.3f" % pipeline.score(x_val, y_val))
    print('pipeline run done :)')

if __name__ == '__main__':
    main()

    