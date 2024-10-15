"""An example of how to represent a group of acquaintances in Python."""

my_group = {
    'Jill' : 
    {
        'Age' : 26,
        'Job' : ['Biologist'],
        'Connections' : {'Friend' : 'Zalika', 'Partner' : 'John'}
    },
    'Zalika' : 
    {
        'Age' : 26,
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

print(my_group)



