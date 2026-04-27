students = [
    {"tst": "test", "name": "jss"}, 
    {"tst": "no", "name": "still no"},
    {"tst": "test", "name": "kinda"}
]

t = next(students for students in students if students["tst"] == "test")
print(t)

print(5+2,5-2,5*2,5/2,5**2,5//2,5%2)