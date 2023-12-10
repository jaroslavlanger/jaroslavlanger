n = 52
f = lambda: n # Reference to `n`, not its value.
n = 1300135
print(f())
