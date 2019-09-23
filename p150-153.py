class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created!")
orl = Orange(10, "dark orange")

# orl.weight = 100
# orl.color = "light orange"

print("重さ:", orl.weight, "g")
print("色:", orl.color)