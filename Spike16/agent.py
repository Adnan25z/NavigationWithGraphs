from vector2d import Vector2D
from graphics import egi
from path import Path

class Agent(object):
    def __init__(self, start_pos, speed, color='GREEN'):
        self.pos = start_pos
        self.path_set = False
        self.color = color
        self.path = Path()
        self.path_pts = []
        self.speed = speed
        
    def update(self):
        self.follow_path()
    
    def set_new_target(self, new_target):
        self.path.set_pts(new_target)
        self.path.current = 0  # Reset the current point index

    def render(self, color=None):
        # draw
        egi.set_pen_color(name=self.color)
        egi.cross(self.pos,10)
        egi.circle(self.pos,10)

    def follow_path(self):
        to_target = self.path.current_pt() - self.pos
        dist = to_target.length()
        threshold = 5
        if dist < threshold and not self.path.is_finished():
            self.path.inc_current_pt()
        # Calculate the direction vector
        direction = (self.path.current_pt() - self.pos).get_normalised()
        # Move agent in the direction of the target by its speed
        self.pos += direction * self.speed