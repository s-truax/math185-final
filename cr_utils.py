def copy_replace_transform(source, target, source_ind, target_ind):
    zipped = zip(source_ind, target_ind)
    out = [ReplacementTransform(source.copy()[i], target[j]) for i, j in zipped]
    return out
