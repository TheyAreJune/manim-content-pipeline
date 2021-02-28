from manim import *
import numpy as n

class disp(Scene):
    def construct(self):
        s = 2

        east = Arrow([-4.5/s, 0/s, 0], ORIGIN, buff=0, color=RED)
        east_text = Text('450,000 J').next_to(east.get_center(), DOWN*0.5).scale(0.5)
        self.play(ShowCreation(east), ShowCreation(east_text))

        north = Arrow([0/s, -4.0/s, 0.0], ORIGIN, buff=0, color=RED)
        north_text = Text('400,000 J').scale(0.5).shift(DOWN*(2/s)+RIGHT)
        self.play(ShowCreation(north), ShowCreation(north_text))

        result = Arrow(ORIGIN, [4.5/s, 4.0/s, 0.0], buff=0, color=RED)
        result_text = Text('602,000 J').scale(0.5).shift(UP*(2/s+0.1)+RIGHT*0.1)
        self.play(ShowCreation(result), ShowCreation(result_text))

        self.wait(0.5)

        east_new = Arrow(ORIGIN, [4.5/s, 0/s, 0], buff=0, color=PURPLE)
        east_new_text = Text('450,000 J').next_to(east_new.get_center(), DOWN*0.5).scale(0.5)

        north_new = Arrow([4.5/2, 0.0, 0.0], [4.5/s, 4.0/s, 0.0], buff=0, color=PURPLE)
        north_new_text = Text('400,000 J').scale(0.5).shift(UP*(2/s)+RIGHT*3.25)
        self.play(
            ShowCreation(east_new),
            ShowCreation(east_new_text),
            FadeOut(east),
            FadeOut(east_text),
            ShowCreation(north_new),
            ShowCreation(north_new_text),
            FadeOut(north),
            FadeOut(north_text)
        )
        self.wait(2)