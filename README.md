# Bula_facil

Descrição do Projeto: Sistema de Download de Bulas de Medicamentos

O projeto consiste em um script Python que realiza o download automático de bulas de medicamentos a partir de uma API pública. A API fornece informações sobre medicamentos, incluindo um identificador único para cada bula, que é usado para acessar e baixar o respectivo arquivo PDF da bula.

Funcionamento:

1. Pesquisa do Medicamento:
   - O usuário fornece o nome de um medicamento como entrada para o programa.
   - O script constrói uma URL com o nome do medicamento em letras minúsculas para consultar na API.

2. Obtenção do ID da Bula:
   - O script faz uma requisição GET para a API de bulas utilizando a URL construída.
   - Os dados são obtidos em formato JSON e o ID da primeira bula é extraído da resposta.

3. Download do PDF da Bula:
   - Com o ID da bula obtido, o script constrói uma nova URL para obter o PDF específico da bula.
   - Uma nova requisição GET é feita para essa URL e o conteúdo do PDF é baixado.

4. Armazenamento Local:
   - O PDF é salvo localmente no diretório de execução do script, com o nome do medicamento fornecido pelo usuário.

5. Tratamento de Erros:
   - O script inclui tratamento de exceções para lidar com problemas comuns, como erros de conexão, respostas JSON inválidas, ou erros HTTP durante as requisições.

Objetivo:

O objetivo do projeto é automatizar o processo de obtenção de bulas de medicamentos em formato PDF, facilitando o acesso e armazenamento local dessas informações para referência posterior.

Tecnologias Utilizadas:

- Python: Linguagem de programação utilizada para desenvolver o script.
- Requests: Biblioteca Python utilizada para fazer requisições HTTP.
- JSON: Formato utilizado para troca de dados com a API.
