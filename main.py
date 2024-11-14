from markov import AlgorithmMarkov


def main():
    successor = [("aL", "La", False),
             ("a0", "0a", False),
             ("a" , "b" , False),
             ("Lb", "b0", False),
             ("0b", "L" , True ),
             ("b" , "L" , True ),
             (""  , "a" , False)]
    algMark = AlgorithmMarkov(word = "L0LL", rules = successor)

    print(algMark.run())

if __name__ == "__main__":
    main()