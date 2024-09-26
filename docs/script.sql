# criando o banco
CREATE DATABASE saladamix;
# usando o banco
USE saladamix;
# criando  uma tabela
CREATE TABLE salada(
   id int primary key auto_increment,
   nome varchar(80) NOT NULL,
   ingredientes varchar(190) NOT NULL
);
SELECT * FROM salada;