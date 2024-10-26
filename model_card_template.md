# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
The model is a RandomForest classifier model from SciKit-Learn. It is used for binary classification and is trained on census data to predict income level above or below $50,000

## Intended Use
This model is intended to be used for educational purposes so I can learn about the deployment of an ML pipeline. It is used to predict whether or not an individual makes more or less that $50k based on demographic data.

## Training Data
The census data was obtained from Udacity through UC Irvine ML repository at https://archive.ics.uci.edu/dataset/20/census+income on 26 October 2024. 

The dataset consists of 14 features and over 48,842 rows.

## Evaluation Data
The data was split on an 80/20 split using test_train_split from sklearn. Both datasets were processed in the same way using the same function to aid in maintaining consistancy in evaluation. 

## Metrics
_Please include the metrics used and your model's performance on those metrics._
The following metrics were used in the model evaluation:
Precision - percentage of correct positive predictions over all positive predictions  
Recall - Percentage of actual positive predictions made by the model
F1 Score - Balanced version of precision and recall. This can be a more accurate measure of the models performance.

Precision: 0.7405
Recall: 0.6340
F1: 0.6831

## Ethical Considerations
This data is demographic data from a census. As such it could contain sensitive information which should be protected. In addition, there is also the potential for bias based on the information collection and reporting methods. If the data was only collected electronically, then the data could be skewed to only people who have a means to enter that data. We would be missing the portion of the population who don't have the ability to participate since they don't have computers. 

## Caveats and Recommendations
This is only a toy model and trained/developed for demonstration purposes. 
Though there is the potential for bias in the data, I do not currently have the means to evaluate or correct that bias. 
As new census data is collected information may change and the model could require updating.