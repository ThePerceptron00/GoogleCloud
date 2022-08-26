gcloud ai-platform local predict --model-dir gs://erwinh-mldemo/scikit/model/model/ \
  --json-instances trainer/predict.json \
  --verbosity debug \
  --framework scikit-learn