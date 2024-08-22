# CS240-Granular-Traffic-Network-Classification
## Environment
1. Python3.8
2. Pycharm/Jupyter Notebook
3. Tensorflow

## Dataset
https://www.kaggle.com/datasets/jiecdeng/240iscx

## Suggested Papers to Read
1. [CNN trafficClassify.pdf](https://github.com/jiechengdeng/CS240-Granular-Traffic-Network-Classification/files/10044521/CNN.trafficClassify.pdf)
2. [Internet_Application_Traffic_Classification_Using_.pdf](https://github.com/jiechengdeng/CS240-Granular-Traffic-Network-Classification/files/9944445/Internet_Application_Traffic_Classification_Using_.pdf)
3. [streamingTraffic.pdf](https://github.com/jiechengdeng/CS240-Granular-Traffic-Network-Classification/files/9892343/streamingTraffic.pdf)
4. [1-s2.0-S156625352100018X-main.pdf](https://github.com/jiechengdeng/CS240-Granular-Traffic-Network-Classification/files/9892348/1-s2.0-S156625352100018X-main.pdf)
5. [Paper_29-Network_Traffic_Classification_using_Machine.pdf](https://github.com/jiechengdeng/CS240-Granular-Traffic-Network-Classification/files/9892347/Paper_29-Network_Traffic_Classification_using_Machine.pdf)
6. [1080091.1080119.pdf](https://github.com/jiechengdeng/CS240-Granular-Traffic-Network-Classification/files/9915614/1080091.1080119.pdf)



# Experiments for CoderEval Dataset 
We use this dataset to test GPT-4 and Gemini Pro on code generation task and find their mistakes and the corresponding reasons for making mistakes.

The dataset can be found at: https://github.com/CoderEval/CoderEval

## Installation
Since our experiments for CoderEval Dataset relies on the docker environment, download the docker environment of our experiments at: 

## Approach
There are 3 major things in this task, and our implementations are in the folder: `GPT_Explanation_Project-main`
### 1. Generated Function Testing
After we generate the code of each problem for both GPT-4 and Gemini Pro, we bring their generated codes to this docker environment to test their correctness. The implementation of testing their code can be found in:

`/home/travis/builds/GPT_Explanation_Project-main/function_testing/src/test.py`

- #### To Run
Go to `src` folder and run `python test.py`

The `test.py` will run either `test_java` or `test_python` method, before you run it, you need to change the global variables that are defined in:
        `/home/travis/builds/GPT_Explanation_Project-main/common_library/project_settings.py`
set `language` to python or java - control which function to call in test.py
set `model_name` to Gemini or GPT-4 - which model's generated codes to use

### 2. Core Reason Verification
We manually find mistakes and their core reasons of incorrect codes based on the method we describe in the paper. Then we verify our concluded core reasons by modifying the input prompt and rerun the test cases to validate our findings.

The implementation to generate the code of new input prompt and test the new generated code can be found in: 
        `/home/travis/builds/GPT_Explanation_Project-main/core_reason_verification/src/main.py`

First set `google_api_key` or `openai_api_key` in `project_settings.py` to your API key for running Gemini or GPT-4. 
Then setting `language` and `model_name` variabes to the one you want to test. After that change the variable `modify_target_num` in `main.py` to the specific incorrect problem's id, this id can be found in:
        `/home/travis/builds/GPT_Explanation_Project-main/core_reason_verification/project_data/{model_name}/{language}_test_files_folder`
This id represents the incorrect problem you want to verify. 

This folder contains all incorrect problems for the specific language and model.

#### To Run
Go to `src` folder and run `python main.py`
The program will be stuck when it prints the model's generated code. You need to copy the code from the terminal to `/home/travis/builds/GPT_Explanation_Project-main/core_reason_verification/project_data/temp_code.txt` then type any key to continue to test the new generated code.
