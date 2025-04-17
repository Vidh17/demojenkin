import sys

if len(sys.argv) < 3:
    print("Usage: python test1.py <x> <y>")
    sys.exit(1)

x = int(sys.argv[1])
y = int(sys.argv[2])

print(" Multiply = ", (x * y))
