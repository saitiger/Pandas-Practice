import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # return employees.assign(
        # bonus=employees.apply(lambda x: x['salary'] if int(x['employee_id']) % 2 != 0 and not x['name'].startswith('M') else 0, axis=1)
    # )[['employee_id', 'bonus']].sort_values(
        # by='employee_id',)
    emp_id = employees[(employees['employee_id']%2!=0)&(~employees['name'].str.startswith('M'))]['employee_id']
    return employees.assign(bonus = employees.apply(lambda x: x['salary'] if x['employee_id'] in emp_id else 0,axis = 1)).sort_values(by = 'employee_id')[['employee_id','bonus']]
