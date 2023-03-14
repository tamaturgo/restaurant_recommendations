from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calcular_similaridade(frase1, frase2):
    # Converter as frases em vetores de frequência de palavras
    vectorizer = CountVectorizer().fit_transform([frase1, frase2])

    # Calcular a similaridade de coseno
    similarity = cosine_similarity(vectorizer)[0][1]

    return similarity


if __name__ == '__main__':
    frase1 = 'Eu gosto de pizza'
    frase2 = 'Eu gosto de pizza e sorvete'
    frase3 = 'Eu gosto de comida japonesa'

    print(f'Frase 1: {frase1}')
    print(f'Frase 2: {frase2}')
    print(f'Frase 3: {frase3}')

    print(
        f'Similaridade entre a frase 1 e a frase 2: {calcular_similaridade(frase1, frase2)}')
    print(
        f'Similaridade entre a frase 1 e a frase 3: {calcular_similaridade(frase1, frase3)}')
    print(
        f'Similaridade entre a frase 2 e a frase 3: {calcular_similaridade(frase2, frase3)}')
