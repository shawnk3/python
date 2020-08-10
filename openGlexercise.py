import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

FPS  = 120
fpsClock = pg.time.Clock()

cubeVertices = ((1,1,1),(1,1,-1),(1,-1,-1),(1,-1,1),(-1,1,1),(-1,-1,-1),(-1,-1,1),(-1, 1,-1)) #specs of cube
cubeEdges = ((0,1),(0,3),(0,4),(1,2),(1,7),(2,5),(2,3),(3,6),(4,6),(4,7),(5,6),(5,7)) # how edges are connected
cubeQuads = ((0,3,6,4),(2,5,6,3),(1,2,5,7),(1,0,4,7),(7,4,6,5),(2,3,0,1)) # 
colors = [(1,1,0),(5,1,0),(2,0,1),(3,0,0),(1,1,1),(0,1,1),(1,0,0),(0,1,0),(0,0,1),(0,0,0),(1,1,1),(0,1,1),]
def wireCube():
    glBegin(GL_LINES)
    for cubeEdge in cubeEdges:
        for cubeVertex in cubeEdge:
            glVertex3fv(cubeVertices[cubeVertex])
    glEnd()
    
def solidCube():
    glBegin(GL_QUADS)
    x = 0
    for cubeQuad in cubeQuads:
        x = 0
        for cubeVertex in cubeQuad:
            x+=1
            glColor3fv(colors[x])
            glVertex3fv(cubeVertices[cubeVertex])
    glEnd()
    
    
pg.init()
display = (720 , 600)
pg.display.set_mode(display, DOUBLEBUF|OPENGL)

#gluPerspective is code that determines the perspective, as it sounds. 
# The first value is the degree value of the field of view (fov). 
# The second value is the aspect ratio, which is the display width divided by the display height. 
# The next two values here are the znear and zfar, which are the near and far clipping planes.

gluPerspective(45, (display[0]/display[1]), 2, 50)

glTranslatef(0.0, 0.0, -5) #chance the field of view,i.e. change the position of objects


while True:
   
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            if event.key  == pg.K_LEFT:
                glTranslate(-1.0,0.0,0.0)
            if event.key  == pg.K_RIGHT:
                glTranslate(1.0,0.0,0.0) 
            if event.key == pg.K_UP:
                   glTranslate(0.0,1.0,0.0)
            if event.key == pg.K_DOWN:
                   glTranslate(0.0,-1.0,0.0)      
        # if event.type == pg.MOUSEBUTTONDOWN:
        #     if event.button == 4:
        #         glTranslate(0.0,0.0,1.0)
        #     if event.button == 5:
        #         glTranslate(0.0,0.0,-1.0)       
        # glRotatef(1, 1, 1, 1)
        x = glGetDoublev(GL_MODELVIEW_MATRIX)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glTranslate(0.0,0.0,.10) 
        solidCube()
        wireCube()
        pg.display.flip()
        pg.time.wait(1)
    fpsClock.tick(FPS)