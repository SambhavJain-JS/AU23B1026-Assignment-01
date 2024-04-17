from ice_cream import * 

print('Enter scoop size you want:\n1.small\n2.medium\n3.Large')
scoop_size=input()

print('Enter toppings of your wish:\n1.sprinkles\n2.nuts\n3.chocochips\n4.chocklet')
toppings=input().split(',')

print('Choose Shake flower:\n1.nuts\n2.fruit')
flavour=input()


add_topping(scoop_size ,*toppings)
make_shake(flavour)

