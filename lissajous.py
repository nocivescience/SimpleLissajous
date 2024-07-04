from manim import *

class Lissajous(Scene):
    conf = {
        'radius': 1,
        'frequencia_1': 3,
        'frequencia_2': 2,
    }

    def construct(self):
        circle_1 = Circle(radius=self.conf['radius']).move_to(LEFT * 3 + 2 * UP)
        circle_2 = Circle(radius=self.conf['radius']).move_to(RIGHT * 3 + 2 * DOWN)
        dot_1 = Dot().move_to(circle_1.points[0])
        dot_2 = Dot().move_to(circle_2.point_from_proportion(.25))

        def update_dot_1(dot, alpha):
            dot.move_to(circle_1.point_from_proportion(alpha*self.conf['frequencia_1']%1))

        def update_dot_2(dot, alpha):
            dot.move_to(circle_2.point_from_proportion(alpha*self.conf['frequencia_2']%1))

        dot_intesect = Dot().move_to(np.array([dot_1.get_center()[0], dot_2.get_center()[1],0]))
        dot_intesect.add_updater(lambda x: x.move_to(np.array([dot_1.get_center()[0], dot_2.get_center()[1],0])))
        self.add_foreground_mobject(dot_intesect)
        path=TracedPath(dot_intesect.get_center, stroke_color=RED, stroke_width=2)
        
        square = Square(side_length=2, color=WHITE).move_to(np.array([circle_1.get_center()[0], circle_2.get_center()[1],0]))
        
        # square = Square(side_length=2, color=WHITE).move_to(dot_intesect.get_center())
        # square.add_updater(lambda x: x.move_to(dot_intesect.get_center()))

        line_1 = Line(dot_1.get_center(), dot_intesect.get_center(), color=BLUE)
        line_2 = Line(dot_2.get_center(), dot_intesect.get_center(), color=BLUE)
        
        line_1.add_updater(lambda x: x.put_start_and_end_on(dot_1.get_center(), dot_intesect.get_center()))
        line_2.add_updater(lambda x: x.put_start_and_end_on(dot_2.get_center(), dot_intesect.get_center())) 

        # self.play(Create(circle_1), Create(circle_2))
        self.add(dot_intesect, path, line_1, line_2, dot_1, dot_2, square, circle_1, circle_2)
        self.play(
            UpdateFromAlphaFunc(dot_1, update_dot_1, run_time=6, rate_func=linear),
            UpdateFromAlphaFunc(dot_2, update_dot_2, run_time=6, rate_func=linear),
            run_time=5,
        )
        self.wait(1)

# To run the scene, use the following command in your terminal:
# manim -pql your_script_name.py Lissajous
