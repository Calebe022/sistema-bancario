<h2 align="left">Sistema Bancário em Python</h2>

###

<p align="left">Este é um sistema bancário simples desenvolvido como parte de um desafio do bootcamp de Python da DIO. O objetivo do sistema é permitir ao usuário realizar depósitos, saques e consultar o extrato de sua conta. Além disso, há diversas validações implementadas para garantir a integridade das operações.</p>

###

<h3 align="left">Funcionalidades</h3>

###

<p align="left">* Depositar: O usuário pode depositar valores em sua conta. O sistema valida se o valor informado é positivo.<br>* Sacar: O usuário pode realizar saques, mas com algumas restrições:<br>O valor do saque não pode ser maior que o saldo disponível.<br>O valor do saque não pode exceder o limite de R$ 500,00.<br>O número de saques é limitado a 3 por usuário.<br>* Extrato: O usuário pode consultar um extrato com todas as transações realizadas, incluindo depósitos e saques. O sistema também exibe o saldo atual.<br>* Sair: O usuário pode encerrar o sistema a qualquer momento.</p>

###

<h3 align="left">Validações Implementadas</h3>

###

<p align="left">Saldo Insuficiente: Se o valor do saque for maior do que o saldo disponível, a operação é cancelada e o sistema informa o erro.<br>Limite de Saque: O valor do saque não pode ultrapassar o limite estabelecido de R$ 500,00. Caso contrário, a operação será cancelada.<br>Limite de Saques: O sistema permite no máximo 3 saques por usuário. Caso esse limite seja alcançado, o sistema impede novos saques.</p>

###

<h3 align="left">Fluxo de Execução</h3>

###

<p align="left">O sistema funciona em um loop contínuo, exibindo um menu com as opções de depósito, saque, extrato e sair. O usuário deve digitar a opção desejada, e o sistema executa a ação correspondente. O programa só é encerrado quando o usuário escolhe a opção de sair.</p>

###

<h2 align="left">Conclusão</h2>

###

<p align="left">Este desafio foi uma excelente oportunidade para praticar conceitos importantes de programação, como controle de fluxo, manipulação de dados e validação de entradas do usuário. Além disso, ele me proporcionou uma boa experiência em criar um sistema funcional e simples, que pode ser facilmente expandido ou melhorado com mais funcionalidades no futuro.</p>

###
