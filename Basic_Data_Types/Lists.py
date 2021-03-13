if __name__ == '__main__':
    N = int(input())
    StateList = []
    Statement = []
    Data = []
    
    for i in range(N):
        Statement = str(input()).split()
        StateList.append(Statement)
    
    for i in range(N):
        if(StateList[i][0] == "insert"):
            Data.insert(int(StateList[i][1]), int(StateList[i][2]))
        elif(StateList[i][0] == "print"):
            print(Data)
        elif(StateList[i][0] == "remove"):
            Data.remove(int(StateList[i][1]))
        elif(StateList[i][0] == "append"):
            Data.append(int(StateList[i][1]))
        elif(StateList[i][0] == "sort"):
            Data.sort()
        elif(StateList[i][0] == "pop"):
            Data.pop()
        elif(StateList[i][0] == "reverse"):
            Data.reverse()
