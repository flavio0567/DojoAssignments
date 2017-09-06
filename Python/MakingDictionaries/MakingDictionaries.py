'''
Making and Reading from Dictionaries Assignment'''

personal_info = {"name":"Anna",
                 "age":"21",
                 "country_of_birth":"The United States",
                 "favorite_language":"Python"}


def personalinfo():

    print "My Name is ", personal_info["name"]
    print "My age is ", personal_info["age"]
    print "My country of birth is ",  personal_info["country_of_birth"]
    print "My favorite language is ",  personal_info["favorite_language"]


personalinfo()