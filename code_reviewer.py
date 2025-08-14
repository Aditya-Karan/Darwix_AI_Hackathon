from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='meta-llama/Llama-3.1-8B-Instruct',
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)

class CodeReviewer:
    def __init__(self):
        self.prompt_template = """
        You are an empathetic code reviewer acting as a senior developer or patient mentor. 
        Given the following code snippet and review comments, rephrase each comment into a constructive, educational feedback. 
        For each comment, include:
        1. Positive Rephrasing: A gentle and encouraging version of the feedback.
        2. The 'Why': A clear, concise explanation of the underlying software principle (e.g., performance, readability, convention).
        3. Suggested Improvement: A concrete code example demonstrating the recommended fix.

        Code Snippet:
        {code_snippet}

        Original Comments:
        {review_comments}

        Provide the output in Markdown format with sections for each comment.
        """

    def generate_feedback(self, code_snippet, review_comments):
        prompt = self.prompt_template.format(code_snippet=code_snippet, review_comments=review_comments)
        response = model.invoke(prompt)
        return response.content