Resolução do problema do de corte de estoque unidimensional, que consiste otimizar a utilização de matérias-primas (itens grandes e de tamanho fixo)
para a produção de itens menores de comprimento e demanda variável. 
<br> A solução proposta pode ser utilizada para otimizar produção de barras, tubos, perfis, bobinas e quaisquer outras materiais que serão produzidos a partir
de um corte unidimensional.
<br> Utilizou-se o solver de acesso livre CBC, para resolução do método simplex, aplicou-se a abordagem de geração de colunas para sistematizar a geração dos padrões de corte,
e para evitar sobredemanda, aplicou-se a heurística residual "NOVA" prosposta por POLDI(2003), além de heurística gulosa.
<br> Maiores explicações encontram-se no documento alocado neste mesmo repositório, denominado "PROBLEMA_DO_CORTE_DE_ESTOQUE_COM_GERAÇÃO_DE_COLUNAS".
