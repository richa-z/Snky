import base64

"""
To encode a python script to base64, just use a site for it. There's plenty of them. Example: https://gchq.github.io/CyberChef/
After that, just paste the encoded script into the line below.
"""

exec(base64.b64decode("PASTE THE BASE64 ENCODED SCRIPT HERE"))
