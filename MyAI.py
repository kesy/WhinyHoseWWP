# ======================================================================
# FILE:        MyAI.py
#
# AUTHOR:      Abdullah Younis
#
# DESCRIPTION: This file contains your agent class, which you will
#              implement. You are responsible for implementing the
#              'getAction' function and any helper methods you feel you
#              need.
#
# NOTES:       - If you are having trouble understanding how the shell
#                works, look at the other parts of the code, as well as
#                the documentation.
#
#              - You are only allowed to make changes to this portion of
#                the code. Any changes to other portions of the code will
#                be lost when the tournament runs your code.
# ======================================================================
from Agent import Agent
import random

class MyAI ( Agent ):
    
    def __init__ ( self ):
        # ======================================================================
        # YOUR CODE BEGINS
        # ======================================================================
        self.world=dict()
        self.position=(1,1) #(x,y)
        self.direction=0 #{0:L, 1:U, 2:R, 3:D}
        self.deadwumpus=False 
        self.hasarrow=True
        self.num_moves=0
        #adding stuff for testing git

        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================

    def getAction( self, stench, breeze, glitter, bump, scream ):
        # ======================================================================
        # YOUR CODE BEGINS
        # ======================================================================
        action=self.__actions [ random.randrange ( len ( self.__actions ) ) ]
        #if self.position not in self.world:
        self.world[self.position]=[]
        self.observe(self.position, stench, breeze, glitter, bump, scream)
        self.num_moves+=1
        if 'g' in self.world[self.position]:
            return Agent.Action.GRAB
        if 's' in self.world[self.position] and self.hasarrow:
            action = Agent.Action.SHOOT
            self.hasarrow=False
        if self.position == (1,1) and 'b' in self.world[self.position]:
            action = Agent.Action.CLIMB  
        
        print(self.position, self.direction, action, self.num_moves, self.world)  
        self.move(self.position, action)

        return action
        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================
    
    # ======================================================================
    # YOUR CODE BEGINS
    # ======================================================================
    __actions = [
        Agent.Action.TURN_LEFT,
        Agent.Action.TURN_RIGHT,
        Agent.Action.FORWARD,
    ]
    __directions = [0,1,2,3]
    def move(self, postion, action):
        if action==Agent.Action.TURN_LEFT:
            self.direction = (self.direction+1)%4
        elif action==Agent.Action.TURN_RIGHT:
            self.direction = 3-self.direction
        elif action==Agent.Action.FORWARD and self.direction not in self.world[self.position]:
            if self.direction==0:
                self.position=(self.position[0]+1,self.position[1])
            elif self.direction==1:
                self.position=(self.position[0],self.position[1]+1)
            elif self.direction==2 and self.position[0]>1:
                self.position=(self.position[0]-1,self.position[1])
            elif self.direction==3 and self.position[1]>1:
                self.position=(self.position[0],self.position[1]-1)
    
    
    def observe(self, position, stench, breeze, glitter, bump, scream):
        if stench:
            self.world[position].append('s')
        if breeze:
            self.world[position].append('b')
        if glitter:
            self.world[position].append('g')
        if bump:
            if self.direction == 0 or self.direction == 1:
                for key in self.world:
                    if key[0]==position[0] and self.direction not in self.world[key]:
                        self.world[key].append(self.direction)
            else:
                for key in self.world:
                    if key[1]==position[1] and self.direction not in self.world[key]:
                        self.world[key].append(self.direction)
        if scream:
            self.deadwumpus=True
    # ======================================================================
    # YOUR CODE ENDS
    # ======================================================================
