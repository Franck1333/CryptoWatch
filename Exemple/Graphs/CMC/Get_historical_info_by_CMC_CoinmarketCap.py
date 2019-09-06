# -*- coding: utf-8 -*-
#AIDES : https://github.com/Waultics/coinmarketcap-history

#DESCRIPTION DES TESTS EN COURS...:
#Ce programme recceueil l'historique du Prix du BTC en Dollar USD durant une periode donner a nos jours,
#-dans le but de pouvoir etablir un graphique.

import getpass                                              #On importe la blibliotheque "getpass"
global USERNAME
USERNAME = getpass.getuser()                                #On enregistre le Nom de l'Utilisateur

from cmc import coinmarketcap
from datetime import timedelta
from datetime import datetime
import pandas
from pandas import DataFrame

def Recuperation_Historique_Crypto(Nom_Entier_Crypto):
    #Obtention des informations des Informations et Enregistrement de celle-ci en fihcier .CSV
    #~
    #~
    cryptos = [Nom_Entier_Crypto.casefold()]                       #La crypto-monnaie choisi qui sera Visualiser par Graphique

    global Nom_Entier_Crypto_path                                  #Passage en Global de la crypto choisi pour etre utiliser en tant que chemin lorsqu'il sera lu pour et par le système
    Nom_Entier_Crypto_path = Nom_Entier_Crypto                     #Enregistrelent de la crypto choisi pour son utilisation en tanr que chemin de lecture
    #-----
    end_date_datetimevar = datetime.now().strftime('%Y-%m-%d')     #Enregistrement de la date d'aujourdui au format ISO
    end_date = end_date_datetimevar                                #Passage de la variable a une autre pour eviter une erreur du a l'indication du format ISO
    start_date = '2019-05-13'                                      #Date donner pour etablir le debut du graphique
    #------
    # retrieves data and stores .msg files in DOWNLOAD_DIR
    df_cryptos = coinmarketcap.getDataFor(cryptos, start_date, end_date, DOWNLOAD_DIR = 'data/coinmarketcap' , fields = ['Close'])

    #print(df_cryptos['bitcoin']['Close'])                          #Nous recevons la date plus le prix du BTC 
    #Une fois recue, les informations obtenue sont enregistrer dans un fichier CSV avec pour nom de fichier la crypto-monnaie saisie au prealable
    df_cryptos[Nom_Entier_Crypto.casefold()]['Close'].to_csv(r'/home/'+USERNAME+'/CryptoWatch/Exemple/Graphs/CMC/data/'+Nom_Entier_Crypto.casefold()+'_USD.csv', header = True)
    print("CSV Obtenue")                                            #Message afficher dans la console
     
#def Recuperation_CSV():
    #Lecture du fichier CSV recue
    #~
    #~
    df_recue = pandas.read_csv('/home/'+USERNAME+'/CryptoWatch/Exemple/Graphs/CMC/data/'+Nom_Entier_Crypto_path.casefold()+'_USD.csv') #Lecture dans la console du fichier CSV obtenue après traitement
    #print(df_recue.columns)                                                                                                            #Affichage des titres des Colonnes du fichier recue
    #print(df_recue)                                                                                                                    #Affichage du Fichier reçue .CSV

    #Listage des colonnes DATAFRAME 'df_recue' ['Date'] et ['Close']
    INDICE_Date = 0                                                 #Indice pour la navigation dans la liste de la colonne 'Date'
    Taille_Date = len(df_recue['Date'])                             #Variable permettant de connaitre la taille de la colonne 'Date'
    INDICE_Close = 0                                                #Indice pour la navigation dans la liste de la colonne 'Close'
    Taille_Close = len(df_recue['Close'])                           #Variable permettant de connaitre la taille de la colonne 'Clone'

    liste_Date = []                                                 #Creation de la liste 'Date'
    liste_Close = []                                                #Creation de la liste 'Close'
    
    for INDICE_Date in range(Taille_Date):                          #Boucle FOR navigant dans la liste 'Date' en suivant la taille de la liste 'Date'
        #print(df_recue['Date'][INDICE_Date])                       #Affichage debug de la colonne 'Date', ligne par ligne
        liste_Date.append(df_recue['Date'][INDICE_Date])            #Ajout des informations de la colonne 'Date' dans sa liste , ligne-par-ligne

    for INDICE_Close in range(Taille_Close):                        #Boucle FOR navigant dans la liste 'Close' en suivant la taille de la liste 'Close' 
        #print(df_recue['Close'][INDICE_Close])                     #Affichage debug de la colonne 'Close' , ligne-par-ligne
        liste_Close.append(df_recue['Close'][INDICE_Close])         #Ajout des information de la colonne 'Close' dans sa liste, ligne-par-ligne

    print(liste_Date)                                               #Affichage dans la console de la liste 'Date'
    print(liste_Close)                                              #Affichage dans la console de la liste 'Close'

    return liste_Date,liste_Close                                   #Envoie les deux listes pour utilisation utltérieur
    
if __name__ == "__main__":
    print("Pour utiliser ce programme, il vous faut saisir le Nom entier de façon correcte du Coin/Token en question")
    #Recuperation_Historique_Crypto('Bitcoin')                                                                                 #Obtention des informations par rapport a la crypto-monnaie saisi
    #Recuperation_CSV()                                                                                                        #Lecture du fichier CSV
