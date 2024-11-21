from typing import List, Tuple

class AlgorithmMarkov:
    def __init__(self, word : str, rules, alphabet : List[Tuple] = None):
        self._word =  word 
        self._rules = rules
        self._alphabet = alphabet if alphabet else []

    @property
    def word(self):
        return self._word

    def find_rule(self):
        for l, r, b in self._rules:
            if self.contains(self._word, l):
                return l, r, b
        raise ValueError("Правила не определены")
    
    def apply_rule(self, rule):
        l = rule[0]
        r = rule[1]
        return self._word.replace(l, r, 1)
    
    def apply_alg(self):
        _, _, b = rule = self.find_rule()
        return self.apply_rule(rule), b
    
    def run(self):
        if self.contains(self._word, "@") == False:
            self._word = "@" + self._word +"@"
        elements = []
        flag = False                      
        try:
            while not flag:               
                elements.append(self._word)
                self._word, flag = self.apply_alg() 
            elements.append(self._word)
        except ValueError:               
            pass

        if elements[-1] == "":
            elements[-1] = "0"
        result = ' -> '.join(elements)
        return result
    
    def contains(self, s : str, sub : str):
        return s.find(sub) != -1
    
    def get_num(self):
        if self._word == '':
            return 0
        return int(self._word.replace("@", ""))
    

    
