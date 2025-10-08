# To run the code use:  
# poetry run streamlit run app.py

# To stop the code:
# CTRL + C


# Library
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


# Set the app title 
st.title("Swiss Canyon Trail 2024 Results ")


# Load data
@st.cache_data
def load_data(df):
    data = pd.read_csv(df)
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')

data = pd.read_csv("https://raw.githubusercontent.com/elorridestizons/dataTrail/main/swiss_canyon_trail_2024/df_finish.csv")

# Notify the reader that the data was successfully loaded.
data_load_state.text("Success: Data Loaded!")

# Create a text input 
liste_dossard = data.dossard.tolist()
liste_dossard.sort()
selection_dossard = st.multiselect('Selectionnez le(s) numéro(s) de dossard', liste_dossard)




# Analyse de la participation par genre
st.subheader('Analyse de la participation par genre')

## Repartition par genre
df_sexe = data.sexe.value_counts(normalize=True).to_frame("distribution").reset_index()

fig1, ax = plt.subplots(figsize=(6, 4))

ax = sns.barplot(data = df_sexe,
                 x = "sexe",
                 y =  "distribution",
                 palette = "Set2",
                 order = ['F', 'H'])

# Remove the box
sns.despine(bottom = True, left = True)

# Axis and title
plt.xlabel("Genre")
ax.yaxis.set_visible(False)
plt.title("Distribution de la participation par genre")

# Add the values on the bars
for p in ax.patches:
    ax.annotate(f'{p.get_height():.1%}', 
                (p.get_x() + p.get_width() / 2, p.get_height()/2), 
                ha='center', va='center')


## Repartition par genre et distance
df_sexe_distance = data.groupby(['sexe', 'distance']).count()['dossard'].to_frame('distribution').reset_index()
df_sexe_distance['total_distance'] = df_sexe_distance.groupby('distance')['distribution'].transform('sum')
df_sexe_distance['percentage_distance'] = df_sexe_distance['distribution'] / df_sexe_distance['total_distance']

fig2, ax = plt.subplots(figsize=(6, 4))

# Bar plot
ax = sns.barplot(data = df_sexe_distance,
                 x = "distance",
                 y =  "percentage_distance",
                 hue = "sexe",
                 palette = "Set2")

# Remove the box
sns.despine(bottom = True, left = True)

# Axis and title
plt.xlabel("Distance")
ax.yaxis.set_visible(False)
plt.title("Distribution de la participation par genre et distance")
plt.legend(title="") 

# Add the values on the bars
for p in ax.patches:
    if p.get_height() != 0:
        ax.annotate(f'{p.get_height():.1%}', 
                    (p.get_x() + p.get_width() / 2, p.get_height() / 2), 
                    ha='center', va='center',
                    fontsize=8)

with st.container():
    plot1, plot2 = st.columns(2)
    with plot1:
        st.pyplot(fig1)
    with plot2:
        st.pyplot(fig2, use_container_width=True)




# Analyse de la participation par âge
st.subheader('Analyse de la participation par âge')

## Repartition par âge
df_categorie = data.categorie.value_counts(normalize=True).to_frame("distribution").reset_index()

fig1 = plt.figure(figsize = (6, 4))

# Bar plot
ax = sns.barplot(data = df_categorie,
                 x = "categorie",
                 y =  "distribution",
                 palette = "Set2",
                 order = ['Cadet','Junior','Elite','Senior 1','Senior 2','Veteran'])

# Remove the box
sns.despine(bottom = True, left = True)

# Axis and title
plt.xlabel("Category")
ax.yaxis.set_visible(False)
plt.title("Distribution de la participation par âge")

# Add the values on the bars
for p in ax.patches:
    ax.annotate(f'{p.get_height():.1%}', 
                (p.get_x() + p.get_width() / 2, p.get_height() + 0.01), 
                ha='center', va='center')

## Repartition par âge et distance
df_categorie_distance = data.groupby(['categorie', 'distance']).count()['dossard'].to_frame('distribution').reset_index()
df_categorie_distance['total_distance'] = df_categorie_distance.groupby('distance')['distribution'].transform('sum')
df_categorie_distance['percentage_distance'] = df_categorie_distance['distribution'] / df_categorie_distance['total_distance']

fig2 = plt.figure(figsize = (6, 4))

# Bar plot
ax = sns.barplot(data = df_categorie_distance,
                 x = "distance",
                 y =  "percentage_distance",
                 hue = "categorie",
                 palette = "Set2",
                 hue_order = ['Cadet','Junior','Elite','Senior 1','Senior 2','Veteran'])

# Remove the box
sns.despine(bottom = True, left = True)

# Axis and title
plt.xlabel("Distance")
ax.yaxis.set_visible(False)
plt.title("Distribution de la participation par âge et distance")

# Add the values on the bars
for p in ax.patches:
    if p.get_height() != 0:
        ax.annotate(f'{p.get_height():.1%}', 
                    (p.get_x() + p.get_width() / 2, p.get_height()+0.01), 
                    ha='center', va='center',
                    fontsize=8)

# Change legend location so it does not overlap
plt.legend(bbox_to_anchor=(1, 1), loc='upper right', borderaxespad=-0.5, fontsize=8)

with st.container():
    plot1, plot2 = st.columns(2)
    with plot1:
        st.pyplot(fig1)
    with plot2:
        st.pyplot(fig2, use_container_width=True)




# Analyse de la participation par nationalité
st.subheader('Analyse de la participation par nationalité')


## Répartition par nationalité
df_pays = data.pays.value_counts(normalize=True).to_frame("distribution").reset_index()

fig1, ax1 = plt.subplots(figsize=(6, 4))
fig1.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)  # Ajustement des marges

# Bar plot
sns.barplot(data=df_pays[df_pays.distribution >= 0.01],
            x="pays",
            y="distribution",
            palette="Set2",
            ax=ax1)

# Remove the box
sns.despine(bottom=True, left=True, ax=ax1)

# Axis and title
ax1.set_xlabel("Country")
ax1.yaxis.set_visible(False)
ax1.set_title("Distribution de la participation par nationalité")

# Add the values on the bars
for p in ax1.patches:
    ax1.annotate(f'{p.get_height():.1%}', 
                 (p.get_x() + p.get_width() / 2, p.get_height() / 2), 
                 ha='center', va='center')

## Répartition par nationalité et distance
df_pays_distance = data.groupby(['pays', 'distance']).count()['dossard'].to_frame('distribution').reset_index()
df_pays_distance['total_distance'] = df_pays_distance.groupby('distance')['distribution'].transform('sum')
df_pays_distance['percentage_distance'] = df_pays_distance['distribution'] / df_pays_distance['total_distance']

df_pays_distance_SUI_FRA = df_pays_distance[df_pays_distance.pays.isin(['SUI', 'FRA'])]

fig2, ax2 = plt.subplots()
fig2.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)  # Ajustement des marges

# Bar plot
sns.barplot(data=df_pays_distance_SUI_FRA,
            x="distance",
            y="percentage_distance",
            hue="pays",
            palette="Set2",
            ax=ax2)

# Remove the box
sns.despine(bottom=True, left=True, ax=ax2)

# Axis and title
ax2.set_xlabel("Distance")
ax2.yaxis.set_visible(False)
ax2.set_title("Distribution de la participation des Suisses et Français par distance")

# Add the values on the bars
for p in ax2.patches:
    if p.get_height() != 0:
        ax2.annotate(f'{p.get_height():.1%}', 
                     (p.get_x() + p.get_width() / 2, p.get_height() + 0.01), 
                     ha='center', va='center',
                     fontsize=8)

# Change legend location so it does not overlap
ax2.legend(bbox_to_anchor=(1, 1), loc='upper right', borderaxespad=0., fontsize=8)

# Affichage des graphiques
with st.container():
    plot1, plot2 = st.columns(2)
    with plot1:
        st.pyplot(fig1)
    with plot2:
        st.pyplot(fig2)




# Analyse de la performance
st.subheader('Analyse de la performance')

fig = plt.figure(figsize=(10, 5))

# Bar plot
ax = sns.boxplot(data=data, 
                 x="distance",
                 y="temps_seconds",
                 hue="sexe",
                 hue_order=['F', 'H'],
                 palette="Set2")

# Add every data point
sns.stripplot(data=data, 
              x="distance",
              y="temps_seconds",
              color="lightgrey",
              alpha=0.8)

# Add specific points with unique colors
cmap = plt.get_cmap('tab10')
colors = cmap(np.linspace(0, 1, len(selection_dossard)))

for i, dossard in enumerate(selection_dossard):
    data_dossard = data[data.dossard == dossard]
    sns.stripplot(data=data_dossard,
                  x="distance",
                  y="temps_seconds",
                  color=colors[i],
                  s=5,
                  label=f"Dossard {dossard}")

# Remove the box
sns.despine(bottom=True, left=True)

# Axis and title
plt.xlabel("Distance")
ax.yaxis.set_visible(False)
plt.title("Comparaison des temps de course par genre et distance")

st.pyplot(fig)
