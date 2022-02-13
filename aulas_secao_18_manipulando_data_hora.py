"""
Usando Datetime

"""

import datetime

#print(datetime.MAXYEAR)
#print(datetime.MINYEAR)

#print(datetime.datetime.now()) #Retorna data e hora corrente

# .replace() modifica o horário

def date_aniv(aniversario):
    aniversario = (aniversario.split('/'))
    date_aniversario = datetime.datetime(year=datetime.datetime.now().year, month=int(aniversario[0]), day=int(aniversario[1]))
    return date_aniversario

def send_email(aniversario = input(f'Digite por favor a data do seu aniversário (mm/dd)')):
    start = datetime.datetime.now()
    date_aniversario = date_aniv(aniversario)
    print(date_aniversario)
    if start.month > date_aniversario.month:
        date_aniversario.year = start.year++ 1
    if start.day >= date_aniversario.day and start.month == date_aniversario.month:
        date_aniversario.year = start.replace(year = start.year++ 1)

    delta_time = date_aniversario - start

    return print(f' O Email será enviado na data: {delta_time}')


send_email()


