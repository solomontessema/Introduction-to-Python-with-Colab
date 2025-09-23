import ipywidgets as widgets
from IPython.display import display, clear_output

def run_quiz(questions):
    score = 0
    index = 0

    question_output = widgets.Output()
    feedback_output = widgets.Output()
    button = widgets.Button(description="Submit")

    def show_question(i):
        question_output.clear_output()
        feedback_output.clear_output()
        with question_output:
            print(questions[i]["question"])
            radio.options = questions[i]["options"]
            radio.value = None
            display(radio)

    radio = widgets.RadioButtons(options=[], value=None)
    display(question_output, button, feedback_output)

    def on_submit(b):
        nonlocal score, index
        feedback_output.clear_output()
        with feedback_output:
            if radio.value is None:
                print("⚠️ Please select an option before submitting.")
                return
            correct = questions[index]["options"][questions[index]["answer"]]
            if radio.value == correct:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Incorrect. Correct answer: {correct}")
        index += 1
        if index < len(questions):
            show_question(index)
        else:
            question_output.clear_output()
            print(f"\n🎉 Quiz complete! Your score: {score} out of {len(questions)}")

    button.on_click(on_submit)
    show_question(index)
