'''

Este script Python verifica automaticamente todos os arquivos na pasta raiz, identifica o arquivo KML presente,
extrai os nomes das localidades contidos no arquivo KML e os escreve em um arquivo de texto com o mesmo nome do arquivo KML, substituindo a extensão.

'''



import os
from xml.dom import minidom

def parse_kml():
    # Verifica todos os arquivos na pasta raiz do script
    kml_file = None
    for file_name in os.listdir('.'):
        # Verifica se o arquivo é um arquivo KML
        if file_name.endswith('.kml'):
            kml_file = file_name
            break
    else:
        print("Nenhum arquivo KML encontrado na pasta raiz.")
        return

    # Extrai o nome do arquivo sem a extensão
    base_name = os.path.splitext(kml_file)[0]

    try:
        # Parse o arquivo KML usando minidom
        doc = minidom.parse(kml_file)
    except Exception as e:
        print(f"Erro ao analisar o arquivo KML: {e}")
        return

    # Obtenha todos os elementos 'Placemark'
    placemarks = doc.getElementsByTagName('Placemark')

    # Crie um arquivo de texto com o mesmo nome do arquivo KML para escrever os dados
    with open(f'{base_name}.txt', 'w', encoding='utf-8') as txt_file:
        # Itere sobre os elementos 'Placemark'
        for placemark in placemarks:
            # Obtenha o nome do local, se existir
            name_elements = placemark.getElementsByTagName('name')
            if name_elements:
                name = name_elements[0].firstChild.data if name_elements[0].firstChild else 'Nome não disponível'
                # Escreva apenas o nome do local no arquivo de texto
                txt_file.write(f'{name}\n')

    print(f"Dados extraídos e escritos com sucesso no arquivo '{base_name}.txt'.")

# Chamada da função para analisar o KML e gravar os dados no arquivo de texto
parse_kml()
