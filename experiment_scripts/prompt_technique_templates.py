# This file contains all strings for concatenating the prompt templates around the tasks. 
# Both system prompt and extra context prompts

# These variables are implemented to automaticlly build the prompts for the models.
# For the models that does not take a system prompt, the SYSTEM_PROMPT is added to the head_prompt



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



# Vanilla/Baseline
SYSTEM_PROMPT=""
HEAD_PROMPT = ""
TAIL_PROMPT="Give only the code."


# Role prompting (Expert)
'''
SYSTEM_PROMPT="You are a senior software developer in python."
HEAD_PROMPT = ""
TAIL_PROMPT="Give only the code."
'''

# Role prompting (Student)
'''
SYSTEM_PROMPT="You are a university student."
HEAD_PROMPT = ""
TAIL_PROMPT="Give only the code."
'''
