from termcolor import colored
import os, sys
import re

VERSION        = '1.5'
QUIT_COMMAND   = 'q'
REGRET_COMMAND = '_'
REGEX_EXP = "^(.*?) @ (.*?)$"

def ins(message):
    print(message)
    content = input(colored("> ", "blue"))
    if content == QUIT_COMMAND:
        exit()
    while content == '':
        content = input(colored("> ", "blue"))
    return content

def blank():
    print('')

def test(data):
    print(f"- START # {data['title'] if data['title'] != '' else 'Untitled'} -")

    answers = []
    errors = []
    index = 0
    regreted = False
    points = 0
    while index < len(data["word_translations"]):
        answer = ins(f"{index}. {data['word_translations'][index]}")
        if (answer == REGRET_COMMAND) and (index > 0) and (not regreted):
            index -= 1
            regreted = True
            blank()
            continue

        if answer != data["words"][index]:
            errors.append(index)
            points = 0
            print(f"{colored('INCORRECT', 'red')} {data['words'][index] if data['mode'] == 'A' else '0'}")
        else:
            if regreted:
                errors.pop()
            points += 1
            print(f"{colored('CORRECT', 'green')} {points}")

        if regreted:
            answers[index] = answer
            regreted = False
        else:
            answers.append(answer)

        blank()
        index += 1

    number_of_errors = len(errors)
    number_of_words  = len(data["words"])
    print("- END -")

    if (data["mode"] == 'B') and (number_of_errors > 0):
        blank()
        print("Corrections:")
        for index in errors:
            blank()
            print(f"{index}. {data['word_translations'][index]}")
            print(f"Your answer: {colored(answers[index], 'blue')}")
            print(f"Correct answer: {colored(data['words'][index], 'green')}")

    blank()
    if data["title"] != '':
        print(f"# {data['title']}")
    print(f"Total: {colored(number_of_words, 'magenta')}")
    print(f"Incorrect: {colored(number_of_errors, 'red')}")
    if number_of_errors == 0:
        blank()
        print("No errors! Congratulations!")

def convert(word_list_path):
    """
    Get .words file into program use
    Approach: RegEx
    Returns:
        A dict containing words, word_translation and title
    """
    try:
        with open(word_list_path, 'r', encoding='UTF-8') as f:
            words = list()
            word_translations = list()
            for line in f.readlines():
                line = line.replace('\n', '')
                if line[0] == '.':
                    title = line
                elif line:
                    wordt = re.findall(REGEX_EXP, line)[0] # (word, word_translation)
                    words.append(wordt[0])
                    word_translations.append(wordt[1])
    except FileNotFoundError:
        return -1
    else:
        return {
            "words": words,
            "word_translations": word_translations,
            "title": title
        }

def main():
    print("Welcome to Dictationer!")
    print(f"Current version: {colored(VERSION, 'green')}")
    blank()
    print(f"You can type {colored(QUIT_COMMAND, 'cyan')} to quit whenever you are in a input session.")
    print(f"If you want to change your answer (except the first word and the last word) after entering it (at once only), type {colored(REGRET_COMMAND, 'cyan')}.")
    blank()

    word_list_path = ins("* Please enter the path of your word list.")
    while not os.path.isfile(word_list_path):
        word_list_path = ins(colored(f"* Sorry, the file '{word_list_path}' does not exist. Please try again.", "yellow"))
    blank()
    data = convert(word_list_path)
    if data == -1:
        print(colored(f"The file '{word_list_path}' does exist but is not a suitable word-list file for Dictationer.", 'yellow'))
        exit()

    mode = ins(f"* Please enter the mode of the dictation.\n- {colored('A', 'cyan')}: The correction returns for every session.\n- {colored('B', 'cyan')}: The corrections return when all the sessions are finished.")
    while not mode in {'A', 'B'}:
        mode = ins(colored(f"* Sorry, '{mode}' is not a valid mode. Please try again.", "yellow"))
    data["mode"] = mode

    blank()

    test(data)

    blank()

if __name__ == "__main__":
    main()
