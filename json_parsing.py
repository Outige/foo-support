import json

#?#################################################
#?	parse functions
#?#################################################

def file_to_json(fname):
	struct = []
	for line in open(fname, 'r'):
		struct.append(json.loads(line))
	return struct

#?#################################################
#?	sql functions
#?#################################################

def zappos_to_sql(f):
	zappos = file_to_json('zappos.json')
	f.write("--*\n--* zappos\n--*\nINSERT INTO product_apis (id, provider, status) VALUES (DEFAULT, 'zappos', 0);\n\n")

	# products
	for x in zappos:
		f.write("INSERT INTO products (id, api_id, product_id, name, price, rating, brand, link, description, status)" + 
		" VALUES (DEFAULT, 1, '" + str(x['id']) + "', '"  + x['name'] + "', " + str(x['price']) + ", " +
		str(x['rating']) + ", '" + x['brand'] + "', '" +x['productUrl'] + "', " + "NULL" + ", " + "0"+ ");\n")
	f.write('\n')

	# photos
	i = 1
	for x in zappos:
		f.write("INSERT INTO product_images (id, product_id, image_link)" +
		" VALUES (DEFAULT, " + str(i) + ", '" + x['thumbnailImageUrl'] + "');\n")
		i+=1
	f.write('\n')


def makeup_to_sql(f):
	makeup = file_to_json('makeup.json')[0:20]
	f.write("--*\n--* makeup\n--*\nINSERT INTO product_apis (id, provider, status) VALUES (DEFAULT, 'makeup', 0);\n\n")
	count = 0

	# products
	for x in makeup:
		# print(x['product_link'])
		# break
		if x.get('rating', 0) is None:
			x['rating'] = 'NULL'
		if x.get('price', 0) is None:
			x['price'] = 'NULL'
		if x.get('brand', 0) is None:
			x['brand'] = 'NULL'
		if x.get('product_link', 0) is None:
			x['product_link'] = 'NULL'

		x['name'] = x['name'].replace("'","''")
		x['brand'] = x['brand'].replace("'","''")
		x['description'] = x['description'].replace("'","''")
		f.write("INSERT INTO products (id, api_id, product_id, name, price, rating, brand, link, description, status)" + 
		" VALUES (DEFAULT, 2, '" + str(x['id']) + "', '"  + x['name'] + "', " + str(x['price']) + ", " +
		str(x.get('rating', 0)) + ", '" + x['brand'] + "', '" + x['product_link'] + "', '" + x['description'] + "', " + "0"+ ");\n")
		count+=1
	f.write('\n')

	# photos
	i = 21
	for x in makeup:
		f.write("INSERT INTO product_images (id, product_id, image_link)" +
		" VALUES (DEFAULT, " + str(i) + ", '" + x['image_link'] + "');\n")
		i+=1
	f.write('\n')

		

#?#################################################
#?	main
#?#################################################
if __name__ == '__main__':

	f = open('products.sql', 'w')
	f.close()

	f = open('products.sql', 'a+')
	f.write("\c alpha\n\n")
	zappos_to_sql(f)
	makeup_to_sql(f)
	f.close()
