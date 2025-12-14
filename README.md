# Horoscopedujour
Un projet simple en python très basique, débutant ! Une mini app streamlit; générateur d'horoscope aléatoire.

Python 3.14, streamlit 1.52.1
Fichier json pour stocker les horoscopes et les signes astro;
Natif> random pour tirer aléatoirement les horoscopes, os pour gérer les chemins fichiers;


# **Pour lancer l'app** :
 (vérifie que t'as streamlit installé > streamlit --version ou python -m streamlit --version)
Sinon, pour l'installer > python -m pip install streamlit (et pour vérifier > streamlit hello)

Ensuite, pour lancer l'app >
 dans ton terminal, va dans le dossier du projet
 puis > >python -m streamlit run horoscope.py

 Et voilà :D Tu tape ton signe astro (ou un random comme tu veux) et tu as ton conseil du jour! Ttu peux le refaire autant que tu veux, évidemment).


# **Contenu du projet**

  >projetspy/
  -horoscope.py > script python et streamlit
  -h.json > donnée horoscope


# **PS**: json interne donc pas besoin de connexion internet, 
      'est en local,
      streamlit 1.52.1 peut ne pas encore être compatible avec python 3.14 (le 14-12-25) > ne pas hésiter à faire un environnement sur le terminal !
      Je suis débutante et c'est mon tout premier projet python, n'ayant que des connaissances en html/css, donc des erreurs peuvent apparaîtres dans mon code (il run bien mais j'imagine que j'optimise pas encore assez, ce genre de chose, mais ça va venir!)
      Et enfin : j'aimerais améliorer des choses, tel que le styliser (en css integré je pense avec st.markdown), faire en sorte qu'une fois l'horoscope affiché, le signe s'éfface tout seul pour pouvoir en écrire un autre, peut être même ajouter une barre déroulante.) 


*Merci d'avoir lu et d'avoir essayé ma mini app ! Tout conseils est le bievenue, je poste afin de me créer un portefolio et de répertorier mes projets :)* 
