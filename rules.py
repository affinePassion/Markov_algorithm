class Rules:
    def __init__(self, listRules):
        self._listRules = [listRules]

    def add_rule(self, newRule):
        self._listRules.append(newRule)

    def remove_rule(self, removedRule):
        self._listRules.remove(removedRule)

    def create_rules(self, numberTask):
        match numberTask:
            case 1:
                self._listRules = [("1@", "2", False),
                                   ("2@,", "3", False)]
            case _:
                raise Exception("Говно вопрос")
                