from llm_capabilities import LLM_CAPABILITIES
import openai
import os

api_key = os.environ.get('OPENAI_API_KEY')
openai.api_key = api_key

def get_initial_tasks(job_description):
    messages = [
        {"role": "system", "content": "You are a AI Brainstorm assistant. Before you identify ideas for AI, you need to identify the relevant tasks that a person does in their role. You are provided with a job description by the user. Identify the key tasks that this person typically does in their job, with the AI application in mind. Be succinct"},
        {"role": "user", "content": f"Here's the job description: {job_description}"}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.7,
        max_tokens=500
    )

    initial_tasks = response['choices'][0]['message']['content'].split('\\n')
    return initial_tasks

def get_final_ideas(initial_tasks):
    messages = [
        {"role": "system", "content": "You are an AI Brainstorm assistant. Given the initial tasks, identify what large language model capabilities from this list can help. Then come up with the Top 10 ideas based on these tasks."},
        {"role": "user", "content": f"Initial Tasks: {initial_tasks}\\nLLM Capabilities: {LLM_CAPABILITIES}"}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.7,
        max_tokens=500
    )

    final_ideas = response['choices'][0]['message']['content']
    return final_ideas
