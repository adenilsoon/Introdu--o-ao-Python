-- Exclusão de Tabela
DROP TABLE atendimento;
DROP TABLE animal;
drop TABLE veterinario;
DROP TABLE especialidade;
DROP TABLE cliente;

-- Criação das Tabelas

create TABLE especialidade (
  idEspecialidade serial PRIMARY KEY not NULL,
  descricaoEspecialidade VARCHAR(30) not NULL UNIQUE
);

create table cliente (
  idCliente serial PRIMARY KEY not NULL,
  nomeCliente VARCHAR(15) not NULL,
  sobrenomeCliente VARCHAR(15) not NULL,
  telefoneCliente VARCHAR(15) not NULL,
  emailCliente VARCHAR(40) unique not NULL
);

create TABLE veterinario (
  idVet serial PRIMARY KEY not NULL,
  nomeVet VARCHAR(15) not NULL,
  sobrenomeVet VARCHAR(15) not NULL,
  crmvVet VARCHAR(10) not NULL UNIQUE,
  fkIdEspecialidade INT not NULL,
  CONSTRAINT fkEspecialidade FOREIGN KEY (fkIdEspecialidade) REFERENCES especialidade(idEspecialidade)
);

create table animal (
  idAnimal serial PRIMARY KEY NOT NULL,
  nomeAnimal VARCHAR(15) NOT NULL,
  dtNascAnimal DATE,
  especieAnimal VARCHAR(30) NOT NULL,
  racaAnimal VARCHAR(20) NOT NULL,
  generoAnimal VARCHAR(5) not NULL,
  fkIdCliente INT not NULL,
  CONSTRAINT fkCliente FOREIGN KEY (fkIdCliente) REFERENCES cliente(idCliente)
);

CREATE TABLE atendimento (
  idAtend serial PRIMARY KEY NOT NULL,
  dtAtend DATE,
  fkIdVet INT not NULL,
  fkIdAnimal INT not NULL,
  constraint fkVet FOREIGN key (fkIdVet) REFERENCES veterinario(idVet),
  CONSTRAINT fkAnimal FOREIGN KEY (fkIdAnimal) REFERENCES animal(idAnimal)
);

-- Populando as Tabelas

INSERT into especialidade (descricaoespecialidade) VALUES
    ('Cirurgia'),
    ('Dermatologia'), 
    ('Endocrinologia'), 
    ('Cardiologia');

INSERT into veterinario (nomeVet, sobrenomeVet, crmvVet, fkIdEspecialidade) VALUES
    ('Larissa', 'Barbosa', 'SP-67475',1),
    ('Giulia', 'Carneiro', 'SP-53104',1),
    ('Livia', 'Moraes', 'SP-53687',2), 
    ('Danilo', 'Biscaro', 'SP-49753',3), 
    ('Felipe', 'Santos', 'SP-35968',4);

insert into cliente (nomeCliente, sobrenomeCliente, telefoneCliente, emailCliente) VALUES 
    ('Daniela', 'Amorim', '(11) 98221-9132', 'daniela_amorim@gmail.com'),
    ('Veronica', 'Martins', '(11) 97234-9633', 'ver.martins@yahoo.com'),
    ('Tamara', 'Costa', '(11) 98248-9634', 'costa.tamara@gmail.com'),
    ('Geovana', 'Ricci', '(11) 98242-9235', 'geovana.ricci@gmail.com'),
    ('Ariadny', 'Ricci', '(11) 97521-9636', 'ricci.ariadny@gmail.com'), 
    ('Mariana', 'Brito', '(11) 98698-9337', 'mariana.brito@uol.com'), 
    ('Thiago', 'Alves', '(11) 97657-9638', 'thiago.alves@gmail.com'), 
    ('Juliana', 'Mendes', '(11) 98637-9439', 'juliana_mendes@gmail.com'),
    ('Bernardo', 'Pereira', '(11) 99723-9640', 'bernardopereira@gmail.com'),
    ('Angelica', 'Oliveira', '(11) 98759-9541', 'oliveira.angel@gmail.com'),
    ('Gabriel', 'Almeida', '(11) 98789-9642', 'gab.almeida@hotmail.com'),
    ('Ricardo', 'Bueno', '(11) 99826-9643', 'bueno_ricardo@gmail.com'),
    ('Fabio', 'Coutinho', '(11) 97893-9744', 'fabio.coutinho@gmail.com'),
    ('Karina', 'Dias', '(11) 98812-9845', 'karina_dias@gmail.com'),
    ('Camila', 'Nascimento', '(11) 97937-9946', 'camila.nasc@gmail.com');
    
insert into animal (nomeAnimal, dtNascAnimal, especieAnimal, racaAnimal, generoAnimal,fkIdCliente) VALUES
    ('Floki', '2022/01/17', 'Cachorro',  'Shiba Inu', 'Macho', 5),
	('Nala', '2022/02/14', 'Cachorro',  'Shiba Inu', 'Macho', 2),
    ('Noel', '2023/04/15', 'Cachorro',  'Bassenji', 'Macho', 6), 
    ('Julie', '2018/09/10', 'Cachorro',  'Poodle', 'Macho', 9), 
    ('Toddy', '2021/07/22', 'Cachorro',  'Pinscher', 'Macho', 9), 
    ('Princesa', '2017/06/10', 'Gato',  'Siames', 'Macho', 10), 
    ('Luck', '2023/02/11', 'Cachorro',  'Akita', 'Macho', 11), 
    ('Bob', '2020/09/04', 'Cachorro',  'Yorkshire', 'Macho', 12),
    ('Amora', '2021/11/13', 'Gato',  'Persa', 'Macho', 10), 
    ('Belinha', '2021/04/19', 'Cachorro',  'Dachshund', 'Macho', 12), 
    ('Duke', '2020/08/27', 'Cachorro',  'Beagle', 'Macho', 13), 
    ('Romeu', '2021/07/05', 'Gato',  'Persa', 'Macho', 8), 
    ('Bella', '2022/10/10', 'Cachorro',  'Poodle', 'Macho', 15), 
    ('Nala', '2022/08/25', 'Cachorro',  'Yorkshire', 'Macho', 13),
    ('Kiara', '2020/04/28', 'Gato',  'Persa', 'Macho', 8), 
    ('Bob', '2023/03/05', 'Cachorro',  'Golden', 'Macho', 7), 
    ('Zara', '2021/08/20', 'Gato',  'Siames', 'Macho', 14),  
    ('Belinha', '2017/03/15', 'Cachorro',  'Golden', 'Macho', 7),  
    ('Kiara', '2016/05/30', 'Cachorro',  'Spitz', 'Macho', 3),  
    ('Max', '2020/07/26', 'Cachorro',  'Spitz', 'Macho', 3),  
    ('Chloe', '2018/11/07', 'Cachorro',  'Spitz', 'Macho', 4);  
 
insert into atendimento (dtAtend, fkIdVet, fkIdAnimal) VALUES
	('2024/01/05', 2, 9),
    ('2024/01/19', 1, 17),
    ('2024/02/02', 2, 2), 
    ('2024/02/16', 3, 16), 
    ('2024/02/23', 4, 11), 
    ('2024/03/01', 5, 3), 
    ('2024/03/15', 1, 18), 
    ('2024/03/22', 2, 5), 
    ('2024/04/12', 3, 1), 
    ('2024/04/26', 4, 19), 
    ('2024/05/03', 5, 12),
    ('2024/05/17', 5, 6), 
    ('2024/05/24', 4, 21), 
    ('2024/06/14', 3, 13), 
    ('2024/06/21', 2, 4), 
    ('2024/07/12', 1, 10), 
    ('2024/07/19', 1, 7), 
    ('2024/07/26', 2, 14), 
    ('2024/08/02', 3, 20), 
    ('2024/08/16', 4, 15), 
    ('2024/08/23', 5, 8);

-- Consultas SQL

-- Consulta simples na table atendimento / table cliente / table animal / table epsecialidade / table veterinario

SELECT * from cliente;
SELECT * from animal;
SELECT * from especialidade;
SELECT * from veterinario;
SELECT * FROM atendimento;

-- Consulta com mais de uma table - Pesquisando pelo ID do atributo número de atendimento
SELECT atend.idatend as "Nro Atendimento", to_char(atend.dtatend, 'DD/MM/YYYY') as "Data",
		cli.idcliente as "Código Cliente", CONCAT(cli.nomecliente,' ',cli.sobrenomecliente) as "Nome Completo",
		an.generoanimal as "Genero",an.racaanimal as "Raça",an.nomeanimal as "Pet",
        vet.crmvvet as "CRMV",CONCAT(vet.nomevet,' ',vet.sobrenomevet) as "Nome Completo", esp.descricaoespecialidade as "Especialidade"
from atendimento atend
INNER JOIN veterinario vet
ON atend.fkidvet = vet.idvet
INNER JOIN animal an
ON atend.fkidanimal = an.idanimal
INNER JOIN cliente cli
ON an.fkidcliente = cli.idcliente
INNER JOIN especialidade esp
ON vet.fkidespecialidade = esp.idespecialidade
WHERE atend.idatend = 5;

-- Consultando por odem de Data e consulta por um intervalo especifico
SELECT atend.idatend as "Nro Atendimento",to_char(atend.dtatend, 'DD/MM/YYYY') as "Data",
		cli.idcliente as "Código Cliente", CONCAT(cli.nomecliente,' ',cli.sobrenomecliente) as "Cliente",
		an.generoanimal as "Genero",an.racaanimal as "Raça",an.nomeanimal as "Pet",
        vet.crmvvet as "CRMV", CONCAT(vet.nomevet,' ',vet.sobrenomevet) as "Veterinário", esp.descricaoespecialidade as "Especialidade"
from atendimento atend
INNER JOIN veterinario vet
ON atend.fkidvet = vet.idvet
INNER JOIN animal an
ON atend.fkidanimal = an.idanimal
INNER JOIN cliente cli
ON an.fkidcliente = cli.idcliente
INNER JOIN especialidade esp
ON vet.fkidespecialidade = esp.idespecialidade
WHERE atend.dtatend BETWEEN '2024-02-16' and  '2024-07-19'
ORDER by atend.dtatend;

-- Consultando a Quantidade de Animais que cada cliente possui:
SELECT cliente.idcliente as "Código Cliente", CONCAT(cliente.nomecliente,' ',cliente.sobrenomecliente) as "Cliente", COUNT(animal.idanimal) as "QTD de Animais"
FROM animal
JOIN cliente ON animal.fkidcliente = cliente.idcliente
GROUP BY cliente.idcliente
ORDER BY cliente.nomecliente;

-- Quantidade de Animais que um Cliente especifico possuí:
SELECT CONCAT(cliente.nomecliente,' ',cliente.sobrenomecliente) as "Cliente", COUNT(fkidcliente) as "QTD_Animais"
FROM animal
INNER JOIN cliente
ON animal.fkidcliente = cliente.idcliente
WHERE cliente.idcliente=13
GROUP BY cliente.idcliente;

-- Quantidade de Atendimento que cada Veterinario realizou:
SELECT  veterinario.crmvvet as "CRMV", CONCAT(veterinario.nomevet,' ',veterinario.sobrenomevet) AS "Veterinário", COUNT(atendimento.idatend) as "Qtd de Atendimento" 
FROM atendimento
JOIN veterinario ON atendimento.fkidvet = veterinario.idvet
GROUP BY veterinario.idvet
ORDER BY veterinario.nomevet;