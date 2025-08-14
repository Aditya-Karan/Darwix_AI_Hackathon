from code_reviewer import CodeReviewer
from utils import format_markdown_feedback

def main():
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

    reviewer = CodeReviewer()
    raw_feedback = reviewer.generate_feedback(code_snippet, "\n".join(review_comments))
    formatted_feedback = format_markdown_feedback(raw_feedback)
    print(formatted_feedback)

if __name__ == "__main__":
    main()