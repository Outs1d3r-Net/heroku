# Primeira Aplicação no Heroku

#### Este script é um codigo simples para implatação de software no heroku, aqui eu utilizo a biblioteca ```Flask``` do python para criar uma pagina web simples utilizando Html5 e Css3, a forma para fazer isso é adicionar uma variavel com conteudo de bloco no python e depois realizar o ```return``` nela.  
#### O script exibe os primeiros 100 (cem) números primos, que são os primos de 541, para alterar a quantidade e o valor dos números primos basta alterar o valor da variavel ```n2``` dessa forma todo o codigo vai adaptar á pagina para exibir as devidas informações como quantidade de primos e quais são eles.
> [Para visualizar minha aplicação simples, clique aqui.](https://defciber-ac04.herokuapp.com/ "Meu site simples")


### Exemplo:  

```

from flask import Flask
import os

def index():
    html = """
    <html><!-- MEU CODIGO AQUI --></html>
    """
    return html

```  
  
### Instalação para teste local:  

##### Primeiro certifique-se de que a biblioteca Flask esta disponivel na versão do python que você esta utilizando, o script ```server.py``` foi desenvolvido na versao 3.0 do Python, se mais alguma dependencia for necessaria verifique o arquivo ```requirements.txt```.  

> David@LV-223:~$ sudo python3 -m pip install flask  
   
#### Depois basta executar o script. Obs: Você pode alterar a porta web utilizada pelo ```Flask``` , aqui eu utilizo a 8443 (A mesma do EngineX) por que não é necessario privilegios de SuperUsuario (root).  

> David@LV-223:~$ python3 server.py  

#### Espero que gostem ! :shipit: 
