vards = "Simona"

failanosaukums = "woah.txt"
with open(failanosaukums, "w", encoding="utf-8") as f:
    f.write(vards)
    # f.writelines(vards)

# failanosaukums = "woah.txt"
# with open(failanosaukums, "a", encoding="utf-8") as f:  <- append.
    # f.write(vards)