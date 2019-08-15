gcloud ai-platform predict \
  --model MarketingPredictor \
  --version marketing_v1 \
  --json-instances trainer/predict.json