# 📦 Inventário Doméstico

[![GitHub release](https://img.shields.io/github/v/release/DevBernardoBarreto/Inventario_Domestico)](https://github.com/DevBernardoBarreto/Inventario_Domestico/releases/tag/v1.0.0)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)

O **Inventário Doméstico** é uma aplicação desktop desenvolvida em Python com interface gráfica (GUI) que permite registrar, visualizar e gerenciar seus bens pessoais de forma simples, organizada e com conversão de valores para Dólar em tempo real.

---

## 🚀 Como Executar o Projeto (Do Jeito Rápido - Sem instalar Python)

Se você deseja apenas testar ou utilizar o sistema sem precisar instalar o Python ou configurar códigos no seu computador, siga o passo a passo abaixo:

### 1. Baixar o pacote estável
Acesse a página de lançamentos e faça o download do arquivo compactado `.zip`:
👉 **[Baixar Inventário Doméstico v1.0.0 (GitHub Releases)](https://github.com/DevBernardoBarreto/Inventario_Domestico/releases/tag/v1.0.0)**

### 2. Extrair os arquivos
Após concluir o download, extraia o conteúdo do arquivo `.zip` para uma pasta de sua preferência (ex: Área de Trabalho). 
> ⚠️ **Importante:** Não execute o arquivo de dentro do arquivo zipado diretamente. É necessário extrair a pasta inteira para que o programa encontre o banco de dados e os ícones integrados.

### 3. Rodar a aplicação
1. Abra a pasta extraída.
2. Dê um duplo clique no arquivo **`main.exe`** (ou `main`).
3. Se o filtro *Windows SmartScreen* impedir a abertura inicial por ser um executável não assinado, basta clicar em **"Mais informações"** e depois em **"Executar assim mesmo"**.

---

## 💡 Problema Real

Muitas pessoas não possuem um controle estruturado de seus bens domésticos, como eletrônicos, móveis e objetos de valor. Isso pode gerar:
* Perda de informações importantes (como datas de compra e números de série)
* Dificuldade no controle financeiro geral
* Problemas ou dores de cabeça em casos de mudanças ou acionamento de seguros
* Falta de organização geral e controle do patrimônio pessoal

---

## ✨ Solução Proposta

A aplicação permite que o usuário registre seus itens com informações completas e visualize tudo em um único lugar estruturado. 

Além do cadastro convencional de campos detalhados, o sistema conta com cálculos inteligentes e automatizados em tempo real:
* 💰 **Valor Total dos Bens:** Soma instantânea de todos os itens cadastrados exibida em Reais (R$).
* 💵 **Cotação e Conversão Dinâmica:** Integração ativa com API para converter dinamicamente o valor total acumulado para Dólares (USD).
* 📦 **Quantidade Total de Itens:** Contagem automática do volume de itens sob sua gestão.

---

## 🎯 Público-Alvo

* Usuários domésticos e famílias em geral.
* Pessoas que buscam organizar seus bens pessoais de forma digital.
* Pessoas em fase de planejamento de mudança ou inventário de seguros.
* Qualquer usuário focado em manter um controle financeiro e patrimonial básico.

---

## ⚙️ Funcionalidades

* **Cadastro de Itens:** Registro detalhado com Nome do item, Local (sala/área), Descrição, Marca/modelo, Data da compra, Valor, Número de série e imagem associada.
* **Upload de Imagens:** Opção de carregar e visualizar fotos reais dos seus bens dentro do sistema.
* **Edição de Informações:** Atualização rápida de qualquer dado dos itens salvos.
* **Remoção de Registros:** Exclusão fácil de bens que foram vendidos ou descartados.
* **Listagem Completa (Tabela):** Visualização geral de todos os bens cadastrados com busca dinâmica.
* **Monitoramento de Cotação:** Conversão de valores integrada ao mercado de moedas.

---

## 🛠 Tecnologias Utilizadas

* **Python** (Linguagem base)
* **Tkinter** (Interface Gráfica Nativa)
* **SQLite** (Banco de dados local e leve)
* **Pillow** (Processamento de imagem e ícones)
* **tkcalendar** (Seletor visual de datas)
* **Requests** (Consumo da API de Cotação de Moedas - AwesomeAPI)
* **PyInstaller** (Empacotamento do executável final para Windows)

---

## 📂 Estrutura do Projeto
