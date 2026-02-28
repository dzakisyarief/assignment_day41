import streamlit as st 

def get_results():

    # st.tabs

    st.header("Results")

    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11= st.tabs([
        "Heatmap",
        "Job Satisfaction Distribution",
        "Average of Job Satisfaction by Gender",
        "Average of Job Satisfaction by Education Level",
        "Average of Job Satisfaction by Have Overtime",
        "Average of Work  Environment by Job Satisfaction",
        "Average of Workload by Job Satisfaction",
        "Average of Sleep Hours by Job Satisfaction",
        "Average of Job Satisfaction by Job Level",
        "Average of Stress Rating by Job Satisfaction",
        "Average of Job Satisfaction by Departement"
    ]) 
    
    with tab1:
        import full_code
        full_code.heatmap()

    with tab2:
        import full_code
        full_code.job_satisfaction_count()

    with tab3:
        import full_code
        full_code.job_satisfaction_gender()

    with tab4:
        import full_code
        full_code.job_satisfaction_edu_level()

    with tab5:
        import full_code
        full_code.job_satisfaction_ot()

    with tab6:
        import full_code
        full_code.job_satisfaction_work_env()


    with tab7:
        import full_code
        full_code.job_satisfaction_workload()


    with tab8:
        import full_code
        full_code.job_satisfaction_sleep_hours()


    with tab9:
        import full_code
        full_code.job_satisfaction_job_level()


    with tab10:
        import full_code
        full_code.job_satisfaction_stress()


    with tab11:
        import full_code
        full_code.job_satisfaction_departement()
        