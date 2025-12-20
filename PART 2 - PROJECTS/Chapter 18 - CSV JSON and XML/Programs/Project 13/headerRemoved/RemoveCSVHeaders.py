# Remove headers from multiple CSV files at once

# TODO Walk directory to find all csv files and for each file Open file -> read the contents -> rewrite contents without 1st row -> save under same filename


import os, csv

os.makedirs('headerRemoved', exist_ok=True) # check if file exists, if not create folder to store changed files in

# Loop through files in cwd
for csv_file in os.listdir('.'): # for all files in cwd
   if not csv_file.endswith('.csv'): # if file is not csv
      continue # skip it
   
   print('Removing header from' + csv_file + '...')

   # TODO read csv
   csv_rows = []
   csv_file_obj = open(csv_file)
   csv_reader = csv.reader(csv_file_obj)

   # loop through each row
   for row in csv_reader:
      if csv_reader.line_num == 1: # if the row is the 1st row
         continue # skip it
      csv_rows.append(row)
   csv_file.close() # save and close file after processing

   # TODO write csv
   csv_file_obj = open(os.path.join('headerRemoved', csv_file) 'w' newline='')
   csv_writer = csv.writer(csv_file)
   for row in csv_rows:
      csv_writer.writerow(row) #save each row one by one
   csv_file.close()