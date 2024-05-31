'''

O script Python percorre um arquivo GeoJSON fornecido pelo usuário, separando e agrupando as features com base na propriedade 'fill'.
Ele classifica as features em três camadas distintas: 'Green Layer' para aquelas com 'fill' igual a '#00ff00', 'Orange Layer' para aquelas com 'fill' igual a '#ff9600'
e 'Red Layer' para aquelas com 'fill' igual a '#ff0000'. Em seguida, o script salva cada grupo em arquivos GeoJSON separados, conforme especificado pelo usuário.

'''



import json
import geojson

def separar_geojson(input_file, green_file, orange_file, red_file):
    # Carregar o GeoJSON de entrada com a codificação correta
    with open(input_file, 'r', encoding='utf-8') as f:
        data = geojson.load(f)
    
    # Criar contêineres para os novos GeoJSONs
    green_features = []
    orange_features = []
    red_features = []

    # Percorrer as features e separá-las com base na propriedade "fill"
    for feature in data['features']:
        properties = feature.get('properties', {})
        fill = properties.get('fill')
        
        if fill == '#00ff00':
            green_features.append(feature)
        elif fill == '#ff9600':
            orange_features.append(feature)
        elif fill == '#ff0000':
            red_features.append(feature)

    # Criar novos objetos GeoJSON para cada grupo
    green_geojson = geojson.FeatureCollection(green_features)
    orange_geojson = geojson.FeatureCollection(orange_features)
    red_geojson = geojson.FeatureCollection(red_features)

    # Salvar os novos GeoJSONs em arquivos separados
    with open(green_file, 'w', encoding='utf-8') as f:
        geojson.dump(green_geojson, f)

    with open(orange_file, 'w', encoding='utf-8') as f:
        geojson.dump(orange_geojson, f)
    
    with open(red_file, 'w', encoding='utf-8') as f:
        geojson.dump(red_geojson, f)
    
    print(f'GeoJSONs separados e salvos em: {green_file}, {orange_file}, {red_file}')

def main():
    # Solicitar ao usuário o nome do arquivo de entrada sem a extensão
    input_geojson = input('Digite o nome do arquivo GeoJSON de entrada: ')
    input_geojson += '.geojson'  # Adicionar a extensão automaticamente
    
    # Solicitar ao usuário os nomes dos arquivos de saída sem a extensão
    green_output = input('Digite o nome para salvar o arquivo GeoJSON do Green Layer: ')
    green_output += '.geojson'  # Adicionar a extensão automaticamente
    
    orange_output = input('Digite o nome para salvar o arquivo GeoJSON do Orange Layer: ')
    orange_output += '.geojson'  # Adicionar a extensão automaticamente
    
    red_output = input('Digite o nome para salvar o arquivo GeoJSON do Red Layer: ')
    red_output += '.geojson'  # Adicionar a extensão automaticamente
    
    # Chamar a função para separar o GeoJSON
    separar_geojson(input_geojson, green_output, orange_output, red_output)

if __name__ == '__main__':
    main()

