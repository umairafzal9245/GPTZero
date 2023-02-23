from model import GPT2PPL


def test_inference():
    # initialize the model
    model = GPT2PPL()

    sentence = '''Takes in a sentence split by full stop and print the perplexity of the total sentence
                split the lines based on full stop and find the perplexity of each sentence and print
                average perplexity Burstiness is the max perplexity of each sentence'''

    result, out = model(sentence)
    print('test')
    assert out == "The Text is written by Human."


def test_inference2():

    model = GPT2PPL()

    sentence = '''As the weary traveler reached the summit of the mountain, the breathtaking view of the sprawling valley below and the cool, refreshing breeze that caressed his face made all the arduous steps and treacherous obstacles of the journey worth it.'''

    result, out = model(sentence)
    print('Test')
    assert out == "The Text is generated by AI."


def test_inference3():

    model = GPT2PPL()

    sentence = '''As the sun rised the dangling daffodils were seen in the garden. That beautiful scene was one of the 
    best I have ever seen in my life. My attachment with the nature is a never-ending love. Being close to nature makes me feel fresh and energetic. I would like to advise each and every one of you to spare a little time from your busy routine and spend in nature, you won't regret it. '''

    result, out = model(sentence)
    print('Test')
    assert out == "The Text is generated by AI."
