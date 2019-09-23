class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created!")
orl1 = Orange(4, "light orange")
orl2 = Orange(8, "dark orange")
orl3 = Orange(12, "yellow")

print("orl1:", orl1.color)
print("orl2:", orl2.color)
print("orl3:", orl3.color)