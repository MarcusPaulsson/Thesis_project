# This file contains all strings for concatenating the prompt templates around the tasks. 
# Both system prompt and extra context prompts



# Prompt template concatenation for the different models:
''' 
# ChatGPT Format
messages = [
    {"role": "system", "content": prompt.SYSTEM_PROMPT},
    {"role": "user", "content": prompt.TAIL_PROMPT+task_prompt+prompt.TAIL_PROMPT}
],

# Gemini Format
system_prompt = prompt.SYSTEM_PROMPT #or some other system prompt.
user_prompt = system_prompt + prompt.HEAD_PROMPT + task_prompt + prompt.TAIL_PROMPT
'''



# Zero-shot prompting
'''
PROMPT_TECHNIQUE_SETTING = "Zero-shot" # placeholder for storing content to correct result directory

SYSTEM_PROMPT="",
HEAD_PROMPT = ""
TAIL_PROMPT=" Give only the code, no test cases."

'''
# Zero-shot Chain of thougths
'''
PROMPT_TECHNIQUE_SETTING = "Zero-shot-CoT" 

SYSTEM_PROMPT="Solve the following task step by step."
HEAD_PROMPT = ""
TAIL_PROMPT="Give only the code."
'''


# Role prompting (Expert)
'''
PROMPT_TECHNIQUE_SETTING = "Expert-role" 

SYSTEM_PROMPT="You are an expert software developer, skilled in producing clean and well-structured code."
HEAD_PROMPT = ""
TAIL_PROMPT="Give only the code."
'''


# Role prompting (Student)
'''
PROMPT_TECHNIQUE_SETTING = "Student-role" 

SYSTEM_PROMPT="You are a university student studying computer science, with basic knowledge in software enginnering."
HEAD_PROMPT = ""
TAIL_PROMPT="Give only the code."
'''

# Meta prompting
'''
PROMPT_TECHNIQUE_SETTING = "Meta" 

SYSTEM_PROMPT="""- For the following coding task, solve it in the following steps:
1. Define which variables needed.
2. Find a suitable algorithm, structure and approach to solve the task.
3. Refine the previous steps.
4. Give a code solution that solves the task."""
HEAD_PROMPT = ""
TAIL_PROMPT="Give only the code."
'''

# Naive Prompting
'''
PROMPT_TECHNIQUE_SETTING = "Naive" 

SYSTEM_PROMPT="Generate code that is clean, easy to read with low complexity, and uphold high software quality standards."
HEAD_PROMPT = ""
TAIL_PROMPT="Give only the code."
'''

# Iterative refinement prompting
''''''
PROMPT_TECHNIQUE_SETTING = "Iterative" 

SYSTEM_PROMPT="","Read the task description again and refine the provided code to be better and fix potential problems"
HEAD_PROMPT = ""
TAIL_PROMPT="Give only the code."
