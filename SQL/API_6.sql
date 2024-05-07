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