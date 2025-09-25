import ipywidgets as widgets
from IPython.display import display, clear_output, Markdown

def run_quiz(questions):
    radios = []
    output = widgets.Output()
    submit_button = widgets.Button(description="Submit Quiz", button_style="success")

    # Display all questions with Markdown and radio buttons
    for idx, q in enumerate(questions):
        question_md = f"\n\n### ❓ Question {idx + 1}\n**{q['question'].strip()}**"
        display(Markdown(question_md))
        radio = widgets.RadioButtons(options=q["options"], value=None)
        radios.append((q, radio))
        display(radio)

    display(submit_button, output)

    def on_submit(b):
        with output:
            clear_output()
            incorrect = []
            score = 0

            for q, radio in radios:
                selected = radio.value
                correct = q["options"][q["answer"]]
                if selected == correct:
                    score += 1
                else:
                    incorrect.append({
                        "question": q["question"],
                        "selected": selected,
                        "correct": correct
                    })

            display(Markdown(f"## ✅ Your score: **{score}** out of **{len(questions)}**"))

            if incorrect:
                display(Markdown("### ❌ Review the incorrect answers:\n"))
                for item in incorrect:
                    display(Markdown(
                        f"**Question:** {item['question'].strip()}\n\n"
                        f"- Your answer: `{item['selected']}`\n"
                        f"- Correct answer: `{item['correct']}`\n"
                    ))
            else:
                display(Markdown("### 🎉 Perfect score! Well done."))

    submit_button.on_click(on_submit)
