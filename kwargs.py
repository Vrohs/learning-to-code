# exploring more about **kwargs

dict_population_info = {
    "Name" : "John",
    "D.O.B" : "11/8/1999",
    "Age" : 21,
    "Father's Name" : "Jack"
 }

def print_population_info(**kwargs):
    for key, value in kwargs.items():
        print(key,":", value)
   
print_population_info(**dict_population_info)