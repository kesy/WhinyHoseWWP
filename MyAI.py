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
        self.home=False
        self.num_moves=0
<<<<<<< HEAD
        #self.turn=[Agent.Action.FORWARD, Agent.Action.TURN_LEFT]
        self.turned=False
        self.moves=[]
=======
        #adding stuff for testing git
>>>>>>> 37bc0365009b9c563069ec7b6fec48792c676ced

        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================

    def getAction( self, stench, breeze, glitter, bump, scream ):
        # ======================================================================
        # YOUR CODE BEGINS
        # ======================================================================
        action = Agent.Action.TURN_RIGHT#self.__actions [ random.randrange ( len ( self.__actions ) ) ]

        if self.position not in self.world:
            self.world[self.position]=set()
        
        if self.position[0]==1:
            self.world[self.position].add(3)
        if self.position[1]==1:
            self.world[self.position].add(2)
            
        self.observe(self.position, stench, breeze, glitter, bump, scream)
        self.num_moves+=1
        if self.home:
            action = self.go_home()

        elif 'g' in self.world[self.position]:
            self.moves.append(Agent.Action.GRAB)
            self.home=True
            return Agent.Action.GRAB
        elif 's' in self.world[self.position] and self.hasarrow:
            action = Agent.Action.SHOOT
            self.hasarrow=False
        elif self.position == (1,1) and 'b' in self.world[self.position]:
            action = Agent.Action.CLIMB
        elif self.direction in self.world[self.position]:
            action = Agent.Action.TURN_LEFT
        elif self.direction not in self.world[self.position]:
            action = Agent.Action.FORWARD
              
        elif self.num_moves>=10:
            self.home=True
            action=self.go_home()
        
       # print(self.position, self.direction, action, self.num_moves, self.world)  
        print(self.position,self.direction, action, self.moves)
        self.move(self.position, action)
        if not self.home:
            self.moves.append(action)
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
    
    def go_home(self):   
        if self.position == (1,1):
            return Agent.Action.CLIMB
        while self.moves:
            move = self.moves.pop()
            if move == Agent.Action.TURN_RIGHT:
                return Agent.Action.TURN_LEFT
            if move == Agent.Action.TURN_LEFT:
                return Agent.Action.TURN_RIGHT
            if move == Agent.Action.FORWARD and not self.turned:
                self.moves.append(Agent.Action.TURN_RIGHT)
                self.turned=True
                
                return Agent.Action.TURN_RIGHT
            if move == Agent.Action.FORWARD:
                return Agent.Action.FORWARD
            
    
    
    def move(self, postion, action):
        if action==Agent.Action.TURN_LEFT:
            self.direction = (self.direction+1)%4
        elif action==Agent.Action.TURN_RIGHT:
            self.direction = (self.direction-1)%4
        elif action==Agent.Action.FORWARD and self.direction not in self.world[self.position]:
            if self.direction==0 and 0 not in self.world[self.position]:
                self.position=(self.position[0]+1,self.position[1])
            elif self.direction==1 and 1 not in self.world[self.position]:
                self.position=(self.position[0],self.position[1]+1)
            elif self.direction==2 and self.position[0]>1:
                self.position=(self.position[0]-1,self.position[1])
            elif self.direction==3 and self.position[1]>1:
                self.position=(self.position[0],self.position[1]-1)
    
    
    def observe(self, position, stench, breeze, glitter, bump, scream):
        if stench:
            self.world[position].add('s')
        if breeze:
            self.world[position].add('b')
        if glitter:
            self.world[position].add('g')
        if bump:
            #self.world[position].add('w')
            self.world[position].add(self.direction)
        if scream:
            self.deadwumpus=True
    # ======================================================================
    # YOUR CODE ENDS
    # ======================================================================
