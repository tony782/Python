class Orange:
    def __init__(self, w, c):
        """重さはグラム"""
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")
    def rot(self, days, temp):
        """温度は摂氏"""
        self.mold = days * temp

orange = Orange(200, "orange")
print("腐敗度:", orange.mold)
orange.rot(10, 37)
print("腐敗度:", orange.mold)