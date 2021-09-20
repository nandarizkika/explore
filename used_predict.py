import pickle
import numpy as np
import pandas as pd

#Format Input
input_data={
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
#   'loan_status_predict': 0,
#   'loan_status_proba': 0.013454122468829155
  }

with open('model/woe-1.0.0.pkl', 'rb') as f: 
    preprocess= pickle.load(f)

with open('model/model-LR-1.0.0.pkl', 'rb') as f: 
    model= pickle.load(f)

def formatting(input_data):
    """ 
    preprocess input data 
    """

    input_data = pd.DataFrame.from_dict(input_data, orient='index').T.replace({
        None: np.nan,
        "null":np.nan,
        "" : np.nan
    })
    return input_data

def preprocessing(input_data):
 for feature, woe_info in preprocess.items():
    input_data[f'{feature}_WOE'] = pd.cut(input_data[feature], bins=woe_info['binning'], labels=woe_info['labels'])
    input_data[f'{feature}_WOE'] = input_data[f'{feature}_WOE'].values.add_categories('Nan').fillna('Nan') 
    input_data[f'{feature}_WOE'] = input_data[f'{feature}_WOE'].replace('Nan', woe_info['nan'])
    input_data[f'{feature}_WOE'] = input_data[f'{feature}_WOE'].astype(float)
    input_data.drop(columns = f'{feature}', inplace=True)
        
 return input_data

def make_predictions(input_data):
    """ 
    Make your final prediction here
    """
    # Model Predictions
    result = model.predict_proba(preprocessing(formatting(input_data)))[:, 1]
    return result 