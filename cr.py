from manimlib.imports import *

class ComplexMultiplication(Scene):
    def construct(self):
        w = TexMobject("w").move_to(LEFT*1.5)
        z = TexMobject("z").move_to(LEFT*2.5)
        zw = TexMobject("z", "w").move_to(LEFT*2)

        z_and_w = VGroup(z, w)

        w_vec = Vector(np.array([0.5, 2, 0]))
        w_vec.set_color(BLUE)

        z_vec = Vector(np.array([1, 1, 0]))
        z_vec.set_color(RED)

        zw_vec = Vector(np.array([-1.5, 2.5]))
        zw_vec.set_color(PURPLE)

        vector_group = VGroup(z_vec, w_vec, zw_vec)
        vector_group.move_to(RIGHT + UP*0.5)

        w.set_color(BLUE)
        z.set_color(RED)
        zw.set_color(PURPLE)

        self.play(Write(w), ShowCreation(w_vec))
        self.wait()
        self.play(Write(z), ShowCreation(z_vec))

        self.wait()

        animations = [Transform(z_and_w, zw),
                     Transform(vector_group.copy()[0], vector_group[2]),
                     Transform(vector_group.copy()[1], vector_group[2])]

        self.play(*animations)
        self.wait()


class OneQuestion(Scene):
    def construct(self):
        text = TextMobject("Question:")
        self.add(text)
        self.wait()

class MultiplicationQuestion(Scene):
    def construct(self):
        question = TextMobject("What happens when we multiply the square by")
        self.add(question)
        complex_num = TexMobject("3+3i \\, \\, ?")
        self.play(Write(complex_num))
        self.wait()

class ComplexDerivative(Scene):
    def construct(self):
        first_eqn = TexMobject("f", ": U \\to \\mathbf{C}")
        at_x0 = TexMobject("x_0", "\\in \\mathbf{C}")
        second_equn = TexMobject("\\exists", "a", "\\in \\mathbf{C}")

        first_eqn.move_to(UP*2 + LEFT*3)
        at_x0.move_to(UP*2)
        second_equn.move_to(UP*2 + RIGHT*3)

        derivative_eqn = TexMobject("f", "(x) - ", "f", "(", "x_0", ")", "=",
                                     "a", "(x -", "x_0", ")")

        self.play(Write(first_eqn))
        self.wait(2)
        self.play(Write(at_x0))
        self.wait()
        self.play(Write(second_equn))

        self.play(FadeInFrom(derivative_eqn, UP))
