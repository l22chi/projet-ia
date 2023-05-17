# PROJET IA - Fiche Technique

## Les différents environnements virtuels :

### requirements.txt

Ce fichier est utilisé pour exécuter le script *make_sql.py* afin de générer la base de données MySQL et pour éxecuter le script *main.py* afin de lancer l'application de l'intereface web Streamlit.

### requirements-model.txt

Ce fichier est utilisé pur exécuter le notenook jupyter servant à entraîner le modèle et à faire une prédiction.

## Le modèle LSTM :

Ce modèle a été entraîné avec l'API Keras - Tensorflow sur la base de Time Series (provenant d'images de drones annotées).
Pour réaliser la prédiction, nous avons décidées, à partir d'une image contenant des métadonénees géospatiale, prédire le type de culture prédominante sur plusieurs parcelles de terrains d'une région Brézilienne. 
Afin de pouvoir utilisé ce type de données nous avons utilisé la librairie GDAL. Cette librairie nécessite une installation particulière qui eets décrite dans le notebook *projet-IA.ipynb*.

Suite à l'entraînement de ce modèle nous avons les outputs suivants :
1. Un dossier de logs concernant l'entrainement du modèle
2. Une image au format TIF (avec des métadonnées géospatiale) qui sera l'input de la prédiction
3. Un fichier .h5 qui contient les poids enregistrés par notre modèle
4. Une vidéo .mp4 qui est la prédiction de Time Series de notre LSTM que nous avons transposée sur l'image TIF afin d'avoir une visualisastion de la prédiction de notre modèle.


## Notes supplémentaires : 

Afin de réaliser ce projet, nous nous sommes basés sur plus de 3 millions de données. Les input et outputs ainsi que les différents fichiers de configuration sont très volumineux. Ce qui a pour conséquence les éléments suivants :
- Le temps d'attente avant de pouvoir visualiser les résultats sur l'app Streamlit est très long
- Seuls les requirements.txt ont été fournis (les dosssiers d'environnements virtuels ne sont pas fournis)
- Le temps d'entraînement du modèle a été réalisé et optimisé sans GPU (long)
- L'exécution de fichier.sql pour obtenir la base de données peeut engendre des problèmes d'optimisations et de ralentissements dûs aau volume des données