import random

"""
This list itemizes each category of food, it may be rearranged to your taste.
It is a dynamic list and may never be able to satisfy particular standards for completeness. 
You can help by adding missing items which you would prefer on each category.
"""

list1 = "Rice", "Yam", "Pasta", "Noodles", "Semo with Efo Riro", "Amala with Ewedu", "Jollof Rice"

list2 = "Plantain", "Snacks", "Bread and Beans", "Snacks and Soda", "Iyan", "Puff-Puff with Malt", "Beans and Plantain"

list3 = "Potato", "Carrot", "Bacon and eggs", "Porridge", "Bread with Akara", "Moi Moi with Pap", "Salad and Fried Rice"

breakfast = random.choice(list1)
lunch = random.choice(list2)
dinner = random.choice(list3)

print(f"{breakfast} is for breakfast")
print(f"{lunch} is for lunch")
print(f"{dinner} is for dinner")
