import base64

encodedStr = "Uml0ZXNo"

# Standard Base64 Decoding
decodedBytes = base64.b64decode(encodedStr)
decodedStr = str(decodedBytes, "utf-8")

print(decodedStr)