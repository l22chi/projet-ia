import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


########################################################################

# chemin de la data CSV
dataset = "time_series.csv"

# mapping des numéros de classes avec les labels et des couleurs (pour le plotting)
classe_info = {
  'not identified':           {'value':0, 'color': '#000000'},
  'soybean':                  {'value':1, 'color': '#ffe32e'},
  'maize':                    {'value':2, 'color': '#FF0000'},
  'uncultivated soil':        {'value':3, 'color': '#a9b0b0'},
  'coffee':                   {'value':4, 'color': '#75781f'},
  'beans':                    {'value':5, 'color': '#e5eb34'},
  'wheat':                    {'value':6, 'color': '#ff24e5'},
  'sorghum':                  {'value':7, 'color': '#a80a96'},
  'millet':                   {'value':8, 'color': '#fa73eb'},
  'eucalyptus':               {'value':9, 'color': '#c75e0e'},
  'pasture':                  {'value':10, 'color': '#fff68f'},
  'hay':                      {'value':11, 'color': '#c9cf91'},
  'grass':                    {'value':12, 'color': '#12e362'},
  'crotalari':                {'value':13, 'color': '#12e362'},
  'maize+crotalari':          {'value':14, 'color': '#f77159'},
  'cerrado':                  {'value':15, 'color': '#5e2e10'},
  'conversion area':          {'value':16, 'color': '#12e0e3'},
  'cotton':                   {'value':17, 'color': '#0000FF'},
  'ncc':                      {'value':18, 'color': '#12e362'},
  'brachiaria':               {'value':19, 'color': '#12e362'},
}

# récupération des labels
classes = {x : y.get('value') for x, y in classe_info.items()}

# récupération des couleurs
classe_colors = [y.get('color') for x, y in classe_info.items()]

# récupération des feaures (EVI)
features = ['red', 'nir', 'swir']
# récupération du nombre de features
n_features = len(features)

# définir la taille d'une séquence
sequence_size = 30

# définition d'un chemin pour la création du dossier de logs pour l'entrainement du modèle
model_dir = './logs'

data = pd.read_csv('time_series.csv')

# mapping des numéros de classe avec les labels prédéfinies
data['class_name'] = data.apply(lambda row: list(classes.keys())[list(classes.values()).index(row['class'])], axis = 1)
# convertir la colonne date en format datetime compréhenssible pour le modèle
data['date'] = pd.to_datetime(data['date'])

data['year'] = data['date'].apply(lambda x: x.year)

########################################################################

# Affichage des noms des acteurs projets
with st.sidebar:
    st.markdown("*Développeurs Projet :*")
    st.markdown("    AMORIM Valentin")
    st.markdown("    HEINZLE Yann")
    st.markdown("    MAOUCHE Yamina")
    st.markdown("    MEBREK Samir")

# Afficher le titre de la page
st.title('Données Géospatiales des terres agricoles bréziliennes')

# Définir la liste des sections de la page
sections = ["Revue Complète", 
            "Evolution de l'intensité agricole du coton",
            ]

# Ajouter la barre de navigation dans la sidebar
selection = st.sidebar.radio("Navigation dans les sections :", sections)

# Afficher le jeu de données complet
if selection == "Revue Complète":
    st.subheader('Revue Complète')
    st.write(data)

    st.subheader('Affichage des indices RNS moyens par année et par type de culture')
    st.write(data.groupby(['year','class_name'])[['red','nir','swir']].mean())

# Afficher l'intensité (red) par type d'agriculture
if selection == "Evolution de l'intensité agricole du coton":

    selected_culture = st.selectbox(label='Type de culture', options=data['class_name'].unique())
    selected_year = st.selectbox(label='Année', options=data['year'].unique())
    selected_parcelle = st.selectbox(label='Numéro de parcelle', options=data['id'].unique())

    submitted = st.button('Submit')

    if submitted:
        filtered_data = data.loc[(data['class_name'] == selected_culture) & (data['year'] == selected_year) & data['id'] == selected_parcelle]

        st.subheader("Représentation graphique de l'évolution de l'intensité agricole du {} brézilien sur la parcelle n°{} en {}".format(selected_culture, selected_parcelle, selected_year))
        
        #fig = px.line(filtered_data, x='date', y='red')
        #fig.add_trace(px.line(filtered_data, x='date', y='nir'))
        #fig.add_trace(px.line(filtered_data, x='date', y='swir'))
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x = filtered_data['date'],
            y = filtered_data['red'],
        ))
        fig.update_layout(
            title="Evolution de l'intensité agricole (red) du {}, parcelle n°{} - {}".format(selected_culture, selected_parcelle, selected_year),
            xaxis_title="Date",
            yaxis_title="Intensité"
        )
        st.plotly_chart(fig)

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x = filtered_data['date'],
            y = filtered_data['nir'],
        ))
        fig.update_layout(
            title="Evolution de l'intensité agricole (nir) du {}, parcelle n°{} - {}".format(selected_culture, selected_parcelle, selected_year),
            xaxis_title="Date",
            yaxis_title="Intensité"
        )
        st.plotly_chart(fig)

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x = filtered_data['date'],
            y = filtered_data['swir'],
        ))
        fig.update_layout(
            title="Evolution de l'intensité agricole (swir) du {}, parcelle n°{} - {}".format(selected_culture, selected_parcelle, selected_year),
            xaxis_title="Date",
            yaxis_title="Intensité"
        )
        st.plotly_chart(fig)
