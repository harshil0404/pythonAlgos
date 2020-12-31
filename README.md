# Try This BEAST !
A pizza vendor offers 'x' pizzas and with 'y' toppings. A customer plans to spend around 'c' currency units (eg. c = 760 $). The customer wants to ```order only 1 pizza```, and may order any number of available toppings(0,1,2...), ```can not repeat the same toppings```.

you are given list of prize of PIZZAS ([400,450,600,500]) & TOPPINGS ([50,70,110,30]), customer want's to ```spend most of the cash available with him```.
Simply, your function should return an integer/float(say 'i') ```closest or equal to 'c', customer cannot exceed available cash```.

Example : 
-----------
1)  INPUT :
      pizzas = [400,450,600,500]
      toppings = [50,70,110,30]
      c = 770
    OUTPUT : 
      760, 
      because of two possible cases : (a) pizza(600) + topping(110 + 50) = 760 
                                      (b) pizza(500) + topping(50 + 70 + 30 + 110) = 760
2)  INPUT :
      pizzas = [400,450,600,500]
      toppings = [50,70,110,30]
      c = 600
    OUTPUT : 
      600, 
      because 600 is the prize of the pizza itself so he can spend all the cash.

