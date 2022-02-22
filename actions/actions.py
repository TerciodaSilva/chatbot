from typing import Text, List, Any, Dict, Union, Optional
from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet, FollowupAction
import pymongo

import re
import datetime
import sqlite3
import json


# -------------------------- NOME ------------------------------
class ActionNome(Action):
    """
    Ação que preenche o slot nome com o valor digítado pelo usuário.
    """

    def name(self) -> Text:
        return 'action_nome'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        value = tracker.latest_message['text']  # captura o texto digítado pelo usuário
        print(value)
        slot = self.name().split('action_')[1]  # nome do slot que será preenchido.
        return [SlotSet(slot, value)]


# ---------------------- NOME COMPLETO -------------------------
class ActionNomeCompleto(ActionNome):
    """
    Ação que preenche o slot nomeCompleto com o valor digítado pelo usuário.
    """

    def name(self) -> Text:
        return 'action_nomeCompleto'


# ----------------------- RAZÃO SOCIAL -------------------------
class ActionRazaoSocial(ActionNome):
    """
    Ação que preenche o slot razao_social o valor digítado pelo usuário.
    """

    def name(self) -> Text:
        return 'action_razao_social'


# ---------------------- IDENTIFICAÇÃO -------------------------
class ActionIdent(ActionNome):
    """
    Ação que preenche o slot ident com o valor digítado pelo usuário.
    """

    def name(self) -> Text:
        return 'action_ident'


# ------------------------ NASCIMENTO --------------------------
class ActionNascimento(ActionNome):
    """
    Ação que preenche o slot nascimento com o valor digítado pelo usuário.
    """

    def name(self) -> Text:
        return 'action_nascimento'


# --------------------------- DDD ------------------------------
class ActionDDD(ActionNome):
    """
    Ação que preenche o slot DDD com o valor digítado pelo usuário.
    """

    def name(self) -> Text:
        return 'action_DDD'


# ---------------------- NUMERO CELULAR ------------------------
class ActionNumeroCelular(ActionNome):
    """
    Ação que preenche o slot numero_celular com o valor digítado pelo usuário.
    """

    def name(self) -> Text:
        return 'action_numero_celular'


# ---------------------- BAIRRO ENDERECO ------------------------
class ActionBairroEndereco(ActionNome):
    """
    Ação que preenche o slot bairro_endereco com o valor digítado pelo usuário.
    """

    def name(self) -> Text:
        return 'action_bairro_endereco'


# ---------------------- NUMERO ENDERECO ------------------------
class ActionNumeroEndereco(ActionNome):
    """
    Ação que preenche o slot numero_endereco com o valor digítado pelo usuário.
    """

    def name(self) -> Text:
        return 'action_numero_endereco'


# ------------------------- NOME RUA ----------------------------
class ActionNomeRua(ActionNome):
    """
    Ação que preenche o slot nome_rua com o valor digítado pelo usuário.
    """

    def name(self) -> Text:
        return 'action_nome_rua'


# ---------------------------- CEP ------------------------------
class ActionCEP(ActionNome):
    """
    Ação que preenche o slot CEP com o valor digítado pelo usuário.
    """

    def name(self) -> Text:
        return 'action_CEP'


# ---------------------- CODIGO DE BARRAS -----------------------
class ActionCodigoBarras(ActionNome):
    """
    Ação que preenche o slot codigo_barras com o valor digítado pelo usuário.
    """

    def name(self) -> Text:
        return 'action_codigo_barras'


# --------------------- VALOR COMPLEMENTO ------------------------
class ActionValorComplemento(ActionNome):
    """
    Ação que preenche o slot valor_complemento com o valor digítado pelo usuário.
    """

    def name(self) -> Text:
        return 'action_valor_complemento'


# ----------------------- VALOR E-MAIL ---------------------------
class ActionValorEmail(ActionNome):
    """
    Ação que preenche o slot valor_email com o valor digítado pelo usuário.
    """

    def name(self) -> Text:
        return 'action_valor_email'


# -------------------------- PLANO -------------------------------
class ActionEscolherPlano(ActionNome):
    """
    Ação que preenche o slot plano com o valor digítado pelo usuário.
    """

    def name(self) -> Text:
        return 'action_plano'


class ActionAtendenteHumano(Action):
    """
    Ação que direciona o usuário para um atendente humano.
    """

    def name(self) -> Text:
        return 'action_direcionado_atendente_humano'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        send_messages = [
            'Redirecionando para um atendente, aguarde um momento!',
            'https://cutt.ly//EPgLOVt'
        ]

        for message in send_messages:
            dispatcher.utter_message(text=message)

        return [FollowupAction('action_deactivate_loop')]


class ActionAskName(Action):
    """
    Ação que pergunta o nome para o usuário.
    É executado automaticamente quando o slot é requisitado.
    """

    def name(self) -> Text:
        return 'action_ask_nome'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        n_repeticao = int(tracker.get_slot('repeticao'))  # captura quantas vezes o mensagem se repetiu.
        slot = self.name().split('action_ask_')[1]  # captura o nome do slot.

        # caso o numero de repetições for entre 1 e 3.
        if 0 <= n_repeticao <= 2:
            file = open('responses.json', encoding='utf-8')  # abre o arquivo de respostas.
            message = json.load(file)[slot][f'{n_repeticao}']  # pega a resposta correspondente.
        # mantém o contador e redireciona para um atendente humano.
        else:
            return [FollowupAction('action_direcionado_atendente_humano')]

        dispatcher.utter_message(text=message)  # envia a mensagem para o usuário.
        # incrementa o slot repeticao
        return []


class ActionAskIdent(ActionAskName):
    """
    Ação que pergunta uma identificação para o usuário.
    É executado automaticamente quando o slot é requisitado.
    """

    def name(self) -> Text:
        return 'action_ask_ident'


class ActionAskNomeCompleto(ActionAskName):
    """
    Ação que pergunta o nome completo para o usuário.
    É executado automaticamente quando o slot é requisitado.
    """

    def name(self) -> Text:
        return 'action_ask_nomeCompleto'


class ActionAskDDD(ActionAskName):
    """
    Ação que pergunta o DDD para o usuário.
    É executado automaticamente quando o slot é requisitado.
    """

    def name(self) -> Text:
        return 'action_ask_DDD'


class ActionAskCodigoBarras(ActionAskName):
    """
    Ação que pergunta o código de barras do chip para o usuário.
    É executado automaticamente quando o slot é requisitado.
    """

    def name(self) -> Text:
        return 'action_ask_codigo_barras'


class ActionAskCEP(ActionAskName):
    """
    Ação que pergunta o CEP para o usuário.
    É executado automaticamente quando o slot é requisitado.
    """

    def name(self) -> Text:
        return 'action_ask_CEP'


class ActionAskNomeRua(ActionAskName):
    """
    Ação que pergunta o nome da rua para o usuário.
    É executado automaticamente quando o slot é requisitado.
    """

    def name(self) -> Text:
        return 'action_ask_nome_rua'


class ActionAskNumeroEndereco(ActionAskName):
    """
    Ação que pergunta o número do endereco para o usuário.
    É executado automaticamente quando o slot é requisitado.
    """

    def name(self) -> Text:
        return 'action_ask_numero_endereco'


class ActionAskValorComplemento(ActionAskName):
    """
    Ação que pergunta o complemento do endereço para o usuário.
    É executado automaticamente quando o slot é requisitado.
    """

    def name(self) -> Text:
        return 'action_ask_valor_complemento'


class ActionAskBairroEndereco(ActionAskName):
    """
    Ação que pergunta o bairro para o usuário.
    É executado automaticamente quando o slot é requisitado.
    """

    def name(self) -> Text:
        return 'action_ask_bairro_endereco'


class ActionAskNumeroCelular(ActionAskName):
    """
    Ação que pergunta o numero do celular para o usuário.
    É executado automaticamente quando o slot é requisitado.
    """

    def name(self) -> Text:
        return 'action_ask_numero_celular'


class ActionAskNascimento(ActionAskName):
    """
    Ação que pergunta a data de nascimento para o usuário.
    É executado automaticamente quando o slot é requisitado.
    """

    def name(self) -> Text:
        return 'action_ask_nascimento'


class ActionAskRazaoSocial(ActionAskName):
    """
    Ação que pergunta a razão social para o usuário.
    É executado automaticamente quando o slot é requisitado.
    """

    def name(self) -> Text:
        return 'action_ask_razao_social'


class ActionAskValorEmail(ActionAskName):
    """
    Ação que pergunta o e-mail para o usuário.
    É executado automaticamente quando o slot é requisitado.
    """

    def name(self) -> Text:
        return 'action_ask_valor_email'


class ActionGerarLink(Action):
    """
    Ação que gera o link de pagamento do boleto e envia para o usuário.
    """

    def name(self) -> Text:
        return 'action_link'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # mensagens que serão enviadas para o usuário.
        send_message = [
            'Clique no link e escolhe a forma desejada:',
            'https://www.bbc.com/']

        # envia mensagens para o usuário.
        for utter in send_message:
            dispatcher.utter_message(text=utter)
        return []


class ActionCadastrarCliente(Action):
    """
    Ação que cadastra um novo usuário no banco de dados
    """

    def name(self) -> Text:
        return 'action_cadastrar_cliente'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # informações que seram registradas.
        registrar = {
            'nomeCompleto': tracker.get_slot('nomeCompleto'),
            'registro': tracker.get_slot('ident')
        }

        # registra informações
        registrar_usuario(**registrar)
        return []


class ActionAgradecimento(Action):
    """
    Ação que agradece o usuário pelo atendimento.
    """

    def name(self) -> Text:
        return 'action_agradecimento'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        nome = tracker.get_slot('nome')  # captura nome usuário.
        hora = datetime.datetime.now().hour  # captura horário atual.

        send_messages = [
            'Caso tenha alguma dúvida nos contate através do link à seguir',
            'https://cutt.ly//EPgLOVt'
        ]

        if 6 < int(hora) < 18:
            send_messages.append(f'Agradecemos seu contato, tenha um ótimo dia {nome}.')
        else:
            send_messages.append(f'Agradecemos seu contato, tenha uma ótima noite {nome}.')

        for message in send_messages:
            dispatcher.utter_message(text=message)  # envia mensagem para o usuário.

        return []


class ActionAskPlano(Action):
    """
    Ação que pergunta o plano do chip para o usuário.
    É executado automaticamente quando o slot é requisitado.
    """

    def name(self) -> Text:
        return 'action_ask_plano'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # informações que serão enviadas para o usuário.
        send_message = [
            {'text': 'Pronto! Agora só falta escolher o plano. Escolha uma das opções a seguir'},
            {'image': 'https://github.com/TerciodaSilva/rasa_contel_bot/blob/main/folder.jpeg?raw=true'},
            {'response': 'utter_plano'}
        ]

        # envia as mensagens para o usuário.
        for message in send_message:
            dispatcher.utter_message(**message)

        return []


class ValidatePedirDados(FormValidationAction):
    """
    Validação do formulário pedir_dados.
    """

    def name(self) -> Text:
        return 'validate_pedir_dados'

    async def required_slots(self, domain_slots: List[Text], dispatcher: "CollectingDispatcher",
                             tracker: "Tracker", domain: "DomainDict") -> List[Text]:
        """
        Personaliza os slots requisitados pelo formulário.
        """
        list_aux = domain_slots.copy()  # copia a lista de slots requisitados pelo formulário.

        numbers = re.findall(r'\d+', str(tracker.get_slot('ident')))  # captura identificação digítada pelo o usuário.
        valor = str.join('', numbers)  # concatena os valores da identificação em uma string.

        # caso for um CPF
        if len(valor) == 11:
            index_ident = list_aux.index('ident') + 1  # posição que o próximo slot deverá ser inserido.
            list_aux.insert(index_ident, 'nomeCompleto')  # inseri o slot nomeCompleto a lista de slots requeridos.
            index_ident += 1  # incrementa a posição para o próximo slot.
            list_aux.insert(index_ident, 'nascimento')  # inseri o slot nascimento a lista de slots requeridos.
        # caso for um CNPJ
        elif len(valor) == 14:
            index_ident = list_aux.index('ident') + 1  # posição que o próximo slot deverá ser inserido.
            list_aux.insert(index_ident, 'razao_social')  # inseri o slot razao_social a lista de slots requeridos.

        # caso o usuário queira informar um complemento.
        if tracker.get_slot('complemento'):
            index_complemento = list_aux.index(
                'complemento') + 1  # posição onde o slot valor_complemento deverá ser inserido.
            list_aux.insert(index_complemento,
                            'valor_complemento')  # inseri o slot valor_complemento a lista de slots requeridos.

        # caso o usuário queira informar um e-mail.
        if tracker.get_slot('email'):
            index_email = list_aux.index('email') + 1  # posição onde o slot valor_email deverá ser inserido.
            list_aux.insert(index_email, 'valor_email')  # inseri o slot valor_email a lista de slots requeridos.

        # retorna os slots requeridos.
        return list_aux

    def validate_nome(self, slot_value: Any, dispatcher: CollectingDispatcher,
                      tracker: Tracker, domain: DomainDict, ) -> Dict[str, Optional[Any]]:
        """Valida o slot nome"""
        slot_return = {'nome': None, 'repeticao': int(tracker.get_slot('repeticao'))}  # dicionário que será retornado.
        slot_return['repeticao'] += 1

        try:
            slot_value = slot_value.strip()  # remove os espaços em branco no início e final da frase.
        except TypeError:
            return slot_return  # em caso de erro retorne o slot como está.

        # verifica se a frase é uma palavra única.
        if len(slot_value.split(' ')) == 1:
            slot_return['nome'] = slot_value  # armazena a frase digítada.
            slot_return['repeticao'] = 0  # zera o número de repetições da frase.
        else:
            return slot_return

        # envia mensagens ao usuário.
        list_response = ['utter_nome', 'utter_vantagens']
        for utter in list_response:
            dispatcher.utter_message(response=utter)

        # retorna o dicionário.
        return slot_return

    def validate_nomeCompleto(self, slot_value: Any, dispatcher: CollectingDispatcher,
                              tracker: Tracker, domain: DomainDict, ) -> Dict[Text, Any]:
        """Validate cuisine value."""

        slot_return = {'nomeCompleto': None,
                       'repeticao': int(tracker.get_slot('repeticao'))}  # dicionário que será retornado.
        slot_return['repeticao'] += 1

        try:
            slot_value = slot_value.strip()  # remove os espaços em branco no início e final da frase.
        except TypeError:
            return slot_return  # em caso de erro retorne o slot como está.

        # verifica se a frase contém mais de uma palavra única.
        if len(slot_value.split(' ')) > 1:
            slot_return['nomeCompleto'] = slot_value  # armazena a frase digítada.
            slot_return['repeticao'] = 0  # zera o número de repetições da frase.
        # retorna o dicionário.
        return slot_return

    def validate_ident(self, slot_value: Any, dispatcher: CollectingDispatcher,
                       tracker: Tracker, domain: DomainDict, ) -> Dict[Text, Any]:
        """
        Valida o identificador digítado pelo usuário.
        """

        def validarCPF(cpf):
            """
            Válida o CPF digítado pelo usuário.
            """
            cpf = cpf.replace('.', '').replace('-', '')  # remove as pontuações da frase.

            def somatorio(limite_n, limite_v):
                """
                Realiza o cálculo que válida o CPF.
                """
                soma = 0  # soma do valores.
                proximo_limite_n = limite_n + 1
                proximo_limite_v = limite_v + 1

                for valor in cpf[:limite_v]:
                    soma += int(valor) * limite_n
                    limite_n -= 1
                result = (soma * 10) % 11 == int(cpf[limite_v])  # verifica o CPF retornando True ou False.

                if not result or proximo_limite_v == 0:
                    return result

                return somatorio(proximo_limite_n, proximo_limite_v)

            return somatorio(10, -2)

        slot_return = {'continue': True, 'ident': None, 'repeticao': int(tracker.get_slot('repeticao'))}
        slot_return['repeticao'] += 1

        try:
            numbers = re.findall(r'\d+', slot_value)  # separa os dígitos da identificação.
            valor = str.join('', numbers)  # junta os números em uma string.
        except TypeError:
            return slot_return

        #        if consultar_registro(valor):
        #            dispatcher.utter_message(text='Você já tem um cadastro conosco!')
        #            return {"ident": None, "requested_slot": None, "continue": False}

        # caso for um formato de um identificador válido.
        if (len(valor) == 11 and validarCPF(valor)) or len(valor) == 14:
            slot_return['repeticao'] = 0
            slot_return['ident'] = slot_value
        # retorna o dicionário.
        return slot_return

    def validate_CEP(self, slot_value: Any, dispatcher: CollectingDispatcher,
                     tracker: Tracker, domain: DomainDict, ) -> Dict[Text, Any]:
        """
        Válida o CEP digítado pelo usuário.
        """
        slot_return = {'CEP': None, 'repeticao': int(tracker.get_slot('repeticao'))}  # dicionário que será retornado.
        slot_return['repeticao'] += 1

        try:
            numbers = re.findall(r'\d+', slot_value)  # separa os dígitos do CEP digítado.
            valor = str.join('', numbers)  # junta os números em uma string.
        except TypeError:
            return slot_return

        if len(valor) == 8:
            slot_return['CEP'] = slot_value  # armazena a frase digítada.
            slot_return['repeticao'] = 0  # zera o número de repetições da frase.
        # retorna o dicionário.
        return slot_return

    def validate_nascimento(self, slot_value: Any, dispatcher: CollectingDispatcher,
                            tracker: Tracker, domain: DomainDict, ) -> Dict[Text, Any]:
        """
        Válida a data de nascimento digítada.
        """

        slot_return = {'nascimento': None,
                       'repeticao': int(tracker.get_slot('repeticao'))}  # dicionário que será retornado.
        slot_return['repeticao'] += 1

        try:
            numbers = re.findall(r'\d+', slot_value)  # extraí os números da data de nascimento.
            # caso o usuário informar apenas os dois últimos digítos do ano.
            if len(numbers[2]) == 2:
                numbers[2] = '19' + numbers[2]
            datas = {
                'dia': int(numbers[0]),
                'mes': int(numbers[1]),
                'ano': int(numbers[2]),
            }  # estrutura os números da data em um dicionário.
        except IndexError:
            return slot_return

        anoAtual = datetime.date.today().year  # ano atual do atendimento.
        # caso o usuário tiver até 150 anos.
        if anoAtual - datas['ano'] < 150:
            # caso o mês for até 12.
            if 0 < int(datas['mes']) < 13:
                ano = datas['ano']
                # caso for o mês de fevereiro.
                if datas['mes'] == 2:
                    limite = 29 if (ano % 4 == 0 and ano %
                                    100 != 0) or (ano % 400 == 0) else 28  # trata o ano bisiestos.
                else:
                    limite = 31 if int(datas['mes']) in list(
                        range(1, 13, 2)) else 30  # verfica se o mês tem 30 ou 31 dias.

                # verifica se o dia informado está dentro do limite permitido para o mês fornecido.
                if 0 < datas['dia'] < limite + 1:
                    slot_return['nascimento'] = slot_value  # armazena a data informada pelo usuário.
                    slot_return['repeticao'] = 0  # zera o número de repetições da frase.

        return slot_return

    def validate_DDD(self, slot_value: Any, dispatcher: CollectingDispatcher,
                     tracker: Tracker, domain: DomainDict, ) -> Dict[Text, Any]:
        """
        Válida o DDD informado.
        """

        slot_return = {'DDD': None, 'repeticao': int(tracker.get_slot('repeticao'))}  # dicionário que será retornado.
        slot_return['repeticao'] += 1

        try:
            numbers = re.findall(r'\d+', slot_value)  # remove toda a pontuação fornecida.
            valor = str.join('', numbers)  # concatena o valor em uma string.
        except ValueError:
            return slot_return

        # verifica se o valor se encontra entre 1 e 99.
        if 0 < int(valor) < 100:
            slot_return['DDD'] = slot_value  # armazena a informação digítada pelo usuário.
            slot_return['repeticao'] = 0  # zera o número de repetição da frase.
        return slot_return

    def validate_codigo_barras(self, slot_value: Any, dispatcher: CollectingDispatcher,
                               tracker: Tracker, domain: DomainDict, ) -> Dict[Text, Any]:
        """
        Válida o código de barras digítada pelo usuário.
        """
        slot_return = {'codigo_barras': None,
                       'repeticao': int(tracker.get_slot('repeticao'))}  # dicionário que será retornado.
        slot_return['repeticao'] += 1

        try:
            numbers = re.findall(r'\d+', slot_value)  # separa os números informados pelo usuário.
            valor = str.join('', numbers)  # concatena os números em uma string.
        except TypeError:
            return slot_return

        # verifica se o código informado contém 19 digítos e se começa com 8955.
        if len(valor) == 19 and valor[:4] == '8955':
            slot_return['codigo_barras'] = slot_value  # armazena a informação digítada.
            slot_return['repeticao'] = 0  # zera a repetição da frase.
        return slot_return

    def validate_nome_rua(self, slot_value: Any, dispatcher: CollectingDispatcher,
                          tracker: Tracker, domain: DomainDict, ) -> Dict[Text, Any]:
        """
        Valida o nome da rua fornecido pelo usuário.
        """
        slot_result = {'nome_rua': None, 'repeticao': int(tracker.get_slot('repeticao'))}
        slot_result['repeticao'] += 1
        slot_result['nome_rua'] = slot_value

        # verifica se o último caracter da frase é um digíto.
        if slot_value[-1].isnumeric():
            result = re.search('([\w\W]+)\s(\d+)', slot_value)  # separa o nome da rua e o número do endereço.
            slot_result['nome_rua'] = result.group(1)
            slot_result['numero_endereco'] = result.group(2)
            slot_result['repeticao'] = 0

        return slot_result

    def validate_valor_complemento(self, slot_value: Any, dispatcher: CollectingDispatcher,
                                   tracker: Tracker, domain: DomainDict, ) -> Dict[Text, Any]:
        """
        Válida o complemento informando.
        """

        return {'valor_complemento': slot_value, 'repeticao': 0}

    def validate_valor_email(self, slot_value: Any, dispatcher: CollectingDispatcher,
                             tracker: Tracker, domain: DomainDict, ) -> Dict[Text, Any]:
        """
        Válida o e-mail informado pelo usuário.
        """

        return {'valor_email': slot_value, 'repeticao': 0}

    def validate_numero_celular(self, slot_value: Any, dispatcher: CollectingDispatcher,
                                tracker: Tracker, domain: DomainDict, ) -> Dict[Text, Any]:
        """
        Válida o número de celular fornecido pelo usuário.
        """

        slot_return = {'numero_celular': None,
                       'repeticao': int(tracker.get_slot('repeticao'))}  # dicionário que será retornado.
        slot_return['repeticao'] += 1

        # verifica se o valor informado são digítos.
        if slot_value.isnumeric():
            slot_return['numero_celular'] = slot_value  # armazena a informação digítada.
            slot_return['repeticao'] = 0  # zera o número de repetição do slot.

        return slot_return

    def validate_numero_endereco(self, slot_value: Any, dispatcher: CollectingDispatcher,
                                 tracker: Tracker, domain: DomainDict, ) -> Dict[Text, Any]:
        """
        Valida o número do endereço fornecido pelo usuário.
        """

        return {'numero_endereco': slot_value, 'repeticao': 0}

    def validate_bairro_endereco(self, slot_value: Any, dispatcher: CollectingDispatcher,
                                 tracker: Tracker, domain: DomainDict, ) -> Dict[Text, Any]:
        """
        Valida o bairro fornecido pelo usuário.
        """

        return {'bairro_endereco': slot_value, 'repeticao': 0}

    def validate_razao_social(self, slot_value: Any, dispatcher: CollectingDispatcher,
                              tracker: Tracker, domain: DomainDict, ) -> Dict[Text, Any]:
        """
        Valida a razao social fornecida pelo usuário.
        """

        return {'razao_social': slot_value, 'repeticao': 0}


def open_database(func):
    """
    Função decoradora que abre o banco de dados.
    """

    def wrapper(*args, **kwargs):
        con = sqlite3.connect('database.db')
        kwargs['cursor'] = con.cursor()
        response = func(*args, **kwargs)
        con.commit()
        con.close()
        return response

    return wrapper


@open_database
def criar_table(*args, **kwargs):
    """
    Função que cria uma tabela no banco de dados.
    """
    cursor = kwargs.get('cursor')
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS TblUsers (Id INTEGER PRIMARY KEY, 
    nomeCompleto varchar(100), registro varchar(14))
    """)


@open_database
def registrar_usuario(*args, **kwargs):
    """
    Registra dados no banco de dados.
    """
    criar_table()
    cursor = kwargs.get('cursor')
    kwargs.pop('cursor')
    cursor.execute("INSERT INTO TblUsers(nomecompleto, registro) VALUES (?, ?)", list(kwargs.values()))


@open_database
def consultar_registro(ident_user, *args, **kwargs):
    """
    Consulta um registro no banco de dados.
    """
    criar_table()
    cursor = kwargs.get('cursor')
    cursor.execute("SELECT * FROM TblUsers WHERE registro=?", (ident_user,))
    return False if len(cursor.fetchall()) == 0 else True
