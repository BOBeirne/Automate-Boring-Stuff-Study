
While a computer can search for text quickly, it must be told precisely what to look for. 
Regular expressions allow you to specify the pattern of characters you are looking for, rather than the exact text itself. 

In fact, some word processing and spreadsheet applications provide find-and-replace features that allow you to search using regular expressions. 
The punctuation-heavy syntax of regular expressions is composed of qualifiers that detail what to match and quantifiers that detail how many to match.


Find out more:
official Python documentation at https://docs.python.org/3/library/re.html. 
tutorial website https://www.regular-expressions.info. 


# [[REGEX]] module

Regular expression = **[regex]**

import **re** - regex module

The re module that comes with Python lets you **compile a regex string into a Pattern object**. 

* **compile()** - returns **Pattern** object, need to be called only **once**, needs to use **regular expression**

These objects have several methods: 

* **search()** - Returns **Match** object if found anywhere in the string, **None** if not found
* **match()** - returns **ONLY** 1st match  it finds one
* **findall()**  - returns strings of *every match* as long as there are no groups in the regular expression! if there are groups, it will return **TUPLE
* **sub()** - find-and-replace substitution of text

## Regex testers

https://regex101.com
https://pythex.org

---
## Regex syntax

### Groups

``` python
import re
phone_re = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_re.search('My number is 415-555-4242.') # mo variable holds a "match object" that was returned by .search()
mo.group(1) # returns only the 1st group of the matched text
mo.group(2) # returns only 2nd group of matched text
mo.group(0) # returns full matched text

mo.groups() # returns ALL groups at once
area_code, main_nr = mo.groups()
print(area_code) # print 1st group
print(main_nr) # print 2nd group
```

## Using escape characters

in this case we are escaping the ( and ) characters

``` python
phone_re = re.compile(r'(\(\d\d\d))-(\d\d\d-\d\d\d\d)') 
mo.pattern.search('My phone number is (415) 555-4242.')
mo.group(1)
mo.group(2)
```

following chars have special meaning and need to be escaped:

``` python
$ ( ) * + - . ? [ \ ] ^ { | }
```

this is how to escape them

``` python
\$ 
\*
\+
\-
\.
\?
\^
\|
\\
\( \)
\{ \}
\[  \]
```

if you miss to escape character you will receive error msg about **"missed"** or **"unbalanced parenthesis"**

## Matching chars from alternate groups

### pipe | - alternation operator

using |

``` python
'cat | dog'
```

will match either 'cat' or 'dog'

you can also specify just a **prefix**

Example:

trying to match caterpillar, catastrophe, catch or category

``` python
import re
pattern = re.compile(r'cat(erpillar|astrophe|ch|egory)')
match = pattern.search('catch me if you can')
match.group()
```

'catch'

``` python
match.group(1)
```

'ch'

## Returning all matches

### .findall() method

**findall()** method - returns strings of *every match* as long as there are no groups in the regular expression! if there are groups, it will return **TUPLE**

### No groups

``` python
import re
pattern = re.compile(r'\d{3}-\d{3}-\d{4}') # this regex has no groups
pattern.findall('Cell: 415-555-9999 Work: 221-555-9999)
```

['415-555-9999', '221-551-9999']

### With groups

``` python
import re
pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})') # this regex has HAS groups
pattern.findall('Cell: 415-555-9999 Work: 221-555-9999)
```

[('415', '555', '9999'), ('221', '555', '9999')]

### No overlapping matches

Because 1st 3 digits have been matched (123) the digits 234 or 345 won't be included in matches even though the fit the pattern!

``` python
import re
pattern = re.compile(r'\d{3}')
pattern.findall('1234')
```

['123']

``` python
pattern.findall('12345')
```

['123']

``` python
pattern.findall('123456')
```

['123', '456']

## [Qualifier]s and [Quantifier]s

* **Qualifiers** - dictate what chars you are trying to match eg. r'\d and '-'
* **Quantifier** - follows qualifiers, dictate how many chars are you trying to match eg. '{3}'

---

### [Qualifier] syntax

#### Set of characters

* you can define a single char to match or a whole set of characters inside a square brackets []
* for example [aeiouAEIOU] will match any vowel in lower and uppercase
* it's the equivalent of writing a|e|i|o|u|A|E|I|O|U

``` python
import re
vowel_pattern = re.compile(r'[aeiouAEIOU]')
vowel_pattern.findall('robocop eats BABY FOOD')
```

['o', 'o', 'o', 'e', 'a', 'A', 'O', 'O']

### Range of characters

* you can also define a range of characters or numbers by using  a hyphen
* for example [a-zA-Z0-9] will match all lowercase, uppercase and numbers
* also char class does **not need escape characters!**, you can just search using [()]

``` python
import re
alphanumeric_pattern = re.compile(r'[a-zA-Z0-9]')
alphanumeric_pattern.findall('robocop eats BABY FOOD')
```

['r', 'o', 'b', 'o', 'c', 'o', 'p', 'e', 'a', 't', 's', 'B', 'A', 'B', 'Y', 'F', 'O', 'O', 'D']

### Negative character class

* make it by placing ^ just after character's class's opening
* it will match all characters that are not defined in the class
* keep in mind result include spaces, newlines, punctuations, characters and numbers!

``` python
import re
consonant_pattern = re.compile(r'[^aeiouAEIOU]')
consonant_pattern.findall('robocop eats BABY FOOD')
```

['r', 'b', 'c', 'p', ' ', 't', 's', ' ', 'B', 'B', 'Y', ' ', 'F', 'D']

### Shorthand Character Classes

There are many shorthand regular expressions such as \d standing for any numeric digit , which is a shorthand for regular expression 0|1|2|3|4|5|6|7|8|9

* \d        Any numeric digit 0-9
* \D        Opposite of \d
* \w        Any letter, numeric digit or underscore ("word" characters)
* \W        Opposite of \w
* \s        Any space, tab or newline character (matching "space" characters)
* \S        Opposite of \s

**! Remember to use escape characters!**

**There is no** shorthand that matches **only letters** (\w matches also underscore) but you can **use [a-zA-Z] instead!**

### Proceeding character set 

``` python
import re
pattern = re.compile(r'\d+\s\w+')
pattern.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
```

['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']

The + in a regular expression means "one or more" of the preceding character set.

* \d+ matches one or more numeric digits.
* \s matches a single whitespace character.
* \w+ matches one or more word characters (letters, numbers, or the underscore).

So, \d+ is what allows it to match '12' and '11' instead of just a single digit like '1' or '2'.

The regular expression \d+\s\w+ will match text that has one or more numeric digits (\d+), followed by a whitespace character (\s), followed by one or more letter/digit/underscore characters (\w+). The findall() method returns all matching strings of the regular expression pattern in a list.

### Matching everything with a dot . character

* . matches any character except for a newline
* it will match just 1 character! this is where 'lat' in 'flat' comes from.
* To match the actual period '.' character you need to use escape symbol \.

``` python
import re
at_re = re.compile(r'.at')
at_re.findall('The cat in the hat sat on the flat mat.')
```

['cat', 'hat', 'sat', 'lat', 'mat']

### Be careful what you match for

* [A-Z] or [a-z] will only match either uppercase or lowercase, to match both you must use [a-zA-Z]
* it accepts only plain, unaccented letters
* \w matches also accented letters BUT also numbers and underscore characters, so \w+ may match more than you anticipated
* Sinead O'Connor using \w+ would only capture her name uip to the apostrophe character so group would capture last name as 'O'
* Straight and smart quote characters are considered completely different and need to be specified each (''""`` etc)

#### More to read

* https://www.kalzumeus.com/2010/06/17/falsehoods-programmers-believe-about-names/
* https://www.youtube.com/watch?v=PYYfVqtcWQY

---

## [Quantifier] Syntax

* In regex string, quantifiers follow qualifiers to specify how many chars to mach
* if there are no specified quantifiers the quantifier must appear exactly once (eg. r'\d == r'\d{1})

### Matching optional pattern (?)

Sometimes you want to match pattern only optionally. That regex should match 0 or 1 of the preceding qualifiers as optional.

You could get by without using the optional "?" quantifier, or even the "*" and "+" quantifiers:

* The ? quantifier is the same as {0,1}.
* The * quantifier is the same as {0,}.
* The + quantifier is the same as {1,}.

However, the ?, *, and + quantifiers are common shorthand.

``` python
import re
pattern = re.compile(r'42!?')
pattern.search('42!')
```

<re.Match object; span=(0, 3), match='42!'>

``` python
pattern.search('42')
```

<re.Match object; span=(0, 2), match='42'>

'?' part of regex means that '!' is optional.

Watch out for syntax here, it gets tricky.

* r'42!?' means 42 optionally followed by !
* r'42?!' means 4 by optionally followed by 2 followed by !

#### Making multiple characters optional

To make multiple characters optional place them in a group and then place ? after the group.

You can think of the ? as saying, “Match zero or one of the group preceding this question mark.”

``` python
import re
pattern = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
match1 = pattern.search('My number is 415-555-4242')
match1.group()
```

'415-555-4242'

``` python
match2 = pattern.search('My number is 555-4242')
match2.group()
```

'555-4242'

### Matching 0 or more qualifiers

* '*' means match 0 or more
* The qualifier that precedes the star can occur any number of times in the text. It can be completely absent or repeated over and over again.

``` python
import re
pattern = re.compile('Eggs( and spam)*')
pattern.search('Eggs')
```

<re.Match object; span=(0, 4), match='Eggs'>

``` python
pattern.search('Eggs and spam')
```

<re.Match object; span=(0, 13), match='Eggs and spam'>

``` python
pattern.search('Eggs and spam and spam')
```

<re.Match object; span=(0, 22), match='Eggs and spam and spam'>

``` python
pattern.search('Eggs and spam and spam and spam')
```

<re.Match object; span=(0, 31), match='Eggs and spam and spam and spam'>

* While the 'Eggs' part of the string must appear once, there can be any number of ' and spam' following it, including zero instances.

### Matching 1 or More Qualifiers

* Unlike the star, which does not require its qualifier to appear in the matched string, the plus requires the qualifier preceding it to appear at least once. It is not optional.

``` python
pattern = re.compile('Eggs( and spam)+')
pattern.search('Eggs and spam')
```

<re.Match object; span=(0, 13), match='Eggs and spam'>

``` python
pattern.search('Eggs and spam and spam')
```

<re.Match object; span=(0, 22), match='Eggs and spam and spam'>

``` python
pattern.search('Eggs and spam and spam and spam')
```

<re.Match object; span=(0, 31), match='Eggs and spam and spam and spam'>

* The regex 'Eggs(and spam)+' will not match the string 'Eggs', because the plus sign requires at least one ' and spam'.
* You’ll often use parentheses in your regex strings to group together qualifiers so that a quantifier can apply to the entire group.
* For example, you could match any combination of dots and dashes of Morse code with r'(\.|\-)+' (though this expression would also match invalid Morse code combinations).

### Matching a Specific Number of Qualifiers

* Follow a group in your regex with a nr of curly brackets: eg. regex (ha){3} will match 'hahaha' but not 'haha'
* You can also leave out the first or second number in the curly brackets to keep the minimum or maximum unbounded. 
* **(Ha){3,}** will match three or more instances of the (Ha) group, while** (Ha){,5}** will match zero to five instances

```(Ha){3}``` - will match only this specific scenario

```(Ha){3,5}``` - Will match HaHaHa, HaHaHaHa and HaHaHaHaHa, it's alternative of saying (HaHaHa) | (HaHaHaHa) | (HaHaHaHaHa)

``` python
import re
haRegex = re.compile(r'(Ha){3})
match1 = haRegex.search('HaHaHa')
match.group()
```

'HaHaHa'

``` python
match = haRegex.search('HaHa')
match == None
```

True

### Greedy and non-Greedy matching

* Python’s regular expressions are greedy by default, which means that in ambiguous situations, they will match the longest string possible.
* Lazy (Non-greedy) version of curly brackets, matches the shortest string possible.
* Lazy version needs to follow the closing curly "{}" brackets with "?"

``` python
import re
greedy_pattern = re.compile(r'(Ha){3,5}')
match1 = greedy_pattern.search('HaHaHaHaHaHa')
match1.group()
```

'HaHaHaHaHa'

``` python
lazy_pattern = re.compile(r'(Ha){3,5}?')
match2 = lazy_pattern.search('HaHaHaHaHaHaHa')
match.group()
```

'HaHaHa'

### Question mark "?" can have two meanings in regular expressions

* declaring a lazy match
* declaring an optional qualifier.

These meanings are entirely unrelated.

#### Alternatives

You could theoretically get by without using the optional "?" quantifier, or even the `"*"` and `"+"` quantifiers

* The ? quantifier is the same as {0,1}.
* The * quantifier is the same as {0,}.
* The + quantifier is the same as {1,}.

However, the `?`, `*`, and + quantifiers are common shorthand.

### Matching EVERYTHING

* Sometimes you may want to match everything and anything
for example: match `str'First name'` followed by any and all txt and then followed by `str'last name'` followed by `any text`
* **you can use ".*" for that "everything"** (greedy mode)
  * "." char means "any single char except newline"
  * "*" means 0 + of the proceeding chars

``` python
import re
name_pattern = re.compile(r'First name: (.*) Last name: (.*)')
name_match = name_pattern.search('First name: Al Last Name: Sweigart')
name_match.group(1) # 'Al'
Name_match.group(2) # Sweigart
```


* To match in Non-Greedy (Lazy) way use (.*?)
* Both regexes roughly translate to: 'Match an opening angle bracket followed by anything, followed by a closing angle bracket.
* Lazy method stops at the shortest possible str match, while greedy grabs a longest possible str.

#### Matching **LAZY** way

``` python
import re
lazy_pattern = re.compile(r'<.*?>')
match1 = lazy_pattern.search('<To Serve man> for dinner.')
match.group() # '\<To Serve Man>'
```

#### Matching **GREEDY** way

``` python
import re
lazy_pattern = re.compile(r'<.*>')
match1 = lazy_pattern.search('<To Serve man> for dinner.')
match.group() # '\<To Serve man> for dinner.'
```

### Matching All, incl. Newline characters

passing **re.DOTALL** as a 2nd arg in `re.compile()` it will allow `'.'`char to match all chars, including newline

#### * Without .DOTALL

``` python
import re
no_newline = re.compile(r'.*')
no_newline.search('Serve the public trust.\nProtect the innocent. \nUphold the law.').group() 
# 'Serve the public trust.'
```
#### * With re.DOTALL

``` python
import re
with_newline = re.compile(r'.*', re.DOTALL)
with_newline.search('Serve the public trust.\nProtect the innocent. \nUphold the law.').group()
# 'Serve the public trust.\nProtect the innocent. \nUphold the law.'
```

### Matching Start end End of a str

* Caret **"^"** symbol at the start of regex filters for matches at the **beginning** of the searched str
* Dollar sign **"$"** at the end of regex filters for ending with the regex pattern
* You can use both **^ and $ to enforce the whole str to match the regex**

``` python
import re
begin_hello = re.compile(r'^Hello')
begin_hello.search('Hello World') # <re.Match object; span=(0, 5), match='Hello'>
```

* using ``` r'\d$' ``` matches string ending with numeric chars 0-9

``` python
import re
ends_nr = re.compile(r'\d$')
ends_nr.search('Your nr is 445689') # <re.Match object; span=(16, 17), match='**9**'>
```

* to find whole nr string use "+" sign ```(r'\d+$')```

``` python
import re
ends_nr = re.compile(r'\d+$')
ends_nr.search('Your nr is 445689') #<re.Match object; span=(11, 17), match='445689'>
```

* match strings that match at both beginning and end using ```(r'^\d+$')```

``` python
import re
str_nr = re.compile(r'^\d+$')
str_nr.search('123456789') # <re.Match object; span=(0, 9), match='123456789'>
```

* using **"\b"** in regex make it **match only word boundary**
  * start of a word
  * end of a word
  * both start and end
* for example ```(r'\bcat.*?\b')``` will find all words starting with "cat"

``` python
import re
pattern = re.compile(r'\bcat.*?\b')
pattern.findall('the cat found a catapult catalog in the catacombs.')
# ['cat', 'catapult', 'catalog', 'catacombs']
```

* "\B" matches everything that is not in the word boundary (in the middle of word)

``` python
import re
pattern = re.compile(r'\Bcat\B')
pattern.findall('certifi**cat**e')
# ['cat']
pattern.findall('category')
# []
```

## Summary

* `?` matches 0-1 instances of preceding qualifier
* `*` matches 0+ instances
* `+` matches 1+ instances
* `n` exactly n of instances
* `{n,}` matches n+ of instances
* `{,m}` matches 0-m of instances
* `{n,m}` matches n-m (including n,m) of instances
* `{n,m}?`
  * or `*?`
  * or `+?` performs non-greedy (lazy) match
* `^spam` means str must begin with 'spam'
* `spam$` means str must end with 'spam'
* `.` matches all chars **except newline**
* `\d` matches digit
* `\w` matches word
* `\s` matches space character
* `\D , \W, \S` are opposites of above
* `[abc]` matches any character between square brackets (such as a, b or c)
* `[^abc]` matches any char that IS NOT between square brackets
* `(Hello)` groups 'Hello's together as a single qualifier

## Case-INsensitive matching (re.I)

* to make regex case-insensitive use `re.IGNORECASE` or `re.I` as a 2nd argument in `re.compile()`

``` python
import re
pattern = re.compile(r'robocop', re.I)
pattern.search('RoboCop is part man').group()
```

'RoboCop'

```  python
pattern.search('ROBOCOP protects innocent').group()
```

'ROBOCOP'

``` python
pattern.search('have you seen a robocop?').group()
```

'robocop'

it matches str with any casing.

## substituting strings (.sub)

* regex can also replace new text in place of patterns
* `sub()` method accepts **2 arg**
  * 1st str is what should replace any matches
  * 2nd str is str to be matched

``` python
import re
pattern = re.compile(r'Agent \w+')
pattern.sub('CENSORED', 'Agent alice contacted Agent Bob')
```

'CENSORED contacted CENSORED'

### back-reference

* sometimes you may want to replace **part of the matched text** and use it as a part of sub
* you can use `\1, \2, \3` and so on to mean "enter text of group 1,2,3 and so on as a sub"

``` python
import re
pattern = re.compile(r'Agent (\w)\w*')
pattern.sub(r'\1****', 'Agent alice contacted Agent Bob')
```

'a**** contacted B****'

* in this case `\1` replaces whatever text was matched by group 1 with regex

## Managing complex regexes with Verbose Mode

* as the text can be more complex so will regexes
* you can mitigate some of the confusion using `re.VERBOSE` mode 
* verbose mode ignores whitespaces and comments in a regex so you can spread it out and comment if needed

``` python
pattern = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext\.)\s*\d{2,5})?)')
```

### confusing long line of text can be replaced with verbose

``` python
pattern = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # Area code
    (\s|-|\.)?                      # Separator
    \d{3}                           # First three digits
    (\s|-|\.)                       # Separator
    \d{4}                           # Last four digits
    (\s*(ext|x|ext\.)\s*\d{2,5})?   # Extension
    )''', re.VERBOSE)
```

* it is better to use HUMRE module instead though

## Combining re.IGNORECASE, re.DOTALL and re.VEBOSE

* unfortunately re.compile() can only accept 1 second arg...
* BUT you can get around it using pipe | (bitwise)

``` python
regex = compile.('foo'\ re.IGNORECASE | re.DOTALL | re.VERBOSE)
```

## re.escape() method

* `re.escape()` is not mentioned in "Automate the Boring Stuff."
* It takes a string and puts a backslash (`\`) in front of any character that has a special meaning in a regular expression
* Its purpose is to "de-fang" a string, making sure that when you use it inside a regex pattern, it is treated as a literal sequence of characters, not as special instructions.

``` python
import re 

my_string = "example.com+(v1)" # This string has '.', '+', '(', and ')' which are all special in regex 
escaped_string = re.escape(my_string) # Let's escape it 

print(f"Original string: {my_string}") 
print(f"Escaped string: {escaped_string}")
```


[[MOD9 - NOTES Humre]]