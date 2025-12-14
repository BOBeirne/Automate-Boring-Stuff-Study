# TSV

- TSV stands for "Tab-Separated Values"
- They use .tsv extension
- Just like [[CSV]] files, but use tabs instead of commas
- also use `csv module` to read and write them
- Passing `delimiter='\t'` and `lineterminator='\n\n'` changes the delimiter to a tab and the line terminator to two newlines
  - Cells - use `delimiter` separated by TABs 
  - Rows - use `terminator` separated by double-space

```python
import csv
output_file = open('output.tsv', 'w', newline='') # newline='' is needed to prevent extra line, use w as write mode
output_writer = csv.writer(output_file, delimiter='\t', lineterminator='\n\n') # lineterminator='\n\n' is needed to prevent extra line and use \t as delimiter instead of commas

output_writer.writerow(['spam', 'eggs', 'bacon', 'ham']) # write row
# 21
output_writer.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
# 30
output_writer.writerow([1, 2, 3.141592, 4])
# 16
output_file.close()
```