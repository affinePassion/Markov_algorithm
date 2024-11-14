
class AlgorithmMarkov:
    def __init__(self, word : str, rules):
        self._word = word
        self._rules = rules

    def contains(self, s : str, sub : str):
        return s.find(sub) != -1

    def find_rule(self):
        for l, r, b in self._rules:
            if self.contains(self._word, l):
                return l, r, b
        raise ValueError("not found")
    
    def apply_rule(self, rule):
        l = rule[0]
        r = rule[1]
        return self._word.replace(l, r, 1)
    
    def apply_alg(self):
        _, _, b = rule = self.find_rule()
        return self.apply_rule(rule), b
    
    def run(self):
        result = []
        flag = False                      # whether Halting rule was applied
        try:
            while not flag:               # Normal rule was applied
                result.append(self._word)
                self._word, flag = self.apply_alg() # apply a rule
            result.append(self._word)
        except ValueError:                # No rule was applied
            pass
        return result
    
