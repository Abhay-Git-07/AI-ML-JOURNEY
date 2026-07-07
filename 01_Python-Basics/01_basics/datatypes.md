# Data types/Object types

1. Number - 1234,3.14,3+4j,fraction(),0b111

2. String - 'spam',b'a\x01c'

3. List - square brackets[],list inside list is possible

4. Tuples - paranthesis(),no tuple inside tuple

5. Dictonary - curly braces{},key:value,{'taste':'yum'}

6. Set - {a,b,c},set("abc")

7. Boolean - True,False

8. None - None


# String functions

1. Replace() - To replace words in string


2. Split() - To convert string into list

 join()- To convert list to string

         ex- print("".join(chai))
            here it will join all elements of string ..........
            agr space chiye ya , chiye to "" mai wo cheez daldo


3. Strip() - To remove spaces before and after a string

4. Lower(),Upper() - To convert in uppercase or lowercase

5. Find() - To find a word or character

6. Count() - To find no of times a word is repeated in string

7. format() - To add variables in string 

      example: chai_type="MAsala"
               quantity = 2
               order = "I ordered {} cups of {} chai"
               print(order.format(quantity,chai_type))

8. len() - To print length of string



# List

1. join()- To convert list to string

         ex- print("".join(chai))
            here it will join all elements of string ..........
            agr space chiye ya , chiye to "" mai wo cheez daldo

2. append() - To add an element in the end of a list
      Ex- tea_varities.append("Masala")

3. pop() - To remove last value
      ex- tea_varities.pop()

4. remove() - To remove a particular element            
      Ex- tea_varities.remove("Oolong")

5. insert() - To add an element in list at any position
      Ex- tea_varities.insert(1,"Green")

6. copy() - To create a copy of list in memory 
      Ex - Chai=tea_varities.copy()  

7. **To print a particular range**

       squares = [x**2 for x in range(10)]
       cube = [y**3 for y in range(10)]


# Dictonaries

**chai_type = {"Masala":"spicy", "Ginger":"zesty", "Green":"mild"}**

1. get() - To get the values from dictonary
      Ex- print(chai_type.get("Ginger")

2. chai_type["Green"] = "Fresh"
      This will change the value of Green from zesty to fresh

3. Apply for loop to print the keys
      for chai in chai_type:
            print(chai)

4. **To print values along with keys**
      WE CAN USE items().....

      1. for chai in chai_type:
            print(chai,chai_types[chai])

      2. for key,value in chaitype.items():
            print(key,value)

5. len() - To print length of dictonary(it print the no of keys)

6. **To add new key and vaule in dictonary**
      chai_type["Earl Grey"] = "citrus"

7. **To remove particular key and value**
      1. pop()
      Ex - chai_type.pop("Earl Grey")
      2. del
      Ex - del chai_type["Green"]

8. popitem() - To remove the last key and value
      Ex - chai_type.popitem()

9. copy() - To copy dictonary in memory

10. *loops in dict*
      square_nums = {x:x**2 for x in range(10)}
      **To remove all values from it** 
      1. use clear()
            square_nums.clear()

11. **TO create a new dictonary**
      keys = ["Masala", "Ginger", "Lemon"]
      default_value = "Delicious"
      1. new_dict = dict.fromkeys(keys,default_value)     


# Tuples
. () uses paranthesis 
.. similar to lists just not mutable

tea_types = ("Masala","Ginger")
more_tea = ("Herbal","Lemon")

1. TO ADD TWO TUPLES
   all_tea = more_tea + tea_types

2. count() = No of times an element is present

