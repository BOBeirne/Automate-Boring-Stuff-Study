# Write a program that opens sweigartcats.db database and lists all cats that don’t have vaccines named 'rabies', 'FeLV', and 'FVRCP'. 
# Also, check the database for errors by finding all vaccines that were administered on a date before the cat’s birthday.

import sqlite3, pprint, os

script_dir = os.path.dirname(os.path.abspath(__file__)) # get the directory of the script
db_path = os.path.join(script_dir, 'sweigartcats.db') # create the path to the database
#print(db_path) # TEST the path
conn = sqlite3.connect(db_path, isolation_level=None) # connect to the database

#print(conn.execute('SELECT name FROM sqlite_schema WHERE type="table"').fetchall()) # SQL query for all tables in the database
#print(conn.execute('PRAGMA TABLE_INFO(cats)').fetchall()) # SQL query for all columns in the table cats
#print(conn.execute('PRAGMA TABLE_INFO(vaccinations)').fetchall()) # SQL query for all columns in the table vaccinations
#print(conn.execute('SELECT cat_id FROM vaccinations').fetchall()) # check all vaccination records in th vaccinations table

# check for all cats that contain 'rabies', 'FeLV', OR 'FVRCP'
vaccinated_cats = conn.execute('SELECT * FROM cats INNER JOIN vaccinations ON cats.rowid = vaccinations.cat_id').fetchall() # SQL query for all cats in the database in the cats table with any vaccination
vaxxed_cats = set() # there are duplicates in vaccinated cats list so we use set to remove the duplicates
for cat in vaccinated_cats:
	vaxxed_cats.add(cat[0]) # add the vaccinated cat name to the list
print(f'Vaccinated cats: \n {", ".join(vaxxed_cats)}') # print the list of cats that have been vaccinated


# print all cats that are not vaccinated by comparing the list of all cats to the list of vaccinated cats
unvaccinated_cats = []

for cat in conn.execute('SELECT rowid, * FROM cats').fetchall():
	if cat[0] not in vaxxed_cats:
		unvaccinated_cats.append(cat[1]) # add the unvaccinated cat name to the list
print(f'Unvaccinated cats: \n {", ".join(unvaccinated_cats)}') # print the list of cats that have not been vaccinated


# TODO check for all vaccines that were administered on a date before the cat’s birthday

vaxedCatBirthdays = conn.execute('SELECT * FROM cats INNER JOIN vaccinations ON cats.rowid = vaccinations.cat_id').fetchall()
#print(vaxedCatBirthdays) # testing
susVaccinations = set() # there may be duplicates
for cat in vaxedCatBirthdays: # loop through each vaccination record for each cat in the list
	if cat[5] < cat[1]: # if the vaccination date is before the cat's birthday
		susVaccinations.add(cat[0])  # add the cat name to the list
if susVaccinations == set(): # if the list is empty
	print('No suspicious vaccination dates found')
else:
	print(f'suspicious vaccination dates: \n {", ".join(susVaccinations)}') # print the list of cats that have been vaccinated on a date before their birthday



















##########################################################################################
# This database requires certain steps explained in Chapter 16 to be executed on the downloaded database first as the original has no vaccination records
#
# 1) First, enable the foreign key support in the database
#conn.execute('PRAGMA foreign_keys = ON') 
#
# 2) Create the vaccinations table
#conn.execute('CREATE TABLE IF NOT EXISTS vaccinations (vaccine TEXT, date_administered TEXT, administered_by TEXT, cat_id INTEGER, FOREIGN KEY(cat_id) REFERENCES cats(rowid)) STRICT')
# 
# 3) Add vaccinations to the vaccinations table
#conn.execute('INSERT INTO vaccinations VALUES ("rabies", "2023-06-06", "Dr. Echo", 1)')
#conn.execute('INSERT INTO vaccinations VALUES ("FeLV", "2023-06-06", "Dr. Echo", 1)')
#conn.execute('INSERT INTO vaccinations VALUES ("rabies", "2023-07-11", "Dr. Echo", 23)')
#
# if you run into issues try this syntax
#conn.execute('INSERT INTO vaccinations (vaccine, date_administered, administered_by, cat_id) VALUES ("rabies", "2023-06-06", "Dr. Echo", 1)')
#
# 4) Get all vaccinated cats to confirm that the vaccinations table has been created correctly
#conn.execute('SELECT * FROM cats INNER JOIN vaccinations ON cats.rowid = vaccinations.cat_id').fetchall()
#
# OPTIONAL: Remove the vaccinations table if you run into issues and need to start again
#conn.execute('DROP TABLE IF EXISTS vaccinations') # Drop the vaccinations table if it already exists
#
##########################################################################################