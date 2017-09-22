import  random
px = 3
py = 3
g1x = 2
g1y = 5
g2x = 5
g2y = 4
listx = [3]
listy = [3]
count = 0
move = ["w","a","s","d"]
command = "e"
def action (command,x,y):
    if command == "w":
        y -= 1
        if y < 0:
            y = 6
    elif command == "a":
        x -= 1
        if x < 0:
            x = 6
    elif command == "s":
        y += 1
        if y > 6:
            y = 0
    elif command == "d":
        x += 1
        if x > 6:
            x = 0
    return x,y


while count < 48 :#nếu người chạm vào ghost 1 hoặc 2 hoặc ăn hết các điểm thi vòng while ngừng
    for j  in range (7):
        for i in range (7):
                if i == g1x and j == g1y:
                    print("G",end='')
                elif i == g2x and j == g2y:
                    print("G",end='')
                elif i == px and j == py:
                    print("P",end='')
                else:
                    check1 = True
                    for x in range(count+1):
                        if (i == listx[x] and j == listy[x]):
                                    print(".",end='')
                                    check1 = False
                    if check1 == True :
                        print("-",end='')

        print()

    # //Person action
    command = "e"
    while command !="w" and command !="s" and command!='a' and command!='d' :
        command= input("your move: ")
        if command not in move :
            print("ban nhap sai lenh,vui long nhap lai")
    action(command,px,py)
    px,py= action(command,px,py)

    # truong hop nguoi phi vao ma
    if (px== g1x and py==g1y) or (px == g2x and py == g2y ):
        print('ban da phi vao con ma,ban bi loai')
        break

    # Đoạn này lưu lại những điểm từ '-' thành '.'
    check = True
    for q in range (count+1):
        if listx[q] == px and listy[q] == py :
            check = False
    if check == True :
        listx.append(px)
        listy.append(py)
        count += 1

    # Ghost1 random action
    g1x_notmove = g1x
    g1y_notmove = g1y
    ghost1move = random.choice(move)
    action(ghost1move,g1x,g1y)
    g1x,g1y = action(ghost1move,g1x,g1y)

    #trường hợp ghost 1 va vao ghost 2 thì ghost 1 sẽ ko di chuyển
    if g1x == g2x and g1y == g2y :
        g1x=g1x_notmove
        g1y=g1y_notmove

    #Ghost 2 random action
    g2x_notmove = g2x
    g2y_notmove = g2y
    ghost2move = random.choice(move)
    action(ghost2move, g2x, g2y)
    g2x, g2y = action(ghost1move, g2x, g2y)

    #trường hợp ghost 2 va vào ghost 1 thì ghost 2 sẽ ko di chuyển
    if g1x == g2x and g1y == g2y:
        g2x = g2x_notmove
        g2y = g2y_notmove

    # truong hop ma phi vao nguoi
    if (px == g1x and py == g1y) or (px == g2x and py == g2y ):
        print('con ma da can phai ban,ban bi loai')
        break

for j  in range (7):
    for i in range (7):
            if i == g1x and j == g1y:
                print("G",end='')
            elif i == g2x and j == g2y:
                print("G",end='')
            elif i == px and j == py:
                print("P",end='')
            else:
                check1 = True
                for x in range(count+1):
                    if (i == listx[x] and j == listy[x]):
                                print(".",end='')
                                check1 = False
                if check1 == True :
                    print("-",end='')

    print()
if count == 48:
    print("you win")







