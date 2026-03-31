#  Inventário Doméstico

##  Descrição do Projeto

O **Inventário Doméstico** é uma aplicação desktop desenvolvida em Python com interface gráfica (GUI), que permite ao usuário registrar, visualizar e gerenciar seus bens pessoais de forma simples e organizada.

O sistema foi criado com o objetivo de ajudar pessoas a manterem controle sobre seus objetos domésticos, evitando perda de informações e facilitando o controle financeiro.

---

##  Problema Real

Muitas pessoas não possuem um controle estruturado de seus bens domésticos, como eletrônicos, móveis e objetos de valor. Isso pode gerar:

* Perda de informações importantes
* Dificuldade no controle financeiro
* Problemas em mudanças ou seguros
* Falta de organização geral

---

## 💡 Solução Proposta

A aplicação permite que o usuário registre seus itens com informações completas e visualize tudo em um único lugar, incluindo:

* Nome do item
* Local (sala/área)
* Descrição
* Marca/modelo
* Data da compra
* Valor
* Número de série
* Imagem do item

Além disso, o sistema calcula automaticamente:

* 💰 Valor total dos bens
* 📦 Quantidade total de itens

---

## 🎯 Público-Alvo

* Usuários domésticos
* Famílias
* Pessoas que desejam organizar seus bens
* Quem quer ter controle financeiro básico

---

## ⚙️ Funcionalidades

* Cadastro de itens
* Edição de informações
* Remoção de registros
* Upload e visualização de imagens
* Listagem completa dos itens
* Cálculo automático do valor total
* Contagem automática de itens

---

## 🛠 Tecnologias Utilizadas

* Python
* Tkinter (interface gráfica)
* SQLite (banco de dados local)
* Pillow (manipulação de imagens)
* tkcalendar (seleção de datas)

---

## 📂 Estrutura do Projeto

```
inventario-domestico/
│
├── main.py          # Interface gráfica
├── view.py          # Lógica CRUD
├── banco.py         # Criação do banco de dados
├── dados.db         # Banco SQLite (gerado automaticamente)
└── README.md
```

---

##  Como Executar o Projeto

###  Pré-requisitos

Antes de começar, você precisa ter instalado:

* Python 3.10 ou superior

---

### 📥 1. Clonar o repositório

```bash
git clone https://github.com/DevBernardoBarreto/Inventario_Domestico.git
```

---

###  2. Acessar a pasta do projeto

```bash
cd inventario-domestico
```

---

###  3. Instalar as dependências

```bash
pip install pillow tkcalendar
```

---

###  4. Criar o banco de dados

Execute o arquivo abaixo **apenas uma vez**:

```bash
python banco.py
```

Isso irá criar o banco `dados.db`.

---

### ▶ 5. Executar a aplicação

```bash
python main.py
```

---

##  Como testar o sistema manualmente

Após abrir a aplicação:

1. Preencha os campos do formulário
2. Clique em **Inserir**
3. Veja o item aparecer na tabela
4. Teste:

   * Atualizar
   * Deletar
   * Visualizar imagem

---

## 📦 Versão

```
1.0.0
```

---

## 🔮 Melhorias Futuras

* Exportação de dados em PDF
* Sistema de login
* Dashboard com gráficos
* Backup automático

---

## 👨‍💻 Autor

**Bernardo Santana Barreto**
🔗 LinkedIn: https://www.linkedin.com/in/bernardo-barreto-aa1a20364/

---

## 🔗 Repositório


```
https://github.com/DevBernardoBarreto/Inventario_Domestico.git
```
