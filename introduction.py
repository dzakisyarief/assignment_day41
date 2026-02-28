import streamlit as st 

def introduction():
    
    # Data Intro
    st.header("Introduction")
    st.markdown("Dataset: [Employee Survey](https://www.kaggle.com/datasets/lainguyn123/employee-survey)")
    st.write("The purpose of this analysis is to fund the factor that correlates with job satisfaction")
    st.markdown("""
    * Sleeping Hours
    * Stress 
    * Work Environment
    * etc. """)

    # Data Understanding

    st.header("Data Understanding")
    st.write("There are There are 2766 rows with 23 columns which include information about:")
    st.markdown(
        """ 
        * EmpID: Unique identifier for each employee.
        * Gender: Gender of the employee (e.g., Male, Female, Other).
        * Age: Age of the employee.
        * MaritalStatus: Marital status of the employee (e.g., Single, Married, Divorced, Widowed).
        * JobLevel: Job level of the employee (e.g., Intern/Fresher, Junior, Mid, Senior, Lead).
        * Experience: Number of years of work experience the employee has.
        * Dept: Department where the employee works (e.g., IT, HR, Finance, Marketing, Sales, Legal, Operations, Customer Service).
        * EmpType: Type of employment (e.g., Full-Time, Part-Time, Contract).
        * WLB: Work-life balance rating (scale from 1 to 5).
        * WorkEnv: Work environment rating (scale from 1 to 5).
        * PhysicalActivityHours: Number of hours of physical activity per week.
        * Workload: Workload rating (scale from 1 to 5).
        * Stress: Stress level rating (scale from 1 to 5).
        * SleepHours: Number of hours of sleep per night.
        * CommuteMode: Mode of commute (e.g., Car, Public Transport, Bike, Walk, Motorbike).
        * CommuteDistance: Distance traveled during the commute (in kilometers).
        * NumCompanies: Number of different companies the employee has worked for.
        * TeamSize: Size of the team the employee is part of.
        * NumReports: Number of people reported to by the employee (only applicable for Senior and Lead levels).
        * EduLevel: Highest level of education achieved by the employee (e.g., High School, Bachelor, Master, PhD).
        * haveOT: Indicator if the employee has overtime (True/False).
        * TrainingHoursPerYear: Number of hours of training received per year.
        * JobSatisfaction	Rating of job satisfaction (scale from 1 to 5).
            """
    )
    # Data Preprocessing
    st.subheader("Data Preprocessing")
    st.write("Data Preprocessing Includes: ")
    st.markdown(
        """
        * Check for duplicate data for each row
        * Check for missing value
        * Check for negative values in numerical data category
        * Result visualization
        """
    )

    st.subheader("Final Dataset")
    st.write("The final dataset obtained: **2766 rows with 23 columns**")
    