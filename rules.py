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
                                   ("2@,", "3", False),
                                   ("3@,", "4", False),
                                   ("4@,", "5", False),
                                   ("5@,", "6", False),
                                   ("6@,", "7", False),
                                   ("7@,", "8", False),
                                   ("8@,", "9", False),
                                   ("9@,", "@0", False),
                                   ("@@", "1", False),
                                   ("@,", "", True),]
            case _:
                raise Exception("Говно вопрос")
                