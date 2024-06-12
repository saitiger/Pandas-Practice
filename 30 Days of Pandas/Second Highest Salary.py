import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee.drop_duplicates(subset = 'salary', keep = 'first', inplace = True)
    employee['sal_rnk'] = employee['salary'].rank(method='min',ascending = False)
    employee.rename(columns={'salary':'SecondHighestSalary'},inplace = True)
    if employee.shape[0]<2:
        return pd.DataFrame({column:[None]})    
    else :
        return employee[employee['sal_rnk']==2][['SecondHighestSalary']]
