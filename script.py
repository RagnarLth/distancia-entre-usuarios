users = [        
            {"user": "userA",  
            "Following": ["userB", "userD","userE", "userG"] },
            { "user": "userB",  
            "Following": ["userC", "userJ","userI", "userE"] },
            { "user": "userC",  
            "Following": ["userM", "userN","userJ", "userI", "userE"]
            },
            { "user": "userM",  
            "Following": [ "userA","userC"]
            }
        ]

def get_user(user_searching):  #Función que simula una petición get
    for user in users:    
        if user_searching == user['user'] : 
            return user
    return None
  

def find_distance(start, end, path = []):
    data = get_user(start) # Llamada a la funcion que devuelve un usuario
    
    if not data:
        return None
    
    path += [start]
    
    if end in data['Following']:            
        return (len(path)) 
    for node in data['Following']:
        if node not in path:       
            return find_distance(node, end)
    

print(find_distance('userA', 'userM'))