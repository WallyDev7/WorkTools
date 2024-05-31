'''

Este script Python foi criado para realizar a extração dos valores de "name" de um arquivo GeoJSON e armazená-los em um arquivo de texto.
Primeiramente, é verificado se o GeoJSON fornecido é do tipo "FeatureCollection".
Em seguida, o script percorre os recursos (features) presentes no GeoJSON e verifica se a chave "name" está presente nas propriedades de cada recurso.
Se estiver, o valor correspondente é adicionado a uma lista.
Por fim, os valores da lista são escritos em um arquivo de texto.

'''



import json

# Função para extrair os valores de "name" do GeoJSON e salvá-los em um arquivo de texto
def extract_names_from_geojson(geojson_file, output_file):
    with open(geojson_file, 'r') as f:
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

# Chamada da função para extrair os IDs e salvar em um arquivo de texto
extract_names_from_geojson('Red Layer - Contagem.geojson', 'names.txt')
