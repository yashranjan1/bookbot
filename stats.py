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
