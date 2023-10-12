l = ["bröd", "smör", "ost", "smör"]


l.append (["ägg", "kött", "smör"])

l.extend (["lax"])

l.remove ("smör")

last = l.pop(3)

l.sort()



print(l)

print(l.index("ost"))