#
# raichu.py : Play the game of Raichu
#
# PLEASE PUT YOUR NAMES AND USER IDS HERE!
#
# Based on skeleton code by D. Crandall, Oct 2021
#
import sys
import time
import copy

def Board_to_string(Board, N):
    return "\n".join(Board[i:i+N] for i in range(0, len(Board), N))

def convert(Board,N):
    Board=list(Board)
    input_Board=[[None]*N for _ in range(N)]
    k=0
    for i in range(N):
        for j in range(N):
            input_Board[i][j]=Board[k]
            k=k+1
    return input_Board
def successors(input_Board, N, player):
    
    #print(input_Board)
    successors_list=[]
    for row in range(N):
        for col in range(N):
            if player=='w' or player=='W':
                #white Pichus(w) right down Diagnoal 
                if(row<N-1 and col<N-1) and (row>=0 and col>=0):
                    new_Board=copy.deepcopy(input_Board)
                    if(new_Board[row][col] == 'w') and (new_Board[row+1][col+1] == '.'):
                        new_Board[row][col]='.'
                        new_Board[row+1][col+1]='w'
                        successors_list.append(new_Board)
                #white Pichus(w) left down Diagnoal 
                if(row<N-1 and col<=N-1) and (row>=0 and col>0):
                    new_Board=copy.deepcopy(input_Board)
                    if(new_Board[row][col] == 'w') and (new_Board[row+1][col-1] == '.'):
                        new_Board[row][col]='.'
                        new_Board[row+1][col-1]='w'
                        successors_list.append(new_Board)            
                #white Pikachus(w) right side move(1 step)
                if(row<=N-1 and col<N-1) and (row>=0 and col>=0):
                    new_Board=copy.deepcopy(input_Board)
                    if(new_Board[row][col] == 'W') and (new_Board[row][col+1] == '.'):
                        new_Board[row][col]='.'
                        new_Board[row][col+1]='W'
                        successors_list.append(new_Board)
                #white Pikachus(w) left side move(1 step)
                if(row<=N-1 and col<=N-1) and (row>=0 and col>0):
                    new_Board=copy.deepcopy(input_Board)
                    if(new_Board[row][col] == 'W') and (new_Board[row][col-1] == '.'):
                        new_Board[row][col]='.'
                        new_Board[row][col-1]='W'
                        successors_list.append(new_Board)
                #white Pikachus(w) forward move(1step)
                if(row<N-1 and col<=N-1) and (row>=0 and col>=0):
                    new_Board=copy.deepcopy(input_Board)
                    if(new_Board[row][col] == 'W') and (new_Board[row+1][col] == '.'):
                        new_Board[row][col]='.'
                        new_Board[row+1][col]='W'
                        successors_list.append(new_Board)            
                #white Pikachus(w) right side move(2 step)
                if(row<=N-1 and col<=N-3) and (row>=0 and col>=0):
                    new_Board=copy.deepcopy(input_Board)
                    if(new_Board[row][col] == 'W') and (new_Board[row][col+1] == '.') and (new_Board[row][col+2] == '.'):
                        new_Board[row][col]='.'
                        new_Board[row][col+2]='W'
                        successors_list.append(new_Board)
                #white Pikachus(w) left side move(2 step)
                if(row<=N-1 and col<=N-1) and (row>=0 and col>1):
                    new_Board=copy.deepcopy(input_Board)
                    if(new_Board[row][col] == 'W') and (new_Board[row][col-1] == '.') and (new_Board[row][col-2] == '.'):
                        new_Board[row][col]='.'
                        new_Board[row][col-2]='W'
                        successors_list.append(new_Board)
                #white Pikachus(w) forward move(2step)
                if(row<N-2 and col<=N-1) and (row>=0 and col>=0):
                    new_Board=copy.deepcopy(input_Board)
                    if(new_Board[row][col] == 'W') and (new_Board[row+1][col] == '.') and (new_Board[row+2][col] == '.'):
                        new_Board[row][col]='.'
                        new_Board[row+2][col]='W'
                        successors_list.append(new_Board)
                 #White raichu
                c=0
                if(new_Board[row][col]=='@'):
                    i=row-1
                    j=col-1
                    while i>=0 and j>=0:
                        new_Board=copy.deepcopy(input_Board)
                        if new_Board[i][j]=='.':
                            if c==1:
                                x=row
                                y=col
                                while x>=0 and y>=0:
                                    if new_Board[x][y]=='b' or new_Board[x][y]=='B' or new_Board[x][y]=='$':
                                        new_Board[x][y]='.'
                                        break
                                    x-=1
                                    y-=1
                            new_Board[i+1][j+1]='.'
                            new_Board[row][col]='.'
                            new_Board[i][j]='@'
                            successors_list.append(new_Board)
                            i-=1
                            j-=1
                        if i<=0 or j<=0 or ((new_Board[i][j]=='b' or new_Board[i][j]=='B' or new_Board[i][j]=='$') and c==1) or (new_Board[i][j]=='w' or new_Board[i][j]=='W' or new_Board[i][j]=='@'):
                            c=0
                            break
                        if i>0 and j>0:
                            new_Board=copy.deepcopy(input_Board)
                            if (new_Board[i][j]=='b' or new_Board[i][j]=='B' or new_Board[i][j]=='$') and c==0:
                                if new_Board[i-1][j-1]=='.':
                                    c=1
                                    new_Board[i+1][j+1]='.'
                                    new_Board[row][col]='.'
                                    new_Board[i][j]='.'
                                    new_Board[i-1][j-1]='@'
                                    successors_list.append(new_Board)
                                    i-=2
                                    j-=2
                                else:
                                    break
                c=0        
                new_Board=copy.deepcopy(input_Board)
                if(new_Board[row][col]=='@'):
                    i=row-1
                    j=col+1
                    while i>=0 and j<=N-1:
                        new_Board=copy.deepcopy(input_Board)
                        if new_Board[i][j]=='.':
                            if c==1:
                                x=row
                                y=col
                                while x>=0 and y<N:
                                    if new_Board[x][y]=='b' or new_Board[x][y]=='B' or new_Board[x][y]=='$':
                                        new_Board[x][y]='.'
                                        break
                                    x-=1
                                    y+=1
                            new_Board[i+1][j-1]='.'
                            new_Board[row][col]='.'
                            new_Board[i][j]='@'
                            successors_list.append(new_Board)
                            i-=1
                            j+=1
                        if i<=0 or j>=N-1 or ((new_Board[i][j]=='b' or new_Board[i][j]=='B' or new_Board[i][j]=='$') and c==1) or (new_Board[i][j]=='w' or new_Board[i][j]=='W' or new_Board[i][j]=='@'):
                            c=0
                            break
                        if i>0 and j<N-1:
                            new_Board=copy.deepcopy(input_Board)
                            if (new_Board[i][j]=='b' or new_Board[i][j]=='B' or new_Board[i][j]=='$') and c==0:
                                if new_Board[i-1][j+1]=='.':
                                    c=1
                                    new_Board[i+1][j-1]='.'
                                    new_Board[row][col]='.'
                                    new_Board[i][j]='.'
                                    new_Board[i-1][j+1]='@'
                                    successors_list.append(new_Board)
                                    i-=2
                                    j+=2
                                else:
                                    break
                c=0        
                new_Board=copy.deepcopy(input_Board)
                if(new_Board[row][col]=='@'):
                    i=row+1
                    j=col-1
                    while i<=N-1 and j>=0:
                        new_Board=copy.deepcopy(input_Board)
                        if new_Board[i][j]=='.':
                            if c==1:
                                x=row
                                y=col
                                while x<N and y>=0:
                                    if new_Board[x][y]=='b' or new_Board[x][y]=='B' or new_Board[x][y]=='$':
                                        new_Board[x][y]='.'
                                        break
                                    x+=1
                                    y-=1
                            new_Board[i-1][j+1]='.'
                            new_Board[row][col]='.'
                            new_Board[i][j]='@'
                            successors_list.append(new_Board)
                            i+=1
                            j-=1
                        if i>=N-1 or j<=0 or ((new_Board[i][j]=='b' or new_Board[i][j]=='B' or new_Board[i][j]=='$') and c==1) or (new_Board[i][j]=='w' or new_Board[i][j]=='W' or new_Board[i][j]=='@'):
                            c=0
                            break
                        if i<N-1 and j>0:
                            new_Board=copy.deepcopy(input_Board)
                            if (new_Board[i][j]=='b' or new_Board[i][j]=='B' or new_Board[i][j]=='$') and c==0:
                                if new_Board[i+1][j-1]=='.':
                                    c=1
                                    new_Board[i-1][j+1]='.'
                                    new_Board[row][col]='.'
                                    new_Board[i][j]='.'
                                    new_Board[i+1][j-1]='@'
                                    successors_list.append(new_Board)
                                    i+=2
                                    j-=2
                                else:
                                    break
                c=0        
                new_Board=copy.deepcopy(input_Board)
                if(new_Board[row][col]=='@'):
                    i=row+1
                    j=col+1
                    while i<=N-1 and j<=N-1:
                        new_Board=copy.deepcopy(input_Board)
                        if new_Board[i][j]=='.':
                            if c==1:
                                x=row
                                y=col
                                while x<N and y<N:
                                    if new_Board[x][y]=='b' or new_Board[x][y]=='B' or new_Board[x][y]=='$':
                                        new_Board[x][y]='.'
                                        break
                                    x+=1
                                    y+=1
                            new_Board[i-1][j-1]='.'
                            new_Board[row][col]='.'
                            new_Board[i][j]='@'
                            successors_list.append(new_Board)
                            i+=1
                            j+=1
                        if i>=N-1 or j>=N-1 or ((new_Board[i][j]=='b' or new_Board[i][j]=='B' or new_Board[i][j]=='$') and c==1) or (new_Board[i][j]=='w' or new_Board[i][j]=='W' or new_Board[i][j]=='@'):
                            c=0
                            break
                        if i<N-1 and j<N-1:
                            new_Board=copy.deepcopy(input_Board)
                            if (new_Board[i][j]=='b' or new_Board[i][j]=='B' or new_Board[i][j]=='$') and c==0:
                                if new_Board[i+1][j+1]=='.':
                                    c=1
                                    new_Board[i-1][j-1]='.'
                                    new_Board[row][col]='.'
                                    new_Board[i][j]='.'
                                    new_Board[i+1][j+1]='@'
                                    successors_list.append(new_Board)
                                    i+=2
                                    j+=2
                                else:
                                    break
                c=0        
                new_Board=copy.deepcopy(input_Board)
                if(new_Board[row][col]=='@'):
                    j=col+1
                    while j<=N-1:
                        new_Board=copy.deepcopy(input_Board)
                        if new_Board[row][j]=='.':
                            if c==1:
                                for x in range(col,N):
                                    if new_Board[row][x]=='b' or new_Board[row][x]=='B' or new_Board[row][x]=='$':
                                        new_Board[row][x]='.'
                                        break
                            new_Board[row][j-1]='.'
                            new_Board[row][col]='.'
                            new_Board[row][j]='@'
                            successors_list.append(new_Board)
                            j+=1
                        if j>=N-1 or ((new_Board[row][j]=='b' or new_Board[row][j]=='B' or new_Board[row][j]=='$') and c==1) or (new_Board[row][j]=='w' or new_Board[row][j]=='W' or new_Board[row][j]=='@'):
                            c=0
                            break
                        if j<N-1:
                            new_Board=copy.deepcopy(input_Board)
                            if (new_Board[row][j]=='b' or new_Board[row][j]=='B' or new_Board[row][j]=='$') and c==0:
                                if new_Board[row][j+1]=='.':
                                    c=1
                                    new_Board[row][j-1]='.'
                                    new_Board[row][col]='.'
                                    new_Board[row][j]='.'
                                    new_Board[row][j+1]='@'
                                    successors_list.append(new_Board)
                                    j+=2
                                else:
                                    break
                c=0        
                new_Board=copy.deepcopy(input_Board)
                if(new_Board[row][col]=='@'):
                    j=col-1
                    while j>=0:
                        new_Board=copy.deepcopy(input_Board)
                        if new_Board[row][j]=='.':
                            if c==1:
                                for x in range(col,-1,-1):
                                    if new_Board[row][x]=='b' or new_Board[row][x]=='B' or new_Board[row][x]=='$':
                                        new_Board[row][x]='.'
                                        break
                            new_Board[row][j+1]='.'
                            new_Board[row][col]='.'
                            new_Board[row][j]='@'
                            successors_list.append(new_Board)
                            j-=1
                        if j<=0 or ((new_Board[row][j]=='b' or new_Board[row][j]=='B' or new_Board[row][j]=='$') and c==1) or (new_Board[row][j]=='w' or new_Board[row][j]=='W' or new_Board[row][j]=='@'):
                            c=0
                            break
                        if j>0:
                            new_Board=copy.deepcopy(input_Board)
                            if (new_Board[row][j]=='b' or new_Board[row][j]=='B' or new_Board[row][j]=='$') and c==0:
                                if new_Board[row][j-1]=='.':
                                    c=1
                                    new_Board[row][j+1]='.'
                                    new_Board[row][col]='.'
                                    new_Board[row][j]='.'
                                    new_Board[row][j-1]='@'
                                    successors_list.append(new_Board)
                                    j-=2
                                else:
                                    break
                c=0        
                new_Board=copy.deepcopy(input_Board)
                if(new_Board[row][col]=='@'):
                    i=row-1
                    while i>=0:
                        new_Board=copy.deepcopy(input_Board)
                        if new_Board[i][col]=='.':
                            if c==1:
                                for x in range(row,-1,-1):
                                    if new_Board[x][col]=='b' or new_Board[x][col]=='B' or new_Board[x][col]=='$':
                                        new_Board[x][col]='.'
                                        break
                            new_Board[i+1][col]='.'
                            new_Board[row][col]='.'
                            new_Board[i][col]='@'
                            successors_list.append(new_Board)
                            i-=1
                        if i<=0 or ((new_Board[i][col]=='b' or new_Board[i][col]=='B' or new_Board[i][col]=='$') and c==1) or (new_Board[i][col]=='w' or new_Board[i][col]=='W' or new_Board[i][col]=='@'):
                            c=0
                            break
                        if i>0:
                            new_Board=copy.deepcopy(input_Board)
                            if (new_Board[i][col]=='b' or new_Board[i][col]=='B' or new_Board[i][col]=='$') and c==0:
                                if new_Board[i-1][col]=='.':
                                    c=1
                                    new_Board[i+1][col]='.'
                                    new_Board[row][col]='.'
                                    new_Board[i][col]='.'
                                    new_Board[i-1][col]='@'
                                    successors_list.append(new_Board)
                                    i-=2
                                else:
                                    break
                c=0        
                new_Board=copy.deepcopy(input_Board)
                if(new_Board[row][col]=='@'):
                    i=row+1
                    while i<=N-1:
                        new_Board=copy.deepcopy(input_Board)
                        if new_Board[i][col]=='.':
                            if c==1:
                                for x in range(row,N):
                                    if new_Board[x][col]=='b' or new_Board[x][col]=='B' or new_Board[x][col]=='$':
                                        new_Board[x][col]='.'
                                        break
                            new_Board[i-1][col]='.'
                            new_Board[row][col]='.'
                            new_Board[i][col]='@'
                            successors_list.append(new_Board)
                            i+=1
                        if i>N-1 or ((new_Board[i][col]=='b' or new_Board[i][col]=='B' or new_Board[i][col]=='$') and c==1) or (new_Board[i][col]=='w' or new_Board[i][col]=='W' or new_Board[i][col]=='@'):
                            c=0
                            break
                        if i<N-1:
                            new_Board=copy.deepcopy(input_Board)
                            if (new_Board[i][col]=='b' or new_Board[i][col]=='B' or new_Board[i][col]=='$') and c==0:
                                if new_Board[i+1][col]=='.':
                                    c=1
                                    new_Board[i-1][col]='.'
                                    new_Board[row][col]='.'
                                    new_Board[i][col]='.'
                                    new_Board[i+1][col]='@'
                                    successors_list.append(new_Board)
                                    i+=2
                                else:
                                    break
                        
                #attack
            
                #white Pichus(w) right down Diagnoal 
                if(row<N-2 and col<N-2) and (row>=0 and col>=0):
                    new_Board=copy.deepcopy(input_Board)
                    if(new_Board[row][col] == 'w') and ((new_Board[row+1][col+1] == 'b') and (new_Board[row+2][col+2] == '.')):
                        new_Board[row][col]='.'
                        new_Board[row+1][col+1]='.'
                        new_Board[row+2][col+2]='w'
                        successors_list.append(new_Board)
                #white Pichus(w) left down Diagnoal 
                if(row<N-2 and col<=N-1) and (row>=0 and col>1):
                    new_Board=copy.deepcopy(input_Board)
                    if(new_Board[row][col] == 'w') and (new_Board[row+1][col-1] == 'b' and (new_Board[row+2][col-2] == '.')):
                        new_Board[row][col]='.'
                        new_Board[row+1][col-1]='.'
                        new_Board[row+2][col-2]='w'
                        successors_list.append(new_Board)
            
                #white Pikachus(w) right side move(1 step)
                if(row<=N-1 and col<N-2) and (row>=0 and col>=0):
                    new_Board=copy.deepcopy(input_Board)
                    if(new_Board[row][col] == 'W') and (new_Board[row][col+2] == '.') and ((new_Board[row][col+1] == 'b') or (new_Board[row][col+1] == 'B')):
                        new_Board[row][col]='.'
                        new_Board[row][col+1]='.'
                        new_Board[row][col+2]='W'
                        successors_list.append(new_Board)
                #white Pikachus(w) left side move(1 step)
                if(row<=N-1 and col<=N-1) and (row>=0 and col>1):
                    new_Board=copy.deepcopy(input_Board)
                    if(new_Board[row][col] == 'W') and (new_Board[row][col-2] == '.') and ((new_Board[row][col-1] == 'b') or (new_Board[row][col-1] == 'B')):
                        new_Board[row][col]='.'
                        new_Board[row][col-1]='.'
                        new_Board[row][col-2]='W'
                        successors_list.append(new_Board)
                #white Pikachus(w) forward move(1step)
                if(row<N-2 and col<=N-1) and (row>=0 and col>=0):
                    new_Board=copy.deepcopy(input_Board)
                    if(new_Board[row][col] == 'W') and (new_Board[row+2][col] == '.') and ((new_Board[row+1][col] == 'b') or (new_Board[row+1][col] == 'B')):
                        new_Board[row][col]='.'
                        new_Board[row+1][col]='.'
                        new_Board[row+2][col]='W'
                        successors_list.append(new_Board)
           
                #white Pikachus(w) right side move(2 step)
                if(row<=N-1 and col<N-3) and (row>=0 and col>=0):
                    new_Board=copy.deepcopy(input_Board)
                    if(new_Board[row][col] == 'W') and (new_Board[row][col+3] == '.') and (new_Board[row][col+1] == '.') and ((new_Board[row][col+2] == 'b') or (new_Board[row][col+2] == 'B')):
                        new_Board[row][col]='.'
                        new_Board[row][col+2]='.'
                        new_Board[row][col+3]='W'
                        successors_list.append(new_Board)
                #white Pikachus(w) left side move(2 step)
                if(row<=N-1 and col<=N-1) and (row>=0 and col>2):
                    new_Board=copy.deepcopy(input_Board)
                    if(new_Board[row][col] == 'W') and (new_Board[row][col-3] == '.') and (new_Board[row][col-1] == '.') and ((new_Board[row][col-2] == 'b') or (new_Board[row][col-2] == 'B')):
                        new_Board[row][col]='.'
                        new_Board[row][col-2]='.'
                        new_Board[row][col-3]='W'
                        successors_list.append(new_Board)
                #white Pikachus(w) forward move(2step)
                if(row<N-3 and col<=N-1) and (row>=0 and col>=0):
                    new_Board=copy.deepcopy(input_Board)
                    if(new_Board[row][col] == 'W') and (new_Board[row+3][col] == '.') and (new_Board[row+1][col] == '.') and ((new_Board[row+2][col] == 'b') or (new_Board[row+2][col] == 'B')):
                        new_Board[row][col]='.'
                        new_Board[row+2][col]='.'
                        new_Board[row+3][col]='W'
                        successors_list.append(new_Board)
               

            elif player=='b' or player=='B':
                 #black Pichus(w) right up Diagnoal 
                if(row<=N-1 and col<N-1) and (row>0 and col>=0):
                    new_Board=copy.deepcopy(input_Board)
                    if(new_Board[row][col] == 'b') and (new_Board[row-1][col+1] == '.'):
                        new_Board[row][col]='.'
                        new_Board[row-1][col+1]='b'
                        successors_list.append(new_Board)
                #black Pichus(w) left up Diagnoal 
                if(row<=N-1 and col<=N-1) and (row>0 and col>0):
                    new_Board=copy.deepcopy(input_Board)
                    if(new_Board[row][col] == 'b') and (new_Board[row-1][col-1] == '.'):
                        new_Board[row][col]='.'
                        new_Board[row-1][col-1]='b'
                        successors_list.append(new_Board)
                #Black Pikachus(b) right move(1step)
                if(row<=N-1 and col<N-1) and (row>=0 and col>=0):
                    new_Board=copy.deepcopy(input_Board)
                    if(new_Board[row][col] == 'B') and (new_Board[row][col+1] == '.'):
                        new_Board[row][col]='.'
                        new_Board[row][col+1]='B'
                        successors_list.append(new_Board)
                #Black Pikachus(b) left move(1step)
                if(row<=N-1 and col<=N-1) and (row>=0 and col>0):
                    new_Board=copy.deepcopy(input_Board)
                    if(new_Board[row][col] == 'B') and (new_Board[row][col-1] == '.'):
                        new_Board[row][col]='.'
                        new_Board[row][col-1]='B'
                        successors_list.append(new_Board)
                #Black Pikachus(b) forward move(1step)
                if(row<=N-1 and col<=N-1) and (row>0 and col>=0):
                    new_Board=copy.deepcopy(input_Board)
                    if(new_Board[row][col] == 'B') and (new_Board[row-1][col] == '.'):
                        new_Board[row][col]='.'
                        new_Board[row-1][col]='B'
                        successors_list.append(new_Board)
                        
                        # print(new_Board,'x')
                #Black Pikachus(b) right move(2step)
                if(row<=N-1 and col<=N-3) and (row>=0 and col>=0):
                    new_Board=copy.deepcopy(input_Board)
                    if(new_Board[row][col] == 'B') and (new_Board[row][col+1] == '.') and (new_Board[row][col+2] == '.'):
                        new_Board[row][col]='.'
                        new_Board[row][col+2]='B'
                        successors_list.append(new_Board)
                #Black Pikachus(b) left move(2step)
                if(row<=N-1 and col<=N-1) and (row>=0 and col>1):
                    new_Board=copy.deepcopy(input_Board)
                    if(new_Board[row][col] == 'B') and (new_Board[row][col-1] == '.') and (new_Board[row][col-2] == '.'):
                        new_Board[row][col]='.'
                        new_Board[row][col-2]='B'
                        successors_list.append(new_Board)
                #Black Pikachus(b) forward move(2step)
                if(row<=N-1 and col<=N-1) and (row>1 and col>0):
                    new_Board=copy.deepcopy(input_Board)
                    if(new_Board[row][col] == 'B') and (new_Board[row-1][col] == '.') and (new_Board[row-2][col] == '.'):
                        new_Board[row][col]='.'
                        new_Board[row-2][col]='B'
                        successors_list.append(new_Board)
                #Black Raichu
                c=0
                if(new_Board[row][col]=='$'):
                    i=row-1
                    j=col-1
                    while i>=0 and j>=0:
                        new_Board=copy.deepcopy(input_Board)
                        if new_Board[i][j]=='.':
                            if c==1:
                                x=row
                                y=col
                                while x>=0 and y>=0:
                                    if new_Board[x][y]=='w' or new_Board[x][y]=='W' or new_Board[x][y]=='@':
                                        new_Board[x][y]='.'
                                        break
                                    x-=1
                                    y-=1
                            new_Board[i+1][j+1]='.'
                            new_Board[row][col]='.'
                            new_Board[i][j]='$'
                            successors_list.append(new_Board)
                            i-=1
                            j-=1
                        if i<=0 or j<=0 or ((new_Board[i][j]=='w' or new_Board[i][j]=='W' or new_Board[i][j]=='@') and c==1) or (new_Board[i][j]=='b' or new_Board[i][j]=='B' or new_Board[i][j]=='$'):
                            c=0
                            break
                        if i>0 and j>0:
                            new_Board=copy.deepcopy(input_Board)
                            if (new_Board[i][j]=='w' or new_Board[i][j]=='W' or new_Board[i][j]=='@') and c==0:
                                if new_Board[i-1][j-1]=='.':
                                    c=1
                                    new_Board[i+1][j+1]='.'
                                    new_Board[row][col]='.'
                                    new_Board[i][j]='.'
                                    new_Board[i-1][j-1]='$'
                                    successors_list.append(new_Board)
                                    i-=2
                                    j-=2
                                else:
                                    break
                c=0        
                new_Board=copy.deepcopy(input_Board)
                if(new_Board[row][col]=='$'):
                    i=row-1
                    j=col+1
                    while i>=0 and j<=N-1:
                        new_Board=copy.deepcopy(input_Board)
                        if new_Board[i][j]=='.':
                            if c==1:
                                x=row
                                y=col
                                while x>=0 and y<N:
                                    if new_Board[x][y]=='w' or new_Board[x][y]=='W' or new_Board[x][y]=='@':
                                        new_Board[x][y]='.'
                                        break
                                    x-=1
                                    y+=1
                            new_Board[i+1][j-1]='.'
                            new_Board[row][col]='.'
                            new_Board[i][j]='$'
                            successors_list.append(new_Board)
                            i-=1
                            j+=1
                        if i<=0 or j>=N-1 or ((new_Board[i][j]=='w' or new_Board[i][j]=='W' or new_Board[i][j]=='@') and c==1) or (new_Board[i][j]=='b' or new_Board[i][j]=='B' or new_Board[i][j]=='$'):
                            c=0
                            break
                        if i>0 and j<N-1:
                            new_Board=copy.deepcopy(input_Board)
                            if (new_Board[i][j]=='w' or new_Board[i][j]=='W' or new_Board[i][j]=='@') and c==0:
                                if new_Board[i-1][j+1]=='.':
                                    c=1
                                    new_Board[i+1][j-1]='.'
                                    new_Board[row][col]='.'
                                    new_Board[i][j]='.'
                                    new_Board[i-1][j+1]='$'
                                    successors_list.append(new_Board)
                                    i-=2
                                    j+=2
                                else:
                                    break
                c=0        
                new_Board=copy.deepcopy(input_Board)
                if(new_Board[row][col]=='$'):
                    i=row+1
                    j=col-1
                    while i<=N-1 and j>=0:
                        new_Board=copy.deepcopy(input_Board)
                        if new_Board[i][j]=='.':
                            if c==1:
                                x=row
                                y=col
                                while x<N and y>=0:
                                    if new_Board[x][y]=='w' or new_Board[x][y]=='W' or new_Board[x][y]=='@':
                                        new_Board[x][y]='.'
                                        break
                                    x+=1
                                    y-=1
                            new_Board[i-1][j+1]='.'
                            new_Board[row][col]='.'
                            new_Board[i][j]='$'
                            successors_list.append(new_Board)
                            i+=1
                            j-=1
                        if i>=N-1 or j<=0 or ((new_Board[i][j]=='w' or new_Board[i][j]=='W' or new_Board[i][j]=='@') and c==1) or (new_Board[i][j]=='b' or new_Board[i][j]=='B' or new_Board[i][j]=='$'):
                            c=0
                            break
                        if i<N-1 and j>0:
                            new_Board=copy.deepcopy(input_Board)
                            if (new_Board[i][j]=='w' or new_Board[i][j]=='W' or new_Board[i][j]=='@') and c==0:
                                if new_Board[i+1][j-1]=='.':
                                    c=1
                                    new_Board[i-1][j+1]='.'
                                    new_Board[row][col]='.'
                                    new_Board[i][j]='.'
                                    new_Board[i+1][j-1]='$'
                                    successors_list.append(new_Board)
                                    i+=2
                                    j-=2
                                else:
                                    break
                c=0        
                new_Board=copy.deepcopy(input_Board)
                if(new_Board[row][col]=='$'):
                    i=row+1
                    j=col+1
                    while i<=N-1 and j<=N-1:
                        new_Board=copy.deepcopy(input_Board)
                        if new_Board[i][j]=='.':
                            if c==1:
                                x=row
                                y=col
                                while x<N and y<N:
                                    if new_Board[x][y]=='w' or new_Board[x][y]=='W' or new_Board[x][y]=='@':
                                        new_Board[x][y]='.'
                                        break
                                    x+=1
                                    y+=1
                            new_Board[i-1][j-1]='.'
                            new_Board[row][col]='.'
                            new_Board[i][j]='$'
                            successors_list.append(new_Board)
                            i+=1
                            j+=1
                        if i>=N-1 or j>=N-1 or ((new_Board[i][j]=='w' or new_Board[i][j]=='W' or new_Board[i][j]=='@') and c==1) or (new_Board[i][j]=='b' or new_Board[i][j]=='B' or new_Board[i][j]=='$'):
                            c=0
                            break
                        if i<N-1 and j<N-1:
                            new_Board=copy.deepcopy(input_Board)
                            if (new_Board[i][j]=='w' or new_Board[i][j]=='W' or new_Board[i][j]=='@') and c==0:
                                if new_Board[i+1][j+1]=='.':
                                    c=1
                                    new_Board[i-1][j-1]='.'
                                    new_Board[row][col]='.'
                                    new_Board[i][j]='.'
                                    new_Board[i+1][j+1]='$'
                                    successors_list.append(new_Board)
                                    i+=2
                                    j+=2
                                else:
                                    break
                c=0        
                new_Board=copy.deepcopy(input_Board)
                if(new_Board[row][col]=='$'):
                    j=col+1
                    while j<=N-1:
                        new_Board=copy.deepcopy(input_Board)
                        if new_Board[row][j]=='.':
                            if c==1:
                                for x in range(col,N):
                                    if new_Board[row][x]=='w' or new_Board[row][x]=='W' or new_Board[row][x]=='@':
                                        new_Board[row][x]='.'
                                        break
                            new_Board[row][j-1]='.'
                            new_Board[row][col]='.'
                            new_Board[row][j]='$'
                            successors_list.append(new_Board)
                            j+=1
                        if j>=N-1 or ((new_Board[row][j]=='w' or new_Board[row][j]=='W' or new_Board[row][j]=='@') and c==1) or (new_Board[row][j]=='b' or new_Board[row][j]=='B' or new_Board[row][j]=='$'):
                            c=0
                            break
                        if j<N-1:
                            new_Board=copy.deepcopy(input_Board)
                            if (new_Board[row][j]=='w' or new_Board[row][j]=='W' or new_Board[row][j]=='@') and c==0:
                                if new_Board[row][j+1]=='.':
                                    c=1
                                    new_Board[row][j-1]='.'
                                    new_Board[row][col]='.'
                                    new_Board[row][j]='.'
                                    new_Board[row][j+1]='$'
                                    successors_list.append(new_Board)
                                    j+=2
                                else:
                                    break
                c=0        
                new_Board=copy.deepcopy(input_Board)
                if(new_Board[row][col]=='$'):
                    j=col-1
                    while j>=0:
                        new_Board=copy.deepcopy(input_Board)
                        if new_Board[row][j]=='.':
                            if c==1:
                                for x in range(col,-1,-1):
                                    if new_Board[row][x]=='w' or new_Board[row][x]=='W' or new_Board[row][x]=='@':
                                        new_Board[row][x]='.'
                                        break
                            new_Board[row][j+1]='.'
                            new_Board[row][col]='.'
                            new_Board[row][j]='$'
                            successors_list.append(new_Board)
                            j-=1
                        if j<=0 or ((new_Board[row][j]=='w' or new_Board[row][j]=='W' or new_Board[row][j]=='@') and c==1) or (new_Board[row][j]=='b' or new_Board[row][j]=='B' or new_Board[row][j]=='$'):
                            c=0
                            break
                        if j>0:
                            new_Board=copy.deepcopy(input_Board)
                            if (new_Board[row][j]=='w' or new_Board[row][j]=='W' or new_Board[row][j]=='@') and c==0:
                                if new_Board[row][j-1]=='.':
                                    c=1
                                    new_Board[row][j+1]='.'
                                    new_Board[row][col]='.'
                                    new_Board[row][j]='.'
                                    new_Board[row][j-1]='$'
                                    successors_list.append(new_Board)
                                    j-=2
                                else:
                                    break
                c=0        
                new_Board=copy.deepcopy(input_Board)
                if(new_Board[row][col]=='$'):
                    i=row-1
                    while i>=0:
                        new_Board=copy.deepcopy(input_Board)
                        if new_Board[i][col]=='.':
                            if c==1:
                                for x in range(row,-1,-1):
                                    if new_Board[x][col]=='w' or new_Board[x][col]=='W' or new_Board[x][col]=='@':
                                        new_Board[x][col]='.'
                                        break
                            new_Board[i+1][col]='.'
                            new_Board[row][col]='.'
                            new_Board[i][col]='$'
                            successors_list.append(new_Board)
                            i-=1
                        if i<=0 or ((new_Board[i][col]=='w' or new_Board[i][col]=='W' or new_Board[i][col]=='@') and c==1) or (new_Board[i][col]=='b' or new_Board[i][col]=='B' or new_Board[i][col]=='$'):
                            c=0
                            break
                        if i>0:
                            new_Board=copy.deepcopy(input_Board)
                            if (new_Board[i][col]=='w' or new_Board[i][col]=='W' or new_Board[i][col]=='@') and c==0:
                                if new_Board[i-1][col]=='.':
                                    c=1
                                    new_Board[i+1][col]='.'
                                    new_Board[row][col]='.'
                                    new_Board[i][col]='.'
                                    new_Board[i-1][col]='$'
                                    successors_list.append(new_Board)
                                    i-=2
                                else:
                                    break
                c=0        
                new_Board=copy.deepcopy(input_Board)
                if(new_Board[row][col]=='$'):
                    i=row+1
                    while i<=N-1:
                        new_Board=copy.deepcopy(input_Board)
                        if new_Board[i][col]=='.':
                            if c==1:
                                for x in range(row,N):
                                    if new_Board[x][col]=='w' or new_Board[x][col]=='W' or new_Board[x][col]=='@':
                                        new_Board[x][col]='.'
                                        break
                            new_Board[i-1][col]='.'
                            new_Board[row][col]='.'
                            new_Board[i][col]='$'
                            successors_list.append(new_Board)
                            i+=1
                        if i>=N-1 or ((new_Board[i][col]=='w' or new_Board[i][col]=='W' or new_Board[i][col]=='@') and c==1) or (new_Board[i][col]=='b' or new_Board[i][col]=='B' or new_Board[i][col]=='$'):
                            c=0
                            break
                        if i<N-1:
                            new_Board=copy.deepcopy(input_Board)
                            if (new_Board[i][col]=='w' or new_Board[i][col]=='W' or new_Board[i][col]=='@') and c==0:
                                if new_Board[i+1][col]=='.':
                                    c=1
                                    new_Board[i-1][col]='.'
                                    new_Board[row][col]='.'
                                    new_Board[i][col]='.'
                                    new_Board[i+1][col]='$'
                                    successors_list.append(new_Board)
                                    i+=2
                                else:
                                    break
                #black Pichus(w) right up Diagnoal 
                if(row<=N-1 and col<N-2) and (row>1 and col>=0):
                    new_Board=copy.deepcopy(input_Board)
                    if(new_Board[row][col] == 'b') and (new_Board[row-1][col+1] == 'w' and (new_Board[row-2][col+2] == '.')):
                        new_Board[row][col]='.'
                        new_Board[row-1][col+1]='.'
                        new_Board[row-2][col+2]='b'
                        successors_list.append(new_Board)
                #black Pichus(w) left up Diagnoal 
                if(row<=N-1 and col<=N-1) and (row>1 and col>1):
                    new_Board=copy.deepcopy(input_Board)
                    if(new_Board[row][col] == 'b') and (new_Board[row-1][col-1] == 'w' and (new_Board[row-2][col-2] == '.')):
                        new_Board[row][col]='.'
                        new_Board[row-1][col-1]='.'
                        new_Board[row-2][col-2]='b'
                        successors_list.append(new_Board)
                #Black Pikachus(b) right move(1step)
                if(row<=N-1 and col<N-2) and (row>=0 and col>=0):
                    new_Board=copy.deepcopy(input_Board)
                    if(new_Board[row][col] == 'B') and (new_Board[row][col+2] == '.') and ((new_Board[row][col+1] == 'w') or (new_Board[row][col+1] == 'W')):
                        new_Board[row][col]='.'
                        new_Board[row][col+1]='.'
                        new_Board[row][col+2]='B'
                        successors_list.append(new_Board)
                #Black Pikachus(b) left move(1step)
                if(row<=N-1 and col<=N-1) and (row>=0 and col>1):
                    new_Board=copy.deepcopy(input_Board)
                    if(new_Board[row][col] == 'B') and (new_Board[row][col-2] == '.') and ((new_Board[row][col-1] == 'w') or (new_Board[row][col-1] == 'W')):
                        new_Board[row][col]='.'
                        new_Board[row][col-1]='.'
                        new_Board[row][col-2]='B'
                        successors_list.append(new_Board)
                #Black Pikachus(b) forward move(1step)
                if(row<=N-1 and col<=N-1) and (row>1 and col>=0):
                    new_Board=copy.deepcopy(input_Board)
                    if(new_Board[row][col] == 'B') and (new_Board[row-2][col] == '.') and ((new_Board[row-1][col] == 'w') or (new_Board[row-1][col] == 'W')):
                        new_Board[row][col]='.'
                        new_Board[row-1][col]='.'
                        new_Board[row-2][col]='B'
                        successors_list.append(new_Board)
                #Black Pikachus(b) right move(2step)
                if(row<=N-1 and col<N-3) and (row>=0 and col>=0):
                    new_Board=copy.deepcopy(input_Board)
                    if(new_Board[row][col] == 'B') and (new_Board[row][col+3] == '.') and (new_Board[row][col+1] == '.') and ((new_Board[row][col+2] == 'w') or (new_Board[row][col+2] == 'W')):
                        new_Board[row][col]='.'
                        new_Board[row][col+2]='.'
                        new_Board[row][col+3]='B'
                        successors_list.append(new_Board)
                #Black Pikachus(b) left move(2step)
                if(row<=N-1 and col<=N-1) and (row>=0 and col>2):
                    new_Board=copy.deepcopy(input_Board)
                    if(new_Board[row][col] == 'B') and (new_Board[row][col-3] == '.') and (new_Board[row][col-1] == '.') and ((new_Board[row][col-2] == 'w') or (new_Board[row][col-2] == 'W')):
                        new_Board[row][col]='.'
                        new_Board[row][col-2]='.'
                        new_Board[row][col-3]='B'
                        successors_list.append(new_Board)
                #Black Pikachus(b) forward move(2step)
                if(row<=N-1 and col<=N-1) and (row>1 and col>0):
                    new_Board=copy.deepcopy(input_Board)
                    if(new_Board[row][col] == 'B') and (new_Board[row-3][col] == '.') and (new_Board[row-1][col] == '.') and ((new_Board[row-2][col] == 'w') or (new_Board[row-2][col] == 'W')):
                        new_Board[row][col]='.'
                        new_Board[row-2][col]='.'
                        new_Board[row-3][col]='B'
                        successors_list.append(new_Board)
            
            else:
                print("Invalid player")
                return 0

    for piece in range(len(successors_list)):
        for col in range(len(successors_list[piece][0])):
            if successors_list[piece][0][col]=='b' or successors_list[piece][0][col] =='B':
                successors_list[piece][0][col]='$'
        for col in range(len(successors_list[piece][-1])):
            if successors_list[piece][-1][col]=='w' or successors_list[piece][-1][col] =='W':
                successors_list[piece][-1][col]='@'
    return successors_list

def eval(Board,player):
    score=0
    if player=='w' or player=='W':    
        for i in range(len(Board)):
            for j in range(len(Board[i])):
                if Board[i][j]=='w':
                    score+=1
                if Board[i][j]=='W':
                    score+=10
                if Board[i][j]=='@':
                    score+=50
                if Board[i][j]=='b':
                    score-=1
                if Board[i][j]=='B':
                    score-=10
                if Board[i][j]=='$':
                    score-=50
    if player=='b' or player=='B':    
        for i in range(len(Board)):
            for j in range(len(Board[i])):
                if Board[i][j]=='w':
                    score-=1
                if Board[i][j]=='W':
                    score-=10
                if Board[i][j]=='@':
                    score-=50
                if Board[i][j]=='b':
                    score+=1
                if Board[i][j]=='B':
                    score+=10
                if Board[i][j]=='$':
                    score+=50
    return score

def minmax(Board,z,horizon,player,x,N):
    if z==horizon:
        return eval(Board,player),Board
    if player=='w' or player=='W':
        p='b'
    if player=='b' or player=='B':
        p='w'
    if x==1:
        max=float('-inf')
        new_Board=[]
        # print(successors(Board,N,player),'asd')
        for i in successors(Board,N,player):
            # print(eval(i,player),'sss')
            a,b=minmax(i,z+1,horizon,p,-1,N)
            if max<=a:
                max=a
                new_Board=i
        #print(max,new_Board,'x')
        return max,new_Board
    if x==-1:
        min=float('inf')
        new_Board=[]
        #print(successors(Board,N,player),'asd')
        for i in successors(Board,N,player):
            a,b=minmax(i,z+1,horizon,p,1,N)
            if min>=a:
                min=a
                new_Board=i
        # print(min,new_Board)
        return min,new_Board


def find_best_move(Board, N, player):
    # This sample code just returns the same Board over and over again (which
    # isn't a valid move anyway.) Replace this with your code!

    horizon=1
    #while 1:
    a,b=minmax(Board,0,horizon,player,-1,N)
            # print(a,b)
    string=''
    for i in range(len(b)):
        for j in range(len(b[i])):
            string+=str(b[i][j])
    yield string
        #horizon+=1


if __name__ == "__main__":
    if len(sys.argv) != 5:
        raise Exception("Usage: Raichu.py N player Board timelimit")
        
    (_, N, player, Board, timelimit) = sys.argv
    N=int(N)
    timelimit=int(timelimit)
    if player not in "wb":
        raise Exception("Invalid player.")

    if len(Board) != N*N or 0 in [c in "wb.WB@$" for c in Board]:
        print(len(Board))
        raise Exception("Bad Board string.")

    print("Searching for best move for " + player + " from Board state: \n" + Board_to_string(Board, N))
    # successors(Board, N, player)
    print("Here's what I decided:")
    input_Board=convert(Board,N)
    for new_Board in find_best_move(input_Board, N, player):
        print(new_Board)
