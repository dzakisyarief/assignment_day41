import streamlit as st 

def get_summary(): 

    # Conclusion

    st.subheader("Conclusion")
    st.markdown(
        """
        * There are no correlation between Job Satisfaction with Age, Experience, Physical Activity Hours, Workload, Stress, Number of Companies, Number of Reports, and Training Hours per Year since it shows negative correlation in the heatmap visualization
        * Employees with PhD education level has the lowest job satisfaction
        * Employees with overtime have lower job satisfaction than employee without job satisfaction
        * Employees with the lowest Work Environment Quality and sleep quality have the lowest job satisfaction
        * Employees with the most workload and the highest stress rating have the lowest job satisfaction
        * Employees from IT department have the lowest job satisfaction rating
        * There are no significant difference in job satisfaction rating across gender and job level
        """
    )

    # Recommendation

    st.subheader("Recommendation")
    st.markdown(
        """
        * Provide support to employee with PhD level to increase their job satisfaction rating
        * Provide bonus or incentive to employees doing overtime
        * Improve the work environment quality by giving amenities, doing activity outside of work to create more bonding experience among employees
        * Provide support for employees with high stress rating and workload as well as employees with low work-life balance and sleep hours
        """
    )
      