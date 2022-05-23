# BUILD AND DEPLOY (Median housing value prediction proj)
House Price Prediction.
Predict Median House Value.
Added Docker 

The housing data can be downloaded from https://raw.githubusercontent.com/ageron/handson-ml/master/. The script has codes to download the data. We have modelled the median house value on given housing data. 

The following techniques have been used: 

 - Linear regression
 - Decision Tree
 - Random Forest

 - score:
    - r2
    - rmse
  
## Steps to install image from remote docker repo and run  and test in any local machine.
   Docker helps in building easy and portable application development.
## step l
- newimg is the name of the image
- docker push shankarsreenu/test:newimg (This pulls image from the docker remote repo)
- your image is installed

## step 2
  - Run the command below to run the image and  command prompt will be opened
  - docker run -i -t  newimg  /bin/bash
  
## step3
  - cd HousePricePrediction
  - python3 src/HousePricePrediction/ingest_data.py -h to see argument options.
  - python3 src/HousePricePrediction/ingest_data.py --ingest_data_path INGEST_DATA_PATH --log_level LOG_LEVEL --log_path LOG_PATH --no_console_log
  - python3 src/HousePricePrediction/train.py -h to see argument options.
  - python3 src/HousePricePrediction/train.py  --dataset DATASET --output_model_path OUTPUT_MODEL_PATH --log_level LOG_LEVEL --log_path LOG_PATH --no_console_log
  - python3 src/HousePricePrediction/score.py -h to see argument options.
  - python3 src/HousePricePrediction/score.py --model_folder MODEL_FOLDER --dataset_folder DATASET_FOLDER --output_folder OUTPUT_FOLDER --log_path LOG_PATH
## step 4
 - for functional tests and unit tests 
 - pytest (type pytest on command prompt it automatically detects tests and runs all the tests) 
