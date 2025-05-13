<h1>Credit card fraud simulator</h1>

# table of contents
[Introduction](#introduction)

[Pipeline](#Pipeline)

[Dataset](#dataset)

[Fraud Detection Classifier](#classifier)


## Introduction
<p>This project is simulates credit card transactions, detects fraudulent cases by
using a trained ml-model and displays
various related metrics to an interactive dashboard; mainly, the geographical location of the
transaction,transaction category, amount and fraud status. The aforementioned is achieved by the use of an apache
air-flow pipeline in conjunction with docker.Furthermore, the dashboard shows metrics for predicted fraud,
actual fraud, false positives and false negatives.
 <p>

## Pipeline

![Alt text](pipeline.png)

This project uses the medallion architecture for its pipeline. credit card transaction info is simulated by reading
one line at a time from a csv file. Afterwards the transaction is stored into a log, whilst a copy is transformed and fed into the 
fraud classifier. Then the result of the fraud classifier is combined with the stored transaction log and pushed into
a postgres database. Finally a dash dashboard application will read and display data from the database. 

----------------------------------

## Dataset
the credit card transaction **[dataset](https://www.kaggle.com/datasets/priyamchoksi/credit-card-transactions-dataset)** is
taken from kaggle. It consists of over 20 variables, including credit card holder information (name, credit card number,
job/profession,...etc). the data set contains 1.3 million transactions, where 7506 of them are fraudulent. After removing
all rows with at least one missing value in one of its columns, the total size shrunk to 1.1 million transactions.
For practical reasons, the simulated data stream will consist of a total of 5000 credit card transactions, having a 
80/20 legitimate to fraud ratio.



## Classifier
<p> xgboost was used to create the fraud detection classifier. The reason
for this is due to the fact that it is fairly simple to implement,
while providing lower variance (therefore being more accurate) compared
to other classifier models like logistic regression or random forest. <p>

the training set consisted of 1.1 million credit card transactions, whereas the testing set had 220 thousand transactions,
yielding a 80/20 train/test split 

A learning rate of 0.1 yielded the best results in terms of model 
adequacy. Fraudulent transactions were coded as "0", while legitimate transactions were coded as "1". </p>



**XGBoost classification report**

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0.0   | 1.00      | 1.00   | 1.00     | 218,838 |
| 1.0   | 0.88      | 0.64   | 0.74     | 1,303   |



**confusion matrix**

|               | Predicted 0 | Predicted 1 |
|---------------|-------------|-------------|
| Actual 0      | 218,728     | 110         |
| Actual 1      | 469         | 834         |

Unsurprisingly, the precision and recall for legitimate transactions are 1, which makes sense since the event of
fraud is so rare.  