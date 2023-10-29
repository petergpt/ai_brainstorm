import streamlit as st
from api_logic import get_initial_tasks, get_final_ideas

def main():
    st.title("Optimize Your Job with AI")

    if 'job_description' not in st.session_state:
        st.session_state.job_description = ''
    if 'initial_tasks' not in st.session_state:
        st.session_state.initial_tasks = []
    if 'final_ideas' not in st.session_state:
        st.session_state.final_ideas = ''

    job_description = st.text_area("Please describe what you do in your job:", st.session_state.job_description)

    if st.button("Identify Tasks"):
        with st.spinner('Identifying tasks...'):
            st.session_state.initial_tasks = get_initial_tasks(job_description)
        st.subheader("Suggested Tasks for Your Job")
        for i, task in enumerate(st.session_state.initial_tasks, 1):
            st.write(f"{i}. {task}")

    if st.session_state.initial_tasks and st.button("Generate Ideas"):
        with st.spinner('Generating ideas...'):
            st.session_state.final_ideas = get_final_ideas(st.session_state.initial_tasks)
        st.subheader("Ideas for Applying Tasks")
        st.markdown(st.session_state.final_ideas)

if __name__ == "__main__":
    main()
