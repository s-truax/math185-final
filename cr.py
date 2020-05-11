from manimlib.imports import *

class ComplexMultiplication(Scene):
    def construct(self):
        w = TexMobject("w").move_to(LEFT*2.5)
        z = TexMobject("z").move_to(LEFT*3.5)
        zw = TexMobject("z", "w").move_to(LEFT*3)

        w_vec = Arrow(np.array([1, -1, 0]), np.array([2, 1, 0]))
        w_vec.set_color(BLUE)

        z_vec = Arrow(np.array([1, -1, 0]), np.array([3, 1, 0]))
        z_vec.set_color(RED)

        zw_vec = Arrow(np.array([1, -1, 0]), np.array([-2, 4, 0]))
        zw_vec.set_color(PURPLE)

        w.set_color(BLUE)
        z.set_color(RED)
        zw.set_color(PURPLE)

        self.play(Write(w), ShowCreation(w_vec))
        self.wait()
        self.play(Write(z), ShowCreation(z_vec))

        self.wait()

        z_and_w = VGroup(z, w)
        z_and_w_vec = VGroup(z_vec, w_vec)

        animations = [Transform(z_and_w, zw),
                     Transform(z_and_w_vec.copy()[0], zw_vec, run_time=2),
                     Transform(z_and_w_vec.copy()[1], zw_vec, run_time=2)]

        self.play(*animations)
