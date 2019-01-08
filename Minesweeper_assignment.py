# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 17:51:08 2018

@author: MANISH
"""

    class Solution():
           
        def __init__(self,bomb,rows,cols,arr):
            self.bomb = bomb
            self.rows=rows
            self.cols=cols
            self.arr=arr
    
        def minesweeper(self):
            
            x1=self.bomb[0][0]
            y1=self.bomb[0][1]
        
            
            x2=self.bomb[1][0]
            y2=self.bomb[1][1]
            print("x1,y1, ", x1, y1)
            
    
            arr=self.mine_ops(self.arr,x1,y1)
            arr= self.mine_ops(self.arr,x2,y2)
            return arr
            
        
        def mine_ops(self,arry,x,y):
            
            for i in range(x+2):
                for j in range(y+2):
        
                    if (i==x and j==y):
                        arry[i][j]=-1
                    else:
                        if arry[i][j]>=0:
                            try:
                                arry[i][j] += 1
                            except:
                                pass
            
            return arry
     
    
    
    
    bomb_1=[[0,0],[0,1]]
    row=3
    col=3
    arr_1=  [[0,0,0,0],
                 [0,0,0,0],
                 [0,0,0,0]]
    
    sol = Solution(bomb_1,row,col,arr_1)
    print(sol.minesweeper())

 
