from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing
See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    f = open(fname, 'r')
    file = f.read()
    lines = file.split("\n")
    x = 0
    while(x < len(lines)):
        line = lines[x].split(" ")
        line2 = []
        if(x+1 < len(lines)): line2 = lines[x+1].split(" ")
        if(line[0] == 'line'):
            add_edge(points, int(line2[0]), int(line2[1]), int(line2[2]), int(line2[3]), int(line2[4]), int(line2[5]))
        elif(line[0] == 'ident'):
            ident(transform)
        elif(line[0] == 'scale'):
            matrix_mult(make_scale(int(line2[0]), int(line2[1]), int(line2[2])), transform)
        elif(line[0] == 'translate'):
            matrix_mult(make_translate(int(line2[0]), int(line2[1]), int(line2[2])), transform)
        elif(line[0] == 'rotate'):
            matrix_mult(make_rot(line2[0], int(line2[1])), transform)
        elif(line[0] == 'apply'):
            matrix_mult(transform, points)
        elif(line[0] == 'display'):
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
        elif(line[0] == 'save'):
            clear_screen(screen)
            draw_lines(points, screen, color)
            save_extension(screen, line2[0])
        x = x + 1
    
    

