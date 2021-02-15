from manim import *

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

class NotationExplain(Scene):
    def construct(self):
        centerdivider = Line(UP*1.75, DOWN*1.75)
        header = Tex("\\underline{Knuth's Up-Arrow Notation}")

        knuths1 = MathTex(r"n/a")
        knuths2 = MathTex(r"n/a")
        knuths3 = MathTex(r"a \uparrow b")
        knuths4 = MathTex(r"a \uparrow \uparrow b")
        knuths5 = MathTex(r"a \uparrow \uparrow \uparrow b")
        knuths6 = MathTex(r"a \uparrow \uparrow \uparrow \uparrow b")

        operations1 = Tex("1")
        operations2 = Tex("2")
        operations3 = Tex("3")
        operations4 = Tex("4")
        operations5 = Tex("5")
        operations6 = Tex("6")

        header.move_to(UP*3)

        knuths1.move_to(LEFT+UP*1.5)
        knuths2.move_to(LEFT+UP*0.9)
        knuths3.move_to(LEFT+UP*0.3)
        knuths4.move_to(LEFT+DOWN*0.3)
        knuths5.move_to(LEFT+DOWN*0.9)
        knuths6.move_to(LEFT+DOWN*1.5)

        operations1.move_to(RIGHT+UP*1.5)
        operations2.move_to(RIGHT+UP*0.9)
        operations3.move_to(RIGHT+UP*0.3)
        operations4.move_to(RIGHT+DOWN*0.3)
        operations5.move_to(RIGHT+DOWN*0.9)
        operations6.move_to(RIGHT+DOWN*1.5)

        self.play(Write(header))
        self.play(ShowCreation(centerdivider))
        self.play(ShowCreation(knuths1), ShowCreation(operations1))
        # self.wait(0.5)
        self.play(ShowCreation(knuths2), ShowCreation(operations2))
        # self.wait(0.5)
        self.play(ShowCreation(knuths3), ShowCreation(operations3))
        # self.wait(0.5)
        self.play(ShowCreation(knuths4), ShowCreation(operations4))
        # self.wait(0.5)
        self.play(ShowCreation(knuths5), ShowCreation(operations5))
        # self.wait(0.5)
        self.play(ShowCreation(knuths6), ShowCreation(operations6))
        self.wait(1)

        # Need to do! The collumns are not aligned and must be fixed. LaTeX Tables do not appear to be working.