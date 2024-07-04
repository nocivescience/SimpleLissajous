from manim import *
class Lissajous(Scene):
    conf={
        'radius': 1,
        'frequencia_1': 3,
        'frequencia_2': 2,
    }
    def construct(self):
        circle_1 = Circle(radius=self.conf['radius']).move_to(LEFT*3+2*UP)
        circle_2 = Circle(radius=self.conf['radius']).move_to(RIGHT*3+2*DOWN)
        dot_1 = Dot().move_to(circle_1.points[0])
        dot_2 = Dot().move_to(circle_2.point_from_proportion(.25))
        def update_dot_1(dot, alpha):
            dot.move_to(circle_1.points[alpha])
        circle_1.add(dot_1)
        circle_2.add(dot_2)
        self.play(Create(circle_1), Create(circle_2))
        self.play(
            UpdateFromAlphaFunc(dot_1, update_dot_1),
            UpdateFromAlphaFunc(dot_2, lambda dot, alpha: dot.move_to(circle_2.points[alpha]))
        )
        self.wait(1)