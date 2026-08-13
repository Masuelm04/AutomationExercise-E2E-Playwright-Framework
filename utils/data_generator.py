from uuid import uuid4

def generate_email():
    return f"test_{uuid4().hex[:8]}@example.com"