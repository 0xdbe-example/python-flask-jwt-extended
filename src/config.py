from dotenv import load_dotenv
import os

import jwks
import oidc


load_dotenv()

OIDC_CONFIG = oidc.get_config(os.environ.get('OAUTH2_ISSUER'))

# Flask JWT settings
JWT_ALGORITHM = 'RS256'
JWT_PUBLIC_KEY = jwks.get_public_key_from_jwks_uri(OIDC_CONFIG['jwks_uri'],0)
JWT_DECODE_AUDIENCE = os.environ.get('OAUTH2_AUDIENCE')
JWT_IDENTITY_CLAIM = 'sub'
