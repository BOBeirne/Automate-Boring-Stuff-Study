The Humre page on the Python Package Index is https://pypi.org/project/Humre/.
## [Humre] module (Human-Readable regexes)

* You need to install Humre module before you can use it
* Humre can translate human-readable regex into original regex code to pass into re.compile()
* It is a translator not a replacement for re module!

``` python
from humre import *
regex = exactly(3, DIGIT) + '-' + exactly(3,DIGIT) + '-' + exactly(4,DIGIT)
phone
```

'\\d{3}-\\d{3}-\\d{4}'

### Humre’s constants for the shorthand character classes:

* `DIGIT` and `NONDIGIT` represent `r'\d'` and `r'\D'`, respectively.
* `WORD` and `NONWORD` represent `r'\w`' and `r'\W'`, respectively.
* `WHITESPACE` and `NONWHITESPACE` represent `r'\s'` and `r'\S'`, respectively.
  
### Humre constants exist for escaped characters:

* PERIOD `.`
* PIPE `|`
* DOLLAR_SIGN `$`
* CARET `^`
* QUESTION_MARK `?`  
* ASTERISK `*`
* TILDE `~`  (Not a special character in Python regex)
* HASHTAG `#`  (Only special in verbose mode for comments)
* PLUS `+`
* AMPERSAND `&`(Not a special character in Python regex)
* MINUS `-`
* BACKSLASH`\`
* OPEN_PAREN / CLOSE PAREN `()`
* OPEN_BRACKET / CLOSE_BRACKET `[]`
* CLOSE_BRACE / OPEN_BRACE `{}`

### Humre function | Regex string

* group('A') = `r'(A)'`
  
* optional('A') = `r'A?'`
* either('A', 'B', 'C') = `r'A|B|C'`
* exactly(3, 'A') = `'A{3}'`
* between(3, 5, 'A') = `'A{3,5}'`
* at_least(3, 'A') = `'A{3,}'`
* at_most(3, 'A') = `'A{,3}'`
* chars('A-Z') = `'[A-Z]'`
* nonchars('A-Z') = `'[^A-Z]'`
* zero_or_more('A') = `'A*'`
* zero_or_more_lazy('A') = `'A*?'`
* one_or_more('A') = `'A+'`
* one_or_more_lazy('A') = `'A+?'`
* starts_with('A') = `'^A'`
* ends_with('A') = `'A$'`
* starts_and_ends_with('A') = `'^A$'`
* named_group('name', 'A') = `'(?P<name>A)'`

### Convenience functions

Humre also has several convenience functions that combine common pairs of function calls, instead of using `optional(group('A')) to create '(A)?'`, you can simply call `optional_group('A')`.

#### Convenience function | Function equivalent | Regex string**

* optional_group('A') = optional(group('A')) = `'(A)?'`
  
* group_either('A') = group(either('A', 'B', 'C')) = `'(A|B|C)'`
* exactly_group(3, 'A') = exactly(3, group('A')) = `'(A){3}'`
* between_group(3, 5, 'A') = between(3, 5, group('A')) = `'(A){3,5}'`
* at_least_group (3, 'A') = at_least(3, group('A')) = `'(A){3,}'`
* at_most_group (3, 'A') = at_most(3, group('A')) = `'(A){,3}'`
* zero_or_more_group('A') = zero_or_more(group('A')) = `'(A)*'`
* zero_or_more_lazy_group('A') = zero_or_more_lazy(group('A')) = `'(A)*?'`
* one_or_more_group('A') = one_or_more(group('A')) = `'(A)+'`
* one_or_more_lazy_group('A') = one_or_more_lazy(group('A')) = `'(A)+?'`

#### Passing multiple strings

* All of Humre’s functions except either() and group_either() allow you to pass multiple strings to automatically join them.
* This means that calling `group(DIGIT, PERIOD, DIGIT)` produces the same regex string as group(DIGIT + PERIOD + DIGIT).
* They both return the regex string `r'(\d\.\d)'`.

### Humre constants for common regex patterns

* `ANY_SINGLE` = The `.` pattern that matches any single character (except newlines)
* `ANYTHING_LAZY` = The lazy `.*?` zero or more pattern
* `ANYTHING_GREEDY` = The greedy `.*` zero or more pattern
* `SOMETHING_LAZY` = The lazy `.+?` one or more pattern
* `SOMETHING_GREEDY` = The greedy `.+` one or more pattern

### From humre import *

It helps to import Humre using the `from humre import *` syntax so that you don’t need to put `humre.` before every function and constant.

``` python
import re
from humre import *

phone_regex = group(
    optional_group(either(exactly(3, DIGIT),                # optional area code
        OPEN_PAREN + exactly(3, DIGIT) + CLOSE_PAREN)),
    optional_group(group_either(WHITESPACE, '-', PERIOD)),  # optional separator
    group(exactly(3, DIGIT)),                               # first 3 digits
    group_either(WHITESPACE, '-', PERIOD),                  # separator
    group(exactly(4, DIGIT)),                               # last 4 digits
    optional_group(                                         # optional extension 
        zero_or_more(WHITESPACE),
        group_either('ext', 'x', r'ext\.'),
        zero_or_more(WHITESPACE),
        group(between(2,5, DIGIT))
        )
    )

pattern = re.compile(phone_regex)
match = pattern.search('My number is 415-555-1212.')
print(match.group())
```

415-555-1212

### translating regex into Humre code (not working on pip version)

``` python
import humre
humre.parse(r'\d{3}-\d{3}-\d{4}')
```

### 