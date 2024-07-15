from requests import get
from requests.exceptions import RequestException, JSONDecodeError


def main(medicamento):
    # Constrói a URL para pesquisar o medicamento na API de bulas
    url = f'https://bula.vercel.app/pesquisar?nome={medicamento.lower()}&pagina=1'

    try:
        for attempt in range(10):  # Loop para tentar até 10 vezes
            try:
                # Faz a requisição para obter os dados da API de bulas
                response = get(url)
                response.raise_for_status()  # Lança um erro se a resposta não for bem-sucedida
                data = response.json()  # Converte a resposta JSON para um dicionário Python

                # Obtém o ID da primeira bula encontrada
                id = data['content'][0]['idBulaPacienteProtegido']
                # Monta a URL para baixar o PDF da bula usando o ID obtido
                url_pdf = f"https://bula.vercel.app/bula?id={id}"

                # Faz a requisição para obter o JSON que contém a URL do PDF
                response = get(url_pdf)
                url_pdf = response.json()['pdf']  # Extrai a URL do PDF da resposta JSON

                # Faz a requisição para baixar o PDF da bula
                response = get(url_pdf)
                if( 'error' not in response) or ('erro' not in response):
                    print(f'Para Ddowload: {url_pdf}')
                    # Salva o PDF no diretório local com o nome do medicamento
                    with open(f'{medicamento}.pdf', 'wb') as f:
                        f.write(response.content)
                    # Se tudo ocorreu bem, interrompe o loop
                    break

            except JSONDecodeError:
                print("Erro ao decodificar resposta JSON")

    except (RequestException, IndexError) as e:
        # Captura e exibe qualquer erro de requisição que ocorrer
        print(f"Erro na requisição: {e}")


if __name__ == '__main__':
    r = str(input("Digite o nome do medicamento: ")).strip()
    print(f'Buscando por: {r.title()}')
    main(r)
