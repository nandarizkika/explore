by using dataset 'credit_risk_dataset.csv' from repository 'data/', a prediction will be made to determine credit risk classification

input format (raw - JSON):
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


expected output format:
<pre> 
{
    "model": "credit-risk-scoring-by-rizkika",
    "result": 0.9790118485748639,
    "result_status": "Resiko Tinggi",
    "version": "beta-version-1.0.0"
}
 </pre> 

HTTP method rule:
- http://127.0.0.1:5000/predict using 'POST'
