def analyze_text(text):
    words = text.split()
    word_count = len(words)
    char_count = len(text)
    avg_word_length = char_count / word_count if word_count else 0

    return {
        "word_count": word_count,
        "char_count": char_count,
        "avg_word_length": round(avg_word_length, 2)
    }

if __name__ == "__main__":
    sample = input("Enter text to analyze: ")
    result = analyze_text(sample)
    print(result)
