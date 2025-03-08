Date: 2013-03-12
Title: Django com Postgres na AWS
Category: Web
Lang: pt-br
Tags: django, aws, postgres, python
Status: draft

Então você prefere o Postgres ao MySQL? Não? Talvês você devesse. Mas vamos ao que interessa, você quer saber como se configura o Postgres na AWS, certo?

Como configurar o Postgres na AWS
===

Vamos assumir que você já sabe como subir uma instância nova e fazer login
por SSH. Uma dica legal pra quem ainda não tem uma conta na AWS é quando você se cadastra você ganha free tier bla, bla (http://aws.amazon.com/free/).

Instalando o serviço
===

Para instalar o PostgreSQL voce precisa instalar o pacote postgresql-server usando o comando yum. para quem não conhece, o yum é o gerenciador de pacotes para distribuições baseadas no RedHat. A instalação é feita chamando o yum passando o parâmetro install e o nome do pacote, como é mostrado abaixo:

```bash
$ sudo yum install postgresql-server
```

O PostgreSQL ainda não está rodando, para isso é preciso inicializar o cluster de bancos http://www.postgresql.org/docs/8.4/static/app-initdb.html e iniciar a  o serviço chamando:

```bash
$ sudo service postgresql initdb
$ sudo service postgresql start
```

Agora o postgres deve estar rodando, para fazer o acesso você vai precisar chamar o comando psql, que é o cliente para linha de comando do Postgres como o usuário postgres que foi criado pela instalação. Abaixo está um truque para chamar um comando como um usuário diferente do seu sem precisar se tornar superusuário:

```bash
$ sudo su - postgres psql
```

Você deve ver um prompt como:

    psql>

Configuração de banco
===

criar um usuario novo

    psql> CREATE USER usuario_do_banco WITH PASSWORD '53nh453cr374';

criar o banco com esse usuário como owner

    psql> CREATE DATABASE meu_banco owner usuario_do_banco;


configurar o Postgres para aceitar login com senha (md5)

Editar /var/lib/pgsql9/data/pg_hba.conf, incluir a linha "host    all             tamboro         0.0.0.0/0               md5" (aceita conexão de qualquer IP para o usuário tamboro, autenticado por senha e reiniciar o serviço postgresql

testar local
---

    psql -U tamboro -W -h localhost ludz

testar remoto
---

instalar postgresql9 numa máquina de app
editar /var/lib/pgsql9/data/postgresql.conf na máquina de banco incluindo listen_addresses = '*' para escutar todos os ips
editar host    all             tamboro         0.0.0.0/0               md5

reiniciar o postgresql
---

```bash
$ sudo service postgresql restart
```

psql -U tamboro -W -h ludz

configure security group da AWS
===

Já que o Linux AMI é bem próximo ao RedHat (Decendente?) você pode usar essas instruções pra configurar o seu ambiente local RedHat, CentOS.

Uma outra forma de ter uma instância rodando Postgres é usando uma imagem pronta <https://aws.amazon.com/marketplace/pp/B008PFWGHC/ref=srh_res_product_title?ie=UTF8&sr=0-2&qid=1360969473850>


Configurando o seu projeto Django para usar o Postgres
===

settings.py

$ python manage.py syncdb
Migrando os seus dados do MySQL

dump sql compative
??ferramenta
specializada?dump fixture?

Migrando os seus dados do MySQL
===



<http://craigkerstiens.com/2013/02/13/How-I-Work-With-Postgres/>
