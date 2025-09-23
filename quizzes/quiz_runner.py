import ipywidgets as widgets
from IPython.display import display, clear_output

def run_quiz():
    score = 0
    for q in questions:
        print(q["question"])
        radio = widgets.RadioButtons(options=q["options"])
        display(radio)

        button = widgets.Button(description="Submit")
        output = widgets.Output()

        def on_submit(b):
            with output:
                clear_output()
                if radio.index == q["answer"]:
                    print("✅ Correct!")
                    nonlocal score
                    score += 1
                else:
                    print(f"❌ Incorrect. Correct answer: {q['options'][q['answer']]}")
        
        button.on_click(on_submit)
        display(button, output)