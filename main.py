from stats import letter_frequency
import sys

def count_words(str):
    return len(str.split())

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_name = sys.argv[1]
    with open(book_name) as f:
        file_contents = f.read()
        print(f"============ BOOKBOT ============")
        print()
        print(f"Analyzing book found at {book_name}")
        print()
        print(f"Found {count_words(file_contents)} total words")

        frequencies = letter_frequency(file_contents)

        sorted_frequencies = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)

        for letter, frequency in sorted_frequencies:
            print(f"{letter}: {frequency}") 
        
        print("--- End report ---")

        
if __name__ == "__main__":
    main()
