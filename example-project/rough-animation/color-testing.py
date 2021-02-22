from manim import *

class colortest(Scene):
    def construct(self):
        r = 0.25
        # Blues
        a = Dot(radius=r, fill_opacity=1, color=BLUE_A).move_to(UP*3+LEFT*4)
        b = Dot(radius=r, fill_opacity=1, color=BLUE_B).move_to(UP*3+LEFT*3.25)
        c = Dot(radius=r, fill_opacity=1, color=BLUE_C).move_to(UP*3+LEFT*2.5)
        d = Dot(radius=r, fill_opacity=1, color=BLUE_D).move_to(UP*3+LEFT*1.75)
        e = Dot(radius=r, fill_opacity=1, color=BLUE_E).move_to(UP*3+LEFT)
        f = Dot(radius=r, fill_opacity=1, color=DARK_BLUE).move_to(UP*3+LEFT*.25)
        #Golds
        g = Dot(radius=r, fill_opacity=1, color=GOLD_A).move_to(UP*3+RIGHT)
        h = Dot(radius=r, fill_opacity=1, color=GOLD_B).move_to(UP*3+RIGHT*1.75)
        i = Dot(radius=r, fill_opacity=1, color=GOLD_C).move_to(UP*3+RIGHT*2.5)
        j = Dot(radius=r, fill_opacity=1, color=GOLD_D).move_to(UP*3+RIGHT*3.25)
        k = Dot(radius=r, fill_opacity=1, color=GOLD_E).move_to(UP*3+RIGHT*4)
        #Greens
        l = Dot(radius=r, fill_opacity=1, color=GREEN_A).move_to(UP*2.25+LEFT*4)
        m = Dot(radius=r, fill_opacity=1, color=GREEN_B).move_to(UP*2.25+LEFT*3.25)
        n = Dot(radius=r, fill_opacity=1, color=GREEN_C).move_to(UP*2.25+LEFT*2.5)
        o = Dot(radius=r, fill_opacity=1, color=GREEN_D).move_to(UP*2.25+LEFT*1.75)
        p = Dot(radius=r, fill_opacity=1, color=GREEN_E).move_to(UP*2.25+LEFT)
        q = Dot(radius=r, fill_opacity=1, color=GREEN_SCREEN).move_to(UP*2.25+LEFT*.25)
        #Maroons
        r1 = Dot(radius=r, fill_opacity=1, color=MAROON_A).move_to(UP*2.25+RIGHT)
        s = Dot(radius=r, fill_opacity=1, color=MAROON_B).move_to(UP*2.25+RIGHT*1.75)
        t = Dot(radius=r, fill_opacity=1, color=MAROON_C).move_to(UP*2.25+RIGHT*2.5)
        u = Dot(radius=r, fill_opacity=1, color=MAROON_D).move_to(UP*2.25+RIGHT*3.25)
        v = Dot(radius=r, fill_opacity=1, color=MAROON_E).move_to(UP*2.25+RIGHT*4)
        #Purples
        w = Dot(radius=r, fill_opacity=1, color=PURPLE_A).move_to(UP*1.5+LEFT*4)
        x = Dot(radius=r, fill_opacity=1, color=PURPLE_B).move_to(UP*1.5+LEFT*3.25)
        y = Dot(radius=r, fill_opacity=1, color=PURPLE_C).move_to(UP*1.5+LEFT*2.5)
        z = Dot(radius=r, fill_opacity=1, color=PURPLE_D).move_to(UP*1.5+LEFT*1.75)
        aa = Dot(radius=r, fill_opacity=1, color=PURPLE_E).move_to(UP*1.5+LEFT)

        blues = VGroup(a, b, c, d, e, f)
        golds = VGroup(g, h, i, j, k)
        greens = VGroup(l, m, n, o, p, q)
        maroons = VGroup(r1, s, t, u, v)
        purples = VGroup(w, x, y, z, aa)
        #reds = VGroup()
        #teals = VGroup()
        #yellows = VGroup()

        self.play(Write(blues))
        self.play(Write(golds))
        self.play(Write(greens))
        self.play(Write(maroons))
        self.play(Write(purples))

        self.wait(1)