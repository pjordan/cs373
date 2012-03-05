colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green', 'green', 'green']


motions = [[0, 0], [0, 1], [1, 0], [1, 0], [0, 1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]


def calculate():

    #DO NOT USE IMPORT
    #ENTER CODE BELOW HERE
    #ANY CODE ABOVE WILL CAUSE
    #HOMEWORK TO BE GRADED
    #INCORRECT
  
    def initialize_belief():
        alpha = sum( len(c) for c in colors)
        return [ [1.0/alpha] * len(c) for c in colors]

    def sensor_update( world, Z ):
        hit = Z == world
        return hit * sensor_right + (1-hit) * ( 1.0 - sensor_right)

    def sense_row(p,world,Z):
        return [ p[i] * sensor_update( world[i], Z ) for i in range( len(p) ) ]

    def sense(p, Z):
        q = [ sense_row(p[i], colors[i], Z) for i in range( len(p) ) ]
        alpha = sum( sum(q_row) for q_row in q)
        for i in range( len(q) ):
            for j in range( len(q[i]) ):
                q[i][j] /= alpha
        return q

    def move(p, direction):
        q = []
        for i in range(len(p)):
            q.append( [ 0.0 ] * len(p[i]) )
            for j in range(len(p[i])):
                q[i][j] = p[i][j] * (1.0-p_move) + p[(i-direction[0])%len(p)][(j-direction[1])%len(p[i])] * p_move
        return q

    p = initialize_belief()

    for pair in zip(motions,measurements):
        p = move(p, pair[0])
        p = sense(p, pair[1])

    #Your probability array must be printed 
    #with the following code.

    show(p)
    return p

