# WorkTools
That are some tools that a created to use in my Risk Analysis job

List of tool:

Adiciona_Propriedades.py | Add_Properties.py
	
	O script Python a seguir realiza as seguintes tarefas:
	Abre um arquivo GeoJSON.
	Renomeia a propriedade 'id' para 'name'.
	Adiciona as propriedades especificadas ('stroke', 'stroke-width', 'stroke-opacity', 'fill', 'fill-opacity') a cada recurso (feature) do GeoJSON.

	The following Python script performs the following tasks:
	Opens a GeoJSON file.
	Renames the 'id' property to 'name'.
	Adds the specified properties ('stroke', 'stroke-width', 'stroke-opacity', 'fill', 'fill-opacity') to each feature in the GeoJSON.

Adiciona_Propriedades_2.0.py | Add_Properties_2.0.py

	O script Python a seguir realiza as seguintes tarefas:
	Abre TODOS os arquivos GeoJSON dentro da pasta raiz.
	Renomeia a propriedade 'id' para 'name'.
	Adiciona as propriedades especificadas ('stroke', 'stroke-width', 'stroke-opacity', 'fill', 'fill-opacity') a cada recurso (feature) do GeoJSON.

	The following Python script performs the following tasks:
	Opens ALL GeoJSON files within the root folder.
	Renames the 'id' property to 'name'.
	Adds the specified properties ('stroke', 'stroke-width', 'stroke-opacity', 'fill', 'fill-opacity') to each feature in the GeoJSON.

Adiciona_Propriedades_3.0.py | Add_Properties_3.0.py

	Esse script Python solicita ao usuário o nome de um arquivo GeoJSON (um formato comum para dados geoespaciais),
	adiciona ou renomeia algumas propriedades em cada objeto de recurso no arquivo (como 'name', 'stroke', 'stroke-width', 'stroke-opacity', 'fill' e 'fill-opacity'),
	e depois salva as alterações de volta no arquivo GeoJSON especificado pelo usuário.

	This Python script prompts the user for the name of a GeoJSON file (a common format for geospatial data), adds or renames certain properties in each feature object in the file (such as 'name', 'stroke', 'stroke-width', 'stroke-opacity', 'fill', and 'fill-opacity'), and then saves the changes back to the specified GeoJSON file.

Classifica_Geojson.py | Classify_Geojson.py
	
	O script Python percorre um arquivo GeoJSON fornecido pelo usuário, separando e agrupando as features com base na propriedade 'fill'.
	Ele classifica as features em três camadas distintas: 'Green Layer' para aquelas com 'fill' igual a '#00ff00', 'Orange Layer' para aquelas com 'fill' igual a '#ff9600'
	e 'Red Layer' para aquelas com 'fill' igual a '#ff0000'. Em seguida, o script salva cada grupo em arquivos GeoJSON separados, conforme especificado pelo usuário.

	This Python script iterates through a GeoJSON file provided by the user, separating and grouping features based on the 'fill' property. It classifies features into three distinct layers: 'Green Layer' for those with 'fill' equal to '#00ff00', 'Orange Layer' for those with 'fill' equal to '#ff9600', and 'Red Layer' for those with 'fill' equal to '#ff0000'. Then, the script saves each group into separate GeoJSON files as specified by the user.

Extrai_Names.py | Extract_Names.py
	
	Este script Python foi criado para realizar a extração dos valores de "name" de um arquivo GeoJSON e armazená-los em um arquivo de texto.
	Primeiramente, é verificado se o GeoJSON fornecido é do tipo "FeatureCollection".
	Em seguida, o script percorre os recursos (features) presentes no GeoJSON e verifica se a chave "name" está presente nas propriedades de cada recurso.
	Se estiver, o valor correspondente é adicionado a uma lista.
	Por fim, os valores da lista são escritos em um arquivo de texto.

	This Python script is designed to extract the values of "name" from a GeoJSON file and store them in a text file. It first checks if the provided GeoJSON is of type "FeatureCollection". Then, it iterates through the features in the GeoJSON and checks if the "name" key is present in each feature's properties. If it is, the corresponding value is added to a list. Finally, the values from the list are written to a text file.

Extrai_Names_2.0.py | Extract_Names_2.0.py

	Esse script Python solicita ao usuário o nome de um arquivo GeoJSON de entrada e o nome de um arquivo de texto de saída.
	Ele então extrai os valores da propriedade "name" de cada objeto de recurso no arquivo GeoJSON e os salva no arquivo de texto especificado pelo usuário.

	This Python script prompts the user for the name of an input GeoJSON file and the name of an output text file. It then extracts the values of the "name" property from each feature object in the GeoJSON file and saves them in the text file specified by the user.

Organiza_Geojson-FUNCIONAL.py | Organize_Geojson-FUNCTIONAL.py
	
	Este script em Python organiza arquivos GeoJSON em um diretório específico.
	A função organize_geojson_files percorre os arquivos no diretório, carrega cada arquivo, ajusta sua estrutura utilizando a função organize_geojson,
	e então sobrescreve o arquivo original com os dados organizados. A função organize_geojson ajusta a estrutura dos dados GeoJSON para garantir consistência,
	mantendo apenas um conjunto de coordenadas para polígonos e ambos os conjuntos para linhas.

	This Python script organizes GeoJSON files in a specific directory. The function 'organize_geojson_files' iterates through the files in the directory, loads each file, adjusts its structure using the 'organize_geojson' function, and then overwrites the original file with the organized data. The 'organize_geojson' function adjusts the structure of GeoJSON data to ensure consistency, keeping only one set of coordinates for polygons and both sets for lines.

Pega_Nome.py | Get_Name.py
	
	O script Python a seguir realiza as seguintes tarefas:
	Pega o valor da propriedade 'nome' e colocar em um arquivo txt

	The following Python script performs the following tasks:
	Grabs the value of the 'name' property and puts it in a txt file.
