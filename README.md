## Scraping de dados a partir de uma API dentro do prórpio site :snake:
 -----
 1 - Abrir o site onde deseja coletar as informações:
 Exemplo: [AFL](https://api.afl.com.au/cfs/afl/wagering?application=Web)

 2 - Clicar em inspensionar elemento

 3 - Clicar em Networking ou Rede

 4 - Clicar em XHR

 5 - Atualiar a página novamente e observar os requests realizados

 6 - Você verá que o type do request será de um arquivo json, esse arquivo
  tem todas as informações necessárias para se ter acesso a API, Header e token e etc.

 7 - Copiar o cURL

 8 - Abrir o Postman e clicar em importar

 9 - Na tela de importação selecionar Raw Text

 10 - Clicar em continuar e import

 11 - Após isso você pode fazer um teste de GET para visualizar as informações
  retonadas
  
 12 - Clicar em code e selecionar a linguagem que desejar importar esse código
 
 13 - Usar os dados para seus insights :smile:
