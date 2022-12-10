#simple table join using same key
import pandas as pd
left_df = pd.DataFrame({'ID': ['1','2','3','4'],'ProjectName': ['test1', 'test2', 'test3', 'test4'],})
right_df = pd.DataFrame({'ProjectID': ['2','1','3','4'], 'Division': ['IT', 'Finance', 'HR', 'Executive'],})
a = left_df.merge(right_df, left_on='ID', right_on='ProjectID', how='left')

print(a)