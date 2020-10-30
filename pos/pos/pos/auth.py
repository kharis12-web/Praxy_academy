import python_jwt as jwt, jwcrypto.jwk as jwk, datetime

def create_token(data):
    token = jwt.generate_jwt(data, algorithm='PS512')
    return token

def check_token(token):
    try:
        token_processed = jwt.process_jwt(token)
        return token_processed[1]
    except Exception:
        return { 'id': False }
