# Matplotlib module

- [Documentation](https://matplotlib.org/)
- `import matplotlib.pyplot as plot`
- The `Matplotlib` library can create a wide variety of graphs for use in **professional** publications
- terms `plot`, `graph` and `chart` are used interchangably in the `Matplotlib` library
- Use `.savefig()` to save the plot
- Use `.show()` to show the plot, make sure to use `.save()` method before, as `.show()` method resets the data

## Line graph

- to create a simple, 2D line graph with 2 axes

```python
import matplotlib.pyplot as plot

x_val = [0,1,2,3,4,5]
y_val = [10,13,15,18,16,20]
y_val2 = [9,11,18,16,17,19]

plot.plot(x_val, y_val)
plot.plot(x_val, y_val2)

plot.savefig('linegraph.png')
print('completed')
plot.show() # show result, also resets the data, use save before show!
```

## scatter plot

- use `.scatter()` method to create a scatter plot

```python
import matplotlib.pyplot as plot

x_val = [0,1,2,3,4,5]
y_val = [10,13,15,18,16,20]
y_val2 = [9,11,18,16,17,19]

plot.scatter(x_val, y_val)
plot.scatter(x_val, y_val2)

plot.savefig('scatterplot.png')
print('completed')
plot.show() # show result, also resets the data, use save before show!
```

## Bar graph

- use `.bar()` method to create a bar graph

```python
import matplotlib.pyplot as plot
categories = ['Cats', 'Dogs', 'Mice', 'Moose'] # x axis
values = [100, 200, 300, 400] # y axis

plot.bar(categories, values)

plot.savefig('bargraph.png')
print('completed')
plot.show() # show result, also resets the data, use save before show!
```

## Pie chart

- use `.pie()` method to create a pie chart
- the `.pie()` method takes an optional keyword argument `autopct` for eg `'%.1f%%'` string specifies that the number should show one digit after the decimal point. 
- If you leave this keyword argument out of the function call, the pie chart won’t list the percentage text.
- `Matplotlib` **automatically picks the colors for each slice**, but **you can customize this behavior**, along with many other aspects of the graphs you create.

```python
import matplotlib.pyplot as plot

labels = ['Cats', 'Dogs', 'Mice', 'Moose'] # names of slices
slices = [100, 200, 300, 400] # sizes of slices

plot.pie(slices, labels=labels, autopct='%.1f%%') # autopct shows the percentage of each slice

plot.savefig('piechart.png')
print('completed')
plot.show() # show result, also resets the data, use save before show!
```

## Additional Components

- Check out [Matplotlib documentation](https://matplotlib.org/) for all features
- Add **marker color and label** using optional arguments
  - `o` specifies a **circle**
  - `s` specifies a **square**
  - `color` specifies the **color**, `b` for blue, `r` for red
  - `label` specifies the **label**
- Add **legend** using `.legend()`
- Add **title**, x and y axis **label** using `.title()`, `.xlabel()` and `.ylabel()`
- To enable graph image **grid**, use `.grid(True)`

```python
import matplotlib.pyplot as plot

x_val = [0,1,2,3,4,5]
y_val = [10,13,15,18,16,20]
y_val2 = [9,11,18,16,17,19]

# Add marker color and label
plot.plot(x_val, y_val, marker='o', color='b', label='Line 1') # o makes a circle for each point
plot.plot(x_val, y_val2, marker='s', color='r', label='Line 2') # s makes a square for each point

plot.legend() # add legend
plot.xlabel('X-axis Label') # add x axis label
plot.ylabel('Y-axis Label') # add y axis label
plot.title('Graph Title') # add title
plot.grid(True) # add grid

plot.savefig('additionalComponents.png')
plot.show()
```