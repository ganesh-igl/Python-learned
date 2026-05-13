import sys
types = {
    "int   (Python int)  ": 0,
    "float (Python float)": 0.0,
    "str   (Python str)  ": "",
    "bool  (Python bool) ": True,
}
for name, val in types.items():
    print(f"Size of {name}: {sys.getsizeof(val)} bytes")