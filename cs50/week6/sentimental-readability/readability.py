#!/usr/bin/env python3
def main():

    # TODO: Prompt the user for some text
    while True:
        text = input("Enter text: ")
        if count_letters(text) == 0:
            print("No letters found")
        else:
            break

    # TODO: Count the number of letters, words, and sentences in the text
    letter_count = count_letters(text)
    word_count = count_words(text.strip())
    sentence_count = count_sentences(text)

    # TODO: Compute the Coleman-Liau index
    # Coleman-Liau variables L & S
    L = (letter_count / word_count) * 100
    S = (sentence_count / word_count) * 100
    Coleman_Liau_index = 0.0588 * L - 0.296 * S - 15.8

    # TODO: Print the grade level
    if Coleman_Liau_index > 16:
        print("Grade 16+")
    elif Coleman_Liau_index < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {round(Coleman_Liau_index)}")


def count_letters(text):
    letter_count = 0
    for letter in text:
        if letter.isalpha() == True:
            letter_count += 1
    return letter_count


def count_words(text):
    word_count = 1
    for letter in text:
        if letter == " ":
            word_count += 1
    return word_count


def count_sentences(text):
    sentence_count = 0
    for letter in text:
        if letter == "." or letter == "?" or letter == "!":
            sentence_count += 1
    return sentence_count


main()
