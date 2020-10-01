#!/usr/bin/env python3

# -*- coding: utf-8 -*-

###############################################################
# BY: Juan Regis                                              #
# Ref: https://flask.palletsprojects.com/en/1.1.x/quickstart/ #
###############################################################

#===> LIBRARIES
from flask import Flask
import os

app = Flask(__name__)                            # OBJ CLASS FLASK CREATE.
@app.route("/")                                  # DECORATOR FOR TELL FLASK WHAT URL.

#===> FUNCTIONS ,MAIN AND HTML CS
def index():
    n1 = 1
    n2 = 541                                      # PLEASE CHANGE THIS VARIABLE SO THAT THE RANGE OF PRIME NUMBERS CHANGES.
    primos = []

    for n in range(n1, n2+1):
        if n > 1:
            for i in range(2,n):
                if (n % i) == 0:
                    break
            else:
                primos.append(str(n))

    r = ' '.join(primos)
    pn = len(primos)
    r = "<h1><center>"+str(r)+"</center></h1>"

    re = """
<!-- CODE SOURCE HTML-->
<html>
    <meta charset='UTF-8'>
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0">
    <head>
        <title>Ac 04 - Prof: Antonio</title>
    </head>
    
    <!-- CSS STYLE -->
    <style>
       body{background-color: #ffffff;
			background-image: linear-gradient(#62eb96, #6d6e6d);
       }
       
       #cods{
           background-color: #ffffff;
           border-radius: 12%;
           border: solid 2px black;
       }
      
      #defi{
           background-color: #ffffff;
           border-radius: 5%;
           border: solid 1px black;
       }
    </style>
    
    <!-- TITLE -->
    <center><h1>Numeros primos em python</h1>
    
    <!-- IMAGENS -->
    <img src="https://i.ibb.co/QpKSBsR/Python.png" width="10%" />
    <img src="https://i.ibb.co/sRtcXJf/Html5.png" width="10%" />
    <img src="https://i.ibb.co/68GftgT/Css3.png" width="10%" />
    <img src="https://i.ibb.co/1LK4Qg5/Flask.png" width="13%" />
    <img src="https://i.ibb.co/PCTGb8B/Heroku.png" width="12%" />
    </center><br/>
    
    <pre><h2>Definição:</h2>
    <div id="defi">
            <center>Um número primo é aquele que é dividido apenas por um e por ele mesmo. Entre 0 e """+str(n2)+""" existem """+str(pn)+""" números primos.</center>
        </pre>
    </div><br/><br/>
    
    <h2>Codigo fonte:</h2>
    <div id="cods"><code><pre>
    n1 = """+str(n1)+"""                     		     # Divisor padrão.
    n2 = """+str(n2)+"""                   		     # Numero que deseja achar os primos.
    primos = []                              # Lista para armazenar os primos encontrados.

    for n in range(n1, n2+1):                # 1° Laço FOR cria lista de numeros padrao.
        if n > 1:
            for i in range(2,n):             # 2° Laço FOR procura os numeros primos, se nao condiz com os padroes ele e descartado.
                if (n % i) == 0:
                    break
            else:
                primos.append(str(n))       # Adiciona os primos encontrados na lista com ".append()"  

    print(' '.join(primos))                 # Exibe os primos. obs: No meu codigo a saida dos primos se transforma uma variavel para que ela seja exibida pelo Flask.
    </pre></code></div>


    <!-- START OF THE FUNCTION OF PRIMOS         -->
    <h2>Resultado dos primos de """+str(n2)+""" é igual a """+str(pn)+""":</h2>"""+r+"""
    <!-- END OF THE FUNCTION                     -->
    <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
    <footer><center>
      <p><b>Author:</b> Juan Regis</p>
      <p><i>Defesa Cibernetica 2º Semestre.</i></p>
    </center></footer>
</html>
"""

    return re

#===> MAIN
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8443))
    app.run(host='0.0.0.0', port=port)               # HERE I USE PORT TCP/8443
