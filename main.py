import streamlit as st
from api_logic import get_initial_tasks, get_final_ideas

st.set_page_config(
    page_title="AI to Brainstorm AI tasks",
    page_icon=":robot_face:",
)

def main():
    st.title("How can you apply LLMs to your job?")

    if 'job_description' not in st.session_state:
        st.session_state.job_description = ''
    if 'initial_tasks' not in st.session_state:
        st.session_state.initial_tasks = []
    if 'final_ideas' not in st.session_state:
        st.session_state.final_ideas = ''

    job_description = st.text_area("Please describe what you do in your job:", st.session_state.job_description)

    if st.button("Identify Tasks and Generate AI Ideas"):
        with st.spinner('Step 1: Identifying tasks based on your job description...'):
            st.session_state.initial_tasks = get_initial_tasks(job_description)

        st.subheader("Suggested Tasks for Your Job")
        for i, task in enumerate(st.session_state.initial_tasks, 1):
            st.write(f"{i}. {task}")

        with st.spinner('Step 2: Generating AI ideas based on the identified tasks...'):
            st.session_state.final_ideas = get_final_ideas(st.session_state.initial_tasks)

        st.subheader("Ideas for Applying Tasks")
        st.markdown(st.session_state.final_ideas)

st.markdown("Built by Peter Gostev(https://www.linkedin.com/in/peter-gostev-53058417/)")

if __name__ == "__main__":
    main()
