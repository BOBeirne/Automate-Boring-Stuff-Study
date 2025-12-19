# XML

- **XML** stands for **Extensible Markup Language**
- **Data serialization format** used to store data as **plaintext**
- OLD, widely used in **enterprise software**
- Overly **complicated**

## Syntax

- `XML` involves nesting opening and closing tags inside angle brackets `<>` that contain other content **just like HTML**
- use this syntax for **comment** `<!-- comments -->` just like in HTML
- Each tag is called an `element`
- XML is formatted in plaintext with .xml extension
- whitespaces are **insignificant** outside of tags
- There is no `null` value but you can use either of self closing tags
  - `<xsi:nil="true"/>`
  - `<xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>`
- Attributes can use uppercase or lower, but lower is standard
- Attribute values can use either `"` or `'` but standard is `"`

### Attributes vs subelements

**Subelements example**

- One of the biggest reasons of shy XML lost popularty is because of ambigous rules of when to use **attributes** and **subelements** it became too confusing

```xml
<address>
    <street>100 Larkin St.</street>
    <city>San Francisco</city>
    <zip>94102</zip>
</address>
```

**Attribute example:**

```xml
<address street="100 Larkin St." city="San Francisco" zip="94102" />
```


**Example of XML:**

```xml
<person>
    <name>Alice Doe</name>
    <age>30</age>
    <programmer>true</programmer>
    <car xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>
    <address>
        <street>100 Larkin St.</street>
        <city>San Francisco</city>
        <zip>94102</zip>
    </address>
    <phone>
        <phoneEntry>
            <type>mobile</type>
            <number>415-555-7890</number>
        </phoneEntry>
        <phoneEntry>
            <type>work</type>
            <number>415-555-1234</number>
        </phoneEntry>
    </phone>
</person>
```


- Each XML has to **have one root element**
- `<person>` is the root element, it has **subelements**
  - `<name>` and `<age>` - Those ale **child elements** - `<person>` is **their parent element**
- XML is **not valid if it does have more than one root element**

**Example of invalid XML**
```xml
<person><name>Alice Doe</name></person>
<person><name>Bob Smith</name></person>
<person><name>Carol Watanabe</name></person>
```

## Types of XML files

### SVG files

- Scalable Vector Graphics
- Vector 2D graphics
- SVG files are made up of text written in XML

### RSS and Atom feeds

#### RSS

- Really Simple Syndication
- One of earliest web feed formats developed in 90s
- **XML** based
- **RSS 1.0** and **RSS 2.0** are the most popular versions
- **RSS 2.0** is the latest version and supports multimedia content and elements like "enclosure" to link to audio or video files

#### Atom

- **Atom** is another web feed format
- Modern alternative to RSS developed by IETF (Internet Engineering Task Force) in 2005
- **Atom** is a **XML** based format and supports **full** XML syntax
- - It is more favored favoured over RSS due to its **flexibility** handling metadata and **multimedia** content
- Encoded in UTF-8 by default

### Microsoft Word (.docx)

- Microsoft word documents are essentially ZIP-ped XML files with .docx extension

## reading XML

### DOM 

- `xml.dom`
- DOM - Document Object Model
- Reads entire XML into memory at once but it's slower than SAX, therefore it's less suitable for large files
- Make it easier to access data anywhere in the XML

### SAX

- `xml.sax`
- SAX - Simple API for XML
- SAX is a **streaming** XML parser
- SAX is **lightweight** and **fast** but it's less easy to access data anywhere in the XML

### Etree

- `xml.etree`
- Etree - Element Tree
- This module uses `Element` objects to represent CML element and it's child elements

```python
import xml.etree.ElementTree as ET # so we can use ET instead of long name
xml_str = """<person>
    <name>Alice Doe</name>
    <age>30</age>
    <programmer>true</programmer>
    <car xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>
    <address>
        <street>100 Larkin St.</street>
        <city>San Francisco</city>
        <zip>94102</zip>
    </address>
    <phone>
        <phoneEntry>
            <type>mobile</type>
            <number>415-555-7890</number>
        </phoneEntry>
        <phoneEntry>
            <type>work</type>
            <number>415-555-1234</number>
        </phoneEntry>
    </phone>
</person>"""

root = ET.fromstring(xml_str) # this will return Element object containing data from XML
print(root)
```

#### parse() method

- You can also parse XML from a file using this method

```python
import xml.etree.ElementTree as ET
tree = ET.parse('my_data.xml')
root = tree.getroot()
print(root.tag)

# Get list of all immediate child elements
list(root)

# Access child Element of parent Element using index just like in Python's list
root[0].tag
root[0].text
root[3].tag
root[3].text == None # <car/> has no text
# True
root[4].tag
root[4][0].tag
root[4][0].text

# Using for loop to iterate over immediate child elements
for element in root:
	print(elem.tag, '--', elem.text)
# name -- Alice Doe
# age -- 30 ...

# You can also iterate over all children underneath Element using iter() method to filter for XML elements with matching tag name
for element in root.iter('name'):
	print(element.tag, '--', element.text)
# name -- Alice Doe
for element in root.iter('number'):
	print(element.tag, '--', element.text)
# number -- 415-555-7890
# number -- 415-555-1234
```

### xmltodict

- There is no built-in Python module to convert XML text to Python's data structure, so you need to rely on 3rd party module [xmltodict](https://pypi.org/project/xmltodict/)
- `xmltodict` - Convert XML to Python dictionary
- `pip install xmltodict` to install
- `import xmltodict` to import


```python
import xmltodict
xml_str = """<person>
    <name>Alice Doe</name>
    <age>30</age>
    <programmer>true</programmer>
    <car xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>
    <address>
        <street>100 Larkin St.</street>
        <city>San Francisco</city>
        <zip>94102</zip>
    </address>
    <phone>
        <phoneEntry>
            <type>mobile</type>
            <number>415-555-7890</number>
        </phoneEntry>
        <phoneEntry>
            <type>work</type>
            <number>415-555-1234</number>
        </phoneEntry>
    </phone>
</person>"""

python_data = xmltodict.parse(xml_str) # parse and convert to python dictionary
print(python_data)
# {'person': {'name': 'Alice Doe', 'age': '30', 'programmer': 'true', 'car': {'@xsi:nil': 'true', '@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'}, 'address': {'street': '100 Larkin St.', 'city': 'San Francisco', 'zip': '94102'}, 'phone': {'phoneEntry': [{'type': 'mobile', 'number': '415-555-7890'}, {'type': 'work', 'number': '415-555-1234'}]}}}
```

- Notice the `<programmer>` was incorrectly parsed as a str `"True"` instead of Bool, `True`
- Also `<car>` element turned into awkward `'car': {'@xsi:nil': 'true', '@xmlns:xsi':'http://www.w3.org/2001/XMLSchema-instance'}`
- Those are big reasons why XML has fallen behind in favor of other plaintext data formats

## Wiriting XML

- `etree module` is a bit awkward when writing XML, so use `open()` and `write()` instead to write XML yourself

- To create XML from scratch, you need to use `xml.etree` module
  - To create root Element, use `ET.Element()` method
  - To add child elements, use `SubElement()` method
- To get the XML string, use `ET.tostring().decode()` function
  - You need to specify decode format as it is returned in `bytes` by default

**Example using etree**

```python
person = ET.Element('person') # Create root XML element <person>
name = ET.SubElement(person, 'name') # create <name>, and place it under <person>
name.text = 'Alice Doe' # Set the text between <name> and </name> tags
age = ET.SubElement(person, 'age') # create <age>, and place it under <person>
age.text = '30' # Set the text between <age> and </age> tags
programmer = ET.SubElement(person, 'programmer') # create <programmer>, and place it under <person>
programmer.text = 'true' # Set the text between <programmer> and </programmer> tags
car = ET.SubElement(person, 'car') # create <car>, and place it under <person>
car.set('xsi:nil', 'true') # Set the attribute of <car> to be <xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"> which means null
address = ET.SubElement(person, 'address') # create <address>, and place it under <person>
street = ET.SubElement(address, 'street') # create <street>, and place it under <address>
street.text = '100 Larkin St.' # Set the text between <street> and </street> tags

# To get the XML string, use `ET.tostring().decode()` function
ET.tostring(person, encoding='utf-8').decode('utf-8')
```