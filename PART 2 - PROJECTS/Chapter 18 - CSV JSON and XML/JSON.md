# JSON

- **JSON** stands for **JavaScript Object Notation**
- **Data serialization format** used to store data as **plaintext**
- It was created as a **simpler alternative to XML**
- It is currently the **most popular data serialization format**.
- Uses `.json` extension

## Syntax

- JSON uses the **same syntax** as objects, arrays and data types in **JavaScript** language, and looks quite similar to Python's dictionaries syntax
- does **not require knowledge of JavaScript language**
- `spaces` are **insignificant outside of `"` strings**
- Inside **lists**, you **cannot use trialing commas**

  - `["spam", "eggs"]` - valid JSON
  - `["spam", "eggs",]` - invalid JSON
- `null` is **equivalent** to Python's `None` value
- `true` and `false` are **equivalent** to Python's `True` and `False`
- `[]` and `{}` are **equivalent** to Python's `list` and `dict`
- **All strings use double `"` quotes**

**Example of JSON file**

```json
{
  "name": "Alice Doe",
  "age": 30,
  "car": null,
  "programmer": true,
  "address": {
    "street": "100 Larkin St.",
    "city": "San Francisco",
    "zip": "94102"
  },
  "phone": [
    {
      "type": "mobile",
      "number": "415-555-7890"
    },
    {
      "type": "work",
      "number": "415-555-1234"
    }
  ]
}
```

## json module

- **The `json` module** provides a **way to encode and decode JSON data**
- It is **built-in module** to the Python standard library
- `json.loads()` and `json.dumps()` functions are used to read and write JSON data using Python

## Reading JSON data

- To translate string containing JSON data, pass it to `json.loads()` (load string)
- Note that JSON string always use double quotes
- This should print out data as a Python's Dictionary

```python
import json
json_string = '{
  "name": "Alice Doe",
  "age": 30,
  "car": null,
  "programmer": true,
  "address": {
    "street": "100 Larkin St.",
    "city": "San Francisco",
    "zip": "94102"
  },
  "phone": [
    {
      "type": "mobile",
      "number": "415-555-7890"
    },
    {
      "type": "work",
      "number": "415-555-1234"
    }
  ]
}'

json_string = json.loads(python_data)
print(python_data)
# 
#  This should print out a Python's Dictionary
```


## Writing JSON

- to translate Python data into JSON format use `json.dumps()` (dump string)
- once you have JSON txt as python str value you can write it to a .json file or use it in web request or perform any other operation you can do with a str.

```python
import json
python_data = # This is a Python's dictionary
json_string = json.dumps(python_data)
print(json_string) # This will print out without indentation
json_string = json.dumps(python_data, indent=2) # add indentation for nicer formatting
print(json_string)
```
### There are no comments in JSON format