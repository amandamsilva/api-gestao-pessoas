# api-gestao-pessoas
# Desafio Tech Labs

Aplicação web construída usando Django e Django Rest Framework para gerenciar e armazenar informações sobre pessoas. Esta aplicação fornece uma API RESTful para realizar operações de CRUD em objetos Pessoa.

### Pré-requisitos

- Python 3.x
- Django
- Django Rest Framework

### Instalação

1. Clone o repositório em sua máquina local:

   ```bash
   git clone https://github.com/amandamsilva/api-gestao-pessoas.git

2. Abra o Prompt de Comando e navegue até o diretório do projeto

   cd projeto_gestao

3. Crie e ative um ambiente virtual (opcional):

   python -m venv venv

   venv\Scripts\activate

4. Instalações necessárias:

   pip install django
   pip install djangorestframework

5. Aplique as migrações de banco de dados:

   python manage.py migrate

6. Inicialize o servidor:

   python manage.py runserver


Uso

    Crie uma Nova Pessoa: Use uma ferramenta como Postman ou curl para enviar uma solicitação POST para http://127.0.0.1:8000/pessoas/ com os dados para um novo objeto Pessoa.
   Exemplo:
{
  "nome_completo": "Maria",
  "data_nascimento": "1990-01-15",
  "endereco": "Avenida Brasil",
  "cpf": "12345678901",
  "estado_civil": "solteiro"
}
 
    Listar Objetos Pessoa: Abra seu navegador e visite http://127.0.0.1:8000/pessoas/ para listar todos os objetos Pessoa.

    Visualizar uma Pessoa Específica: Visite http://127.0.0.1:8000/pessoas/<int:id>/ no seu navegador para visualizar detalhes de um objeto Pessoa específico (substitua <int:id> pelo ID real).

    Atualizar uma Pessoa: Use uma ferramenta como Postman ou curl para enviar uma solicitação PUT para http://127.0.0.1:8000/pessoas/<int:id>/ com os dados atualizados para um objeto Pessoa específico.

    Excluir uma Pessoa: Use uma ferramenta como Postman ou curl para enviar uma solicitação DELETE para http://127.0.0.1:8000/pessoas/<int:id>/ para excluir um objeto Pessoa específico.
