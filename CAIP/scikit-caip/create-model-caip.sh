gcloud ai-platform versions create marketing_v1 \
    --model MarketingPredictor \
    --origin gs://erwinh-mldemo/scikit/model/model/ \
    --runtime-version 1.14 \
    --python-version 3.5 \