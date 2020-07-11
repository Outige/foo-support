import json

#?#################################################
#?	helper functions
#?#################################################

def is_restaurant(categories):
	#* not a restaurant if categories == None
	if (not categories):
		return 0

	#* is a business in a food category?
	match_categories = ["restaurants", "food"]
	tokens = categories.split(", ")
	for token in tokens:
		for match in match_categories:
			if (token.lower() == match):
				return 1
	return 0

#?#################################################
#?	parse functions
#?#################################################

def parse_business():
	count = 0
	dump_file = open("json_files/" + CITY_TO_PARSE + "/business_reduced.json", "w")
	for line in open('json_files/business.json', 'r'):
		business = json.loads(line)
		if (is_restaurant(business["categories"]) and business["city"] == CITY_TO_PARSE):
			json.dump(business, dump_file)
			dump_file.write("\n")
			count += 1
	dump_file.close()
	print(count, "Restaurants")

def parse_review():
	business_hash = {}
	for line in open('json_files/' + CITY_TO_PARSE  + '/business_reduced.json', 'r'):
		business = json.loads(line)
		business_hash[business["business_id"]] = business
	i = 0
	count = 0
	dump_file = open("json_files/" + CITY_TO_PARSE + "/review_reduced.json", "w")
	for line in open('json_files/review.json', 'r'):
		review = json.loads(line)
		if (business_hash.get(review["business_id"], None)):
			json.dump(review, dump_file)
			count += 1
			dump_file.write("\n")
		i += 1
	print(count, "Reviews")

def parse_user():
	review_hash = {}
	for line in open('json_files/' + CITY_TO_PARSE  + '/review_reduced.json', 'r'):
		review = json.loads(line)
		review_hash[review["user_id"]] = review
	i = 0
	count = 0
	dump_file = open("json_files/" + CITY_TO_PARSE + "/user_reduced.json", "w")
	for line in open('json_files/user.json', 'r'):
		user = json.loads(line)
		if (review_hash.get(user["user_id"], None)):
			json.dump(user, dump_file)
			count += 1
			dump_file.write("\n")
		i += 1
	print(count, "Users")

def parse_photos():
	business_hash = {}
	for line in open('json_files/' + CITY_TO_PARSE  + '/business_reduced.json', 'r'):
		business = json.loads(line)
		business_hash[business["business_id"]] = business["business_id"]
	i = 0
	count = 0
	dump_file = open("json_files/" + CITY_TO_PARSE + "/photo_reduced.json", "w")
	for line in open('json_files/photo.json', 'r'):
		photo = json.loads(line)
		if (business_hash.get(photo["business_id"], None)):
			json.dump(photo, dump_file)
			count += 1
			dump_file.write("\n")
	print(count, "Photos")

CITY_TO_PARSE = "Mississauga"
print("City: " + CITY_TO_PARSE)
parse_business()
parse_review()
parse_user()
parse_photos()