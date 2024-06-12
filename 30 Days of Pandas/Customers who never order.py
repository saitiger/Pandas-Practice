import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # merged = customers.merge(orders,left_on='id',right_on='customerId',how='left')
    # return merged[merged['customerId'].isna()][['name']].rename(columns={'name':'Customers'})
    return customers[~customers['id'].isin(orders['customerId'])][['name']].rename(columns={'name':'Customers'})
