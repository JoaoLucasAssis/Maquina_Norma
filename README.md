# Projeto de Execução de Instruções (Máquina Norma)

Este projeto consiste em um programa Python para executar uma série de instruções em uma Máquina Norma, implementada com 8 registradores (A, B, C, D, E, F, G, H).

A máquina lê instruções rotuladas de programas monolíticos e retorna uma saída com os valores de cada registrador inicializado a cada instrução até o fim da execução.

O projeto é uma atividade acadêmica da disciplina Teoria da Computação na Universidade Vila Velha.

### Descrição da Máquina Norma

A Máquina Norma implementada neste projeto possui as seguintes características:

#### Operações Disponíveis:

* `add_one`: incrementa em uma unidade um determinado registrador.
* `sub_one`: decrementa em uma unidade um determinado registrador.
* `is_zero`: testa se um determinado registrador contém o valor zero.
  
#### Registradores:

* A, B, C, D, E, F, G, H.

### Como Usar

Para utilizar o programa, siga estas etapas:

* Coloque as instruções desejadas no arquivo ***input.txt***, seguindo o formato descrito abaixo.

* Execute o arquivo ``main.py`. Isso executará as instruções e gerará o arquivo ***output.txt*** com os resultados.

O arquivo ***output.txt*** conterá os valores finais dos registradores após a execução das instruções.

## Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## Instalação
<details>
<summary>Clique aqui!</summary>
<p>

### Pré-requisitos para instalação!

![Git](https://img.shields.io/badge/Git-E34F26?style=for-the-badge&logo=git&logoColor=white)
--------------------------------------------------------------------------------------------

Para começar, clone o repositório do projeto em seu ambiente local. Siga a etapa abaixo:

* Abra o terminal na pasta onde deseja clonar o repositório.

* Clone o repositório para o seu ambiente local usando o seguinte comando:

```git
git clone https://github.com/JoaoLucasAssis/Maquina_Norma.git
```

> :warning: obs: Certifique-se de ter o git instalado antes de executar o comando no terminal

* Navegue até o diretório do projeto e execute o seguinte comando para rodar o programa:

```python
python .\src\main.py
```

Se tudo estiver correto, o arquivo `output.txt` será criado.
</p>
</details>