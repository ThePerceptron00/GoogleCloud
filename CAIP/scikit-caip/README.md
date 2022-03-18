 ### Scikit Learn Pipelines on AI Platform Training and Serving

 This is an example of how you can train and deploy a model using Google Cloud AI Platform. If you follow the steps below to get this example running. 
 
 
#### Upload the data
You can read data from two different sources:

- CSV file from a GCS bucket: Move the marketing-data.csv file to a bucket in your project. 
- BigQuery Table: [Upload](https://cloud.google.com/bigquery/docs/loading-data) the marketing-data.csv in BigQuery and create a table. 

#### Local Train
First you may want to train the model locally. For this you can use the local-train.sh script. But first you need to open the script and change these parameters:

- pathdata: Path to data (if you are using GCS).
- pathoutput: GCS Bucket to output model.joblib: gs://gcs_path
- storage: Where your data is stored: GCS or BQ. 
- bqtable: The full path to your BigQuery table if your data is in a BQ table: yourproject.dataset.table

Use this command to run the script and make sure that you execute it in the folder where you have the trainer folder. 

    bash local-train.sh

#### Cloud AI Platform Train
If the local train works we can now run training using AI Platform Train. 

Change the paramaters of the script following script caip-train:

- Job_name
- pathdata: Path to data (if you are using GCS)
- pathoutput: GCS Bucket to output model.joblib: gs://gcs_path
- storage: Where your data is stored: GCS or BQ. 
- bqtable: The full path to your BigQuery table if your data is in a BQ table: yourproject.dataset.table

Use this command to run the script and make sure that you execute it in the folder where you have the trainer folder. 

    bash caip-train.sh

#### Local Predict
First try if the local predict works. Use the local-predict.sh script to do a prediction that is executed locally. Change this parameter:

- --model-dir: gs://path_to_your_model  (path to the model.joblib file)

Use this command to run the script and make sure that you execute it in the folder where you have the trainer folder. 

    bash local-predict.sh

You should see something like this:

    INFO: Display format: "default table[no-heading](predictions)"
    [True, True]

#### Create Model AI Platform Prediction
When our training is done we can serve our model on AI Platform serving. 

Use this command to run the script and make sure that you execute it in the folder where you have the trainer folder. 

    bash create-model-caip.sh

Check the console to see if the model is created. 


#### Online prediction
Now you can do an online prediction. You can use the caip-predict.sh for this. Change --version and --model if you used something different then the default setting. Run the script using:

    bash caip-predict.sh

You should see something like this:

    INFO: Display format: "default table[no-heading](predictions)"
    [True, True]