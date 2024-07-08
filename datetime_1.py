from datetime import datetime #para isso coloque sempre _1.py no nome do programa.


hoje = datetime.now()
print (f"Data {hoje:%d/%m/%Y}, Horário: {hoje:%H:%M}")