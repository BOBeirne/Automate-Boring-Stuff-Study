import openpyxl

wb = openpyxl.Workbook() # Create new workbook object
sheet = wb.active

for i in range(1,11): # create some data in col A
	sheet['A' + str(i)] = i * i

ref_obj = openpyxl.chart.Reference(sheet, 1, 1, 1, 10) # pass the 5 arguments

series_obj = openpyxl.chart.Series(ref_obj, title='first series') # create a series object
chart_obj = openpyxl.chart.BarChart() # create a chart object in BarChart type
chart_obj.title = 'My chart'
chart_obj.append(series_obj) # append the series object to the chart object

sheet.add_chart(chart_obj, 'C5') # add the chart object to the sheet at the location C5

wb.save('chartExample3.xlsx')