# USE THE FEBRUARY 2019 VERSION OF MANIM TO RUN THESE SCENES

from big_ol_pile_of_manim_imports import *

class SimilarityMatrix(Scene):

    def construct(self):
        m = TexMobject("""\\begin{pmatrix} \\alpha & -\\beta \\\\
        \\beta & \\alpha \\end{pmatrix} """)
        text1 = TextMobject("What is the form of a 2x2 matrix")
        text2 = TextMobject("that has the geometric effect of dialation and rotation?")

        text1.move_to(UP*2)
        text2.move_to(UP)
        m.move_to(DOWN)

        # Set colors
        m[1].set_color(ORANGE)
        m[5].set_color(ORANGE)
        m[4].set_color(GREEN)
        m[3].set_color(GREEN)

        self.play(Write(text1))
        self.play(Write(text2))

        self.wait()

        self.play(Write(m))
