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

class TotalDerivative(Scene):
    color_scheme = {}
    def construct(self):
        matrix_A = TexMobject("A", "\\in \\text{GL}_2 ( \\mathbf{R} )")
        f_def = TexMobject("f(x, y) = (u(x,y), v(x,y))")
        der = TexMobject("""\\begin{pmatrix} u_x & u_y \\\\ v_x & v_y \\end{pmatrix}""")
        a_alone = TexMobject('A', '=')

        # Here we go, set the colors
        matrix_A[0].set_color(PURPLE)
        a_alone[0].set_color(PURPLE)

        f_def[2].set_color(RED) # x
        f_def[10].set_color(RED)
        f_def[17].set_color(RED)
        f_def[4].set_color(BLUE) # y
        f_def[12].set_color(BLUE)
        f_def[19].set_color(BLUE)
        f_def[8].set_color(ORANGE) # u
        f_def[15].set_color(GREEN) # v

        der[1].set_color(ORANGE) # u
        der[3].set_color(ORANGE)
        der[2].set_color(RED) # x
        der[6].set_color(RED)
        der[4].set_color(BLUE) # y
        der[8].set_color(BLUE)
        der[5].set_color(GREEN) # v
        der[7].set_color(GREEN)

        matrix_A.move_to(UP + LEFT * 3.5)
        f_def.move_to(UP + RIGHT * 2)
        a_alone.move_to(LEFT*2 + DOWN)
        der.move_to(DOWN)

        self.play(Write(matrix_A))

        self.wait()

        self.play(Write(f_def))

        self.wait()

        self.play(Write(der), Write(a_alone))

class Finale(Scene):
    def construct(self):
        f_def = TexMobject("f(x, y) = (u(x,y), v(x,y))")
        der = TexMobject("""\\begin{pmatrix} u_x & u_y \\\\ v_x & v_y \\end{pmatrix}""")
        # complex_diff = TextMobject("$f$ complex differentiable")
        iff1 = TexMobject("\\Leftrightarrow")
        eq_sign = TexMobject("=")
        cr = TexMobject("u", "_x", '=', 'v', '_y', "\\, \\, \\text{and} \\, \\,", "u", '_y', '=', '-', 'v', '_x')
        sim_matrix = TexMobject("""\\begin{pmatrix} \\alpha & -\\beta \\\\
        \\beta & \\alpha \\end{pmatrix} """)
        f_complex = TexMobject("""f(x+iy) = u(x, y) + iv(x,y)""")


        # Set colors
        f_def[2].set_color(RED) # x
        f_def[10].set_color(RED)
        f_def[17].set_color(RED)
        f_def[4].set_color(BLUE) # y
        f_def[12].set_color(BLUE)
        f_def[19].set_color(BLUE)
        f_def[8].set_color(ORANGE) # u
        f_def[15].set_color(GREEN) # v

        f_complex[2].set_color(RED) # x
        f_complex[10].set_color(RED)
        f_complex[18].set_color(RED)
        f_complex[5].set_color(BLUE) # y
        f_complex[12].set_color(BLUE)
        f_complex[20].set_color(BLUE)
        f_complex[8].set_color(ORANGE) # u
        f_complex[16].set_color(GREEN) # v

        der[1].set_color(ORANGE) # u
        der[3].set_color(ORANGE)
        der[2].set_color(RED) # x
        der[6].set_color(RED)
        der[4].set_color(BLUE) # y
        der[8].set_color(BLUE)
        der[5].set_color(GREEN) # v
        der[7].set_color(GREEN)

        cr[0].set_color(ORANGE) # u
        cr[6].set_color(ORANGE)
        cr[1].set_color(RED) # x
        cr[11].set_color(RED)
        cr[3].set_color(GREEN) # v
        cr[10].set_color(GREEN)
        cr[4].set_color(BLUE) # y
        cr[7].set_color(BLUE)

        sim_matrix[1].set_color(ORANGE)
        sim_matrix[5].set_color(ORANGE)
        sim_matrix[4].set_color(GREEN)
        sim_matrix[3].set_color(GREEN)

        f_def.move_to(UP*3)
        der.move_to(LEFT*5)
        sim_matrix.move_to(LEFT*2)
        cr.move_to(RIGHT*3)
        eq_sign.move_to(LEFT*3.5)
        iff1.move_to(LEFT*0.2)
        f_complex.move_to(UP*2 + LEFT*0.18)

        # Brace
        brace = Brace(der, UP, buff=SMALL_BUFF)
        b_text = brace.get_text("Real derivative of $f$").scale(0.7)

        brace2 = Brace(sim_matrix, DOWN, buff=SMALL_BUFF)
        b2_text = brace2.get_text("Form of a rotation and dilation matrix").scale(0.7)

        self.play(Write(f_def))
        self.play(*[FadeInFrom(f_complex[i], DOWN) for i in range(7, 22)])

        self.play(Write(der))
        self.play(GrowFromCenter(brace), FadeIn(b_text) )
        self.play(GrowFromCenter(eq_sign))
        self.play(Write(sim_matrix))
        self.play(GrowFromCenter(brace2), FadeIn(b2_text))

        self.wait()

        self.play(GrowFromCenter(iff1))

        self.wait()

        self.play(Write(cr))
