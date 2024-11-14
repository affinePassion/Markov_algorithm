from typing import List, Tuple

class Rules:
    def __init__(self, listRules: List[Tuple] = None):
        self._listRules = listRules if listRules else []

    def add_rule(self, newRule: Tuple):
        self._listRules.append(newRule)

    def remove_rule(self, removedRule: Tuple):
        self._listRules.remove(removedRule)

    def rules_for_digits(self, numberTask: int) -> List[Tuple]:
        match numberTask:
            case 1:
                return [
                    ("0@", "1", False),
                    ("1@", "2", False),
                    ("2@", "3", False),
                    ("3@", "4", False),
                    ("4@", "5", False),
                    ("5@", "6", False),
                    ("6@", "7", False),
                    ("7@", "8", False),
                    ("8@", "9", False),
                    ("9@", "@0", False),
                    ("@@", "1", False),
                    ("@", "", True)
                ]
            case 2:
                return [
                    ("9@", "8", False),
                    ("8@", "7", False),
                    ("7@", "6", False),
                    ("6@", "5", False),
                    ("5@", "4", False),
                    ("4@", "3", False),
                    ("3@", "2", False),
                    ("2@", "1", False),
                    ("1@", "0", False),
                    ("0@", "@9", False),
                    ("@0", "", False),
                    ("@", "", True),
                ]
            case _:
                raise Exception()
                