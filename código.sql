INSERT INTO `cliente`(`nome`,`cpf`,`telefone`) 
VALUES ('João da Silva','111.111.111-11','48991234567'), 
       ('Maria Oliveira','222.222.222-22','48997654321');

INSERT INTO `empregado`(`nome`,`cpf`,`cargo`)
VALUES ('Carlos Pereira','333.333.333-33','Analista de Sistemas'),
       ('Ana Souza','444.444.444-44','Gerente de Projetos');

INSERT INTO `projeto` (`nome`,`descricao`,`preco`,`dtFim`,`dtEstimada`,`dtSolicitacao`,`CpfGerente`,`CpfCliente`) 
VALUES('Sistema de Vendas','Plataforma para e-commerce','15000.00','2025-12-01','2025-11-15','2025-09-10','444.444.444-44','111.111.111-11'), 
      ('Aplicativo Financeiro','Gestão de despesas pessoais','12000.00','2025-10-30','2025-10-20','2025-09-12','444.444.444-44','222.222.222-22');

INSERT INTO `projEmp`(`cpfEmpregado`,`codProj`,`hrTrab`) 
VALUES ('333.333.333-33','1','40'), 
       ('444.444.444-44','1','20'), 
       ('444.444.444-44','2','35');

INSERT INTO `cliente`(`nome`,`cpf`,`telefone`) 
VALUES ('Pedro Gomes','555.555.555-55','48999887766'), 
       ('Fernanda Lima','777.777.777-77','48991231231');

INSERT INTO `empregado`(`nome`,`cpf`,`cargo`) 
VALUES ('Lucas Andrade','666.666.666-66','Desenvolvedor Backend');

INSERT INTO `projeto` (`nome`,`descricao`,`preco`,`dtFim`,`dtEstimada`,`dtSolicitacao`,`cpfGerente`,`cpfCliente`)
VALUES ('Site Institucional', 'Página para empresa local', '5000', '2025-11-01','2025-10-25','2025-09-20','444.444.444-44', '555.555.555-55'),
       ('Controle de Estoque', 'Sistema para loja de roupas','8000','2025-12-20','2025-12-05', '2025-09-25', '444.444.444-44','777.777.777-77');
       
INSERT INTO `projEmp`(`cpfEmpregado`,`codProj`,`hrTrab`)
VALUES ('666.666.666-66','3','50');





