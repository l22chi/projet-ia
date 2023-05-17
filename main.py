import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Définir la fonction pour le diagramme circulaire
def pie_chart(data):
    labels = data['Labels']
    sizes = data['Sizes']
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)

# Définir la fonction pour le lineplot
def line_plot(data,col_y):
    fig, ax = plt.subplots()
    ax.plot(data.index, data[col_y])
    st.pyplot(fig)

# Créer un jeu de données
data = pd.read_csv('DataFrame_ProjetIA.csv', sep=';', decimal='.', encoding='cp1252', index_col='Annee')
data_preticted = pd.read_csv('y_predict.csv', sep=';', decimal='.', encoding='cp1252', index_col='Annee')


# -- # Filtres
var_target = 'EastAsia&Pacific_CoutsImport_MD'

col_to_keep_cmd = ['World_CoutsImport_MD',
               'EastAsia&Pacific_CoutsImport_MD',
               'Europe&CentralAsia_CoutsImport_MD',
               'LatinAmerica&Caribbean_CoutsImport_MD',
               'MiddleEast&NorthAfrica_CoutsImport_MD',
               'Sub-SaharanAfrica_CoutsImport_MD']

col_to_keep_pi = ['World_PartImport',
               'EastAsia&Pacific_PartImport',
               'Europe&CentralAsia_PartImport',
               'LatinAmerica&Caribbean_PartImport',
               'MiddleEast&NorthAfrica_PartImport',
               'Sub-SaharanAfrica_PartImport']

##

# Affichage des noms des acteurs projets
with st.sidebar:
    st.markdown("*Acteurs projet :*")
    st.markdown("    ALIA Hervé")
    st.markdown("    BAËGERT Marc")
    st.markdown("    BONNET Swann")
    st.markdown("    BEN SLIMANE Lamiaa")
    st.markdown(" ")
    st.markdown(" ")

# Afficher le titre de la page
st.title('Tableau de données - Import de vêtement et de tissu en France')

# Définir la liste des sections de la page
sections = ["Tableau de données complet", 
            "Données - Coût d'import en MD", 
            "Données - Part d'import/production",
            "Evolution de la population en France",
            "Modélsation - Prédiction des coûts d'import en MD"]

# Ajouter la barre de navigation dans la sidebar
selection = st.sidebar.radio("Navigation dans les sections :", sections)

# Afficher le jeu de données complet
if selection == "Tableau de données complet":
    st.subheader('Tableau de données complet')
    st.write(data)

# Afficher le tableau de données pour le coût d'import en MD par pays
if selection == "Données - Coût d'import en MD":
    st.subheader("Tableau de données des principales parties du monde - Coût d'import en MD")
    data_cmd = data[col_to_keep_cmd].copy()
    st.write(data_cmd)

# Afficher le tableau de données pour la part d'import/production par pays
if selection == "Données - Part d'import/production":
    st.subheader("Tableau de données des principales parties du monde - Part d'import/production")
    data_pi = data[col_to_keep_pi].copy()
    st.write(data_pi)

# Afficher l'évolution de la population en France
if selection == "Evolution de la population en France":
    st.subheader("Représentation graphique de l'évolution de la population en France")
    fig =px.line( x=data.index, y=data.Population)
    fig.update_layout(
        title="Evolution de la population en France",
        xaxis_title="Année",
        yaxis_title="Population en France"
    )
    st.plotly_chart(fig)
    
# Afficher l'évolution de la population en France
if selection == "Modélsation - Prédiction des coûts d'import en MD":
    st.subheader("Mise en place d'un modèle prédictif sur le coût d'importation des tissus et des vêtements en France en provenance des pays issues de l'est Asie et du Pacific")
    fig, ax = plt.subplots()
    ax.plot(data.index, data[var_target], 'r', label='Valeurs réelles')
    ax.plot(data_preticted.index, data_preticted.values, 'b', label='Valeurs prédites')
    ax.set_title(f'Prédiction de la valeur {var_target}\n entre 2016 et 2020')
    ax.legend()
    st.pyplot(fig)