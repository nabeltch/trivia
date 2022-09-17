#author:nabeltch@gmail.com
#name:Nabel Torres

import random
import time
#importa los datos de la trivia
import data_trivia

puntaje = random.randint(0, 10)

RED = '\033[31m'
GREEN = '\033[32m'

BLUE = '\033[34m'

RESET = '\033[39m'

score = random.randint(0, 10)
intents = 0
name = ''


#funcion que hace las preguntas
def get_question(question):
    global intents
    intents += 1
    data = data_trivia
    print('\nPregunta', question, ' de ', len(data.trivia), 'preguntas\n')
    print(data.trivia['question ' + str(question)]['question'], '\n')
    [
        print(i, ')', v)
        for i, v in data.trivia['question ' +
                                str(question)]['options'].items()
    ]
    response = input('\ningrese su respuesta:\n').lower()
    response_question(response, data, question)


#funcion que resuelve las preguntas
def response_question(response, data, question):
    while response not in ('a', 'b', 'c', 'd'):
        response = input(
            'ingrese nuevamente, la opcion ingresada no se encuentra en la pregunta: '
        ).lower()

    global score
    trivia = data.trivia['question ' + str(question)]
    if response == trivia['response']:
        score = score * int(trivia['score'][response][1])
        print('\n', GREEN + trivia['items_feeback'][response] + RESET, '\n')
        continue_question(question)
    else:
        if trivia['score'][response][0] == '+':
            score = score + int(trivia['score'][response][1])
        elif trivia['score'][response][0] == '-':
            score = score - int(trivia['score'][response][1])
        else:
            score = score / int(trivia['score'][response][1])

        print('\n', RED + trivia['items_feeback'][response], RESET, '\n')
        continue_question(question)


#funcion que resuelve la contuinidad
def continue_question(question):

    if intents < len(data_trivia.trivia):
        response_continue = input(
            'Deseas continuar ? response con (s/S) para continuar: para salir presiona cualquier tecla: \n'
        ).lower()
        if response_continue == 's':
            print('\nMuy bien ', name, ' sigamos..')
            time.sleep(2)
            get_question(question + 1)
        else:
            print('\nNo hay problema ', name, ' que te vaya bien\n')
            get_response()
    else:
        get_response()


#funcion del resultado final
def get_response():
    print(BLUE + 'Muy bien ', name, ' haz terminado' + RESET)
    print(BLUE + 'tienes ', score, ' puntos ganados' + RESET)


#comienza la ejecución del programa
name = input('Hola Bienvenido, ¿Cuál es tu nombre?:').upper()
#inicialiaza la trivia
get_question(1)
