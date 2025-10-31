class QuestionError(Exception):
    pass

def ask_user(question):
    if question == '':
        raise QuestionError
    answer = int(input(question))
    return answer

try:
    age = ask_user('Ikäsi? ')
except ValueError:
    print('Virheellinen ikä')
except QuestionError:
    print('Question is empty')
except:
    print('Undefined error')
else:
    print(f'Olet {age} vuotta vanha')

