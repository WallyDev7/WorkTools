'''

O script Python a seguir realiza as seguintes tarefas:
Pega o valor da propriedade 'nome' e colocar em um arquivo txt

'''


import json


def extract_names_to_txt(geojson_file, output_txt):
    with open(geojson_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    names = []

    # Extrair os valores da propriedade 'name'
    for feature in data['features']:
        name = feature['properties'].get('name', None)
        if isinstance(name, str):
            names.append(name)

    # Escrever os valores extraídos em um arquivo de texto
    with open(output_txt, 'w', encoding='utf-8') as txt_file:
        for name in names:
            txt_file.write(str(name) + '\n')  # Garantindo que seja uma string


if __name__ == "__main__":
    geojson_file = 'Praia Grande.geojson'  # Altere para o caminho do seu arquivo GeoJSON
    output_txt = 'nomes.txt'  # Nome do arquivo de texto de saída
    extract_names_to_txt(geojson_file, output_txt)
