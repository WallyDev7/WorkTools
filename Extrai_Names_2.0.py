'''

Esse script Python solicita ao usuário o nome de um arquivo GeoJSON de entrada e o nome de um arquivo de texto de saída.
Ele então extrai os valores da propriedade "name" de cada objeto de recurso no arquivo GeoJSON e os salva no arquivo de texto especificado pelo usuário.

'''

import json

# Função para extrair os valores de "name" do GeoJSON e salvá-los em um arquivo de texto
def extract_names_from_geojson(geojson_file, output_file):
    with open(geojson_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

        # Verifica se o GeoJSON é do tipo "FeatureCollection"
        if data['type'] != 'FeatureCollection':
            print("O GeoJSON fornecido não é um FeatureCollection.")
            return

        # Percorre os recursos (features) no GeoJSON
        names = []
        for feature in data['features']:
            # Verifica se a chave "name" está presente nas propriedades de cada recurso
            if 'name' in feature['properties']:
                names.append(feature['properties']['name'])

        # Escreve os names em um arquivo de texto
        with open(output_file, 'w') as output:
            for name in names:
                output.write(name + '\n')

if __name__ == "__main__":
    geojson_file = input("Por favor, insira o nome do arquivo GeoJSON de entrada (sem a extensão .geojson): ") + '.geojson'
    output_file = input("Por favor, insira o nome do arquivo de texto de saída (sem a extensão .txt): ") + '.txt'
    extract_names_from_geojson(geojson_file, output_file)
