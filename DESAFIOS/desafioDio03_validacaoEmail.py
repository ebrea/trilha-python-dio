# Entrada do usuário
email = input().strip()       # email = 'user@outlook.com'

c = list()              # c = lista de caracteres do email
for i in email:
    c += i

n = len(c)
if c[0] == '@' or c[n-1] == '@' or '@' not in email or ' ' in email:
    print('E-mail inválido')

elif 'gmail.com' not in email and 'outlook.com' not in email:
    print('E-mail inválido')

else:
    print('E-mail válido')