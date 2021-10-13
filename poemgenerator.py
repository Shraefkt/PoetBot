import re
import random
import json


with open("poetrydata/poemstructures.json") as poemstructuresfile:
    poem_structures = json.load(poemstructuresfile)

with open("poetrydata/structuretypes.json") as structuretypesfile:
    structure_types = json.load(structuretypesfile)

def generate_poem_structure(poem_structures_f,type_f):
                                            # [2,3,3]
    poem_structure_f = []
    poem_structure_f.append("title \n\n")
    for stanza in type_f:
        for i in range(int(stanza)):
            new_line = random.SystemRandom().choice(poem_structures_f)
            while new_line in poem_structure_f:
                new_line = random.SystemRandom().choice(poem_structures_f)
            poem_structure_f.append(new_line)
            poem_structure_f.append("\n")
        poem_structure_f.append("\n")

    poem_structure_f = " ".join(poem_structure_f)
    return poem_structure_f


def generate_poem(poem_structure_f,structure_types_f):
    poem_structure_f = re.split(" ",poem_structure_f)
    for i in range(len(poem_structure_f)):
        if poem_structure_f[i] in structure_types_f:
            poem_structure_f[i] = random.SystemRandom().choice(structure_types_f[poem_structure_f[i]])
    poem = " ".join(poem_structure_f)
    return poem


