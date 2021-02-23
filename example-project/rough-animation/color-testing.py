from manim import *

class colors(Scene):
    def construct(self):
        # Radius
        r = 0.25

        l = 0
        s = 5.5

        #labels
        misc = Tex("\\underline{Miscellaneous}").move_to(RIGHT*((7*s)/10))

        a = Tex("A").move_to(UP*3 + LEFT*((s-2)-0.75))
        b = Tex("B").move_to(UP*3 + LEFT*((s-2)-0.75*2))
        c1 = Tex("C").move_to(UP*3 + LEFT*((s-2)-0.75*3))
        d = Tex("D").move_to(UP*3 + LEFT*((s-2)-0.75*4))
        e = Tex("E").move_to(UP*3 + LEFT*((s-2)-0.75*5))

        purple = Tex("PURPLE -")
        blue = Tex("BLUE -")
        teal = Tex("TEAL -")
        green = Tex("GREEN -")
        yellow = Tex("YELLOW -")
        gold = Tex("GOLD -")
        red = Tex("RED -")
        maroon = Tex("MAROON -")

        c = (
            PURPLE_A,
            PURPLE_B,
            PURPLE_C,
            PURPLE_D,
            PURPLE_E,
            BLUE_A,
            BLUE_B,
            BLUE_C,
            BLUE_D,
            BLUE_E,
            TEAL_A,
            TEAL_B,
            TEAL_C,
            TEAL_D,
            TEAL_E,
            GREEN_A,
            GREEN_B,
            GREEN_C,
            GREEN_D,
            GREEN_E,
            YELLOW_A,
            YELLOW_B,
            YELLOW_C,
            YELLOW_D,
            YELLOW_E,
            GOLD_A,
            GOLD_B,
            GOLD_C,
            GOLD_D,
            GOLD_E,
            RED_A,
            RED_B,
            RED_C,
            RED_D,
            RED_E,
            MAROON_A,
            MAROON_B,
            MAROON_C,
            MAROON_D,
            MAROON_E,
            WHITE,
            LIGHT_GRAY,
            GRAY,
            GREY_BROWN,
            DARK_GREY,
            DARKER_GREY,
            LIGHT_PINK,
            PINK,
            ORANGE,
            LIGHT_BROWN,
            DARK_BROWN,
            DARK_BLUE,
            GREEN_SCREEN,
        )

        section = (
            5, #blues
            5, #golds
            5, #greens
            5, #maroons
            5, #purples
            5, #reds
            5, #teals
            5, #yellows
            6, #misc1
            7 #misc 2
        )

        self.play(Write(a), run_time=0.25)
        self.play(Write(b), run_time=0.25)
        self.play(Write(c1), run_time=0.25)
        self.play(Write(d), run_time=0.25)
        self.play(Write(e), run_time=0.25)

        for o in range(len(section)):
            for w in range(section[o]):
                if o < 8:
                    if o == 0 and w == 0:
                        purple.move_to(UP * (2.25 - ((3 * o) / 4)) + LEFT * (s-(3*(w + 1))/4))
                        self.play(Write(purple), run_time=0.25)
                        self.play(
                            Write(
                                Dot(
                                    point = UP * (2.25 - ((3 * o) / 4)) + LEFT * ((s-2)-(3*(w + 1))/4),
                                    radius = r,
                                    fill_opacity = 1,
                                    color = c[l],
                                )
                            ),
                        run_time=0.25
                        )
                    elif o == 1 and w == 0:
                        blue.move_to(UP * (2.25 - ((3 * o) / 4)) + LEFT * (s-(3*(w + 1))/4))
                        self.play(Write(blue), run_time=0.25)
                        self.play(
                            Write(
                                Dot(
                                    point = UP * (2.25 - ((3 * o) / 4)) + LEFT * ((s-2)-(3*(w + 1))/4),
                                    radius = r,
                                    fill_opacity = 1,
                                    color = c[l],
                                )
                            ),
                        run_time=0.25
                        )
                    elif o == 2 and w == 0:
                        teal.move_to(UP * (2.25 - ((3 * o) / 4)) + LEFT * (s-(3*(w + 1))/4))
                        self.play(Write(teal), run_time=0.25)
                        self.play(
                            Write(
                                Dot(
                                    point = UP * (2.25 - ((3 * o) / 4)) + LEFT * ((s-2)-(3*(w + 1))/4),
                                    radius = r,
                                    fill_opacity = 1,
                                    color = c[l],
                                )
                            ),
                        run_time=0.25
                        )
                    elif o == 3 and w == 0:
                        green.move_to(UP * (2.25 - ((3 * o) / 4)) + LEFT * (s-(3*(w + 1))/4))
                        self.play(Write(green), run_time=0.25)
                        self.play(
                            Write(
                                Dot(
                                    point = UP * (2.25 - ((3 * o) / 4)) + LEFT * ((s-2)-(3*(w + 1))/4),
                                    radius = r,
                                    fill_opacity = 1,
                                    color = c[l],
                                )
                            ),
                        run_time=0.25
                        )
                    elif o == 4 and w == 0:
                        yellow.move_to(UP * (2.25 - ((3 * o) / 4)) + LEFT * (s-(3*(w + 1))/4))
                        self.play(Write(yellow), run_time=0.25)
                        self.play(
                            Write(
                                Dot(
                                    point = UP * (2.25 - ((3 * o) / 4)) + LEFT * ((s-2)-(3*(w + 1))/4),
                                    radius = r,
                                    fill_opacity = 1,
                                    color = c[l],
                                )
                            ),
                        run_time=0.25
                        )
                    elif o == 5 and w == 0:
                        gold.move_to(UP * (2.25 - ((3 * o) / 4)) + LEFT * (s-(3*(w + 1))/4))
                        self.play(Write(gold), run_time=0.25)
                        self.play(
                            Write(
                                Dot(
                                    point = UP * (2.25 - ((3 * o) / 4)) + LEFT * ((s-2)-(3*(w + 1))/4),
                                    radius = r,
                                    fill_opacity = 1,
                                    color = c[l],
                                )
                            ),
                        run_time=0.25
                        )
                    elif o == 6 and w == 0:
                        red.move_to(UP * (2.25 - ((3 * o) / 4)) + LEFT * (s-(3*(w + 1))/4))
                        self.play(Write(red), run_time=0.25)
                        self.play(
                            Write(
                                Dot(
                                    point = UP * (2.25 - ((3 * o) / 4)) + LEFT * ((s-2)-(3*(w + 1))/4),
                                    radius = r,
                                    fill_opacity = 1,
                                    color = c[l],
                                )
                            ),
                        run_time=0.25
                        )
                    elif o == 7 and w == 0:
                        maroon.move_to(UP * (2.25 - ((3 * o) / 4)) + LEFT * (s-(3*(w + 1))/4))
                        self.play(Write(maroon), run_time=0.25)
                        self.play(
                            Write(
                                Dot(
                                    point = UP * (2.25 - ((3 * o) / 4)) + LEFT * ((s-2)-(3*(w + 1))/4),
                                    radius = r,
                                    fill_opacity = 1,
                                    color = c[l],
                                )
                            ),
                        run_time=0.25
                        )
                    else:
                        self.play(
                            Write(
                                Dot(
                                    point = UP * (2.25 - ((3 * o) / 4)) + LEFT * ((s-2)-(3*(w + 1))/4),
                                    radius = r,
                                    fill_opacity = 1,
                                    color = c[l],
                                )
                            ),
                        run_time=0.25
                        )

                elif w == 0 and o == 8:
                    self.play(Write(misc))
                    self.play(
                        Write(
                            Dot(
                                point = UP * (5 - ((3 * o) / 4)) + RIGHT * (((s-4.5)+(3*(w + 1))/4)),
                                radius = r,
                                fill_opacity = 1,
                                color = c[l],
                            )
                        ),
                    run_time=0.25
                    )
                else:
                    self.play(
                        Write(
                            Dot(
                                point = UP * (5 - ((3 * o) / 4)) + RIGHT * (((s-4.5)+(3*(w + 1))/4)),
                                radius = r,
                                fill_opacity = 1,
                                color = c[l],
                            )
                        ),
                    run_time=0.25
                    )
                l = l + 1