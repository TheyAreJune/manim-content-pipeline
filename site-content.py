from manim import *
import math

class OpeningManim(Scene):
    def construct(self):
        grid = NumberPlane()

        self.add(grid)
        self.play(
            ShowCreation(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.animate.apply_function(
                lambda p: p
                          + np.array(
                    [
                        np.sin(p[1]) * 0.5,
                        np.sin(p[0]) * 0.5,
                        0,
                    ]
                )
            ),
            run_time=3,
        )
        self.wait()
