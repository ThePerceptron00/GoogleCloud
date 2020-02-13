gcloud ai-platform local train \
   --module-name=trainer.task \
   --package-path=trainer/ \
   -- \
   --pathdata gs://erwinh-mldemo/scikit/marketing-data.csv \
   --pathoutput gs://erwinh-mldemo/scikit/model \
   --storage BQ \
   --numberestimators 40 \
   --bqtable erwinh-mldemo.marketing.marketing_propensity_main

