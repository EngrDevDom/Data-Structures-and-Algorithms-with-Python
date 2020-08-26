# Creating Objects and Calling Methods

boyDog = Dog("Mesa", 5, 15, 2004, "WOOOF")
girlDog = Dog("Sequioa", 5, 6, 2004, "barkbark")

print(boyDog.speak())
print(girlDog.speak())

print(boyDog.birthDate)
print(girlDog.birthDate)

boyDog.changebark("woofywoofy")
print(boyDog.speak())

