import pygame
import pygame.gfxdraw

def color_scale(hex_str, scale_factor):
    """
    :param hex_str:
    :param scale_factor:
    :return:
    """
    hex_str = hex_str.strip('#')
    if scale_factor < 0 or len(hex_str) != 6:
        return hex_str
    r, g, b = int(hex_str[:2], 16), int(hex_str[2:4], 16), int(hex_str[4:], 16)
    r = int(_clamp(r * scale_factor))
    g = int(_clamp(g * scale_factor))
    b = int(_clamp(b * scale_factor))
    return r, g, b

def _clamp(val, minimum=0, maximum=255):
    if val < minimum:
        return minimum
    if val > maximum:
        return maximum
    return val

def color_scale_hexa(hex_str, scale_factor):
    """
    :param hex_str:
    :param scale_factor:
    :return: code couleur en hexadecimal
    """
    r, g, b = color_scale(hex_str, scale_factor)
    return '#%02x%02x%02x' % (r, g, b)

def filled_aacircle(screen, x_center, y_center, ray, color):
    pygame.gfxdraw.filled_circle(screen, x_center, y_center, ray, color)
    pygame.gfxdraw.aacircle(screen, x_center, y_center, ray, color)

# -------------------------------------------------------------
# FUNCTION : get_line_points
#   Bresenham's Line Algorithm
#   Produces a list of tuples
#   from start and end
#   points1 = get_line_points((0, 0), (3, 4))
#   points2 = get_line_points((3, 4), (0, 0))
#   assert (set(points1) == set(points2))
#   print points1[(0, 0), (1, 1), (1, 2), (2, 3), (3, 4)]
#   print points2[(3, 4), (2, 3), (1, 2), (1, 1), (0, 0)]
# -------------------------------------------------------------
def get_line_points(start, end):
    """
    :param start: tuples(x, y)
    :param end: tuples(x, y)
    :return: [(x1, y1), (x2, y2)]
    """

    #
    #   Setup initial conditions
    #
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1

    #
    #   Determine how steep the line is
    #
    is_steep = abs(dy) > abs(dx)

    #
    #   Rotate line
    #
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    #
    #   Swap start and end points if necessary and store swap state
    #
    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True

    #
    #   Recalculate differentials
    #
    dx = x2 - x1
    dy = y2 - y1

    #
    #   Calculate error
    #
    error = int(dx / 2.0)
    ystep = 1 if y1 < y2 else -1

    #
    #   Iterate over bounding box generating points between start and end
    #
    y = y1
    points = []
    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx

    #
    #   Reverse the list if the coordinates were swapped
    #
    if swapped:
        points.reverse()

    #
    #   return points
    #
    return points

class GridCoords:
    def __init__(self, width, height, step):
        self.x = []
        self.y = []
        x = 0
        for i in range(0, width):
            self.x.append(x)
            x += step
        y = 0
        for i in range(0, height):
            self.y.append(y)
            y += step
