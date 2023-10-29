import streamlit as st
from api_logic import get_relevant_tasks, get_task_ideas
from ui_components import get_job_description, get_task_count, display_suggested_tasks, display_ideas

def main():
    st.title("Optimize Your Job with AI")
    
    job_description = st.session_state.get('job_description', '')
    n_tasks = st.session_state.get('n_tasks', 5)
    
    st.session_state['job_description'] = get_job_description(job_description)
    st.session_state['n_tasks'] = get_task_count(n_tasks)
    
    if st.button("Generate Ideas"):
        with st.spinner('Generating ideas...'):
            try:
                relevant_tasks = get_relevant_tasks(st.session_state['job_description'], st.session_state['n_tasks'])
                display_suggested_tasks(relevant_tasks)
                task_ideas = get_task_ideas(st.session_state['job_description'], relevant_tasks)
                display_ideas(task_ideas)
            except Exception as e:
                st.error(f"Something went wrong: {e}")

if __name__ == "__main__":
    main()
