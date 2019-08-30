SELECT 
  *
FROM 
  ML.EVALUATE(MODEL `marketing.propensity_v1`, ( 
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
 `erwinh-mldemo.marketing.marketing_propensity_main`))