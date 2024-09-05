create table aluno (
	id SERIAL PRIMARY key,
  	nome VARCHAR(30) UNIQUE,
  	cpf INT(13) NOT NULL,
 	email VARCHAR(20),
  	endereco VARCHAR(30)
)