if __name__ == '__main__':
    seclist = []
    classe = []

    N = int(input())
    for i in range(N):
        classe.append([input(), float(input())])
    classe.sort(key=lambda x:x[1])

    second = classe[0][1]
    for i in range(N):
        if classe[i][1] > second:
            second = classe[i][1]
            break

    for i in range(N):
        if classe[i][1] == second:
            seclist.append(classe[i])
    seclist.sort(key=lambda y:y[0])

    for std in seclist:
        print(std[0])
