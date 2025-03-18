#!/bin/bash
# cognitive_complexity.sh
#
# THIS SCRIPT WILL MEASURE THE COGNITIVE COMPLEXITY OF ALL THE RESULTS OF THE AI GENERATED FILES THAT 
# EXIST IN THE 'result' FOLDER AND FOR EACH OF THE MODELS AND THE PROMPTING TECHNIQUE

# Determine the directory where the script is located
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
UPPER_DIR="$(realpath "$SCRIPT_DIR/../")"       # Access content one step up

### Hardcode a file paths for all results:

# ChatGPT
CHATGPT_CLASSEVAL="$UPPER_DIR/results/ChatGPT/classEval" # (Python)
CHATGPT_CLI_GAMES="$UPPER_DIR/results/ChatGPT/cli_games" # (Python)

# Gemini
GEMINI_CLI_GAMES="$UPPER_DIR/results/Gemini/cli_games" # (Python)
GEMINI_CLASSEVAL="$UPPER_DIR/results/Gemini/classEval" # (Python)

# WizardCoder
#TODO

# DeepSeek
#TODO

# Run complexipy on the hardcoded file path and capture its output
OUTPUT=$(complexipy "$CHATGPT_CLI_GAMES")

# Extract the line containing "Total Cognitive Complexity:"
COMPLEXITY_LINE=$(echo "$OUTPUT" | grep "Total Cognitive Complexity:")

if [ -n "$COMPLEXITY_LINE" ]; then
    echo "Cognitive Complexity for '$CHATGPT_CLI_GAMES':"
    echo "$COMPLEXITY_LINE"
else
    echo "Could not extract cognitive complexity from output."
fi


# Run complexipy on the hardcoded file path and capture its output
OUTPUT=$(complexipy "$GEMINI_CLI_GAMES")

# Extract the line containing "Total Cognitive Complexity:"
COMPLEXITY_LINE=$(echo "$OUTPUT" | grep "Total Cognitive Complexity:")

if [ -n "$COMPLEXITY_LINE" ]; then
    echo "Cognitive Complexity for '$GEMINI_CLI_GAMES':"
    echo "$COMPLEXITY_LINE"
else
    echo "Could not extract cognitive complexity from output."
fi

