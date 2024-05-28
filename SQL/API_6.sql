create database API_6
use api_6;
SELECT * FROM rotas;

#Quantidade transportada por cada fabrica
SELECT `CO.Fabrica`, SUM(`Qtd.Transp`) AS QuantidadeTransp
FROM rotas
GROUP BY `CO.Fabrica`;

#Quantidade de CIF e FOB por fabrica
SELECT 
    `CO.Fabrica`,
    SUM(CASE WHEN Incoterm = 'FOB' THEN `Qtd.Transp` ELSE 0 END) AS Quantidade_FOB,
    SUM(CASE WHEN Incoterm = 'CIF' THEN `Qtd.Transp` ELSE 0 END) AS Quantidade_CIF
FROM 
    rotas
GROUP BY 
    `CO.Fabrica`;

#Valor do frete por mês em cada fabrica
SELECT 
    `CO.Fabrica`,
    CASE 
        WHEN `Mes.Base` = 1 THEN 'Janeiro'
        WHEN `Mes.Base` = 2 THEN 'Fevereiro'
        WHEN `Mes.Base` = 3 THEN 'Março'
        WHEN `Mes.Base` = 4 THEN 'Abril'
        WHEN `Mes.Base` = 5 THEN 'Maio'
        WHEN `Mes.Base` = 6 THEN 'Junho'
        WHEN `Mes.Base` = 7 THEN 'Julho'
        WHEN `Mes.Base` = 8 THEN 'Agosto'
        WHEN `Mes.Base` = 9 THEN 'Setembro'
        WHEN `Mes.Base` = 10 THEN 'Outubro'
        WHEN `Mes.Base` = 11 THEN 'Novembro'
        ELSE 'Dezembro'
    END AS Mes,
    SUM(`Vlr.Frete`) AS Valor_Frete
FROM 
    rotas
GROUP BY 
    `CO.Fabrica`, `Mes.Base`;

#Calculando a produtividade dos veiculos 
SELECT 
    Veiculo,
    AVG(Produtividade) AS Media_Produtividade
FROM 
    rotas
GROUP BY 
    Veiculo;

#Calculando produtividade de cada fabrica
SELECT 
    `CO.Fabrica`,
    SUM(`Qtd.Transp`) AS Quantidade_Transportada,
    CASE 
        WHEN `CO.Fabrica` = 3403208 THEN SUM(`Qtd.Transp`) / 90000000 * 100
        WHEN `CO.Fabrica` = 3423909 THEN SUM(`Qtd.Transp`) / 56000000 * 100
        WHEN `CO.Fabrica` = 3424402 THEN SUM(`Qtd.Transp`) / 90000000 * 100
        ELSE 0
    END AS Porcentagem_Capacidade_Utilizada
FROM 
    rotas
GROUP BY 
    `CO.Fabrica`;
    
    
#Lista de Cliente por Custo
SELECT `CO.Cliente`, SUM(rotas.`Vlr.Frete`) AS Custo_Total_Com_Frete
FROM rotas
WHERE `CO.Cliente` = '2345'
GROUP BY `CO.Cliente`;


SELECT `CO.Cliente`, SUM(rotas.`Vlr.Frete`) AS Custo_Total_Com_Frete
FROM rotas
GROUP BY `CO.Cliente`;


#Distância média por fabrica para cliente
SELECT `CO.Fabrica`, `CO.Cliente`, AVG(Nova_Dist) AS Distancia_Media_Percorrida
FROM rotas
GROUP BY `CO.Fabrica`, `CO.Cliente`;


#Custo por Km/fabrica
SELECT `CO.Fabrica`, AVG(`Frete/km`) AS Custo_por_Km_por_Fabrica
FROM rotas
GROUP BY `CO.Fabrica`;

#Custo por km de cada fabrica para cada cliente 
SELECT `CO.Fabrica`, `CO.Cliente`, AVG(`Frete/km`) AS Custo_por_Km_por_Fabrica_para_Cliente
FROM rotas
GROUP BY `CO.Fabrica`, `CO.Cliente`;

#Lista de Cliente por Quantidade Transportada
SELECT `CO.Cliente`, SUM(rotas.`Qtd.Transp`) AS Quantidade_Transportada
FROM rotas
WHERE `CO.Cliente` = '2345'
GROUP BY `CO.Cliente`;


SELECT `CO.Cliente`, SUM(rotas.`Qtd.Transp`) AS Quantidade_Transportada
FROM rotas
GROUP BY `CO.Cliente`;

#Frete médio por fabrica para cliente
#Frete/km
SELECT `CO.Fabrica`, `CO.Cliente`, AVG(`Frete/km`) AS Frete_médio_km
FROM rotas
GROUP BY `CO.Fabrica`, `CO.Cliente`;

#Frete/Quantidade
SELECT `CO.Fabrica`, `CO.Cliente`, AVG(`Frete/Qtd`) AS Frete_médio_km
FROM rotas
GROUP BY `CO.Fabrica`, `CO.Cliente`;








SELECT `CO.Cliente` FROM rotas;

SELECT DISTINCT `CO.Cliente`FROM rotas;



select * from rotas;

drop table rotas;

select count(`CO.Cliente`) from rotas;

