import random


class Chaining:

    def __init__(self, KB):
        self.KB = KB

    def run(self):


        for subject_set in self.KB.facts:
            results = []
            for rule in self.KB.backup:
                if self.forward(subject_set, rule.CONCLUSION) and rule.CONCLUSION not in results:
                    results.append(rule.CONCLUSION)
                elif self.backward(subject_set,rule.CONCLUSION) and rule.CONCLUSION not in results:
                    results.append(rule.CONCLUSION)
            print(f"Resultados: {subject_set.subject} {results}")

    def forward(self, subject_set, goal):
        facts = subject_set.fact_set

        if facts[list(goal.keys())[0]] == goal:
            return True

        new_facts = []

        return self.FC_newcycle(self.KB.rules, subject_set, new_facts, goal)

    def FC_newcycle(self, rules, facts, new_facts, goal):

        if not len(rules):
            if not len(new_facts):
                self.KB.restore_rulebase()
                return False

            self.KB.add_fact_by_dict(facts, new_facts)
            new_facts = []

            return self.FC_newcycle(self.KB.rules, facts, new_facts, goal)

        random_rule = random.choice(rules)
        rules = [x for x in rules if x != random_rule]

        intersec = dict(random_rule.PREMISE.items() & facts.fact_set.items())

        if random_rule.PREMISE == intersec:
            if random_rule.CONCLUSION == goal:
                return True

            new_facts.append(random_rule.CONCLUSION)
            self.KB.rules.remove(random_rule)

        return self.FC_newcycle(rules, facts, new_facts, goal)

    def backward(self, facts, goal):

        if goal.items() & facts.fact_set.items():
            return True

        return self.BC_stablish1(facts, self.KB.rules, goal)

    def BC_stablish1(self, facts, rules, goal):
        if not len(rules):
            return False

        random_rule = random.choice(rules)
        rules = [x for x in rules if x != random_rule]

        if random_rule.CONCLUSION == goal:
            if self.BC_stabilish2(facts, random_rule):
                return True

        return self.BC_stablish1(facts, rules, goal)

    def BC_stabilish2(self, facts, rule):
        objectives = rule.PREMISE

        return self.factconj(facts, objectives)

    def factconj(self, facts, objectives):
        if not len(objectives):
            return True

        key, value = random.choice(list(objectives.items()))
        objectives = {k: v for k, v in objectives.items() if k != key}

        if not self.backward(facts, {key: value}):
            self.ask_something(facts, key)
            return False

        return self.factconj(facts, objectives)

    def ask_something(self, facts, key):

            if facts.fact_set[key] is None:
                answer = input(f"{facts.subject} TEM REGISTRO DE {key}?\n").upper()
                facts.fact_set[key] = answer
