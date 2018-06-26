#tic tac toe

# This fucntion will do sanity check of the position

def player_pos_chk(player_pos):
    
    if (player_pos <= 3):
        if ((row1_player[player_pos - 1] == 'P1') or (row1_player[player_pos - 1] == 'P2')):
            chk_flag = 'fail'
        else:
            chk_flag = 'pass'
            
    elif ((player_pos > 3) & (player_pos <= 6)):
        if ((row2_player[player_pos - 4] == 'P1') or (row2_player[player_pos - 4] == 'P2')):
            chk_flag = 'fail'
        else:
            chk_flag = 'pass'
         
    else:
        #print("In range 7 to 9",row3_number[player_pos - 7])
        if ((row3_player[player_pos - 7] == 'P1') or (row3_player[player_pos - 7] == 'P2')):
            chk_flag = 'fail'
        else:
            chk_flag = 'pass'

    return chk_flag;

# This fucntion will place the player's turn in the corresponding cell
def player_pos(player_num,player_pos) :
    if (player_pos <= 3):
        row1_number[player_pos - 1] = player_pos
        row1_player[player_pos - 1] = player_num
        
    
    elif ((player_pos > 3) & (player_pos <= 6)):
        row2_number[player_pos - 4] = player_pos
        row2_player[player_pos - 4] = player_num
         
    else:
        row3_number[player_pos - 7] = player_pos
        row3_player[player_pos - 7] = player_num

    if (player_num =='P1'):
        player_1_flag = 'y'
    else:
        player_1_flag = 'n'
        
    
    print("",row1_player,"\n",row2_player,"\n",row3_player)    

    return;

#*************Main Starts Here *************************************#
row1_number=['X','X','X']
row1_player=['1','2','3']

row2_number=['X','X','X']
row2_player=['4','5','6']

row3_number=['X','X','X']
row3_player=['7','8','9']

play_count=1
chk_result = 'pass'
player_1_flag = 'n'
player_2_flag = 'n'

# This is the basic gaming structure
print("***-----------Tic Tac Toe table---------------------------***")
print(" [1,2,3]\n","[4,5,6]\n","[7,8,9]")
print("***-------------------End---------------------------------***")

#Total 9 opportunities will be present for 2 players
while (play_count <= 9):
    print("play_count:",play_count)

    player_1_pos = int(input("Player_1: Enter your position:"))
    chk_result = player_pos_chk(player_1_pos)
    #print("chk_result:",chk_result)
        
    if (chk_result == 'pass') :
        player_pos('P1',player_1_pos)
        play_count = play_count + 1
    else:
        print('Position Already Accupied!')
    
    if (play_count <= 9):
        print("play_count:",play_count)
        player_2_pos = int(input("Player_2: Enter your position:"))
        chk_result = player_pos_chk(player_2_pos)

        #print("chk_result:",chk_result)

        if (chk_result == 'pass') :
            player_pos('P2',player_2_pos)
            play_count = play_count + 1
        else:
            print('Position Already Accupied!') 
    else:
        print('Game Ends!')







    
