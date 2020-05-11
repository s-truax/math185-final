from manimlib.imports import *

class ComplexMultiplication(Scene):
    def construct(self):
        w = TexMobject("w").move_to(LEFT*3)
        zw = TexMobject("z", "w").move_to(LEFT*3)
        w_vec = Arrow(ORIGIN, UR*2).move_to(RIGHT*3)
        z_vec = Arrow(ORIGIN, UP*2).move_to(RIGHT*3)

        self.play(Write(w), ShowCreation(w_vec))
        self.wait()
        self.play(Transform(w, zw), ShowCreation(z_vec))

class ComplexMultiplicationTest(Scene):
    def construct(self):
        w = TexMobject("w").move_to(LEFT*3)
        zw = TexMobject("z", "w").move_to(LEFT*3)

        # transforms = [ReplacementTransform(w[0], zw[0]),
                      # ReplacementTransform(w[1], zw[1])]

        self.play(Write(w))
        self.wait()
        self.play(ReplacementTransform(w, zw[1]))
        self.play(Write(zw[0]))
