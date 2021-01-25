import json, requests
from jwt.algorithms import RSAAlgorithm

def get_public_key_from_jwks_uri(jwks_uri, index):
  jwks = requests.get(jwks_uri, verify=True).json()
  return RSAAlgorithm.from_jwk(json.dumps(jwks['keys'][index]))
