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



`input format` (raw - JSON):
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


`expected output format`:
<pre> 
{
    "model": "credit-risk-scoring-by-rizkika",
    "result": 0.9790118485748639,
    "result_status": "Resiko Tinggi",
    "version": "beta-version-1.0.0"
}
 </pre> 

`HTTP method rule`:
- http://127.0.0.1:5000/predict using 'POST'
