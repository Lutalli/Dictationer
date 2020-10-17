# Dictationer

`Oct. 17th, 2020`

Realize the process of vocabulary dictations on your console!

## Requirement

- `termcolor` (Python module)
- Your word file (see below)

## Usage

### Prepare the word list

Before starting your dictation, you need a list of *word couples*.

> A *word couple* includes a word in foreign language, which is called the *original word* and a corresponding translation in your mother language or another, which is called the *translation*.

In order to let Dictationer understand your words, a file of special format is needed.

Here are the standards:

1. The first line can optionally start with a dot `.` and then the title of your word file. For instance, the first line can be `.Colors`, and the title `Colors` will be showed in the dictation. Otherwise `Untitled` will be showed.

2. Other lines are for the word couples and each is of the form
```
<original word> @ <translation>
```
The `@` works like a splitting symbol. Notice that the spaces need to be strictly placed.

3. You can choose any file suffix for the word list: `.words`, `.txt`, `.list`, etc. The file is only required to be of a plain-text format.

For example, this is a valid word-list file for Dictationer (named `colors.words`):
```
.Colors
rot @ red
grün @ green
blau @ blue
```
If you have another kind of file that also contains word couples (like an Excel file), you can write a script to convert it to Dictationer's standard.

After the word list is prepared, run Dictationer and enter the path to you file.

### Dictation

In a dictation, the words are asked one by one. At present there're two modes for the dictation:

`A`: In every session, if you enter the wrong answer, the correction will be showed at once.

`B`: The corrections won't be showed during the dictation; instead they will be showed when the whole dictation is finished.

There is also a "current score" - this score increases when you did it correctly and resets to 0 when wrong. This score is showed for every session.

### Tricks

For every situation that a input is required, you can enter `q` to quit the program. For every dictation session, you can enter `_` to modify the last answer (perhaps you pressed the wrong button accidently) (but the "score" won't insist). You can't enter `_` twice or more at a time.

----

More features may be added in the future, including "running with arguments".

Contact me if you meet any bug or have a suggestion (by E-mailing me or opening an issue).

My E-mail: `mylutalli@gmail.com`

Also have fun modifying the source code. Enjoy!
