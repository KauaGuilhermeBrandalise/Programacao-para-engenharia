salariohoras = float(input('Quanto voce ganha por horas? '))
numeromes = float(input('Numero de horas trabalhadas no mes: '))
impostorenda = 0.11
inss = 0.08
sindicato = 0.05


salariobruto = (salariohoras * numeromes)
valorinss = salariobruto * inss
valorsindicato = salariobruto * sindicato
ir = (salariobruto - inss - valorsindicato) * impostorenda
salarioliquido = salariobruto - valorinss - valorsindicato - ir
print('Salário Bruto R$',salariobruto)
print('Imposto de renda (11%) R$ ',ir)
print('INSS (8%) R$ ',valorinss)
print('Sindicato (5%) R$ ',valorsindicato)
print('Salário líquido R$ ',salarioliquido)