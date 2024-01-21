import tkinter as tk
from tkinter import ttk
from deep_translator import GoogleTranslator

class TranslatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Text Translator")

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Enter text to translate:")
        self.label.pack()

        self.entry = tk.Entry(self.master, width=50)
        self.entry.pack()

        self.language_label = tk.Label(self.master, text="Select target language:")
        self.language_label.pack()

        self.language_combobox = ttk.Combobox(self.master, values=["English (en)", "Tamil (ta)", "Hindi (hi)"])
        self.language_combobox.set("English (en)")
        self.language_combobox.pack()

        self.translate_button = tk.Button(self.master, text="Translate", command=self.translate_text)
        self.translate_button.pack()

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()

    def translate_text(self):
        text_to_translate = self.entry.get()
        target_language = self.get_target_language_code()

        if text_to_translate and target_language:
            translated_text = self.translate(text_to_translate, target_language)
            self.result_label.config(text=f"Translated text: {translated_text}")
        else:
            self.result_label.config(text="Please enter text and select a target language.")

    def translate(self, text, target_language):
        translator = GoogleTranslator(source="auto", target=target_language)
        result = translator.translate(text)
        return result

    def get_target_language_code(self):
        selected_language = self.language_combobox.get()
        language_mapping = {"English (en)": "en", "Tamil (ta)": "ta", "Hindi (hi)": "hi"}
        return language_mapping.get(selected_language, None)

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
