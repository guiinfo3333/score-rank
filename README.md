# Score Hank
#### Esse programa foi um desafio proposto para o fim de ano a fim de aprendermos sobre uma linguagem nova.
##### O desafio era criar um sistema que pudesse prever os resultados do brasileirão 2023, utilizando análise de dados das estatísticas entre os 2 times e machine learning

## 🚧 STATUS DO PROJETO
- [x] Criação do Banco de dados
- [x] Pegar dados de api externa sobre informações dos jogos de cada time
- [x] Criação da classe inteligence que armazena a machine learning que irá aprender e dirá para nós os resultados
- [x] Nível de percentual de acerto de 49% quando treinamos a máquina utilizando dados de 2019 a 2022, a fim de prever o brasileirão de 2023

## ❌ Dificuldades encontradas
- [x] Não sabíamos quase nada de aprendizado de máquina quando inciamos, havia uma gama de algoritmos e não sabiamos qual era o mais adequado para esta tarefa.
- [x] Mesmo depois de implementar-mos a inteligência, percebemos que somente os dados que nós tínhamos como chute a gol, gols.. não era suficientes para determinar o resultado do jogo, assim era preciso outras variáveis das quais nós não teríamos

## 🎲 Equipe
Projeto desenvolvido para fins de estudos, é composta pelos seguintes integrantes:
<ul>
    <li>Lucas Macedo (Desenvolvedor)</li>
    <li>Antônio Guilherme do Nascimento Pereira (Desenvolvedor)</li>
    <li>Yan Victor (Desenvolvedor)</li>
    <li>Ramiro Damasceno (Desenvolvedor) </li>
    <li>Lucas Café (Desenvolvedor)</li>
    <li>Linconln Damasceno (Analista de Testes)</li>
    <li>Maria Moreira (Analista de Requisitos)</li>
</ul> 

## 📅 Data da última atualização
    29/12/2023

## 🏃 Como rodar?
<ul>
    <li>Executar pip install scikit-learn no diretorio do projeto</li>
    <li>Executar pip install psycopg2 no diretorio do projeto</li>
    <li>Altere seus dados do banco de dados no arquivo config.py</li>
    <li>Ter o banco de dados do score rank na máquina, ele se encontra na basta backup, restaure ele em seu postgres local usando psql</li>
    <li>Executar python main.py para rodar o projeto </li>
</ul> 


## Passos para aprendizagem de máquina

Primeiro passo é o tratamento dos dados, por exemplo uma base dados com idade negativa, você que tratar isso, coisas q vc pode fazer
 - apagar o registro
 - substituir o dado por um valor válido
 - colocar como sendo a média dos outros atributos pode ser uma solução viável para este problema


## Link Codelab

https://colab.research.google.com/drive/1gEFE0Hvg4mvap78AUsgd-A80gDcKqTjq#scrollTo=BarTN4PJhgfW