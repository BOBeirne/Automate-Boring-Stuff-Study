## Q1 - What are escape characters?

they allow manipulation of str using escape chars like \n for newline or \\ to put in \ in a str without it breaking

## Q2 - what are \n and \t escape characters

`\n` is newline
`\t` is horizontal tab (insert TAB in a str)

## Q3 - How can you put \ char in a str

`\\`
## Q4 Why is `"Howl's moving castle"` a valid str

because it uses `""` double quotes

## Q5 - if you don't want to us \n in a str how to put newlines in a str

use triple double quotes `""" """`

## Q6 - what do following expressions evaluate to:

`'hello word!'[1]` - 2nd char of the str
`'hello word!'[0:5]` -  first to 5th char of str
`'hello word!'[:5]` - same as above
`'hello word!'[3:]` - chars from 4th char to end of str

## Q7 - what do following expressions evaluate to:

`'Hello'.upper()` - changes all chars to uppercase
`'Hello'.upper().isupper()` - True
`'Hello'.upper().lower()` - changes all char to lower

## Q8 - what do following expressions evaluate to: 
`'Remember, remember the fifth of november'.split()`

it splits the str into a list for words
`'-'.join('There can be only one'.split())`
prints the string joined by `'-'`

## Q9 - What str methods can you use to right-justify or left justify?

`rjust()` and `ljust()`

## Q10 - how can you trim whitespaces at the end or beginning of each str?

`text = text.strip()`


