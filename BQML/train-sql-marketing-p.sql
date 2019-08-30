CREATE OR REPLACE MODEL
  marketing.propensity_v1
OPTIONS
  (model_type='LOGISTIC_REG') AS
SELECT
  age,
  job,
  education,
  housing,
  contact,
  duration,
  pdays,
  previous,
  poutcome,
  month,
  y AS label
FROM
  `erwinh-mldemo.marketing.marketing_propensity_main`