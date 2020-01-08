![ChatterBot: Machine learning in Python](image/projetoX.png)

# Projeto-X


"Project-X" is a program that aims to create an artificial intelligence system that can recognize people and communicate with them.
The system is based on Python and its own functions to create chatbot artificial intelligence.

[![Package Version](https://img.shields.io/pypi/v/chatterbot.svg)](https://pypi.python.org/pypi/chatterbot/)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Requirements Status](https://requires.io/github/gunthercox/ChatterBot/requirements.svg?branch=master)](requirements.txt)
[![Coverage Status](https://img.shields.io/coveralls/gunthercox/ChatterBot.svg)](https://coveralls.io/r/gunthercox/ChatterBot)

The purpose of this project is to create an artificial intelligence that most closely resembles the AI ​"Jarvis used in the Iron Man movie.

## How artificial intelligence works

The communication system searches your database for the closest phrase to what you said. If she finds nothing and training mode is enabled, she will ask if she wants to add her phrase to the database and a possible answer.
If training mode is disabled and the AI ​​confidence level is low, it will be ignored and say "I don't understand".

## Installation

For project startup the repository must be cloned:

```
git clone https://github.com/bobyzoo/ProjetoX.git
```

## Basic Usage

```
from classBot import *

Bot = classBot('Assist.db', mode_train=False)

while True:
    Quest = input('You: ')
    answer = Bot.procuraResposta(Quest)
    print(f'Bot: {answer}')

```


# Development pattern for contributors

1. [Create a fork](https://help.github.com/articles/fork-a-repo/) of
   the [main ProjetoX repository](https://github.com/bobyzoo/ProjetoX) on GitHub.
2. Make your changes in a branch named something different from `master`, e.g. create
   a new branch `my-pull-request`.
3. [Create a pull request](https://help.github.com/articles/creating-a-pull-request/).

