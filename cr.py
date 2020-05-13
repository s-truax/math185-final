from manimlib.imports import *
from cr_utils import *

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
        color_scheme = {'a':RED, 'z_0':BLUE, 'z':GREEN}

        first_eqn = TexMobjectWrapper(["f", ": U^{open} \\to \\mathbf{C}"], color_scheme)
        at_x0 = TexMobjectWrapper(["z_0", "\\in \\mathbf{C}"], color_scheme)
        second_equn = TexMobjectWrapper(["\\exists", "a", "\\in \\mathbf{C}"], color_scheme)

        first_eqn.move_to(UP*2 + LEFT*3)
        at_x0.move_to(UP*2)
        second_equn.move_to(UP*2 + RIGHT*3)

        derivative_eqn = TexMobjectWrapper(["f", "(", "z", ")", "-", "f", "(", "z_0",
                                    ")", "=", "a", "(", "z", "-", "z_0", ")", "+",
                                    "R", "(", "z", ")"], color_scheme)

        self.play(Write(first_eqn))
        self.wait(4)
        self.play(Write(at_x0))
        self.wait(3)
        self.play(Write(second_equn))
        self.wait(2)

        f_replacements = first_eqn.transform_to(derivative_eqn, 'f', 'f')

        x0_replacements = at_x0.transform_to(derivative_eqn, 'z_0', 'z_0')

        replace_a = second_equn.transform_to(derivative_eqn, 'a', 'a')

        replacements = f_replacements + x0_replacements + replace_a
        leftovers = derivative_eqn.write_leftovers()

        self.play(*replacements)
        self.play(*leftovers)
        self.wait()
        der_eqn2 = TexMobject(*["f", "(", "z", ")", "-", "f", "(", "z_0",
                                    ")", "=", "a", "(", "z", "-", "z_0", ")", "+",
                                    "R(z)"])
        brace = Brace(der_eqn2[17], DOWN, buff=SMALL_BUFF)
        b_text = brace.get_text("$\\lim \\limits_{z \\to z_0} \\frac{R(z)}{z-z_0} = 0$")
        self.play(GrowFromCenter(brace), FadeIn(b_text))
        self.wait(2)
        self.play(FadeOut(brace), FadeOut(b_text))

        approx_eqn = TexMobjectWrapper(["f", "(", "z", ")", "-", "f", "(", "z_0",
                                    ")", "\\approx", "a", "(", "z", "-", "z_0", ")",
                                    "+", "f", "(", "z_0", ")"], color_scheme)

        der_to_appox_map = ((0,0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6),
                         (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12),
                         (13, 13), (14, 14), (15, 15), (16, 9), (17, 9),
                         (18, 9), (19, 9), (20, 9))
        der_to_approx = jenky_transform(derivative_eqn, approx_eqn, der_to_appox_map)
        self.play(*der_to_approx)
        self.wait()

        affine_add = TexMobjectWrapper(["f", "(", "z", ")", "+", "f", "(", "z_0",
                                        ")", "\\approx", "a", "(", "z", "-",
                                        "z_0", ")", "+", "f", "(", "z_0", ")"], color_scheme)
        affine_add.move_to(DOWN*0.8)
        affine_add_inds = (4, 5, 6, 7, 8, 16, 17, 18, 19, 20)
        self.play(*[FadeInFrom(affine_add[i]) for i in affine_add_inds])

        affine_eqn = TexMobjectWrapper(["f", "(", "z", ")", "\\approx", "a", "(", "z", "-",
                                        "z_0", ")", "+", "f", "(", "z_0", ")"], color_scheme)

        approx_to_affine_map = ((0, 0), (1, 1), (2, 2), (3, 3), (9, 4),
                                (10, 5), (11, 6), (12, 7), (13, 8), (14, 9),
                                (15, 10))
        approx_drop = (4, 5, 6, 7, 8)
        approx_to_affine = jenky_transform(approx_eqn, affine_eqn, approx_to_affine_map)
        fade_out_approx =  [FadeOut(approx_eqn[i]) for i in approx_drop]

        affine_add_drop = (4, 5, 6, 7, 8)
        affine_add_keep = ((16,11), (17,12), (18,13), (19,14), (20,15))

        add_to_final = jenky_transform(affine_add, affine_eqn, affine_add_keep)

        fade_out_affine_add = [FadeOutAndShift(affine_add[i], UP) for i in affine_add_drop]
        final_transform = approx_to_affine + fade_out_approx + add_to_final + fade_out_affine_add
        self.play(*final_transform)

        self.wait()

        # Some real spaghetti code


class ComplexToReal(Scene):
    color_scheme = {'z':PURPLE, 'x':RED, 'y':BLUE, 'u':ORANGE,
                    'v':GREEN, 'w':YELLOW_D, 'f':YELLOW_D}
    def construct(self):
        complex_eqn = TexMobjectWrapper(tuple('f(z)=w'), self.color_scheme)
        complex_eqn2 = TexMobjectWrapper(tuple('f(x+iy)=u+iv'), self.color_scheme)
        real_eqn = TexMobjectWrapper(tuple('f(x,y)=u(x,y)+iv(x,y)'), self.color_scheme)
        vector_eqn = TexMobjectWrapper(tuple('f(x,y)=(u(x,y),v(x,y))'), self.color_scheme)

        # Positioning
        complex_eqn.move_to(LEFT*2 + UP*1.5)
        complex_eqn2.move_to(RIGHT*2 + UP*1.5)
        real_eqn
        vector_eqn.move_to(DOWN + LEFT*0.09) # make it look aligned

        self.play(Write(complex_eqn))

        self.wait()

        # Time to get fancy
        # Transformation indicies
        first_transform_indicies = ((0, 0), (1, 1), (2, 2), (2, 3), (2, 4),
                                    (3, 5), (4, 6), (5, 7), (5, 8), (5, 9),
                                    (5, 10), (5, 11))
        first_transform = jenky_copy_transform(complex_eqn, complex_eqn2, first_transform_indicies)

        second_transform_indicies = ((0, 0), (1, 1), (2, 2), (3, 3), (4, 14),
                              (5, 4), (6, 5), (7, 6), (8, 7), (9, 13), (10, 14),
                              (11, 15), (1, 8), (1, 16), (5, 12), (5, 20),
                              (2, 9), (2, 17), (4, 11), (4, 19), (9, 10), (9,18))
        second_transform = jenky_copy_transform(complex_eqn2, real_eqn, second_transform_indicies)

        third_transform_indicies = ((6, 6), (7, 8), (8, 9), (9, 10), (10, 11),
                                    (11, 12), (12, 13), (13, 14), (14, 14),
                                    (15, 15), (16, 16), (17, 17), (18, 18),
                                    (19, 19), (20, 20))
        third_transform = jenky_copy_transform(real_eqn, vector_eqn, third_transform_indicies)

        vector_eqn_write_indicies = (7, 21)

        self.play(*first_transform)
        self.wait()
        self.play(*second_transform)
        self.wait()
        self.play(*third_transform)
        self.play(*[Write(vector_eqn[i]) for i in vector_eqn_write_indicies])

        self.wait(3)

        vector_eqn_fade_out = self.fade_out_vector_eqn(vector_eqn,
                                                        third_transform_indicies)
        parens_fade_out = [FadeOut(vector_eqn[i]) for i in vector_eqn_write_indicies]
        other_eqns_fade_out = [FadeOut(complex_eqn), FadeOut(complex_eqn2),
                               FadeOut(real_eqn)]

        fade_out_all = vector_eqn_fade_out + parens_fade_out + other_eqns_fade_out

        self.play(*fade_out_all)

        self.wait()

    def fade_out_vector_eqn(self, mobject, indicies):
        return [FadeOut(mobject[j]) for i, j in indicies]

class RealDerivativeQuestion(Scene):
    def construct(self):
        text1 = TextMobject("When is a function $f: \\mathbf{R}^2 \\to \\mathbf{R}^2$")
        text2 = TextMobject("complex differentiable", "?")

        # Positioning
        text1.move_to(UP)

        # Colors
        text2[0].set_color(RED)

        self.play(Write(text1))
        self.play(Write(text2))
        self.wait()

class RealDerivative(Scene):
    color_scheme = {'z':PURPLE, 'x':RED, 'y':BLUE, 'x_0':RED,
                    'y_0':BLUE, 'w':YELLOW_D, 'f':YELLOW_D, 'a': GREEN,
                    'A': GREEN, 'z_0':ORANGE}

    def construct(self):
        f_domains = TexMobjectWrapper(["f", ":", "\\mathbf{R}^2 \\to \\mathbf{R^2}"], self.color_scheme)
        x0y0 = TexMobjectWrapper(["(", "x_0", ",", "y_0", ")", "\\in \\mathbf{R}^2"], self.color_scheme)
        exists_A = TexMobjectWrapper(["\\exists", "A", "\\in \\text{GL}_2(\\mathbf{R})"], self.color_scheme)
        real_der = TexMobjectWrapper(["f", "(","x",",", "y",")","-","f","(","x_0",",","y_0",")" ,'=', "A","((","x",",", "y",")","-(","x_0",",", "y_0","))", "+","R(","x",",","y",")"], self.color_scheme)
        complex_der = TexMobjectWrapper(["f", "(", 'z', ')', '-', 'f', '(', 'z_0',')=','a','(','z','-','z_0',')','+R(','z',')'], self.color_scheme)
        real_der_copy = TexMobject("f(x, y)-f(x_0,y_0) =", "A((x, y)-(x_0, y_0))", "+", "R(x, y)")
        complex_der_copy = TexMobject("f(z)-f(z_0)=", "a(z-z_0)", "+R(z)")

        # Positioning
        f_domains.move_to(UP*2 + LEFT*4)
        x0y0.move_to(UP*2)
        exists_A.move_to(UP*2 + RIGHT*4)
        complex_der.move_to(DOWN*2)
        complex_der_copy.move_to(DOWN*2)

        # boxes
        real_box = SurroundingRectangle(real_der_copy[1], buff=SMALL_BUFF)
        complex_box = SurroundingRectangle(complex_der_copy[1], buff=SMALL_BUFF)

        # brace
        brace = Brace(real_der_copy[3], DOWN, buff=SMALL_BUFF)
        b_text = brace.get_text("$\\lim \\limits_{|(x,y)| \\to 0} \\frac{R(x,y)}{|(x,y)|} = 0$")

        self.play(Write(f_domains))
        self.play(Write(x0y0))
        self.play(Write(exists_A))

        self.play(Write(real_der))
        self.play(GrowFromCenter(brace), FadeIn(b_text))

        self.play(FadeOut(brace), FadeOut(b_text))
        self.play(Write(complex_der))

        self.play(ShowCreation(complex_box))
        self.play(ShowCreation(real_box))

        self.play(FadeOut(f_domains), FadeOut(x0y0), FadeOut(exists_A),
                  FadeOut(complex_der), FadeOut(real_der), FadeOut(complex_box),
                  FadeOut(real_box))
