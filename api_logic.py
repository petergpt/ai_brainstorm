from llm_capabilities import LLM_CAPABILITIES
import openai
import os

api_key = os.environ.get('OPENAI_API_KEY')
openai.api_key = api_key

def get_initial_tasks(job_description):
    messages = [
        {"role": "system", "content": "You are an AI Brainstorm assistant. Before identifying AI-centric ideas, you need to grasp the key tasks involved in the user's role. You have been given a job description. Identify the key tasks that the person typically does in their job, keeping AI applications in mind. Be succinct"},
        {"role": "user", "content": f"Here's the job description: {job_description}"}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.7,
        max_tokens=500
    )

    response_content = response['choices'][0]['message']['content']
    initial_tasks = response_content.split('\\n') if '\\n' in response_content else [response_content]
    return initial_tasks

def get_refined_tasks(job_description, initial_tasks, user_feedback):
    messages = [
        {"role": "system", "content": "You are an AI Brainstorm assistant. Refine the initial set of tasks based on the user's feedback."},
        {"role": "user", "content": f"Initial Tasks: {initial_tasks}\\nFeedback: {user_feedback}"}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.7,
        max_tokens=500
    )

    response_content = response['choices'][0]['message']['content']
    refined_tasks = response_content.split('\\n') if '\\n' in response_content else [response_content]
    return refined_tasks

def get_final_ideas(refined_tasks):
    messages = [
        {"role": "system", "content": "You are an AI Brainstorm assistant. Given the refined tasks, identify the large language model capabilities that can assist and come up with the Top 10 ideas."},
        {"role": "user", "content": f"Refined Tasks: {refined_tasks}\\nLLM Capabilities: {LLM_CAPABILITIES}"}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.7,
        max_tokens=500
    )

    final_ideas = response['choices'][0]['message']['content']
    return final_ideas
