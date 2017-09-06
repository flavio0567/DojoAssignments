'''
 Lists to Dict Assignment '''


def make_dict(arr1, arr2):

    new_dict = {}
    if len(arr1) >= len(arr2):
        new_dict = zip(arr1,arr2)
    else:
        new_dict = zip(arr2,arr1)

    return new_dict

favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]

x =make_dict(favorite_animal, name)
print (x)
