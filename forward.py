from classes.kb import *
from classes.chaining import *
import sys

with open(sys.argv[1]) as f:
    knowledge = f.read().splitlines()

KB = KnowledgeBase()

KB.add_knowledge(knowledge)
strr = input("Insira o objetivo(exemplo: R=SIM): ")
splitted = strr.split("=")
meta = {splitted[0]:splitted[1]}

print(f"{strr} é {Chaining(KB).forward(KB.facts[0], meta)}")