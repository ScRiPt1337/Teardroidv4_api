import jwt
encoded = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
print(encoded)
data = jwt.decode(encoded, "secret", algorithms=["HS256"])
print(data)