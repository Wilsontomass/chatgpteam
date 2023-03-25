# ChatGPTeam

This was an idea I had to make chatgpt write and test simple programs.

It works by making ChatGPT talk to itself, by labelling one set of messages
the "programmer" and the other the "product owner". The "two" AIs
go back and forth writing a program until they either run out of time
or are done. 
There's also a seperate chat that is created whenever the program is tested, allowing chatGPT to try out its code.
## How to use:
Clone the repo, then create a file called `.env` and enter your open AI information
```
OPENAI_API_KEY=sk-<YOUR-API-KEY>
OPENAI_ORG=org-<YOUR-ORG>
```

Install all the python requirements (I'd reccomend doing that in a venv) with `python -m pip install -r requirements.txt`

Set the project you would like the AIs to work on by changing `PROJECT` in `src/common.py`

Then run main with `python src/main.py`

## Examples:
The (rather crude) result of the starter project, a command line inventory management app, can be seen in `example.py` as well as the far more interesting
AI discussion in `example.md`. This starter project is so simple that
a very similar program can be achieved by just asking ChatGPT to produce it
in a one shot, so perhaps harder projects and longer run times should be tried.

## Issues:
The main issue right now is that the AIs seem to give up a little too easily, and
end up just complimenting eachother in circles, rather than continuing to improve
the program. They also don't seem to use the KeywordDone keyword often enough.