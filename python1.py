import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# ✅ Download required NLTK data
nltk.download('punkt')
nltk.download('punkt_tab')  # 🔧 This line fixes the error you got

def summarize_text(text, sentences_count=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count)
    print("\n📌 Summary:\n")
    for sentence in summary:
        print("-", sentence)

def main():
    print("🔹 TEXT SUMMARIZER TOOL 🔹")
    choice = input("Choose input method:\n1. Type/Paste Article\n2. Load from .txt File\nEnter 1 or 2: ")

    if choice == "1":
        print("\nPaste or type your article below. Press Enter twice to finish:")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        article = "\n".join(lines)

    elif choice == "2":
        file_path = input("Enter path of your .txt file (e.g., article.txt): ")
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                article = file.read()
        except FileNotFoundError:
            print("❌ File not found.")
            return
    else:
        print("❌ Invalid choice.")
        return

    try:
        num_sentences = int(input("Enter number of sentences for summary: "))
    except ValueError:
        print("⚠️ Invalid input. Using default value: 3")
        num_sentences = 3

    summarize_text(article, num_sentences)

if __name__ == "__main__":
    main()
