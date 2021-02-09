from manim import *
import math

class CasesExample(Scene):
    def construct(self):
        title = Tex(r"\underline{Hyperoperations}")
        title.move_to(UP*3)

        text = MathTex(
            r"H_n(a, b)=a[n]b="
            r"\begin{cases}"
            r"b+1, & \text{if } n=0 \\"
            r"a, & \text{if } n=1 \text{ and } b=0 \\"
            r"0, & \text{if } n=2 \text{ and } b=0 \\"
            r"1, & \text{if } n \geq 3 \text{ and } b=0 \\"
            r"H_{n-1}(a,H_n(a,b-1)), & \text{otherwise}"
            r"\end{cases}"
        ).scale(0.85)

        text1 = MathTex(
            r"H_n(a, b)=a[n]b="
            r"\begin{cases}"
            r"b+1, & \text{if } n=0 \\"
            r"a, & \text{if } n=1 \text{ and } b=0 \\"
            r"0, & \text{if } n=2 \text{ and } b=0 \\"
            r"1, & \text{if } n \geq 3 \text{ and } b=0 \\"
            r"H_{n-1}(a,H_n(a,b-1)), & \text{otherwise}"
            r"\end{cases}"
        ).scale(0.85)

        eq = MathTex(
            "=",  #0
            r"a[n-1](a[n-1](a[n-1](\cdots [n-1](a[n-1](a[n-1]a \cdots))),",  #1
            r"\ \  n \geq 2"  #2
        ).scale(0.85)

        text1.move_to(UP)
        eq.next_to(text1, DOWN*3)

        # title = MathTex(r"\text{The Recursive Definition of } \mathbb{N}_0 \text{:}")
        # title.next_to(text, UP)
        self.play(DrawBorderThenFill(text), Write(title))
        self.play(Transform(text, text1))
        self.play(DrawBorderThenFill(eq))

        brace = Brace(eq[1], DOWN, buff=SMALL_BUFF)
        t1 = brace.get_text("b copies of a")

        self.play(
            GrowFromCenter(brace),
            FadeIn(t1)
        )
        self.wait(2)
        # self.play(Write(title))

class HyperOpDemo(Scene):
    def construct(self):
        title = Tex(r"\underline{Multiplication}")
        title.move_to(UP*3)

        subtitle = MathTex(r"H_2(a, 7)=a[2]7")
        subtitle.to_edge(LEFT)
        subtitle.shift(RIGHT)
        subtitle.shift(UP*2)

        # centerText = MathTex("a+a+a+a+a+a=7a")

        c1 = MathTex("a")
        p1 = MathTex("+")
        c1.move_to(LEFT*3)
        p1.move_to(LEFT*2.5)

        c2 = MathTex("a")
        p2 = MathTex("+")
        c2.move_to(LEFT*2)
        p2.move_to(LEFT*1.5)

        c3 = MathTex("a")
        p3 = MathTex("+")
        c3.move_to(LEFT)
        p3.move_to(LEFT*0.5)

        c4 = MathTex("a")
        p4 = MathTex("+")
        p4.move_to(RIGHT*0.5)

        c5 = MathTex("a")
        p5 = MathTex("+")
        c5.move_to(RIGHT)
        p5.move_to(RIGHT*1.5)

        c6 = MathTex("a")
        p6 = MathTex("+")
        c6.move_to(RIGHT*2)
        p6.move_to(RIGHT*2.5)

        c7 = MathTex("a")
        c7.move_to(RIGHT*3)

        self.play(Write(title), Write(subtitle))
        # self.play(Write(centerText))
        self.wait(2)

        self.play(Write(c1), run_time=0.5)
        self.play(Write(p1), run_time=0.25)
        self.play(Write(c2), run_time=0.5)
        self.play(Write(p2), run_time=0.25)
        self.play(Write(c3), run_time=0.5)
        self.play(Write(p3), run_time=0.25)
        self.play(Write(c4), run_time=0.5)
        self.play(Write(p4), run_time=0.25)
        self.play(Write(c5), run_time=0.5)
        self.play(Write(p5), run_time=0.25)
        self.play(Write(c6), run_time=0.5)
        self.play(Write(p6), run_time=0.25)
        self.play(Write(c7), run_time=0.5)
