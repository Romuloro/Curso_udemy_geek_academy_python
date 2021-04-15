"""
Criando nossa própria versão de loop


"""

def my_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


my_for('Romulo Rodrigues')
