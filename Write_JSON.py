"""An example of how to represent a group of acquaintances in Python."""
import os
import json

my_group = {
    'Jill' : 
    {
        'Age' : 26,
        'Job' : ['Biologist'],
        'Connections' : {'Friend' : 'Zalika', 'Partner' : 'John'}
    },
    'Zalika' : 
    {
        'Age' : 28,
        'Job' : ['Artist'],
        'Connections' : {'Friend' : 'Jill'}
    },
    'John' : 
    {
        'Age' : 27,
        'Job' : ['Writer'],
        'Connections' : {'Partner' : 'Jill'}
    },
    'Nash' : 
    {
        'Age' : 34,
        'Job' : ['Chef'],
        'Connections' : {'Cousin' : 'John', 'Landlord' : 'Zalika'}
    }
    
}

#Adjustments to get the folder correct
file_loc = os.path.join(os.getcwd(),'Week 3','friend-group','friend_group.json')


with open(file_loc, 'w') as json_data_out:
    json_data_out.write(json.dumps(my_group))
    
with open(file_loc) as json_data_in:
    my_group_file = json.load(json_data_in)

print(my_group_file)
#Functions are not the same in terms of memory address
print(my_group_file is my_group)
#Functions are the same in terms of the data stored within
print(my_group_file == my_group)