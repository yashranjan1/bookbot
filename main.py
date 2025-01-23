def count_words(str):
    return len(str.split())

def letter_frequency(str):

    lowercase = str.lower()
    
    frequency = {}

    for letter in lowercase:
        if letter.isalpha():
            if letter in frequency:
                frequency[letter] += 1
            else:
                frequency[letter] = 1
    
    return frequency

def main():
    book_name = "books/frankenstein.txt"
    with open(book_name) as f:
        file_contents = f.read()
        print(f"--- Begin report of {book_name} ---")
        print()
        print(f"{count_words(file_contents)} words found in this document")

        frequencies = letter_frequency(file_contents)

        sorted_frequencies = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)

        for letter, frequency in sorted_frequencies:
            print(f"The letter '{letter}' was found {frequency} times") 
        
        print("--- End report ---")

        
if __name__ == "__main__":
    main()