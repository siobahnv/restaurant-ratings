def print_dictionary(current_ratings):
	current_ratings = sorted(current_ratings.items())
	for restaurant, rating in current_ratings:
		print(restaurant + " is rated at a " + str(rating) + ".")


def clean_ratings(filename):
	my_file = open(filename)
	ratings = {}
	for line in my_file:
		line = line.strip()
		restaurant, rating = line.split(":")
		ratings[restaurant] = rating
	ratings = sorted(ratings.items())
	# for restaurant, rating in ratings:
	# 	print(restaurant + " is rated at a " + rating + ".")

	return dict(ratings)


def get_new_rating(original_ratings):
	new_restaurant = input("What would you like to enter? ")
	new_restaurant = new_restaurant.capitalize()
	try:
		new_score = int(input("What would you score it as? "))

		if type(new_score) == int and new_score >= 1 and new_score <= 5:

			original_ratings[new_restaurant] = new_score
			return original_ratings

		else:
			print("Please enter a valid rating. ")
			get_new_rating(ratings)
	except ValueError:
		print("Please enter a number")
		get_new_rating(ratings)




# def get_new_rating(original_ratings):
# 	new_restaurant = input("What would you like to enter? ")
# 	new_score = (input("What would you score it as? "))

# 	valid_scores = ["1", "2", "3", "4", "5"]

# 	if new_score in valid_scores:

# 		original_ratings[new_restaurant] = new_score
# 		original_ratings = sorted(original_ratings.items())
			
# 		for restaurant, rating in original_ratings:
# 			print(restaurant + " is rated at a " + (rating) + ".")
		
# 	else:
# 		print("Please enter a valid rating. ")
# 		get_new_rating(ratings)

def restaurant_ratings(filename):
	ratings = clean_ratings(filename)
	while True:

		user_input = input("What would you like to do? (S)ee all ratings, (A)dd new restaurant, or (Q)uit. ")

		if user_input.upper() == "S":
			print_dictionary(ratings)
		elif user_input.upper() == "A":
			get_new_rating(ratings)
		elif user_input.upper()== "Q":
			print("Goodbye!")
			break
		else:
			print("Please enter a valid command")


restaurant_ratings("scores.txt")