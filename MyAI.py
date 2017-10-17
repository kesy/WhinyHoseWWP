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

        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================

    def getAction( self, stench, breeze, glitter, bump, scream ):
        # ======================================================================
        # YOUR CODE BEGINS
        # ======================================================================
        action=self.__actions [ random.randrange ( len ( self.__actions ) ) ]
        self.world[self.position]=[]
        self.observe(self.position, stench, breeze, glitter, bump, scream)
        self.move(self.position, action)
        print(self.position, action, self.world)
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
        Agent.Action.CLIMB,
        Agent.Action.SHOOT,
        Agent.Action.GRAB
    ]
    __directions = [0,1,2,3]
    def move(self, postion, action):
        if action==Agent.Action.TURN_LEFT:
            self.direction = self.direction+1%4
        elif action==Agent.Action.TURN_RIGHT:
            self.direction = abs(self.direction-1%4)
        elif action==Agent.Action.FORWARD:
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
            self.world[position].append('w')
        if scream:
            self.deadwumpus=True
    # ======================================================================
    # YOUR CODE ENDS
    # ======================================================================
