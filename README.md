# math-expression-to-words

Creation of this programm was inspired by <a href="https://evo.company/">EVO</a>'s task.

<h2>Usage</h2>
Use this willing code for converting math expression to words (of each element).
<br>You need to activate virtual environment
<code>user@user:~$ pip install virtualenv</code>
<code>user@user:~$ virtualenv math_to_str</code>
<code>user@user:~$ source math_to_str/bin/activate</code>
then to install all packages from 'requirements.txt'
<code>(math_to_str) user@user:~$ pip install -r requirements.txt</code>
and to run python file 'run.py' in console.
<code>(math_to_str) user@user:~$ python run.py</code>

<h2>Tests</h2>
To check tests — run the file 'main_test.py' through library 'pytest'.
<code>pytest main_test.py</code>
or you can play with the code by yourself:
<h4>Examples</h4>
<code>(math_to_str) user@user:~$ python</code>
<code>>>> from main import math_to_str as mts</code>
<code>>>> mts('1 + 2 = 3')</code>
<code>one plus two equals three</code>
<code>>>> mts('1+ 2 = 3')</code>
<code>invalid input</code>
<code>>>> mts(' 0000000  ')</code>
<code>zero</code>
<code>>>> mts(' rg00000  ')</code>
<code>invalid input</code>
<code>>>> mts('123456789123456789123456789123456789')</code>
<code>one hundred and twenty-three decillion, four hundred and fifty-six nonillion, seven hundred and eighty-nine octillion, one hundred and twenty-three septillion, four hundred and fifty-six sextillion, seven hundred and eighty-nine quintillion, one hundred and twenty-three quadrillion, four hundred and fifty-six trillion, seven hundred and eighty-nine billion, one hundred and twenty-three million, four hundred and fifty-six thousand, seven hundred and eighty-nine</code>
and so on...

<h2>Technologies</h2>
<ul>
  <li>Python 3.7.1</li>
  <li>pytest 4.4.1</li>
</ul>
