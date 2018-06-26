#tic tac toe

row1_number=['X','X','X']
row1_player=['1','2','3']

row2_number=['X','X','X']
row2_player=['4','5','6']

row3_number=['X','X','X']
row3_player=['7','8','9']

play_count=1

player_1_flag = 'n'
player_2_flag = 'n'

print("***-----------Tic Tac Toe table---------------------------***")
print(" [1,2,3]\n","[4,5,6]\n","[7,8,9]")
print("***-------------------End---------------------------------***")

while (play_count <= 9):
    player_1_pos = int(input("Player_1: Enter your position:"))
    if (player_1_pos <= 3):
        row1_number[player_1_pos - 1] = (player_1_pos)
        row1_player[player_1_pos - 1] = 'P1'
        
    
    elif ((player_1_pos > 3) & (player_1_pos <= 6)):
        row2_number[player_1_pos - 4] = (player_1_pos)
        row2_player[player_1_pos - 4] = 'P1'
         
    else:
        row3_number[player_1_pos - 7] = (player_1_pos)
        row3_player[player_1_pos - 7] = 'P1'

    player_1_flag = 'y'
    play_count = play_count + 1
    print("",row1_player,"\n",row2_player,"\n",row3_player)

    if ((player_1_flag == 'y') & (play_count <= 9)):
        player_2_pos = int(input("Player_2: Enter your position:"))
        if (player_2_pos <= 3):
            row1_number[player_2_pos - 1] = player_2_pos
            row1_player[player_2_pos - 1] = 'P2'
        
    
        elif ((player_2_pos > 3) & (player_2_pos <= 6)):
            row2_number[player_2_pos - 4] = player_2_pos
            row2_player[player_2_pos - 4] = 'P2'
         
        else:
            row3_number[player_2_pos - 7] = player_2_pos
            row3_player[player_2_pos - 7] = 'P2'

    player_1_flag = 'n'
    play_count = play_count + 1
    print("",row1_player,"\n",row2_player,"\n",row3_player)







    
