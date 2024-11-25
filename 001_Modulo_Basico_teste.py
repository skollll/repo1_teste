# Módulo Básico 1 - Última Revisão: 16/08/2024
# --------------------------------------------
#        1         2         3         4         5         6         7         8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#
# CRUD stands for Create, Read, Update, and Delete. 

print("""
                          ÍNDICE
 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  $01. Introdução               §11. CLS 
  §02. Carga navegador padrão   §12. Dicionários
  §03. Importando módulos       §13. Lista Resumo
  §04. Colorama                 §14. Corte de strings(com régua)
  §05. Título e subtítulos      §15. StringIO
  §06. Resumão de formatação    §16. Print para arquivo
  §07. Caracteres especiais     §17. Detectando usuário
  §08. Timer / Temporizador     §18. Tkinter genérico 
  §09. Tratando erros           §19. Carregando imagem c/ OpenCV
  §10. Escapes                  §20. File path
 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
""")


# §01. Introdução
#! python3.
#! /usr/bin/env python3.
#! /usr/bin/python3.
# §1. As 3 linhas cima são chamadas de shebang line Windows, OS X e Linux 

# black -l 100 -t py312 <nome_do_programa>.py

# tit=" ";print(F"\n\n\n\n\n{'▬'*len(tit)}\n{tit}\n{'▬'*len(tit)}")
# t="1. ";print(F"\n{t}\n{'¯'*len(t)}")
# st="1.1 ";print(F"\n{st}\n{'-'*len(st)}")

# O normal é __debug__ true >> python -O my_script.py -> debug mode is disabled
if __debug__:
    print("Debug mode is enabled.")
else:
    print("Debug mode is disabled.")


cont = input("continua...")


# §02. Python was inspired by ABC, Haskell, Java, Lisp, Icon, and Perl
# import webbrowser 
# webbrowser.open("https://www.programming-hero.com/")

# arq1 = ".\\dados\\[nome_do_arquivo.ext]"
#
# Anulador de trecho de programa,parte final: ###'''



# §03. Importando módulos 
"""
import mod -> para usar as variáveis -> mod.s  mod.foo mod.a   mod.__file__ <- mostra 
o caminho de onde importou

from mod import s, foo -> pode usar as variáveis direto:  s, foo

from mod import * -> vai importar tudo, porem cuidado para não sobrepor 

from mod import s as string_1, a as alist -> vai importar mudando os nomes
 
import mod as mod_novo_nome  -> dá um novo nome, então para acessar as variáveis mod_novo_nome.a

import os
print(os)
"""



# §04. Colorama
from colorama import Fore 
from colorama import init as colorama_init
colorama_init(autoreset=False) # <--- True
u = dict(Fore.__dict__.items())
PR,AZ,CY,VD,CZ,AZB=u['BLACK'],u['BLUE'],u['CYAN'],u['GREEN'],u['LIGHTBLACK_EX'],u['LIGHTBLUE_EX']
CYB,VDB,MGB,VMB,BRB=u['LIGHTCYAN_EX'],u['LIGHTGREEN_EX'],u['LIGHTMAGENTA_EX'],u['LIGHTRED_EX'],u['LIGHTWHITE_EX']
AMB,MG,VM,RS,BR,AM=u['LIGHTYELLOW_EX'],u['MAGENTA'],u['RED'],u['RESET'],u['WHITE'],u['YELLOW']
#print(F"[{PR}*{AZ}*{CY}*{VD}*{CZ}*{AZB}*{CYB}*{VDB}*{MGB}*{VMB}*{BRB}*{AMB}*{MG}*{VM}*{RS}*{BR}*{AM}{RS}]")
print(F"""
-----------------------------------------------
{PR}#.#  {CZ}PR   {AZ}#.#  AZ   {CY}#.# CY   {CYB}#.# CYB   {AZB}#.# AZB
{VD}#.#  VD   {VDB}#.# VDB
{MGB}#.# MGB   {VMB}#.# VMB   {MG}#.# MG   {VM}#.#  VM
{BR}#.#  BR   {BRB}#.# BRB   {AM}#.# AM   {AMB}#.# AMB
{CZ}#.#  CZ   {RS}RS(reset)
-----------------------------------------------
""")


cont = input("continua...")


# §05. Título e sub-títulos 
tit="Módulo Básico";print(F"\n\n\n\n\n{'▬'*len(tit)}\n{tit}\n{'▬'*len(tit)}")
print(AMB)
t="1. tipo 1";print(F"\n{t}\n{'¯'*len(t)}")
t="tipo 2";print(F"\n{t}\n{'ˆ'*len(t)}")
t="tipo 3";print(F"\n{t}\n{'˄'*len(t)}") # esse não aparece no trabalho 
t="tipo 4";print(F"\n{t}\n{'■'*len(t)}")
t="tipo 5";print(F"\n{t}\n{'▬'*len(t)}")
print(CY)
st="1.1 Direto";print(F"\n{st}\n{'¯'*len(st)}")
print(RS)

#quit()

# §06. Resumão de formatação 
import datetime
nome, idade, ocupacao, PI, A = "Eva", 36, "arquiteta", 3.141592653589793, 42
print(F"{AM}\n\n======================================")
print("{     \\Resumão de formatação\\        }")
print("======================================")
print("1. %s | %d | %s" % (nome, idade, ocupacao))
print("2. {} | {} | {}".format(nome, idade, ocupacao))
print(F"3. {nome:^5}| {idade} | {ocupacao=}")
print(F"4. {datetime.datetime.now():%d/%m/%Y e %Hh%Mm} {{1+1=2}}")
print(F"5. {PI:.4f} | {PI:.2f} | {PI:012.5f}, {A:04}")
print(F"6. |{nome:<10}|{nome:>10}|{nome:10}|")
print("7. -1234567890-1234567890-1234567890") 
print(F"8. |{nome:#<10}|{nome:_>10}|{nome:.^10}|")
print(F"9. Hex:{A:x}   Oct:{A:o}   Sci:{A:e}")
print(F"10.Bin:{A:07b}■■Bin:{A:<7b}■Dec:{A:05}")
print(F"11.■■¯¯■■ˆˆ■■~~■■■■■■■■■■■ ■■■■■■■■■■")
print("======================================")

# bota , como separador e troca por .
v = 8027793812
vn = F"{v:11,}".replace(",", ".")
print(F"\n{VDB} População mundial: {vn}")

v = 1234.56
vn = F"{v:11,}"
vn1 = vn.replace(",", "|")
vn2 = vn1.replace(".", ",")
vn3 = vn2.replace("|", ".")
print(vn3)


cont = input("continua...")


# §07. Caracteres especiais
print(CY, """ 
Tabela com alguns caracteres especiais 
--------------------------------------
áéíóúÁÉÍÓÚàÀçÇâêôÂÊÔãõÃÕüÜ
“ double quotes ”  ː⧸⧹2•■»«►‘aspas1’↑
""")
#   \’  Single quote       \f         Formfeed
#   \"  Double quote       \v         Vertical Tab
#   \\  Backslash          \0         Null Character
#   \n  Newline            \N{Name}   Unicode character Database named lookup ???
#   \r  Carriage Return    \uxxxxxxxx Unicode character with a 16-bit hex value
#   \t  Horizontal Tab     \Uxxxxxxxx Unicode character with a 32-bit hex value
#   \a  Bell(som Windows)  \000       Character with octal value ooo
#   \b  Backspace          \xhh       Character with hex value h
#   ''' use para anular trechos 



# §08. Timer / Temporizador
import time # TIMER 
start = time.perf_counter()
time.sleep(1)
print(F"Tempo de execução:{(time.perf_counter()-start):5.6f}")



# §09. Tratando erros  compacto e longo
try:
    print(42/0)
except Exception as EX:
    msge = F"| Erro->> {type(EX).__name__} | Args->> {EX.args} |"
    ml, mc = len(msge)-2, "-"  # caractere
    print(F" {ml*mc}\n{msge}\n {ml*mc}")
"""
    msge = F"Erro >> {type(EX).__name__}  | Args >> {EX.args}"
    print(F"{len(msge)*'>'}\n{msge}\n{len(msge)*'<'}")
"""
try:
    42/0
except Exception as EX:
    tipo = type(EX).__name__
    print(F"{'-'*65}\nErro classe --> {tipo}\nArgs --> {EX.args}\n{'-'*65}")
  
 
    
# §10. Escapes
print(VMB, """
Controles de ESCAPE
-------------------
Reserve ''' para anular trechos   #-mexendo  ##-incompleto/defeito  
Lista de caracteres epeciais
\\n  Breaks the string into a new line print(‘I designed this rhyme to explain in due time\nAll I know’)
\\t  Adds a horizontal tab 
\\  Prints a backslash 
\'  Prints a single quote print(‘It doesn\’t even matter how hard you try’)
\"  Prints a double quote print('It is so \"unreal\"')
\a  makes a sound like a bell print(‘\a’) 
""", RS)



# §11. CLS 
# para limpar a tela em qualquer sistema 
import os
#os.system('cls' if os.name == 'nt' else 'clear')



# §12. Dicts 
"""
Resumo Dict 6 Formas
-------------------------------------------------------------------
                 Direto: d1 = {"A": 100, "E": 104}
                   Dict: d2 = dict(A=100, E=104))
             Atribuindo: d3, d3["A"], d3["E"] = {}, 100, 104
      Dic.Comprehension: d4 = {i: ord(i)+35 for i in ['A', 'E']}
Dic.Comprehension & Zip: k5, p5 = ['A', 'E'], [100, 104]
                         d5 = {k: p for k, p in zip(k5, p5)}
             Dict & Zip: d6 = dict(zip(["A", "E"], [100, 104]))
-------------------------------------------------------------------    

# Melhor forma de gravar um Dict é usando o formato json
arquivo = "<nome do arquivo>"

with open(arquivo, "w") as arq:
    json.dump(capitais, arq) # gravando  

with open(arquivo, "r") as arq:
    capitais_2 = json.load(arq) # lendo
    
print(json.dumps(capitais_2, indent=4, ensure_ascii=False))
"""

'''
# Dic chave/valor -> variável/valor
dict_1 = {"a":100,"b":1891,"d":"205-numero", "z":300}
A = types.SimpleNamespace(**dict_1)
print(F"A.d:{A.d}\nA.b:{A.b}\nA.a:{A.a}")
print("A.z:", A.z)
print(vars(A))
'''



# §13 - LISTA - RESUMO ##################################################################
"""
Python List Methods
-------------------
Method	   Description
append()   add an item to the end of the list
extend()   add items of lists and other iterables to the end of the list
insert()   inserts an item at the specified index
remove()   removes item present at the given index
pop()	   returns and removes item present at the given index
clear()	   removes all items from the list
index()	   returns the index of the first matched item
count()    returns the count of the specified item in the list
sort()	   sort the list in ascending/descending order
reverse()  reverses the item of the list
copy()	   returns the shallow copy of the list
"""
#      0   1   2   3   4 
L1 = ["a","e","i","o","u"]
#     -5  -4  -3  -2  -1  
L1.append("z") # adicionar item ao fim da lista 
L1[0] = "A" # alterar item pelo índice ->>> IndexError: list assignment index out of range
L1.extend(['abacaxi', 'banana', 'caju', 'banana'])   # somar uma lista, é mais rápido do que +
L1.insert(15, "---") # inserir na posição, se exceder o indice, aceita e bota como ultimo 
L1.remove("u") # Se não existir ->>> ValueError: list.remove(x): x not in list
print("Removidos:", L1.pop(0), L1.pop(3))
print("primeira banana na posição:", L1.index('banana')) # L1.index('banana', 5)
print("Contagem:", L1.count('banana')) # tem 2
L1.sort()
print(L1)
lista_copia = L1.copy() # copiar assim para ter uma lista independente
###############################################################################################



# §14. Corte de strings
#    012345 
A = "albedo"
A_direita = ("##########" + A)[-10:]
A_esquerda = (A + "**********")[0:10]
A_meio = A[2:4] # 4 exclusivo
print(F"{MGB}{A_direita}\n{A_esquerda}\n{A_meio}")



# §15. StringIO - cuidado com espacos depois do indice, por exemplo 
import pandas as pd
from io import StringIO

arq = StringIO("""         quantidade, preco, indice
A,   40,   10,  1
B,   93,   30,  2
C,  188,  220,  3
D,    0,    0,  4""")

df = pd.read_csv(arq, index_col=0, delimiter=',', skipinitialspace=True)
#print(df)



# §16. Imprimir para arquivo
# print("\n\n\n\n\nAhá, pode imprimir para aquivo")
# with open(".\\dados\\print1.txt", "w+") as arq:
#     print("Fui impresso em arquivo", file=arq)



# §17. Detectando usuário
import socket
maquina = socket.gethostname()
print(F"Equipamento: {maquina}")
if maquina == "ET00186531":
    nome_arq = "D:\\PYTHON_3\\02_HUGE_DATA\\netflix_titles.csv"
elif maquina == "C8":
    nome_arq = "C:\\PYTHON_3\\02_HUGE_DATA\\netflix_titles.csv"
else:
    print("Não consigo detectar a maquina, favor ajustar nomes de arquivo")
    quit


        
# §18. Tkinter genérico 
from tkinter import *
from tkinter import messagebox
from tkinter import font as tkFont 

top = Tk()
top.geometry("200x200")

h12 = tkFont.Font(family='Helvetica', size=12, weight='normal') 
c16 = tkFont.Font(family='Courier New', size=10, weight='bold')   

def hello():
   messagebox.showinfo("[ ! ] Tkinter Label","Usaremos Label1, Label2, Label3...")
   messagebox.showwarning("t ! t Tkinter Label","Usaremos Label1, Label2, Label3...") # /!\
   messagebox.showerror("( x ) Tkinter Label","Usaremos Label1, Label2, Label3...")
   
t1 = "nono no nonono nono no " * 200   

text = Text(top, height = 10) # 10 linhas, excedeu, corta no fim 
# top.geometry("200x100")
text.insert(INSERT, t1)  
text.pack()   
  
bk = "\u232B"  # simbolo de backspace
B1 = Button(top, text = "Leia isso"+bk, command = hello)
B1.place(x = 10,y = 20)

"""
from tkinter import filedialog as fd
path: str = fd.askopenfilename(title="Selecione um arquivo") #, initialdir=, filetypes=(('PDF', '*.pdf'), (MP3, '*.mp3')))
print(path)
"""
top.mainloop()



# §19. Carregando a imagem com o OpenCV
import cv2 # pip install opencv-python
img = cv2.imread(".\\img\\modulo_basico.jpg") 
cv2.imshow("TITULO da IMAGEM", img) # Output img with window name as 'image'
cv2.waitKey(0)            # Maintain output window utill user presses a key      
cv2.destroyAllWindows()     # Destroying present windows on screen



# §20. File path
from tkinter import filedialog as fd
path: str = fd.askopenfilename(title="Selecione um arquivo") #, initialdir=, filetypes=(('PDF', '*.pdf'), (MP3, '*.mp3')))
print(path)


"""
         1         2         3         4         5         6         7         8
12345678901234567890123456789012345678901234567890123456789012345678901234567890
"""

print("\n*** fim ***") 


