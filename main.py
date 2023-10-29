import streamlit as st
from api_logic import get_initial_tasks, get_refined_tasks, get_final_ideas

def main():
    st.title("Optimize Your Job with AI")

    # Step 1: User inputs their job description
    job_description = st.text_area("Please describe what you do in your job:", "")
    if st.button("Identify Tasks"):
        with st.spinner('Identifying tasks...'):
            try:
                initial_tasks = get_initial_tasks(job_description)
                st.subheader("Identified Tasks for Your Job")
                for i, task in enumerate(initial_tasks, 1):
                    st.write(f"{i}. {task}")

                # Step 3: User provides feedback
                user_feedback = st.text_area("Provide feedback to amend the tasks:", "")

                if st.button("Generate Ideas"):
                    with st.spinner('Generating ideas...'):
                        try:
                            # Step 4: Get refined set of tasks based on feedback
                            refined_tasks = get_refined_tasks(job_description, initial_tasks, user_feedback)

                            # Step 5: Get final set of ideas based on refined tasks
                            final_ideas = get_final_ideas(refined_tasks)
                            st.subheader("Top 10 Ideas for Your Job")
                            st.markdown(final_ideas)
                        except Exception as e:
                            st.error(f"Something went wrong: {e}")
            except Exception as e:
                st.error(f"Something went wrong: {e}")

if __name__ == "__main__":
    main()
