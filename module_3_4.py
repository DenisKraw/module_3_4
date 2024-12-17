def  single_root_words( root_word, *other_words):
    same_words = []
    o_w = list(other_words)
    for i in other_words:
        if root_word.lower() in i.lower() or i.lower() in root_word.lower():
            same_words.append(i)
    return (same_words)

r1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')

r2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(r1)
print(r2)