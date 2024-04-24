import tkinter as tk
from transformers import pipeline

# Create a summarization pipeline using the T5 model
summarizer = pipeline("summarization", model='t5-base', tokenizer='t5-base', framework='pt')

def summarize_text():
    text = text_entry.get("1.0", "end-1c")

    summary = summarizer(text, max_length=100, min_length=10, do_sample=False)

    output_text.delete("1.0", "end")
    output_text.insert("1.0", summary[0]['summary_text'])

window = tk.Tk()
window.title("Text Summarizer")

text_entry = tk.Text(window, height=10, width=50)
text_entry.pack()

summarize_button = tk.Button(window, text="Summarize", command=summarize_text)
summarize_button.pack()

output_text = tk.Text(window, height=10, width=50)
output_text.pack()

window.mainloop()
