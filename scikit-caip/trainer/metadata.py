
CSV_COLUMNS = [
  'age',
  'job',
  'marital',
  'education',
  'balance',
  'housing',
  'loan',
  'contact',
  'day',
  'month',
  'duration',
  'campaign',
  'pdays',
  'previous',
  'poutcome',
  'y'             
  ]

CATEGORICAL_FEATURES = [
  'job',
  'marital',
  'education',
  'contact',
  'month',
  'poutcome',
  ]

NUMERIC_FEATURES = [
  'age',
  'balance', 
  'day',
  'duration',
  'campaign', 
  'pdays', 
  'previous',     
  ]

BOOLEAN_FEATURES = [
  'housing',
  'loan',
  ]


FEATURE_COLUMNS = [
  'age',
  'job',
  'marital',
  'education',
  'balance',
  'housing',
  'loan',
  'contact',
  'day',
  'month',
  'duration',
  'campaign',
  'pdays',
  'previous',
  'poutcome',
  ]

LABEL = 'y'

METRIC_FILE_NAME = 'eval_metrics.joblib'
MODEL_FILE_NAME = 'model.joblib'

QUERY = '''
select 
  age,
  job,
  marital,
  education,
  balance,
  housing,
  loan,
  contact,
  day,
  month,
  duration,
  campaign,
  pdays,
  previous,
  poutcome,
  y
from 
  `{table}`
 '''