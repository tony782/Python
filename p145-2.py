men = []
women = []


def collect_names():
    name = "名前を入力してください"
    ask = "mかwどちらかを入力してください。qで終わります。"

    while True:
        genre = input(ask)
        if genre == "q":
            break

        if genre == ("m"):
            m = input(name)
            men.append(m)

        elif genre ==("w"):
            w = input(name)
            women.append(w)

        else:
            print("Invalid.")
    print("男性:",men)
    print("女性:",women)

collect_names()