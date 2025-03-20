<h2 align="left">Sistema Bancário em Python</h2>

###

<p align="left">Este é um sistema bancário simples desenvolvido como parte de um desafio do bootcamp de Python da DIO. O objetivo do sistema é permitir ao usuário realizar depósitos, saques e consultar o extrato de sua conta. Além disso, há diversas validações implementadas para garantir a integridade das operações.</p>

###

<div align="center">
  <img height="200" src="https://camo.githubusercontent.com/5162a0ebecec495cc74f8992e3145e4bb4d8f7cb5746685bcc0dd7921dd65814/68747470733a2f2f6173736574732e64696f2e6d652f7771464e4644315f37414b4e314d70625a76757259316355637055585132454c4d6657354269395238564d2f663a776562702f683a3132302f713a38302f4c33527959574e726379396c4e324d7a5a6a566b4e7930794d5445774c5451334e325974596d59784d5330774e6a67334d6a517a4d6a5a6a597a45756347356e"  />
</div>

###

<h2 align="left">Funcionalidades</h2>

###

<h3 align="left">Depositar: O usuário pode depositar valores em sua conta. O sistema valida se o valor informado é positivo.</h3>

###

<h3 align="left">Sacar: O usuário pode realizar saques, mas com algumas restrições:</h3>

###

<p align="left">- O valor do saque não pode ser maior que o saldo disponível.<br>- O valor do saque não pode exceder o limite de R$ 500,00.<br>- O número de saques é limitado a 3 por usuário.</p>

###

<h3 align="left">Extrato: O usuário pode consultar um extrato com todas as transações realizadas, incluindo depósitos e saques. O sistema também exibe o saldo atual.</h3>

###

<h3 align="left">Sair: O usuário pode encerrar o sistema a qualquer momento.</h3>

###

<h2 align="left">Validações Implementadas</h2>

###

<h3 align="left">Saldo Insuficiente: Se o valor do saque for maior do que o saldo disponível, a operação é cancelada e o sistema informa o erro.</h3>

###

<h3 align="left">Limite de Saque: O valor do saque não pode ultrapassar o limite estabelecido de R$ 500,00. Caso contrário, a operação será cancelada.</h3>

###

<h3 align="left">Limite de Saques: O sistema permite no máximo 3 saques por usuário. Caso esse limite seja alcançado, o sistema impede novos saques.</h3>

###

<h2 align="left">Fluxo de Execução</h2>

###

<p align="left">O sistema funciona em um loop contínuo, exibindo um menu com as opções de depósito, saque, extrato e sair. O usuário deve digitar a opção desejada, e o sistema executa a ação correspondente. O programa só é encerrado quando o usuário escolhe a opção de sair.</p>

###

<h2 align="left">Conclusão</h2>

###

<p align="left">Este desafio foi uma excelente oportunidade para praticar conceitos importantes de programação, como controle de fluxo, manipulação de dados e validação de entradas do usuário. Além disso, ele me proporcionou uma boa experiência em criar um sistema funcional e simples, que pode ser facilmente expandido ou melhorado com mais funcionalidades no futuro.</p>

###
