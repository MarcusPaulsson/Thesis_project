# This file contains all strings for concatenating the prompt templates around the tasks. 
# Both system prompt and extra context prompts



# Prompt template concatenation for the different models:
''' 
# ChatGPT Format
messages = [
    {"role": "system", "content": prompt.SYSTEM_PROMPT},
    {"role": "user", "content": task_prompt+prompt.TAIL_PROMPT}
],

# Gemini Format
messages = [
        types.Content(
            role="user", parts=[types.Part.from_text(text= prompt.SYSTEM_PROMPT+ task_prompt + prompt.TAIL_PROMPT)],
        ),
    ]

# Gemma3 Format
messages = [
        types.Content(
            role="user", parts=[types.Part.from_text(text= prompt.SYSTEM_PROMPT+ task_prompt + prompt.TAIL_PROMPT)],
        ),
    ]
'''



# Zero-shot prompting
'''
PROMPT_TECHNIQUE_SETTING = "Zero-shot" # placeholder for storing content to correct result directory

SYSTEM_PROMPT=""
HEAD_PROMPT = ""
TAIL_PROMPT=" Give only the code, no test cases."
'''

# Zero-shot Chain of thougths
'''

PROMPT_TECHNIQUE_SETTING = "Zero-shot-CoT" 

SYSTEM_PROMPT="Solve the following task step by step."
HEAD_PROMPT = ""
TAIL_PROMPT="Give only the code, no test cases."
'''
# Role prompting (Expert)
'''
PROMPT_TECHNIQUE_SETTING = "Expert-role" 

SYSTEM_PROMPT="You are an expert software developer, skilled in producing clean and well-structured code."
HEAD_PROMPT = ""
TAIL_PROMPT="Give only the code, no test cases."
'''

# Role prompting (Student)
'''
PROMPT_TECHNIQUE_SETTING = "Student-role" 

SYSTEM_PROMPT="You are a university student studying computer science, with basic knowledge in software enginnering."
HEAD_PROMPT = ""
TAIL_PROMPT="Give only the code, no test cases."
'''

# Naive Prompting
'''
PROMPT_TECHNIQUE_SETTING = "Naive" 

SYSTEM_PROMPT="Generate code that is clean, easy to read with low complexity, and uphold high software quality standards."
HEAD_PROMPT = ""
TAIL_PROMPT="Give only the code, no test cases."
'''

# Iterative refinement prompting
'''
PROMPT_TECHNIQUE_SETTING = "Iterative" 

SYSTEM_PROMPT="","Read the task description again and refine the provided code to be better and fix potential problems"
HEAD_PROMPT = ""
TAIL_PROMPT="Give only the code, no test cases."
'''

# Combined Heuristic
''''''
PROMPT_TECHNIQUE_SETTING = "Combined" # Expert, Naive, Iterative

SYSTEM_PROMPT="""You are an expert software developer, skilled in producing clean and well-structured code. Generate code that is clean, easy to read with low complexity, and uphold high software quality standards.
""","Read the task description again and refine the provided code to be better and fix potential problems. Generate code that is clean, easy to read and with low complexity, and uphold high software quality standards."
HEAD_PROMPT = ""
TAIL_PROMPT="Give only the code, no test cases."


