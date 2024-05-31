'''

Esse script Python solicita ao usuário o nome de um arquivo GeoJSON (um formato comum para dados geoespaciais),
adiciona ou renomeia algumas propriedades em cada objeto de recurso no arquivo (como 'name', 'stroke', 'stroke-width', 'stroke-opacity', 'fill' e 'fill-opacity'),
e depois salva as alterações de volta no arquivo GeoJSON especificado pelo usuário.

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


if __name__ == "__main__":
    filename = input("Por favor, insira o nome do arquivo GeoJSON (sem a extensão .geojson): ")
    geojson_file = filename + '.geojson'
    rename_and_add_properties(geojson_file)
