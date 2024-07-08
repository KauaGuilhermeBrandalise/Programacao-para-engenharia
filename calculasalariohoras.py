shoras = float(input('Quanto voce ganha por hora? R$'))
smes = float(input('Número de horas trabalhadas por mes? '))
imposto_renda = 0.11
inss = 0.08
sindicato = 0.05

salario = shoras * smes
valorinss = salario * inss 
valorsindicato = salario * sindicato
ir = (salario - inss - valorsindicato) * imposto_renda
salarioliquido = salario - valorinss - valorsindicato - ir
print('Salário Bruto R$',salario)
print('Imposto de renda (11%) R$ ',ir)
print('INSS (8%) R$ ',valorinss)
print('Sindicato (5%) R$ ',valorsindicato)
print('Salário líquido R$ ',salarioliquido)
