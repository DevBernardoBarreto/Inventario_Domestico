# 📦 Inventário Doméstico

![GitHub release](https://img.shields.io/github/v/release/DevBernardoBarreto/Inventario_Domestico)
![Python Version](https://img.shields.io/badge/python-3.11-blue)
![CI](https://github.com/DevBernardoBarreto/Inventario_Domestico/actions/workflows/ci.yml/badge.svg)

O Inventário Doméstico é uma aplicação desktop desenvolvida em Python com interface gráfica (GUI) que permite registrar, visualizar e gerenciar seus bens pessoais de forma simples, organizada e com conversão de valores para Dólar em tempo real.

---

## 👥 Integrantes do Grupo

| Nome | Matrícula |
|------|-----------|
| Bernardo Barreto | 22509877 |
| Fernando Henrique Silva de Carvalho | 22505938 |
| Vinicius Alves da Costa Silva | 22508475 |

---

## 🚀 Como Executar o Projeto (Do Jeito Rápido - Sem instalar Python)

Se você deseja apenas testar ou utilizar o sistema sem precisar instalar o Python ou configurar códigos no seu computador, siga o passo a passo abaixo:

### 1. Baixar o pacote estável
Acesse a página de lançamentos e faça o download do arquivo compactado `.zip`:
👉 [Baixar Inventário Doméstico v1.0.0 (GitHub Releases)](https://github.com/DevBernardoBarreto/Inventario_Domestico/releases)

### 2. Extrair os arquivos
Após concluir o download, extraia o conteúdo do arquivo `.zip` para uma pasta de sua preferência (ex: Área de Trabalho).

> ⚠️ **Importante:** Não execute o arquivo de dentro do arquivo zipado diretamente. É necessário extrair a pasta inteira para que o programa encontre o banco de dados e os ícones integrados.

### 3. Rodar a aplicação
- Abra a pasta extraída.
- Dê um duplo clique no arquivo `main.exe` (ou `main`).
- Se o filtro Windows SmartScreen impedir a abertura inicial por ser um executável não assinado, basta clicar em "Mais informações" e depois em "Executar assim mesmo".

---

## 🖥️ Como Executar Localmente (Com Python)

### Pré-requisitos
- Python 3.11+
- Conta no [Supabase](https://supabase.com) com as variáveis de ambiente configuradas

### Instalação

```bash
# Clone o repositório
git clone https://github.com/DevBernardoBarreto/Inventario_Domestico.git
cd Inventario_Domestico

# Instale as dependências
pip install -r requirements.txt
```

### Variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto com:

```
SUPABASE_URL=sua_url_aqui
SUPABASE_KEY=sua_chave_aqui
```

### Executar
```bash
python main.py
```

### Rodar os testes
```bash
python -m unittest discover -p "test_*.py"
```

---

## 💡 Problema Real

Muitas pessoas não possuem um controle estruturado de seus bens domésticos, como eletrônicos, móveis e objetos de valor. Isso pode gerar:

- Perda de informações importantes (como datas de compra e números de série)
- Dificuldade no controle financeiro geral
- Problemas ou dores de cabeça em casos de mudanças ou acionamento de seguros
- Falta de organização geral e controle do patrimônio pessoal

---

## ✨ Solução Proposta

A aplicação permite que o usuário registre seus itens com informações completas e visualize tudo em um único lugar estruturado.

Além do cadastro convencional de campos detalhados, o sistema conta com cálculos inteligentes e automatizados em tempo real:

- 💰 **Valor Total dos Bens:** Soma instantânea de todos os itens cadastrados exibida em Reais (R$).
- 💵 **Cotação e Conversão Dinâmica:** Integração ativa com API para converter dinamicamente o valor total acumulado para Dólares (USD).
- 📦 **Quantidade Total de Itens:** Contagem automática do volume de itens sob sua gestão.

---

## 🎯 Público-Alvo

- Usuários domésticos e famílias em geral.
- Pessoas que buscam organizar seus bens pessoais de forma digital.
- Pessoas em fase de planejamento de mudança ou inventário de seguros.
- Qualquer usuário focado em manter um controle financeiro e patrimonial básico.

---

## ⚙️ Funcionalidades

- **Cadastro de Itens:** Registro detalhado com Nome do item, Local (sala/área), Descrição, Marca/modelo, Data da compra, Valor, Número de série e imagem associada.
- **Upload de Imagens:** Opção de carregar e visualizar fotos reais dos seus bens dentro do sistema.
- **Edição de Informações:** Atualização rápida de qualquer dado dos itens salvos.
- **Remoção de Registros:** Exclusão fácil de bens que foram vendidos ou descartados.
- **Listagem Completa (Tabela):** Visualização geral de todos os bens cadastrados com busca dinâmica.
- **Monitoramento de Cotação:** Conversão de valores integrada ao mercado de moedas.

---

## 🛠 Tecnologias Utilizadas

| Tecnologia | Uso |
|------------|-----|
| Python 3.11 | Linguagem base |
| Tkinter | Interface Gráfica Nativa |
| Supabase (PostgreSQL) | Banco de dados em nuvem |
| SQLite | Banco de dados local auxiliar |
| Pillow | Processamento de imagem e ícones |
| tkcalendar | Seletor visual de datas |
| Requests | Consumo da API de Cotação (AwesomeAPI) |
| PyInstaller | Empacotamento do executável para Windows |
| GitHub Actions | Pipeline de CI/CD |

---

## ✅ Melhorias adicionadas nesta versão

- Integração com Supabase (PostgreSQL) para persistência em nuvem
- Pipeline de CI/CD com GitHub Actions rodando testes automaticamente
- Testes de integração (`test_integration.py`)
- Validação do campo Valor da compra, aceitando formato brasileiro como `1500,00`
- Correção para evitar erro quando o usuário cancela a escolha da imagem
- Correção no botão Atualizar, evitando travamento quando nenhum item está selecionado
- Confirmação antes de deletar um item
- Botão Limpar para limpar os campos da tela
- Campo Buscar item para filtrar os itens cadastrados
- Botão Exportar CSV para gerar relatório do inventário
- Correção nas funções de exclusão e consulta por ID no Supabase
- Arquivo `requirements.txt` em UTF-8 para facilitar a instalação das dependências
