
def password_is_valid(password):

    val = True
    if len(password) < 8: 
        raise Exception('length should be at least 8') 
        val = False

    if password == None: 
        raise Exception('Password should not be empty') 
        val = False

    if not any(char.isupper() for char in password): 
        raise Exception('Password should have at least one uppercase letter') 
        val = False

    if not any(char.islower() for char in password): 
        raise Exception('Password should have at least one lowercase letter') 
        val = False
    if not any(char.isdigit() for char in password): 
        raise Exception('Password should have at least one numeral') 
        val = False   
    if val: 
        return val 
        
def password_is_ok(password):
    count = 0
    while(count < 0):
        val = True
        if len(password) < 8: 
            raise Exception('length should be at least 8') 
            count += 1
            val = False
            return val

        if password == None: 
            raise Exception('Password should not be empty') 
            count += 1
            val = False

        if not any(char.isupper() for char in password): 
            raise Exception('Password should have at least one uppercase letter') 
            count += 1
            val = False

        if not any(char.islower() for char in password): 
            raise Exception('Password should have at least one lowercase letter') 
            count += 1
            val = False
        if not any(char.isdigit() for char in password): 
            raise Exception('Password should have at least one numeral') 
            count += 1
            val = False   
        if val: 
            return val 
            