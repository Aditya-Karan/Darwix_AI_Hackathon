# Empathetic Code Reviewer

## Overview
The Empathetic Code Reviewer is a tool designed to transform critical code review comments into constructive, empathetic, and educational feedback. It acts as a bridge between senior developers and junior team members, fostering a supportive environment by rephrasing feedback with clear explanations and practical suggestions. This project leverages the LangChain framework with a Hugging Face model to process code snippets and review comments.

## Tagline
Transforming Critical Feedback into Constructive Growth.

## Prerequisites
- Python 3.7 or higher
- Internet connection (required for Hugging Face API)
- Hugging Face API token

## Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd empathetic-code-reviewer
```

### 2. Create a Virtual Environment
To isolate dependencies, create a virtual environment:
- On Windows:
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  python -m venv venv
  source venv/bin/activate
  ```

### 3. Install Dependencies
With the virtual environment activated, install the required packages:
```bash
pip install langchain-huggingface python-dotenv
```

### 4. Set Up Environment Variables
- Create a `.env` file in the project root directory.
- Add your Hugging Face API token:
  ```
  HUGGINGFACEHUB_API_TOKEN=your_api_token_here
  ```
  (Replace `your_api_token_here` with your actual token from Hugging Face account settings.)

## Project Structure
- `code_reviewer.py`: Contains the `CodeReviewer` class that handles the LangChain model and prompt engineering.
- `utils.py`: Includes utility functions like formatting the Markdown output.
- `main.py`: The main script that ties everything together and runs the code review process.
- `README.md`: This file, providing project documentation.

## Usage

### Running the Program
1. Activate the virtual environment (as described in Installation).
2. Run the main script:
   ```bash
   python main.py
   ```
3. The program will process a predefined code snippet and review comments, outputting a Markdown-formatted feedback report to the console.

### Example Input
Modify `main.py` to test with different inputs. An example is provided:
```python
code_snippet = '''def get_active_users(users):
    results = []
    for u in users:
        if u.is_active == True and u.profile_complete == True:
            results.append(u)
    return results'''

review_comments = [
    "This is inefficient. Don't loop twice conceptually.",
    "Variable 'u' is a bad name.",
    "Boolean comparison '== True' is redundant."
]
```

### Example Output
The output will be a Markdown report similar to the following based on the example input:

**Code Review Feedback**
=======================

### 1. Inefficient Looping

#### Positive Rephrasing
Great job on breaking down the logic into a separate function! However, let's see if we can optimize the loop to make it more efficient.

#### The 'Why'
In this case, the issue is that we're looping over the `users` list twice: once in the `for` loop and again when calling the `is_active` and `profile_complete` methods on each user object. This can lead to unnecessary iterations and slower performance.

#### Suggested Improvement
```python
def get_active_users(users):
    return [u for u in users if u.is_active and u.profile_complete]
```
By using a list comprehension, we can eliminate the need for an explicit loop and make the code more concise and efficient.

### 2. Poor Variable Naming

#### Positive Rephrasing
You're off to a great start with the function name, but let's make sure the variable names are clear and descriptive too.

#### The 'Why'
Variable names should be chosen to accurately reflect their purpose and make the code easier to understand. In this case, the variable name `u` is not very descriptive and could be improved.

#### Suggested Improvement
```python
def get_active_users(users):
    results = []
    for user in users:
        if user.is_active and user.profile_complete:
            results.append(user)
    return results
```
By renaming the variable to `user`, we've made it clearer what the loop is iterating over.

### 3. Redundant Boolean Comparison

#### Positive Rephrasing
You're close! However, let's make sure the boolean comparisons are as concise and readable as possible.

#### The 'Why'
In Python, the `== True` comparison is redundant because the `True` value is a boolean constant. We can simply use the `is_active` attribute directly.

#### Suggested Improvement
```python
def get_active_users(users):
    results = []
    for user in users:
        if user.is_active and user.profile_complete:
            results.append(user)
    return results
```
this is my example output use as it is in my readme

## Workflow
1. **Input Processing**: The `main.py` script provides a JSON-like object with `code_snippet` and `review_comments`.
2. **Prompt Engineering**: The `CodeReviewer` class in `code_reviewer.py` uses a predefined prompt template to guide the Hugging Face model.
3. **Feedback Generation**: The LangChain model (`meta-llama/Llama-3.1-8B-Instruct`) generates empathetic and educational feedback.
4. **Output Formatting**: The `utils.py` module formats the response into Markdown for readability.
5. **Display**: The formatted feedback is printed to the console.

## Customization
- **Change Input**: Update the `code_snippet` and `review_comments` in `main.py` to review different code.
- **Model Adjustment**: Modify the `repo_id` in `code_reviewer.py` to use a different Hugging Face model if desired.
- **Add Features**: Extend the `CodeReviewer` class to include contextual awareness or resource links as suggested in the hackathon guidelines.

## Thanks for inviting me to participate in this hackathon.