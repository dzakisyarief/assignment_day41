import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 

pd.set_option("display.max_columns", None)

df = pd.read_csv("assignment_employee_survey.csv")

# Total Row and Columns
total_row = df.shape[0]
total_columns = df.shape[1]

print("Dataset Rows:", total_row)
print("Dataset Columns:", total_columns)

# Describe
df.describe()

# Value Counts per columns
# for columns in df.columns:
#   print(f"Value Counts in {columns}")
#   display(df[columns].value_counts())

# Data Cleaning

# Check for missing value
df.isna().sum()

# check for duplicate through employee id (unique values)
df[df.duplicated(['emp_id'], keep = 'first')].sort_values(by = 'emp_id')

# find negative value in numeric columns
numeric_columns = df.select_dtypes(include=['int64','float64']).columns

for column_name in numeric_columns:
  print(f"=== {column_name} ===")
  print((df[column_name] < 0).value_counts())
  print()

# Heatmap

# filter new dataset without employee id column since it wont give any insight for matrix correlation
df_corr = df.drop(columns='emp_id')
df_corr.head()

def heatmap():
  corr = df_corr.select_dtypes(include=['int64','float64']).corr()
  corr
  # plt.figure(figsize=(14,12))
  fig, ax = plt.subplots(figsize=(14,12))
  sns.heatmap(corr, ax=ax, annot=True, fmt=".2f", cmap='coolwarm', linewidths=0.25, square=True)
  st.pyplot(fig)
  st.write("Job Satisfaction is negatively correlate with:")
  st.markdown(
    """
    * Age
    * Experience
    * Workload
    * Stress
    * Number of Companies
    * Number of Reports
    * Training per Year
    """
  )

def job_satisfaction_count():
  job_satisfaction_count = df['job_satisfaction'].value_counts().reset_index()
  st.bar_chart(job_satisfaction_count, horizontal = True, x_label = "Total", y_label = "Job Satisfaction", width=500)
  st.write("The rating with the most people categorized is rating 4 with 40.74%, followed by rating 3 (18.76%) and rating 5 (17.28%).")

def job_satisfaction_gender():
  job_satisfaction_mean_gender = df.groupby('gender')['job_satisfaction'].mean().round(2).reset_index()
  st.bar_chart(job_satisfaction_mean_gender,x ='gender',x_label = 'Gender', width = 300, height = 400, color ='#D63D22')
  st.write('The average job satisfaction for Female (3.39) and Male 3.37) is relatively the same with')

def job_satisfaction_edu_level():
  job_satisfaction_mean_edu = df.groupby('edu_level')['job_satisfaction'].mean().round(2).reset_index()
  st.bar_chart(job_satisfaction_mean_edu, x='edu_level', y_label ='Average of Job Satisfaction', x_label='Education Level',color ='#4f6f73', width=500)
  st.markdown(
    """
    * The highest average job satisfaction rating is from Master degree with 3.73 rating, followed by Highschool (3.43) and Bachelor (3.34)
    * PhD has the lowest job satisfaction score with 2.93
    """
  )

def job_satisfaction_ot():
  job_satisfaction_mean_ot = df.groupby('have_ot')['job_satisfaction'].mean().round(2).reset_index()
  st.bar_chart(job_satisfaction_mean_ot, x='have_ot', x_label = "Have Overtime",y_label = 'Average of Job Satisfaction',width = 300, height = 500, color = '#c48a8f')
  st.write('The average for people who don’t have overtime (3.51) is higher than people with overtime (3.09)')

def job_satisfaction_work_env():
  job_satisfaction_mean_work_env = df.groupby('job_satisfaction')['work_env'].mean().round(2).reset_index()
  st.bar_chart(job_satisfaction_mean_work_env, x='job_satisfaction', x_label = 'Job Satisfaction', y_label = 'Average of Work Environment',color ='#6A397D', width=500)
  st.markdown(
    """
    * The average work life balance for the rating 1 in job satisfaction is the lowest (2.24) compared to other rating
    * The highest average for work life balance is from people with job satisfaction rating 5 (3.45), followed by rating 4 (3.26), and rating 2 (3.30)
    """
  )

def job_satisfaction_workload():
  job_satisfaction_mean_workload = df.groupby('job_satisfaction')['workload'].mean().round(2).reset_index()
  st.bar_chart(job_satisfaction_mean_workload, x='job_satisfaction',x_label='Job Satisfaction', y_label='Average of Workload',color='#298F8D', width=500)
  st.markdown(
    """
    * Employees with the most workload (3.80) have the lowest job satisfaction rating
    * Conversely, employees with the lowest workload (2.62) have the highest job satisfaction rating
    """
  )

def job_satisfaction_sleep_hours():
  job_satisfaction_mean_sleephours = df.groupby('job_satisfaction')['sleep_hours'].mean().round(2).reset_index()
  st.bar_chart(job_satisfaction_mean_sleephours, x='job_satisfaction',x_label='Average of Sleep Hours',y_label='Average of Sleep Hours',color='#84856B', width=500)
  st.markdown(
    """
    * Employees with the lowest average sleep hours (6.6 hours) also have the lowest job satisfaction rating
    * Conversely, employees with the highest average sleep hours have the the highest job satisfaction rating
    """
  )

def job_satisfaction_job_level():
  job_satisfaction_mean_job_level = df.groupby('job_level')['job_satisfaction'].mean().round(2).reset_index()
  st.bar_chart(job_satisfaction_mean_job_level, x='job_level',x_label='Job Level',y_label='Average of Job Satisfaction',color='#7481AD', width = 500)
  st.write('There are no significant difference on average job satisfaction rating across job level, with the highest in job level mid (3.41)')

def job_satisfaction_stress():
  job_satisfaction_mean_stress = df.groupby('job_satisfaction')['stress'].mean().round(2).reset_index()
  st.bar_chart(job_satisfaction_mean_stress,x='job_satisfaction',x_label='Job Satisfaction',y_label='Average of Stress Rating',color = '#B55507',width=500)
  st.write('Employees with the highest stress rating (2.28) are from employees with the lowest job satisfaction rating')

def job_satisfaction_departement():
  job_satisfaction_mean_departement = df.groupby('dept')['job_satisfaction'].mean().round(2)
  index1 = job_satisfaction_mean_departement.index
  st.bar_chart(job_satisfaction_mean_departement, horizontal=True,y_label='Departement',x_label='Average of Job Satisfaction',color='#9E9898', width=500)
  st.markdown(
    """
    * Employees from the IT department have thelowest average job satisfaction, with 3.29 rating
    * Employees with the highest average job satisfaction rating are from Sales department (3.48), followed by Operations (3.46) and Finance (3.42)
    """
  )
  