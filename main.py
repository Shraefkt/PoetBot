import json
import os
import poemgenerator as pg
import imagegenerator as ig
import poster
if __name__ == '__main__':
    with open("poetrydata/poemstructures.json") as poemstructuresfile:
        poem_structures = json.load(poemstructuresfile)

    with open("poetrydata/structuretypes.json") as structuretypesfile:
        structure_types = json.load(structuretypesfile)

    poem_structure = pg.generate_poem_structure(poem_structures, [3,3,2])
    poem = pg.generate_poem(poem_structure, structure_types)

    print("Poem generated:\n")
    print(poem)

    imgname = ig.create_image(poem,"imagedata/background.jpg")
    print("Image generated.")

"""
    poster.clean_up()
    poster.upload_post("imagedata/post.jpg")


    if os.path.exists("imagedata/post.jpg"):
        os.remove("imagedata/post.jpg")

    if os.path.exists("imagedata/post.jpg.REMOVE_ME"):
        os.remove("imagedata/post.jpg.REMOVE_ME")

    print("Done!")
    print("View post at https://www.instagram.com/roastedroses.poetry/")
"""