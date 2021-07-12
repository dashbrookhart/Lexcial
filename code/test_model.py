import gensim.downloader as api
from scipy import spatial

from similarity_model.lexical_similarity import spacy_similaity

# can import other functions from lexical_similarity once implemented


def test_equal():
    """
    Tests if they are the same answer
    """
    CORRECT_ANSWER = "In statistics, linear regression is a linear approach to\
    modelling the relationship between a scalar response and one or more \
    explanatory variables (also known as dependent and independent variables).\
    The case of one explanatory variable is called simple linear regression; \
    for more than one, the process is called multiple linear regression."
    assert (spacy_similaity(CORRECT_ANSWER, CORRECT_ANSWER) == 1)


def test_close():
    """
    Tests if two texts are close
    """
    input1 = "cat"
    input2 = "the cat"
    assert(round(spacy_similaity(input1, input2), 3) == 0.567)
