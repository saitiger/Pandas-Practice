import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    # low = accounts[accounts.income < 20000].shape[0]
    # average = accounts[(accounts.income >= 20000) & (accounts.income <=50000)].shape[0]
    # high = accounts[accounts.income > 50000].shape[0]
    # data  = {'category': ['Low Salary','Average Salary','High Salary'],
    #         'accounts_count':[low, average, high]}
    # df = pd.DataFrame(data)
    # return df

    def salary_def(i):
        if i<20000:
            res = "Low Salary"
        elif i>=20000 and i<=50000:
            res = "Average Salary"
        else :
            res = "High Salary"
        return res
    
    accounts['category'] = accounts['income'].apply(salary_def)
    df = accounts.groupby('category')['account_id'].count().reset_index().rename(columns={'account_id':'accounts_count'})
    
