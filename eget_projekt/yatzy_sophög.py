choices = {1: "tvef", 2: "dqdq"}

table = {1: "sifjow", 2: "dqdq", 3: "tvefd", 4: "tvef"}
list = ["sifjow", "dqdq", "tvefd", "tvef"]

placement = 1

stake = choices.get(placement)
investment = list.index(stake)

print(investment)

list.pop(list.index(stake))
print(list)