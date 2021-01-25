import requests
from urllib.parse import urljoin

def get_config(issuer_uri):
  url = urljoin(issuer_uri,'.well-known/openid-configuration')
  config = requests.get(url, verify=True).json()
  return config
