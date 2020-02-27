from display import *
from draw import *
from matrix import *
from parser import *
import math
import random

screen = new_screen()
color = [ 255, 255, 255 ]
edges = []
transform = ident(new_matrix())

add_edge(edges, 0, 0, 0, 100, 0, 0)
add_edge(edges, 100, 0, 0, 100, 100, 0)
add_edge(edges, 100, 100, 0, 0, 100, 0)
add_edge(edges, 0, 100, 0, 0, 0, 0)
add_edge(edges, 0, 0, 100, 100, 0, 100)
add_edge(edges, 100, 0, 100, 100, 100, 100)
add_edge(edges, 100, 100, 100, 0, 100, 100)
add_edge(edges, 0, 100, 100, 0, 0, 100)
add_edge(edges, 0, 0, 0, 0, 0, 100)
add_edge(edges, 0, 100, 0, 0, 100, 100)
add_edge(edges, 100, 100, 0, 100, 100, 100)
add_edge(edges, 100, 0, 0, 100, 0, 100)

transform = make_scale(2, 2, 2)
print_matrix(transform)
print("\n")
draw_lines(edges, screen, color)

matrix_mult(make_rotZ(45), transform)
#print_matrix(transform)
#print("\n")
matrix_mult(make_translate(50, 50, 50), transform)
print_matrix(transform)



matrix_mult(transform, edges)
draw_lines(edges, screen, color)


display(screen)
#save_ppm(screen, 'binary.ppm')
#save_ppm_ascii(screen, 'ascii.ppm')
#save_extension(screen, 'img.png')
