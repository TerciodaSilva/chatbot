# README
![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)
Documentação de instalação do chatbot CONTEL.

Esse trabalho está vinculado ao projeto de pesquisa em parceria da CONTEL com a UNISC que tem como propósito o desenvolvimento de um piloto de chatbot para atendimento ao cliente, no processo que envolva ativação de chip.

![alt text](https://github.com/TerciodaSilva/rasa_contel_bot/blob/461277423c29dcd9511645044cbe25078cfa595b/Captura%20de%20tela%202022-02-22%20152347.png)

# Como instalar
> Faça o clone desse projeto.
```sh
git clone https://github.com/TerciodaSilva/chatbot.git
```
> Entre no diretório do projeto.
```sh
cd chatbot
```
> Crie um novo ambiente virtual escolhendo um interpretador Python e criando um diretório .\\venv para mantê-lo:
```sh
python3 -m venv ./venv
```
>Ative o ambiente virtual:
```sh
.\venv\Scripts\activate
```
>Instale o Rasa Open Source usando pip (requer Python 3.7 ou 3.8).
```sh
pip3 install rasa
```

### Mais informações
| recurso | link |
|---------|------|
| Rasa | https://rasa.com/docs/rasa/installation/ |
| Comunidade Rasa Stack Brasil | https://t.me/RasaBrasil |

### 🛠 Tecnologias
 As seguintes ferramentas foram utilizadas no construção do projeto.
- [python](https://www.python.org/)
- [rasa](https://rasa.com/)

# Como usar o chatbot
Para usar o chatbot é necessário que todos os passos anteriores de instalção tenham sido realizados.
> Primeiro é necessário executar a parte lógica do chatbot.
```sh
rasa run actions
```
> Depois em um segundo terminal é necessário realizar o treinamento do modelo da IA.
```sh
rasa train
```
> Para testar o chatbot no terminal.
```sh
rasa shell
```
> Para rodar o chatbot em um canal de chat, mas antes não esqueça de configurar o arquivo credentials.yml.
```sh
rasa run
``` 
> Esse chatbot usa como teste para canais de chat o ngrok, você pode baixá-lo [AQUI](https://ngrok.com/download).
> Para criar um túnel HTTP use o comando.
```sh
ngrok http 5005
```


# Licença
> MIT

Made with 🧡 by Tércio da Silva 🖐 [See my LinkedIn](https://www.linkedin.com/in/t%C3%A9rcio-da-silva-a5b385197/)
