# write a program that prompts the user for input of meal and it's list of ingredients and stores them in a database "meals.db"
# and then allows the user to search for a meal and find the list of ingredients for it
# if user enters 'quit' break out of the loop

import sqlite3, sys, os

script_dir = os.path.dirname(os.path.abspath(__file__)) # get the directory of the script
db_path = os.path.join(script_dir, 'meals.db') # create the path to the database
print(db_path)

# create a database called meals.db
conn = sqlite3.connect(db_path) # connect to the database

# Create 2 tables, one for meals and one for listOfIngredients
conn.execute('CREATE TABLE IF NOT EXISTS meals (name TEXT) STRICT')
conn.execute('CREATE TABLE IF NOT EXISTS Ingredients (name TEXT, meal_id INTEGER, FOREIGN KEY(meal_id) REFERENCES meals(rowid)) STRICT')
#listOfIngredients = [] # create an empty list for listOfIngredients

#Ask user for input
while True:
	try:
		print('OPTION: type "quit" or "q" to exit, "meal" or "m" to add meal and "view" or "v" to view meals currently in the database')
		decision = input('>')

		# Add a new meal
		if decision.lower() == 'meal' or decision.lower() == 'm':
			print('Provide meal name, followed by a colon and a comma-delimited list of list of ingredients in the following format: meal:ingredient1,ingredient2')
			meal = input('>') # get the meal name and list of ingredients from the user
			mealSplit = meal.split(':', 1) # split the string at the first colon
			mealName = mealSplit[0].strip() # store the meal name as a variable "mealName"
			listOfIngredients = mealSplit[1].split(',') # split the string at the commas and store the list of listOfIngredients as a variable "listOfIngredients"
			# print(mealName)
			# print(listOfIngredients)
			conn.execute('INSERT INTO meals (name) VALUES (?)', [mealName]) # insert the meal name into the meals table
			meal_id = conn.execute('SELECT rowid FROM meals WHERE name = ?', [mealName]).fetchone() # get the rowid of the meal
			meal_id_int = int(meal_id[0])
			#print(f'meal ID: {meal_id[0]}')
			#ingredients_to_insert = [(meal_id[0]), ingredient in listOfIngredients] # create a tuple of the rowid and the listOfIngredients
			
			for ingredient in listOfIngredients: # loop through the listOfIngredients
				conn.execute('INSERT INTO ingredients (name, meal_id) VALUES (?, ?)', [ingredient.strip(), meal_id_int]) # insert the listOfIngredients into the listOfIngredients table referencing the meal id
			conn.commit()
			print(f'Added meal "{mealName}"\n with the following list of ingredients: {listOfIngredients}')
			break

		# Search for a meal by either meal name or an ingredient
		if decision.lower() == 'view' or decision.lower() == 'v':
			while True:
				print('Type "meal" to search for a meal, "ingredient" to search for an ingredient or "quit" to exit')
				decision_2 = input('>')
				
				# search by meal name
				if decision_2.lower() == 'meal' or decision_2.lower() == 'm':
					#print(f'Current list of meals in the database: {conn.execute("SELECT name FROM meals").fetchall()}') # not as pretty print
					print(f'Current list of meals in the database:') 
					meal_names = [meal[0] for meal in conn.execute('SELECT name FROM meals').fetchall()] # get the list of meal names from the database
					print(meal_names)
					mealName = input('Provide a meal name:').lower()
					mealNameRowID= conn.execute('SELECT rowid FROM meals WHERE name = ?', [mealName]).fetchall() # get the rowid(foreign key for ingredients table) of the meal matching the name
					mealRowID = mealNameRowID[0][0] # get the integer value of the rowid
					#print(f'{mealRowID} - ID') # print the rowid for testing
					ingredientList = conn.execute('SELECT * FROM ingredients WHERE meal_id =?', [mealRowID]).fetchall() # get the list of ingredients for the meal
					print(f'Meal Name: {mealName} Ingredients: {ingredientList}')
					break

				# search by ingredient name
				elif decision_2.lower() == 'ingredient' or decision_2.lower() == 'i':
					ingredientName = input('Provide an ingredient name:').strip().lower()
					ingredientID = conn.execute('SELECT meal_id FROM ingredients WHERE name = ?', [ingredientName]).fetchall() # get all rowids of the ingredients matching the name
					if not ingredientName:
						print('No results found')
					else:
						#print(f'{ingredientID} - ID') # print the rowids for testing 
						MealIDList = [] # create an empty list to store the rowids
						for row in ingredientID:
							MealIDList.append(row[0]) # append the rowids to a list
						#print(MealIDList) # print the list for testing
						for id in MealIDList:
							mealName = conn.execute('SELECT name FROM meals WHERE rowid = ?', [id]).fetchall() # get the meal names for the rowids
							strippedMealName = mealName[0][0].strip()
							print(f'Meal Name: {strippedMealName}')
							print('Ingredients:')
							ingredientList = conn.execute('SELECT name FROM ingredients WHERE meal_id =?', [id]).fetchall() # get the list of ingredients for the meal
							for ingredient in ingredientList: # loop through the list of ingredients if there are more than one occurrence of the same ingredient
								strippedIngredients  = ingredient[0].strip() # strip the whitespaces
								print(strippedIngredients) # print the ingredients
								break

				# Exit option
				elif decision_2.lower() == 'quit' or decision_2.lower() == 'q':
					sys.exit()
				else:
					print('Invalid input')

		# Exit option
		if decision.lower() == 'quit' or decision.lower() == 'q':
			print('Goodbye!')
			sys.exit()
		else:
				print('Invalid input, try again')

	except IndexError: # if the input is not long enough
		print('Invalid syntax, try again')
	except ValueError: # if the input is not an integer
		print('Invalid syntax, try again')
	except EOFError: # CTRL + Z
		print('Quitting program...')
		sys.exit()