# math-expression-to-words

Creation of this programm was inspired by <a href="https://evo.company/">EVO</a>'s task.

<h2>Usage</h2>
Use this willing code for converting math expression to words (of each element).
<br>You need to activate virtual environment
<br><code>user@user:~$ pip install virtualenv</code>
<br><code>user@user:~$ virtualenv math_to_str</code>
<br><code>user@user:~$ source math_to_str/bin/activate</code>
<br>then to install all packages from 'requirements.txt'
<br><code>(math_to_str) user@user:~$ pip install -r requirements.txt</code>
<br>and to run python file 'run.py' in console.
<br><code>(math_to_str) user@user:~$ python run.py</code>

<h2>Tests</h2>
To check tests — run the file 'main_test.py' through library 'pytest'.
<br><code>pytest main_test.py</code>
<br>or you can play with the code by yourself:
<h4>Examples</h4>
<code>(math_to_str) user@user:~$ python</code>
<br><code>>>> from main import math_to_str as mts</code>
<br><code>>>> mts('1 + 2 = 3')</code>
<br><code>one plus two equals three</code>
<br><code>>>> mts('1+ 2 = 3')</code>
<br><code>invalid input</code>
<br><code>>>> mts(' 0000000  ')</code>
<br><code>zero</code>
<br><code>>>> mts(' rg00000  ')</code>
<br><code>invalid input</code>
<br><code>>>> mts('123456789123456789123456789123456789')</code>
<br><code>one hundred and twenty-three decillion, four hundred and fifty-six nonillion, seven hundred and eighty-nine octillion, one hundred and twenty-three septillion, four hundred and fifty-six sextillion, seven hundred and eighty-nine quintillion, one hundred and twenty-three quadrillion, four hundred and fifty-six trillion, seven hundred and eighty-nine billion, one hundred and twenty-three million, four hundred and fifty-six thousand, seven hundred and eighty-nine</code>
<br>and so on...

<h2>Technologies</h2>
<ul>
  <li>Python 3.7.1</li>
  <li>pytest 4.4.1</li>
</ul>
