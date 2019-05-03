# math-expression-to-words

Creation of this programm was inspired by [EVO](https://evo.company/)'s task.

## Usage
Use this willing code for converting math expression to words (of each element).
You need to activate virtual environment
```bash
user@user:~$ pip install virtualenv
user@user:~$ virtualenv math_to_str
user@user:~$ source math_to_str/bin/activate
```
then to install all packages from *requirements.txt*
```bash
(math_to_str) user@user:~$ pip install -r requirements.txt
```
and to run python file *run.py* in console:
```bash
(math_to_str) user@user:~$ python run.py
```
or quick call using system args (expression in quotes):
```bash
(math_to_str) user@user:~$ python quick_run.py '1 + 4 = 6'
one plus four equals six
```

## Tests
To check tests — run the file *main_test.py* through library *pytest*
```bash
pytest main_test.py
```
or you can play with the code by yourself:
#### Examples
```bash
(math_to_str) user@user:~$ python
>>> from main import math_to_str as mts
>>> mts('1 + 2 = 3')
one plus two equals three
>>> mts('1+ 2 = 3')
invalid input
>>> mts(' 0000000  ')
zero
>>> mts(' rg00000  ')
invalid input
>>> mts('123456789123456789123456789123456789')
one hundred and twenty-three decillion, four hundred and fifty-six nonillion, seven hundred and eighty-nine octillion, one hundred and twenty-three septillion, four hundred and fifty-six sextillion, seven hundred and eighty-nine quintillion, one hundred and twenty-three quadrillion, four hundred and fifty-six trillion, seven hundred and eighty-nine billion, one hundred and twenty-three million, four hundred and fifty-six thousand, seven hundred and eighty-nine
```
and so on...

## Technologies
* Python 3.7.1
* pytest 4.4.1

