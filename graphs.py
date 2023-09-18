from manim import * 
from mov_functions import MRU_pos

class graphMRU(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0,5,1],
            y_range=[0,20,4],
            y_length=[5.0],
            tips=False,
            axis_config={"include_numbers": True},
            y_axis_config={"unit_size": 5}
        )

        mov_graph = ax.plot(MRU_pos)
        self.play(Create(ax), run_time = 5)
        self.play(Create(mov_graph), run_time = 5)