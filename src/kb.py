from classes.rule import *
from classes.fact import *


class KnowledgeBase:

    def __init__(self):
        self.rules = []
        self.facts = []
        self.backup = []

    def add_rule(self, new_rule):

        premise = {}
        conclusion = None

        for i in range(len(new_rule)):

            if new_rule[i] == "THEN":
                splitted = new_rule[i + 1].split("=")
                conclusion = {splitted[0]: splitted[1]}
                break

            splitted = new_rule[i].split("=")

            premise[splitted[0]] = splitted[1]

        self.rules.append(Rule(premise, conclusion))

        self.backup = self.rules.copy()

    def add_facts_by_text(self, new_facts):

        current_fact_set = None

        if "HAS" in new_facts:
            current_subject = new_facts[0]

            for i in self.facts:
                if i.subject == current_subject:
                    current_fact_set = i.fact_set
                    break

            if not current_fact_set:
                self.facts.append(Facts(current_subject))
                current_fact_set = self.facts[-1].fact_set

            for i in range(2, len(new_facts)):
                splitted = new_facts[i].split("=")
                current_fact_set[splitted[0]] = splitted[1]

        else:
            self.facts.append(Facts(""))
            current_fact_set = self.facts[0].fact_set

            for i in range(len(new_facts)):
                splitted = new_facts[i].split("=")
                current_fact_set[splitted[0]] = splitted[1]

    def add_fact_by_dict(self, subject, new_facts):
        for i in new_facts:
            subject.fact_set[list(i.keys())[0]] = i.get(list(i.keys())[0])

    def add_knowledge(self, file):

        for line in file:
            splitted = line.split(" ")

            if splitted[0] == "RULE":
                self.add_rule(splitted[1:])

            elif splitted[0] == "FACTS":
                self.add_facts_by_text(splitted[1:])

            for rule in self.rules:
                for premise_element in [k for (k, v) in list(rule.PREMISE.items())]:
                    for fact_subject in self.facts:
                        facts_index = [k for (k, v) in list(fact_subject.fact_set.items())]
                        if premise_element not in facts_index:
                            fact_subject.fact_set[premise_element] = None

                        facts_index = [k for (k, v) in list(fact_subject.fact_set.items())]
                        conclusion = [k for (k, v) in list(rule.CONCLUSION.items())][0]

                        if conclusion not in facts_index:
                            fact_subject.fact_set[conclusion] = None

    def print_rules(self):
        for rule in self.rules:
            print(f"IF {rule.PREMISE} THEN {rule.CONCLUSION}")

    def print_facts(self):
        for fact in self.facts:
            print(fact.subject, fact.fact_set)

    def restore_rulebase(self):
        self.rules = self.backup.copy()
