from flask import Flask, render_template, abort

app = Flask(__name__)

# Sample quiz questions data
quiz_questions = {
    1: {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"]
    },
    2: {
        "question": "Which language is primarily used for web development?",
        "options": ["Python", "JavaScript", "C++", "Java"]
    },
    3: {
        "question": "What does CPU stand for?",
        "options": ["Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Central Processor Unit"]
    }
}

@app.route('/')
def home():
    return "<h1>Welcome! Use /quiz/&lt;question_id&gt; to preview quiz questions.</h1>"

@app.route('/quiz/<int:question_id>')
def quiz_preview(question_id):
    question_data = quiz_questions.get(question_id)
    if not question_data:
        abort(404, description="Question not found.")
    return render_template('quiz_preview.html', question=question_data, qid=question_id)

if __name__ == '__main__':
    app.run(debug=True)
