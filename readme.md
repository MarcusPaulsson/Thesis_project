# Master’s Thesis Project: LLM experiments

This repository contains the code and resources for the thesis experiments


## Project Structure and Setup

This repository contains scripts and data for evaluating code generation models. The project is organized as follows:

* **`data/`**: Stores input datasets. Most dataset are downloaded from HuggingFace.
* **`results/`**: Contains raw model outputs, filtered code snippets
* **`ChatGPT, Deepseek, Gemini, WizardCoder/`**: Holds Python scripts for running inference on the models.
* **`evaluation_scripts/`**: Holds python scripts for calculating metrics, statistical data and visuliazation plots.

**External Model Dependency:**

For running the local models (**`Deepseek`** and **`Wizardcoder`**), it expects a directory named `Models` to be located in the parent directory of this repository (`../Models/`). This directory should contain the model files for each local model used in the evaluation. This setup allows for the use of large models without bloating the Git repository.


**API Model Dependency:**

For running the API based models, addition API keys needs to be listed in a python file ```config.py``` in the main folder.

**Virtual Environment:**

It is assumed that a virtual environment (`venv`) has been created and activated for this project. To set up your environment, follow these steps:

1.  Navigate to the project directory.
2.  Create a virtual environment: `python3 -m venv venv`
3.  Activate the virtual environment:
    * On macOS/Linux: `source venv/bin/activate`
    * On Windows: `venv\Scripts\activate`
4.  Install the required dependencies: `pip install -r requirements.txt`
