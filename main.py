import streamlit as st
from api_logic import get_initial_tasks, get_refined_tasks, get_final_ideas

def main():
    st.title("Optimize Your Job with AI")

    if 'job_description' not in st.session_state:
        st.session_state.job_description = ''
    if 'user_feedback' not in st.session_state:
        st.session_state.user_feedback = None
    if 'initial_tasks' not in st.session_state:
        st.session_state.initial_tasks = []
    if 'refined_tasks' not in st.session_state:
        st.session_state.refined_tasks = []
    if 'final_ideas' not in st.session_state:
        st.session_state.final_ideas = ''

    job_description = st.text_area("Please describe what you do in your job:", st.session_state.job_description)

    if st.button("Identify Tasks"):
        with st.spinner('Identifying tasks...'):
            st.session_state.initial_tasks = get_initial_tasks(job_description)
        st.subheader("Suggested Tasks for Your Job")
        for i, task in enumerate(st.session_state.initial_tasks, 1):
            st.write(f"{i}. {task}")

        user_feedback = st.text_area("Provide your feedback on the tasks (optional):", st.session_state.user_feedback)
        st.session_state.user_feedback = user_feedback if user_feedback else 'No feedback provided.'

        if st.button("Refine Tasks"):
            with st.spinner('Refining tasks based on your feedback...'):
                st.session_state.refined_tasks = get_refined_tasks(job_description, st.session_state.initial_tasks, st.session_state.user_feedback)
            st.subheader("Refined Tasks for Your Job")
            for i, task in enumerate(st.session_state.refined_tasks, 1):
                st.write(f"{i}. {task}")

    if st.session_state.refined_tasks and st.button("Generate Ideas"):
        with st.spinner('Generating ideas...'):
            st.session_state.final_ideas = get_final_ideas(st.session_state.refined_tasks)
        st.subheader("Ideas for Applying Tasks")
        st.markdown(st.session_state.final_ideas)

if __name__ == "__main__":
    main()
