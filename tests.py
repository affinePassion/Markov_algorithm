import pytest
from markov import AlgorithmMarkov
from rules import Rules

def test_init():
    word = "example"
    rules = [("a", "b", False), ("b", "c", True)]
    alphabet = [("a",), ("b",), ("c",)]
    markov = AlgorithmMarkov(word, rules, alphabet)
    assert markov.word == word
    assert markov._rules == rules
    assert markov._alphabet == alphabet

def test_find_rule():
    word = "example"
    rules = [("ex", "new", False), ("new", "old", True)]
    markov = AlgorithmMarkov(word, rules)
    rule = markov.find_rule()
    assert rule == ("ex", "new", False)

def test_find_notfound():
    word = "example"
    rules = [("not", "found", False)]
    markov = AlgorithmMarkov(word, rules)
    with pytest.raises(ValueError):
        markov.find_rule()

def test_find_rule1():
    word = "@19@"
    rules = Rules().rules_for_digits(1)
    markov = AlgorithmMarkov(word, rules)
    rule = markov.find_rule()
    assert rule == ("9@", "@0", False)

def test_apply_rule1():
    word = "example"
    rules = [("ex", "new", False)]
    markov = AlgorithmMarkov(word, rules)
    new_word = markov.apply_rule(markov.find_rule())
    assert new_word == "newample"

def test_apply_rule():
    word = "@19@"
    rules = Rules().rules_for_digits(1)
    markov = AlgorithmMarkov(word, rules)
    new_word = markov.apply_rule(markov.find_rule())
    assert new_word == "@1@0"

def test_apply_alg():
    word = "19"
    rules = Rules().rules_for_digits(1)
    markov = AlgorithmMarkov(word, rules)
    new_word, flag = markov.apply_alg()
    assert new_word == "20"
    assert flag == False

def test_apply_alg():
    word = "example"
    rules = [("ex", "new", False)]
    markov = AlgorithmMarkov(word, rules)
    new_word, flag = markov.apply_alg()
    assert new_word == "newample"
    assert flag == False

def test_run():
    word = "example"
    rules = [("ex", "new", False), ("new", "", True)]
    markov = AlgorithmMarkov(word, rules)
    result = markov.run()
    assert result == "@example@ -> @newample@ -> @ample@"

def test_run1():
    word = "@19@"
    rules = Rules().rules_for_digits(1)
    markov = AlgorithmMarkov(word, rules)
    result = markov.run()
    assert result == "@19@ -> @1@0 -> @20 -> 20" 

def test_run_notfound():
    word = "example"
    rules = [("not", "found", False)]
    markov = AlgorithmMarkov(word, rules)
    result = markov.run()
    assert result == "@example@"

def test_contains():
    word = "example"
    rules = [("ex", "new", False)]
    markov = AlgorithmMarkov(word, rules)
    assert markov.contains(word, "ex") == True
    assert markov.contains(word, "not") == False

def test_contains1():
    word = "19"
    rules = Rules().rules_for_digits(1)
    markov = AlgorithmMarkov(word, rules)
    assert markov.contains(word, "9") == True
    assert markov.contains(word, "not") == False

def test_get_num():
    word = "19"
    rules = Rules().rules_for_digits(1)
    markov = AlgorithmMarkov(word, rules)
    assert markov.get_num() == 19
    markov.run()
    assert markov.get_num() == 20

def test_increment():
    word = "19"
    rules = Rules().rules_for_digits(1)
    markov = AlgorithmMarkov(word, rules)
    markov.run()
    assert markov.get_num() == 20

def test_decrement():
    word = "19"
    rules = Rules().rules_for_digits(2)
    markov = AlgorithmMarkov(word, rules)
    markov.run()
    assert markov.get_num() == 18