# Hello, Below is a list of the top 12 produce items that found the
#  highest amounts of pesticides attached to them after reasearch according to an articled
# posted by delish in 2019, found here: https://www.delish.com/food-news/a26872638/dirty-dozen-foods-list-2019/

#This is simply for study purposes to understanding list items in python.

#Say I have this list of items, say I wanted to seperate them into fruits and vegetables.
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches",
#                 "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

#I could make two seperate lists like so, but these two lists are related, because theyre within
# the high pesticied list, so how do we achieve this?
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

#Well we can make a list within a list.
dirty_dozen = [fruits, vegetables]

#with the use of these brackets in our print statement we can choose between which nested list item 
#in this case either 0 or 1/ fruits or vegetables. and the second bracket would select the index item
#from the list chosen by the first bracket. 
#in this case we've selected the nested list item fruits, and we've chosen apples from that list. 
print(dirty_dozen[0][2])