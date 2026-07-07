#Customize a coffee order:- small,medium or large with an option for "Extra shot" of expresso.

order_size = "Medium"
extra_shot = True

if extra_shot==True:
    coffee = order_size + " Coffee with an extra shot"
else:
    coffee = order_size + " Coffee"

print("Order:-",coffee)

    
   




