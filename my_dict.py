dict = {
   "grocer": "shopkeeper",
    "sinister": "evil or harmful",
    "stern": "very serious and strict",
    "blazing": "shining",
    "conjectures": "hypothesis",
    "extricated": "free",
    "floundering": "walk with great difficulty",
    "lattice": "work of wood"
}
print("options are", dict.keys())
a = input("Enter the word\n")
# print("The meaning that word is:", dict[a])
#Below line will not throw if key is not present
print("The meaning that word is:", dict.get(a))
