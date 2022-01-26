from classes.kb import *
from classes.chaining import *
import sys

with open(sys.argv[1]) as f:
    knowledge = f.read().splitlines()

KB = KnowledgeBase()

KB.add_knowledge(knowledge)

Chaining(KB).run()
