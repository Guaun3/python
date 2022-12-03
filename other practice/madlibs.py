# string concatenation
# create string that says "subscribe to ___"
youtuber = "yun"

# method 1
print("subscribe to "+youtuber)
# method 2: format
print("subscribe to {}".format(youtuber))
# method 3: f-string
print(f"subscribe to {youtuber}")

adj = input("adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")
madlib = f"computer programming is so {adj}! It makes me so excited all the time because \
         I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)
