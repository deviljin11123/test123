drinks = [
   {
      "id": 1,
      "drink": "Ice Lemon Tea",
      'price': 5
   },
   {
      "id": 2,
      "drink": "Coca-Cola",
      'price': 3
   },
   {
      "id": 3,
      "drink": "Sprite",
      'price': 4
   },
   {
      "id": 4,
      "drink": "Revive",
      'price': 3
   },
   {
      "id": 5,
      "drink": "100-Plus",
      'price': 3
   },
   {
      "id": 6,
      "drink": "Tiger",
      'price': 12
   }
]
addedDrinks = []

def addDrink(drink_id):
    for drink in drinks:
        if drink['id'] == drink_id:
            addedDrinks.append(drink)
            return True
    return False

print("-- Please choose a drink to buy: --\n")

total = 0
stillBuying = True

for i in drinks:
   print(f"Drink: {i['drink']} --- Price: {i['price']} --- ID: {i['id']}")
def vendingMachine(drinks, stillBuying, addedDrinks):
   while stillBuying:
      buy = int(input("\nEnter the id to select drink: (0 to exit)"))
      if buy == 0:
         stillBuying = False
      elif addDrink(buy):
        print("Drink has been added")

   if not stillBuying:
      total_sum = sum(item.get('price', item.get('itemPrice')) for item in addedDrinks)
      print(f"\nTotal sum of selected items: ${total_sum}")
def sumItem(item):
   sumItems = 0
   for i in item:
      sumItems += i["itemPrice"]
   return sumItems

# Main Code
vendingMachine(drinks, stillBuying, addedDrinks)