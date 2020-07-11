import requests
import json

def json_to_file(products, api):
    # save json
    fname = api + '.json'
    dump_file = open(fname, "w")
    for item in products:
        json.dump(item, dump_file)
        dump_file.write("\n")
    dump_file.close()
    
    # save keys
    fname = api + '.keys'
    dump_file = open(fname, "w")
    keys = set()
    for product in products:
        for key in product.keys():
            keys.add(key)
    for key in keys:
        dump_file.write(key + "\n")
    dump_file.close()


#?#################################################
#?	get functions
#?#################################################

def get_zappos_products():
    url = "https://zappos-6pm-findzen-vrsnl-shops.p.rapidapi.com/products?page=1"
    headers = {
        'x-rapidapi-host': "zappos-6pm-findzen-vrsnl-shops.p.rapidapi.com",
        'x-rapidapi-key': "528d5db260mshd951243b8a4c7d4p153ffcjsnb324b534ca97"
        }
    response = requests.request("GET", url, headers=headers).json()
    total = response['total']
    entities = response['entities']
    return entities

def get_makeup_products():
    url = "https://makeup.p.rapidapi.com/products.json"
    headers = {
        'x-rapidapi-host': "makeup.p.rapidapi.com",
        'x-rapidapi-key': "528d5db260mshd951243b8a4c7d4p153ffcjsnb324b534ca97"
        }

    response = requests.request("GET", url, headers=headers).json()#, params=querystring)
    return response

if __name__ == '__main__':
    # j = get_zappos_products()
    # json_to_file(j, 'zappos')

    j = get_makeup_products()
    json_to_file(j, 'makeup')