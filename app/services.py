import uuid
import bcrypt

def generate_uuid():
    return str(uuid.uuid4())

def hash_password(password):
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")