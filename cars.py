showroom = set()

showroom.add("Tesla 1")
showroom.add("Tesla 2")
showroom.add("Tesla 3")
showroom.add("Tesla 4")

print(len(showroom))

showroom.add("Tesla 1")
showroom.update(["Tesla 5", "Tesla 6"])
showroom.discard("Tesla 1")

junkyard = ("Beamer", "Bug", "Pickup", "Tesla 2", "Tesla 3", "Tesla 4")

print(showroom.intersection(junkyard))

showroom = showroom.union(junkyard)
showroom.discard("Tesla 6")
showroom.discard("Tesla 5")
showroom.discard("Tesla 4")
showroom.discard("Tesla 3")
print(showroom)
