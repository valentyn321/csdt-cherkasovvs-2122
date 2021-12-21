_First name_ : Valentyn

_Last name_ : Cherkasov

_Group_ : KI - 48

_Student number_ : #19:
* Game - Tennis
* Data driven format - XML
* HW i-face - UART

***Play modes: ∙ Man vs AI ∙ Man vs Man ∙ AI vs AI AI should support next complexity levels: ∙ Random move; ∙ Win strategy; Actions: ∙ New; ∙ Save; ∙ Load; The proposal for data driven approach: configuration (saved in configuration file or DB): ∙ board size; ∙ distance; ∙ tool size; ∙ win statement;∙ lose statement; ∙ AI parameters***

How to build project:

You need to clone this repo, preinstall python (if you are using Widnows).
Creating virtual environment is a nice idea. All dependecies are written into 2 files - `requirements.txt` and `Pipfile.lock`. Choose the way which suits you more.
After that you run server with the command from the `recognition_django` folder:

`python manage.py runserver`

How to build and run tests:
Project contains 4 tests.
```
a) Unit tests;

b) Integration tests;

c) Automation tests;

d) Manual tests;
```
They run before each commit, but you can also run them manually - run this command in the root of the probject:

`
pytest
`

Created tag: csdt-cherkasovvs-2122_v2.0_5021502
