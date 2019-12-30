CREATE OR REPLACE MODEL `kfp-primer-workshop.marketing_data.bq_model` 
OPTIONS(model_type='logistic_reg') AS
SELECT
    IF(totals.transactions IS NULL, 0, 1) AS label,
    IFNULL(geoNetwork.country, "") AS country,
    IFNULL(totals.pageviews, 0) AS pageviews,
    IFNULL(device.operatingSystem, "") AS os,
    IF(device.isMobile,1,0) AS is_mobile
FROM
    `bigquery-public-data.google_analytics_sample.ga_sessions_*`
WHERE
    _TABLE_SUFFIX BETWEEN '20160801' AND '20170631'
LIMIT 100000;

--------------------------------------------------------------------

SELECT
  country,
  SUM(predicted_label) as total_predicted_purchases
FROM
  ml.PREDICT(MODEL `kfp-primer-workshop.marketing_data.bq_model`, (
SELECT
  IFNULL(device.operatingSystem, "") AS os,
  IF(device.isMobile,1,0) AS is_mobile,
  IFNULL(totals.pageviews, 0) AS pageviews,
  IFNULL(geoNetwork.country, "") AS country
FROM
  `bigquery-public-data.google_analytics_sample.ga_sessions_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20170701' AND '20170801'))
GROUP BY country
ORDER BY total_predicted_purchases DESC
LIMIT 10;

-----------------------------------------------

CREATE OR REPLACE MODEL `kfp-primer-workshop.marketing_data.tf_model_erwinh`
OPTIONS (model_type='tensorflow',
         model_path='gs://kfp-scikit/code/bqml-master/model_output/1568359585/*')

-----------------------------------------------

# Select a bunch of data 
WITH input_data AS(
SELECT 
      IFNULL(device.operatingSystem, "") AS os,
      IF(device.isMobile,1,0) AS is_mobile,
      IFNULL(geoNetwork.country, "") AS country,
      IFNULL(totals.pageviews, 0) AS pageviews
FROM 
      `bigquery-public-data.google_analytics_sample.ga_sessions_*`
WHERE
      _TABLE_SUFFIX BETWEEN '20170801' AND '20170802'    
  ),

# Do the predictions
predictions AS(
SELECT * FROM ML.PREDICT(MODEL project.dataset.tf_model_2,
                    (SELECT * FROM input_data))
  )

# Select predictions
SELECT * FROM predictions
LIMIT 100