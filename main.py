from vagas import Texto, Design, Negrito

antes = Texto('O Edificio Garagem possui 137 vagas disponíveis') 
depois = Negrito(Design(antes))

print('Antes: ' + antes.print() + "\n")
print('Depois:\n' + depois.print())