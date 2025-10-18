# --- DEMO: Truthiness ---
samples = [0, 1, "", "text", [], [1], {}, {"k": 1}, None]
for item in samples:
    if item:
        print(repr(item), "→ Truthy")
    else:
        print(repr(item), "→ Falsy")

# --- DEMO: f-strings ---
name = "John"
score = 95
print(f"{name} scored {score}% (next: {score + 1}%)")