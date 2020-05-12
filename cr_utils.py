from manimlib.imports import *

# Behold the spaghetti code

def copy_replace_transform(source, target, source_ind, target_ind):
    zipped = zip(source_ind, target_ind)
    out = [ReplacementTransform(source.copy()[i], target[j]) for i, j in zipped]
    return out

class TexMobjectWrapper(TexMobject):

    def __init__(self, text_list, color_scheme):
        super().__init__(*text_list)
        self.text_list = text_list
        self.color_scheme = color_scheme
        self.used_inds = []

        for ind, char in enumerate(text_list):
            if char in color_scheme:
                self[ind].set_color(color_scheme[char])

    def get_char_indicies(self):
        return list(enumerate(self.text_list))

    def transform_to(self, other, source_char, *target_chars):
        source_char_index = self.text_list.index(source_char)

        transforms = []

        for i, char in enumerate(other.text_list):
            if char in target_chars:
                t = ReplacementTransform(self.copy()[source_char_index], other[i])
                transforms.append(t)
                other.used_inds.append(i)

        return transforms

    def write_leftovers(self, rt=1):
        num_chars = len(self.text_list)
        return [Write(self[i], rum_time=rt)
                for i in range(num_chars) if i not in self.used_inds]
