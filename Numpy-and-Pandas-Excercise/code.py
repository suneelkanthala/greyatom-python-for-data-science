# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here
bank = pd.read_csv(path)

categorical_var = bank.select_dtypes(include = 'object')
#print(categorical_var)
print(categorical_var.shape)
numerical_var = bank.select_dtypes(include = 'number')
#print(numerical_var)
print(numerical_var.shape)

# STEP 2
banks = bank.drop(['Loan_ID'],axis = 1)
#print(banks.isnull().sum())
bank_mode = banks.filter(['Gender','Married','Dependents','Self_Employed','LoanAmount','Loan_Amount_Term','Credit_History']).mode()
#print(bank_mode)
banks[['Gender','Married','Dependents','Self_Employed','LoanAmount','Loan_Amount_Term','Credit_History']] = banks[['Gender','Married','Dependents','Self_Employed','LoanAmount','Loan_Amount_Term','Credit_History']].fillna(value = bank_mode.iloc[0])
print(banks.shape)
print(banks.isnull().sum().values.sum())


# STEP 3
avg_loan_amount = pd.pivot_table(banks, values = 'LoanAmount', index = ['Gender','Married','Self_Employed'], aggfunc = np.mean)
print(round(avg_loan_amount['LoanAmount'][1],2))

# STEP 4
loan_approved_se = banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')]
#print(loan_approved_se)

loan_approved_nse = banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')]
#print(loan_approved_nse)

percentage_se = round((len(loan_approved_se)/len(banks)) * 100,2)
percentage_nse = round((len(loan_approved_nse)/len(banks)) * 100,2)
print(percentage_nse,percentage_se)

# STEP 5
loan_term = banks['Loan_Amount_Term'].apply(lambda x: x / 12)
big_loan_term = len(loan_term[loan_term >= 25])
#big_loan_term = len(loan_term[loan_term['Loan_Amount_Term'] > 25])
print(big_loan_term)

# STEP 6
loan_groupby = banks.groupby('Loan_Status')[['ApplicantIncome', 'Credit_History']]
mean_values = loan_groupby.mean()
print(mean_values)




















