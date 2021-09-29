import pandas as pd
import numpy as np

columns = ['job_title','Company', 'working_place','website', 'posted_time', 'working_type', 'job_description']
data = pd.read_csv('job_list.csv', names=columns, index_col=False)

#parsing job_descriptions.

data['big_data'] = data['job_description'].apply(lambda x: 1 if 'big data' in x.lower() else 0)
data['analysis'] = data['job_description'].apply(lambda x: 1 if 'analysis' in x.lower() else 0)
data['data_visualization'] = data['job_description'].apply(lambda x: 1 if 'visualization' in x.lower() else 0)
data['Hadoop'] = data['job_description'].apply(lambda x: 1 if 'hadoop' in x.lower() else 0)
data['Database'] = data['job_description'].apply(lambda x: 1 if 'database' in x.lower() else 0)
data['Apache'] = data['job_description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
#data['r_studio'] = data['job_description'].apply(lambda x: 1 if 'r-studio' in x.lower() else 0)
#parsing the posted_time

data.to_csv('jobs_data_cleaned.csv', index=False)
test = pd.read_csv('jobs_data_cleaned.csv')
