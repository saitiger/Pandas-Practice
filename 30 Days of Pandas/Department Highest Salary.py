import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    return employee.merge(department,left_on='departmentId',right_on='id',how='inner').groupby('departmentId').apply(lambda x : x[x['salary']==x['salary'].max()])[['name_y','name_x','salary']].rename(columns={'name_y':'Department','name_x':'Employee','salary':'Salary'})
    
