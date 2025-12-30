import bcrypt

def hash_password(password):
        b_password = password.encode('utf-8')
        hashed = bcrypt.hashpw(b_password, bcrypt.gensalt())
        return hashed.decode('utf-8')
    
def check_password(stored_password, password):
    bytes_password = password.encode('utf-8')
    bytes_stored_hash = stored_password.encode('utf-8')
    return bcrypt.checkpw(bytes_password, bytes_stored_hash)