# Projeto To-Do List em Flask

Um simples aplicativo web de lista de tarefas (To-Do List) construído com Python e Flask.

## Sobre o Projeto

Este é um projeto de estudo para criar um CRUD (Create, Read, Update, Delete) básico. A aplicação permite que o usuário adicione novas tarefas, marque-as como concluídas e as remova da lista. Todos os dados são persistidos em um banco de dados SQLite.

##  Funcionalidades

* **Adicionar Tarefas:** Adicione novas tarefas à sua lista.
* **Concluir Tarefas:** Marque tarefas como "concluídas" com um clique.
* **Deletar Tarefas:** Remova tarefas que não são mais necessárias.
* **Feedback Visual:** Receba mensagens de sucesso ao concluir ou deletar uma tarefa.
* **Persistência de Dados:** As tarefas são salvas em um banco de dados `tasks.db`.

##  Tecnologias Utilizadas

* **Python:** Linguagem principal da aplicação.
* **Flask:** Micro-framework web para o backend.
* **Flask-SQLAlchemy:** Extensão para gerenciamento do banco de dados (SQLite).
* **HTML5:** Estrutura do site.
* **CSS3:** Estilização da interface.

##  Como Executar o Projeto Localmente

Siga os passos abaixo para rodar o projeto na sua máquina.

### Pré-requisitos

* [Python 3.7+](https://www.python.org/downloads/)
* [Git](https://git-scm.com/downloads)

### Passo a Passo

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/guigas1/Projeto_ToDoList-em-Flask.git](https://github.com/guigas1/Projeto_ToDoList-em-Flask.git)
    cd Projeto_ToDoList-em-Flask
    ```

2.  **Crie e ative um ambiente virtual:**
    * *No Linux/macOS:*
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    * *No Windows:*
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Instale as dependências:**
    (Primeiro, crie o arquivo `requirements.txt` listado abaixo na raiz do seu projeto)
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação:**
    ```bash
    python main.py
    ```

5.  **Acesse no navegador:**
    Abra seu navegador e acesse [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
