from display import *
from draw import *
from matrix import *
from parser import *
import math
import random

screen = new_screen()
color = [ 0, 0, 0 ]
edges = []
transform = [[1, 0, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 1]]
#
#add_edge(edges, 0, 0, 0, 100, 0, 0)
#add_edge(edges, 100, 0, 0, 100, 100, 0)
#add_edge(edges, 100, 100, 0, 0, 100, 0)
#add_edge(edges, 0, 100, 0, 0, 0, 0)
#add_edge(edges, 0, 0, 100, 100, 0, 100)
#add_edge(edges, 100, 0, 100, 100, 100, 100)
#add_edge(edges, 100, 100, 100, 0, 100, 100)
#add_edge(edges, 0, 100, 100, 0, 0, 100)
#add_edge(edges, 0, 0, 0, 0, 0, 100)
#add_edge(edges, 0, 100, 0, 0, 100, 100)
#add_edge(edges, 100, 100, 0, 100, 100, 100)
#add_edge(edges, 100, 0, 0, 100, 0, 100)
#
#matrix_mult(make_scale(2, 2, 2), transform)
#
#matrix_mult(make_rotX(30), transform)
#
#matrix_mult(make_rotY(30), transform)
#
#matrix_mult(make_translate(200, 200, 200), transform)
#
#
#
#matrix_mult(transform, edges)
#draw_lines(edges, screen, color)

parse_file("script", edges, transform, screen, color)


#display(screen)
#save_ppm(screen, 'binary.ppm')
#save_ppm_ascii(screen, 'ascii.ppm')
#save_extension(screen, 'img.png')
