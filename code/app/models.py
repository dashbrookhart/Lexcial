from sentence_transformers import SentenceTransformer, util
from Levenshtein import distance



def basic_similarity(STUDENT_ANSWER, CORRECT_ANSWER):
    return STUDENT_ANSWER.strip().lower() == CORRECT_ANSWER.strip().lower()


def machine_learning_similarity(STUDENT_ANSWER, CORRECT_ANSWER):
    pass


def other_similarity_fuction(STUDENT_ANSWER, CORRECT_ANSWER):
    pass


def BERT_similarity(STUDENT_ANSWER, CORRECT_ANSWER):
    model = SentenceTransformer('paraphrase-distilroberta-base-v1')
    student_emb = model.encode(STUDENT_ANSWER)
    correct_emb = model.encode(CORRECT_ANSWER)
    similarity = util.pytorch_cos_sim(correct_emb, student_emb)
    return similarity.numpy()[0][0]

def levenshtein_distance(STUDENT_ANSWER, CORRECT_ANSWER):
	return 1 - distance(STUDENT_ANSWER, CORRECT_ANSWER) / max(len(STUDENT_ANSWER), len(CORRECT_ANSWER))
