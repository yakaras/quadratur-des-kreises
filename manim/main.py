#Johann Uhl
from manim import *


class Kochanski(Scene):
    def construct(self):
        group = VGroup()
        Mittelpunkt = Dot([0,0,0], radius=0.05)
        m_label = Text(text="M", font_size=18).next_to(Mittelpunkt, UR).shift(0.23*DOWN).shift(0.23*LEFT)
        circle = Circle(radius=2, color=WHITE)
        line = Line(start=(0,0,0), end=(2,0,0), stroke_width=0.5)        

        group.add(Mittelpunkt)
        group.add(m_label)
        group.add(circle)
        group.add(line)
        dot_a = Dot([0,2,0],radius=0.05)
        dot_b = Dot([-2,0,0],radius=0.05)
        dot_c = Dot([0,-2,0],radius=0.05)
        group.add(dot_a)
        group.add(dot_b)
        group.add(dot_c)

        a_label = Text(text="A", font_size=20).next_to(dot_a, UR).shift(0.15*DOWN).shift(0.23*LEFT)
        b_label = Text(text="B", font_size=20).next_to(dot_b, UL).shift(0.23*DOWN).shift(0.1*RIGHT)
        c_label = Text(text="C", font_size=20).next_to(dot_c, DR).shift(0.23*LEFT).shift(0.1*UP)
        group.add(a_label)
        group.add(b_label)
        group.add(c_label)

        self.play(Create(circle), Create(Mittelpunkt), Create(m_label))
        self.play(Create(line))
        self.wait(1.5)
        self.play(Create(dot_a), Create(dot_b), Create(dot_c), Create(a_label), Create(b_label), Create(c_label))
        self.wait(3)

        gerade_ac = Line(start=dot_a, end=dot_c, stroke_width=0.8)
        gerade_cd = Line(start=dot_b, end=(2,0,0), stroke_width=0.8)
        group.add(gerade_ac)
        group.add(gerade_cd)

        self.play(Create(gerade_ac), Create(gerade_cd))

        self.wait(2)


        dot_y = Dot([-1,-1.732,0],radius=0.05)
        gerade_by = Line(start=dot_b, end=dot_y, stroke_width=0.8)
        radius_arc = ArcBetweenPoints(end=0, start=[-1,-1.732,0], stroke_width=0.8 , color=YELLOW, radius=2)
        gerade_my = Line(start=Mittelpunkt, end=dot_y, stroke_width=0.8)
        group.add(dot_y)
        group.add(gerade_by)
        group.add(radius_arc)
        group.add(gerade_my)
        self.play(Create(dot_y), Create(gerade_by), Create(radius_arc), Create(gerade_my))

        self.wait(2)
        tangente = TangentLine(circle, alpha=0.75, length=5, color=WHITE, stroke_width=0.8)
        group.add(tangente)
        self.play(Create(tangente))

        self.wait(2)
        dot_x = Dot([-1.155554,-2,0],radius=0.05)
        x_label = Text(text="X", font_size=20).next_to(dot_x, DR).shift(0.23*LEFT).shift(0.1*UP)
        gerade_mx = Line(start=Mittelpunkt, end=dot_x, stroke_width=0.8)
        group.add(dot_x)
        group.add(x_label)
        group.add(gerade_mx)


        self.play(Create(gerade_mx))
        self.play(Create(dot_x), Create(x_label))

        self.wait(2)
        dot_x1 = Dot([-1.155554+2,-2,0],radius=0.02)
        dot_x2 = Dot([-1.155554+4,-2,0],radius=0.02)
        dot_z =  Dot([-1.155554+6,-2,0],radius=0.05)
        z_label = Text(text="Z", font_size=20).next_to(dot_z, DR).shift(0.23*LEFT).shift(0.1*UP)
        gerade_xx1 = Line(start=dot_x, end=dot_x1, stroke_width=1.5)
        gerade_x1x2 = Line(start=dot_x1, end=dot_x2, stroke_width=1.5)
        gerade_x2z = Line(start=dot_x2, end=dot_z, stroke_width=1.5)
        group.add(dot_x1)
        group.add(dot_x2)
        group.add(dot_z)
        group.add(z_label)
        group.add(gerade_xx1)
        group.add(gerade_x1x2)
        group.add(gerade_x2z)

        self.play(Create(dot_x1), Create(gerade_xx1))
        self.play(Create(dot_x2), Create(gerade_x1x2))
        self.play(Create(dot_z), Create(gerade_x2z), Create(z_label))
        self.wait(1)

        gerade_az = Line(start=dot_a, end=dot_z, stroke_width=1)
        group.add(gerade_az)
        self.play(Create(gerade_az))
        gerade_az1 = Line(start=dot_a, end=dot_z, stroke_width=1.5, color=RED)
        group.add(gerade_az1)
        self.play(Create(gerade_az1))

        dot_z1 = Dot([6.1178416,-0.457774,0],radius=0.02)
        dot_a1 = Dot([1.2733972135,3.5422255141,0],radius=0.02)
        gerade_aa1 = Line(start=dot_a, end=dot_a1, stroke_width=0.8)
        gerade_zz1 = Line(start=dot_z, end=dot_z1, stroke_width=0.8)
        gerade_a1z1 = Line(start=dot_a1, end=dot_z1, stroke_width=0.8)
        group.add(dot_z1)
        group.add(dot_a1)
        group.add(gerade_aa1)
        group.add(gerade_zz1)
        group.add(gerade_a1z1)

        self.play(Create(dot_z1), Create(dot_a1), Create(gerade_aa1), Create(gerade_zz1), Create(gerade_a1z1))
        self.wait(2)



        rect = Polygon([0,2,0], [-1.155554+6,-2,0], [6.1178416,-0.457774,0], [1.2733972135,3.5422255141,0], color=RED, stroke_width=1)
        rect1 = Polygon([3.296537535,0-1,0], [-3.296537535,0-1,0], [-3.296537535,2-1,0], [3.296537535,2-1,0], color=RED, stroke_width=1)
        rect2 = Polygon([3.296537535,0-1,0], [-3.296537535,0-1,0], [-3.296537535,2-1,0], [3.296537535,2-1,0], color=RED, stroke_width=1, fill_opacity=1)

        self.play(Create(rect), FadeOut(group))
        self.wait(0.5)
        self.play(Transform(rect, rect1, stretch=True))
        self.wait(0.3)
        self.play(Transform(rect1, rect2, stretch=True))
        self.wait(1)
        self.play(GrowFromCenter(MathTex(r"\pi")))
        self.wait(2)



#unten links (-3.296537535,0)
#unten rechts (3.296537535,0)
#oben links (-3.296537535,2)
#oben rechts (3.296537535,2)
