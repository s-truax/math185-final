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
        question = TextMobject("Question:")
        self.add(question)
        self.wait()

class MultiplicationQuestion(Scene):
    def construct(self):
        text = TextMobject("What happens when we multiply the square by")
        text.move_to(UP)
        two_plus_2i = TexMobject("3+3i \\, \\, \\text{?}")
        question_mark = TextMobject("?").move_to(DOWN)
        self.add(text)
        self.wait()
        self.play(Write(two_plus_2i))
        self.wait()
