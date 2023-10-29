import streamlit as st

# Function to render the job description input
def get_job_description(current_value):
    return st.text_area("Please describe what you do in your job:", current_value)

# Function to render the task count selector
def get_task_count(current_value):
    return st.selectbox("How many tasks would you like to explore?", list(range(1, 11)), index=current_value-1)

# Function to display the suggested tasks
def display_suggested_tasks(tasks):
    st.subheader("Suggested Tasks for Your Job")
    for i, task in enumerate(tasks, 1):
        st.write(f"{i}. {task}")

# Function to display the generated ideas
def display_ideas(ideas):
    st.subheader("Ideas for Applying Tasks")
    st.markdown(ideas)
