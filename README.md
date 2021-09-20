# Credit Risk Exercise
## Dataset Information
by using dataset `credit_risk_dataset.csv` from repository `data/`, a prediction will be made to determine credit risk classification.

The dataset contains `32518 rows` and `12 features` for predictions. It also contains `165 duplicated rows` and will be removed in the early step of preprocessing with the feature explanation will be presented below:

|Field|	Description|	Value|
| --- | --- | --- |
|person_age	|Age.	|Integer|
|person_income	|Annual Income.|	Integer|
|person_home_ownership	|Home ownership.	|'RENT', 'MORTGAGE', 'OWN', or 'OTHER'|
|person_emp_length|	Employment length (in years)	|Integer|
|loan_intent	|Loan intent.|	'PERSONAL', 'EDUCATION', 'MEDICAL', 'VENTURE', 'HOMEIMPROVEMENT', or 'DEBTCONSOLIDATION'|
|loan_grade|	Loan grade.|	'A', 'B', 'C, 'D', 'E', 'F', or 'G'|
|loan_amnt|	Loan amount.|	Integer|
|loan_int_rate|	Interest rate.	|Float|
|loan_percent_income	|Percent income.|	Float|
|cb_person_default_on_file	|Historical default.|	'Y', or 'N'|
|cb_person_cred_hist_length	|Credit history length.	|Integer|

## Handling Missing Values
- There are two columns with missing values, `loan_int_rate` and `person_emp_length`
- This model will use Weight of Evidence (WOE) as a method for handling missing value
- The missing value will return to specific values based on Weight of Evidence and Information Value Results

## Handling Outlier
- Outlier will be handlel by using Weight of Evidence (WOE) too
- The WOE Features will be a new columns which is needed as a monotonic features, one of requirements of logistic regression model
- The original features will be dropped from the dataset to prevent multicolinearity in the model

## Model Evaluation
![image](https://user-images.githubusercontent.com/66078743/133960406-68326636-c3bd-4917-b152-bf4f58b448e9.png)

Actually, using xgboost will produce a better result. But, it will be hard to translate and present the model to business teams, so logistic regression with Weight of Evidence could be the answer and can be presented using score card method. Furthermore, the results from Logistic Regression is also as good as using XGBoost

## Input Format (raw - JSON)
<pre> 
{
    'person_age': 21,
    'person_income': 9600,
    'person_home_ownership': "OWN",
    'person_emp_length': 5.0,
    'loan_intent': "PERSONAL",
    'loan_grade': "D",
    'loan_amnt': 35000,
    'loan_int_rate': 16.02,
    'loan_percent_income': 0.59,
    'cb_person_default_on_file': "Y",
    'cb_person_cred_hist_length': 3,
}
 </pre> 

expected test proba result from above input: .97901185


## Expected Output Format:
<pre> 
{
    "model": "credit-risk-scoring-by-rizkika",
    "result": 0.9790118485748639,
    "result_status": "Resiko Tinggi",
    "version": "beta-version-1.0.0"
}
 </pre> 

## HTTP Method Rule:
- http://127.0.0.1:5000/predict using 'POST'
