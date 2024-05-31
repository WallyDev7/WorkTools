'''

O script Python a seguir realiza as seguintes tarefas:

Abre TODOS os arquivos GeoJSON dentro da pasta raiz.
Renomeia a propriedade 'id' para 'name'.
Adiciona as propriedades especificadas ('stroke', 'stroke-width', 'stroke-opacity', 'fill', 'fill-opacity') a cada recurso (feature) do GeoJSON.

'''


import os
import json


def rename_and_add_properties(geojson_file):
    with open(geojson_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Renomear a propriedade 'id' para 'name'
    for feature in data['features']:
        if 'id' in feature['properties']:
            feature['properties']['name'] = feature['properties'].pop('id')

        # Adicionar propriedades adicionais
        feature['properties']['stroke'] = '#ffff00'
        feature['properties']['stroke-width'] = 2
        feature['properties']['stroke-opacity'] = 1
        feature['properties']['fill'] = '#ff0000'
        feature['properties']['fill-opacity'] = 0.5

    # Salvar o GeoJSON modificado
    with open(geojson_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def process_geojson_files_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.geojson'):
            geojson_file = os.path.join(directory, filename)
            rename_and_add_properties(geojson_file)


if __name__ == "__main__":
    directory = '.'  # Diretório raiz
    process_geojson_files_in_directory(directory)
