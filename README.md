Resolução do problema do de corte de estoque unidimensional, que consiste otimizar a utilização de matérias-primas (itens grandes e de tamanho fixo)
para a produção de itens menores de comprimento e demanda variável. 

<p align="center">
  <img
    width="585"
    height="775"
    alt="visão_geral"
    src="https://github.com/user-attachments/assets/37df33f9-91bc-44eb-8d0c-bc0e2719d229"
  />
</p>

<br> A solução proposta pode ser utilizada para otimizar produção de barras, tubos, perfis, bobinas e quaisquer outras materiais que serão produzidos a partir
de um corte unidimensional.
<br> Utilizou-se o solver de acesso livre CBC, para resolução do método simplex, aplicou-se a abordagem de geração de colunas para sistematizar a geração dos padrões de corte,
e para evitar sobredemanda, aplicou-se a heurística residual "NOVA" prosposta por POLDI(2003), além de heurística gulosa.
<br> Maiores explicações encontram-se no documento alocado neste mesmo repositório, denominado "PROBLEMA_DO_CORTE_DE_ESTOQUE_COM_GERAÇÃO_DE_COLUNAS".
<br> Abaixo seguem alguns prints, que apresentam uma visão geral do funcionamento do algoritmo, um arquivo completo denominado "Exemplo", está alocado neste mesmo repositório.
# Exemplo de preenchimento de planilha com dados de entrada</center>

<p align="center">
  <img
    width="585"
    height="775"
    alt="visão_geral"
    src="https://github.com/user-attachments/assets/d1b1063a-2434-4228-ac37-34f7e328de93"
  />
</p>

# Exemplo primeira página da ordem de produção
<p align="center">
  <img
    width="585"
    height="775"
    alt="visão_geral"
    src="https://github.com/user-attachments/assets/1124231b-948f-4997-9a4e-cafe1b86fd4f"
  />
</p>

# Exemplo de padrão de corte gerado</center>

<p align="center">
  <img
    width="585"
    height="775"
    alt="visão_geral"
    src="https://github.com/user-attachments/assets/95836292-7d1d-4809-9d5a-ecbb118a5dd1"
  />
</p>
