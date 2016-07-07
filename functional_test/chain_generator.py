from pymarkovchain import MarkovChain

seed_file = open('./fixtures/wikipedia_india_content.txt')
mc = MarkovChain("../markov_db")
seed_text = seed_file.read()
mc.generateDatabase(seed_text)
print mc.generateString()
