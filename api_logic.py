from llm_capabilities import LLM_CAPABILITIES
import openai
import os

# Fetch API Key from environment variables
api_key = os.environ.get('OPENAI_API_KEY')

# Initialize OpenAI API
openai.api_key = api_key

# API call to GPT-4 for generating relevant tasks
def get_relevant_tasks(job_description, n_tasks=5):
    messages = [
        {"role": "system", "content": f"You are provided with a job description by the user.. You need to first break out the job description into the possible set of tasks where large language models can be helpful. Then you need to You need to come up with different tasks that this job might involve and evaluate it against the capabilities of a large language model. Here is the job description: "},
        {"role": "user", "content": f"Given the job description, what large language model capabilities from this list can help me? {LLM_CAPABILITIES}"}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.7,
        max_tokens=500
    )
    
    # Assuming the response contains a list of relevant tasks. This part should be updated based on the actual response structure.
    relevant_tasks = response['choices'][0]['message']['content']
    return relevant_tasks

# API call to GPT-4 for generating ideas for the tasks
def get_task_ideas(job_description, selected_tasks):
    messages = [
        {"role": "system", "content": f"Here are the relevant LLM capabilities that would be helpful for the role: {selected_tasks}. Come up with some specific ideas that would be suitable. Please format them in Markdown."},
        {"role": "user", "content": "Could you provide me with specific ideas?"}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.7,
        max_tokens=500
    )
    
    # Extract and return the ideas in Markdown table format
    return response['choices'][0]['message']['content']
