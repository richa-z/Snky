import base64
import gzip

token = "TOKEN_HERE"

#token -> gzip -> base64
token_gzip = gzip.compress(token.encode("utf-8"))
token_base64 = base64.b64encode(token_gzip)
print(token_base64)