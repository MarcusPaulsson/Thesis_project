# Master’s Thesis Project: LLM experiments

This repository contains the code and resources for the thesis thesis.

## Repository Structure

This project contains scripts and data for evaluating code generated by LLMs. The repository is organized as follows:

* **`data/`**: Stores input datasets. Most dataset are downloaded from HuggingFace.
* **`evaluation_scripts/`**: Holds python scripts for calculating metrics, statistical data and visuliazation plots.
* **`experiment_scripts/`**: Holds Python scripts for running inference on the models. (Rewrite to experiment scripts)
* **`results/`**: Contains raw model outputs, filtered code snippets and images. Evaluation scripts refer to this folder.
* **`interview/`**: Contains resources for the interview.

**External Model Dependency:**

For running the local models (**`experiment_scripts/Deepseek`** and **`experiment_scripts/Wizardcoder`**), it expects a directory named `Models` to be located in the parent directory of this repository (`../Models/`). This directory should contain the model files for each local model used in the evaluation. This setup allows for the use of large models without bloating the Git repository.

**API Model Dependency:**

For running the API based models, addition API keys needs to be listed in a python file ```config.py``` in the main folder.

**Virtual Environment Setup:**

1.  Navigate to the project directory.
2.  Create a virtual environment: `python3 -m venv venv`
3.  Activate the virtual environment:
    * On macOS/Linux: `source venv/bin/activate`
    * On Windows: `venv\Scripts\activate`
4.  Install the required dependencies: `pip install -r requirements.txt`


## Run experiments and evaluation scripts:

Description how to run the experiments with different configurations

**Prompt setup:**
Each input prompt to the models consist of 4 pieces which is formulated in file: `experiment_scripts/prompt_technique_template.py`. Depending which prompt technique to run, make sure only the present techniques prompt constants are accessable, keep the others commented out!

**models scripts**
In `experiment_scripts/`, each model has its own folder together with the scripts to run the experiments on each of the datasets. The result from these scripts are saved in the result folder. OBS! note that the saved result overrides previous content and no differnt file naming is used when changing prompting techniques.

**Evaluation scripts** 
For the three different metrics used in this project, each has a corresponding script in `evaluation_scripts/`. For **Cognitive Complexity**, the python library ''complexipy'' is used for the calculations. The script is hardcoded to run on the subfolders to each model. 