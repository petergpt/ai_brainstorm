import streamlit as st
from api_logic import get_initial_tasks, get_refined_tasks, get_final_ideas

def main():
    st.title("Optimize Your Job with AI")

    job_description = st.session_state.get('job_description', '')
    user_feedback = st.session_state.get('user_feedback', None)
    initial_tasks = st.session_state.get('initial_tasks', [])
    refined_tasks = st.session_state.get('refined_tasks', [])

    job_description = st.text_area("Please describe what you do in your job:", job_description)
    st.session_state['job_description'] = job_description

    if st.button("Identify Tasks"):
        initial_tasks = get_initial_tasks(st.session_state['job_description'])
        st.session_state['initial_tasks'] = initial_tasks
        st.subheader("Suggested Tasks for Your Job")
        for i, task in enumerate(initial_tasks, 1):
            st.write(f"{i}. {task}")

        user_feedback = st.text_area("Provide your feedback on the tasks (optional):", user_feedback)
        st.session_state['user_feedback'] = user_feedback if user_feedback else None

        if st.button("Refine Tasks"):
            refined_tasks = get_refined_tasks(st.session_state['job_description'], initial_tasks, st.session_state['user_feedback'])
            st.session_state['refined_tasks'] = refined_tasks
            st.subheader("Refined Tasks for Your Job")
            for i, task in enumerate(refined_tasks, 1):
                st.write(f"{i}. {task}")

            if st.button("Generate Ideas"):
                final_ideas = get_final_ideas(refined_tasks)
                st.subheader("Ideas for Applying Tasks")
                st.markdown(final_ideas)

if __name__ == "__main__":
    main()
