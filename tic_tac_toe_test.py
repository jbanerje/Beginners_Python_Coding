
# This is the basic gaming structure
print("***-----------Tic Tac Toe table---------------------------***")
print(" [1,2,3]\n","[4,5,6]\n","[7,8,9]")
print("***-------------------End---------------------------------***")

play_count = 0
player1=[[1,2,3],[4,5,6],[7,8,9]]
#Total 9 opportunities will be present for 2 players
while (play_count <= 9):
    #print("play_count:",play_count)

    player_1_pos = int(input("Player_1: Enter your position:")) 
    if ( player_1_pos == 1) :
        player1[0][0] = 'P1'
        
    elif ( player_1_pos == 2) :
        player1[0][1] = 'P1'
        
    elif ( player_1_pos == 3) :
        player1[0][2] = 'P1'
        
    elif ( player_1_pos == 4) :
        player1[1][0] = 'P1'
        
    elif ( player_1_pos == 5) :
        player1[1][1] = 'P1'
        
    elif ( player_1_pos == 6) :
        player1[1][2] = 'P1'
        
    elif ( player_1_pos == 7) :
        player1[2][0] = 'P1'
        
    elif ( player_1_pos == 8) :
        player1[2][1] = 'P1'
        
    else :
        player1[2][2] = 'P1'

    play_count = play_count + 1

    print(player1)

    player_2_pos = int(input("Player_2: Enter your position:"))

    if ( player_2_pos == 1) :
        player1[0][0] = 'P1'
        
    elif ( player_2_pos == 2) :
        player1[0][1] = 'P1'
        
    elif ( player_2_pos == 3) :
        player1[0][2] = 'P1'
        
    elif ( player_2_pos == 4) :
        player1[1][0] = 'P1'
        
    elif ( player_2_pos == 5) :
        player1[1][1] = 'P1'
        
    elif ( player_2_pos == 6) :
        player1[1][2] = 'P1'
        
    elif ( player_2_pos == 7) :
        player1[2][0] = 'P1'
        
    elif ( player_2_pos == 8) :
        player1[2][1] = 'P1'
        
    else :
        player1[2][2] = 'P1'

    play_count = play_count + 1
    
    print(player1)
