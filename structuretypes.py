import os
from pattern.text.en import pluralize
import json
"""
def singulars_to_plurals():
   path = os.path.join(os.getcwd(), "poetrydata")
   for filename in os.listdir(path):

      if filename == "poemstructures.json" or "pronoun" in filename or "singular" not in filename:
         continue

      with open(os.path.join(path, filename), 'r') as f:
         f = f.read()
         singulars = f.split("\n")
         plurals = [pluralize(singular) for singular in singulars]

         new_filename = filename.split("_")
         try:
            new_filename.remove("singular")
         except:
            pass
         new_filename.append("plural")
         new_filename = "_".join(new_filename)
         try:
            f = open(f"poetrydata/{new_filename}", "x")
         except:
            f = open(f"poetrydata/{new_filename}", "w")
         f.write("\n".join(plurals))

"""
def create_structuretypesjson():

   path = os.path.join(os.getcwd(),"poetrydata")
   structuretypes = {}
   for filename in os.listdir(path):

      if filename == "poemstructures.json" or filename == "structuretypes.json":
         continue

      with open(os.path.join(path, filename), 'r') as f:
         f = f.read()
         f = f.split("\n")
         structuretypes[filename] = f

   with open("poetrydata/structuretypes.json", "w") as f:
      structuretypes = json.dumps(structuretypes)
      f.write(structuretypes)


if __name__ == '__main__':
    create_structuretypesjson()