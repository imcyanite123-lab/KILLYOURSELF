import hashlib
target = "f5b2104764f2d830a4cf0f4279a401c57f19c95f6b14696e3e880f5856070d57"
x = input("FINAL> ").strip()
print("ACCEPTED" if hashlib.sha256(x.encode()).hexdigest() == target else "REJECTED")