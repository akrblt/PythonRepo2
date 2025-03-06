'''
Micro-surveillance de mouvements
MicroMotion
Idée et réalisation. JP Chavey
fév 2025
v1.1 03.03.2025 
'''
'''
Dernières améliorations:
- Scanner tout le répertoire et proposer une liste déroulante (au démarrage)
- DONE: Permettre le choix du facteur de réduction
- DONE: Déplacer les parties interactives dans un frame à gauche
- MOITIE DONE: permettre que le changement de zoom n'ait pas besoin de refaire l'analyse (un peu comme les scrollbars)
- DONE: pouvoir changer le blob_size et blob_min_percentage
- DONE: corriger bug double traitement au départ 
- DONE: ajouter une zone d'exclusion autour de l'image (pour ne pas y compter les taches)
- DONE: afficher les taches sous forme de carrés bleus (en taille réelle), mais pas en zoom.
- DONE: permettre l'agglomération des taches et afficher les plus grandes à leur taille réelle
- DONE: Proposer un mode automatique qui va voir toutes les 10s si une nouvelle image est arrivée
- Choisir définition du canvas (actuellement 900x600)
- Ajouter case à cocher pour activer ou non l'alarme sonore
- Déplacer les log en print dans un widget texte
- Permettre de choisir un répertoire par une fenêtre
- DONE: Espace: Permettre de voir les 2 images originales dans le canvas 
- etc
'''

import tkinter as tk
import cv2
import numpy as np
from PIL import Image, ImageTk, ImageEnhance
import os
import glob
import time
import math
import copy

''' 
==================================================================================================================================
Fonctions générales hors de la fenêtre de traitement d'images 
==================================================================================================================================
'''

def generate_image_files(directory):
    # Récupère toutes les images d'un dossier et les trie par ordre alphabétique.
    valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".tiff")  # Extensions valides
    image_files = sorted([os.path.join(directory, f) for f in os.listdir(directory) if f.lower().endswith(valid_extensions)])

    if not image_files:
        raise ValueError("Aucune image trouvée dans le répertoire spécifié.")
    
    print("Images trouvées :", image_files)  # Pour débogage
    return image_files

def align_images(img1, img2, scale_factor=0.5):
    """ Aligne img2 sur img1 en utilisant un recalage sur une version réduite, uniquement translation """
    # Réduire la taille des images pour accélérer le recalage
    small_img1 = cv2.resize(img1, (0, 0), fx=scale_factor, fy=scale_factor)
    small_img2 = cv2.resize(img2, (0, 0), fx=scale_factor, fy=scale_factor)

    # Convertir en niveaux de gris
    img1_gray = cv2.cvtColor(small_img1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(small_img2, cv2.COLOR_BGR2GRAY)

    # Initialiser la transformation (translation uniquement)
    warp_matrix = np.eye(2, 3, dtype=np.float32)

    try:
        # Recalage avec moins d'itérations pour accélérer
        criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 20, 1e-5)
        _, warp_matrix = cv2.findTransformECC(img1_gray, img2_gray, warp_matrix, cv2.MOTION_TRANSLATION, criteria)

        # Adapter la transformation pour l'image pleine résolution
        warp_matrix[0, 2] *= 1 / scale_factor  # Correction du facteur d'échelle
        warp_matrix[1, 2] *= 1 / scale_factor  

        # Appliquer la transformation à l'image originale
        img2_aligned = cv2.warpAffine(img2, warp_matrix, (img1.shape[1], img1.shape[0]), flags=cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP)

        return img2_aligned
    except cv2.error:
        print("⚠️ Alignement échoué, on garde l'image d'origine.")
        return img2  # En cas d'erreur, on garde img2 inchangée


def compare_images(img1, img2, gray_mode, threshold):
    # Compare deux images et renvoie l'image de base et l'image de différence
    # 🔥 Charger les images
    sizex=img1.shape[1] #taille de l'image en x à renvoyer
 
    # 🔥 Mise à l'échelle si les images n'ont pas la même taille
    if img1.shape != img2.shape:
        start = time.perf_counter()
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
        print_time("mise à l'échelle si img1<>img2",start)

    # 🔥 Alignement des images
    start = time.perf_counter()
    img2=align_images(img1, img2)
    print_time("Alignement des 2 images",start)

    # 🔥 Calcul de la différence
    start = time.perf_counter()   
    diff = cv2.absdiff(img1, img2)
    _, thresh = cv2.threshold(cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY), threshold, 255, cv2.THRESH_BINARY)
    print_time("Différence 2 images", start)

    # 🔥 Conversion en couleur
    start = time.perf_counter()
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    print_time("Passage en couleur",start)

    # 🔥 Conversion en niveaux de gris si demandé
    start = time.perf_counter()
    base_image = Image.fromarray(img1)
    if gray_mode:  
        base_image = base_image.convert("L")  # Convertir en niveaux de gris
        base_image = ImageEnhance.Brightness(base_image).enhance(1.5)  # 🔥 Augmenter un peu la luminosité
        base_image = base_image.convert("RGB")  # Convertir en RGB pour éviter les erreurs
    print_time("passage en gris si demandé",start)    

    # 🔥 Mettre en rouge les différences
    start = time.perf_counter()
    red_diff = np.array(base_image)
    if len(red_diff.shape) == 2:  
        red_diff = cv2.cvtColor(red_diff, cv2.COLOR_GRAY2RGB)
    red_diff[thresh == 255] = [255, 0, 0]  # Mettre en rouge les pixels différents
    print_time("Différences en rouge",start)    

    return base_image, red_diff, sizex

def agglomerate(mvt_blobs):
    # Fusionner les taches qui se touchent
    def blobs_touch(b1, b2):
        x1, y1, sx1, sy1 = b1
        x2, y2, sx2, sy2 = b2
        return (
            (x1 <= x2 + sx2 and x1 + sx1 >= x2 and y1 <= y2 + sy2 and y1 + sy1 >= y2)
        )

    def merge_blobs(blobs):
        min_x = min(b[0] for b in blobs)
        min_y = min(b[1] for b in blobs)
        max_x = max(b[0] + b[2] for b in blobs)
        max_y = max(b[1] + b[3] for b in blobs)
        return [min_x, min_y, max_x - min_x, max_y - min_y]

    clusters = []
    for blob in mvt_blobs:
        merged = False
        for cluster in clusters:
            if any(blobs_touch(blob, b) for b in cluster):
                cluster.append(blob)
                merged = True
                break
        if not merged:
            clusters.append([blob])
    return [merge_blobs(cluster) for cluster in clusters]

def detect_blobs(diff_image, blob_size, blob_min_percentage, points=None):
    # Détecter les taches de mouvement dans l'image de différence
    height, width, _ = diff_image.shape
    mvt_blobs = []
    #print("Détection des taches",height,width,"points reçus",points)

    # Convertir l'image en un masque binaire (1 si rouge, 0 sinon)
    red_mask = (diff_image[:, :, 0] == 255) & (diff_image[:, :, 1] == 0) & (diff_image[:, :, 2] == 0)

    # Vérifier si un polygone est défini
    has_polygon = points is not None and len(points) > 2
    if has_polygon:
        polygon = np.array(points, dtype=np.int32)  # Conversion en tableau NumPy à l'échelle
        k=app.img_sizex/app.width/app.fact_reduc
        #k=1
        for p in polygon:
            p[0]=p[0]*k
            p[1]=p[1]*k
        #print("Polygone temporaire",polygon)

    # Parcourir l'image par blocs
    for col in range(2, height // blob_size - 2):
        for line in range(2, width // blob_size - 2):
            # Extraire un bloc et calculer le pourcentage de pixels rouges
            block = red_mask[col * blob_size:(col + 1) * blob_size, line * blob_size:(line + 1) * blob_size]
            red_ratio = np.sum(block) / (blob_size ** 2)

            # Si le pourcentage dépasse le seuil, vérifier si le blob est dans le polygone
            if red_ratio > blob_min_percentage:
                blob_x = line * blob_size + blob_size // 2  # Centre du blob (X)
                blob_y = col * blob_size + blob_size // 2  # Centre du blob (Y)

                if not has_polygon or cv2.pointPolygonTest(polygon, (blob_x, blob_y), False) >= 0:
                    mvt_blobs.append([col * blob_size, line * blob_size, blob_size, blob_size])

    return mvt_blobs


def print_time(text,start):
    # prendre le temps et afficher depuis dernière prise (permet de chronométrer une fonction avec un texte en parmètre)
    print(f"{text : <35}{time.perf_counter() - start:.5f}")

''' 
==================================================================================================================================
Fenêtre principale avec ses fonctions
==================================================================================================================================
'''

class ImageViewer(tk.Tk):
    def __init__(self,directory):
        super().__init__()
        # variables d'affichage ==================================================================================================
        self.width=900 #*1.5 si on veut un affichage plus grand, fonctionne bien en plus grand aussi
        self.height=600 #*1.5
        self.title("MicroMotion - Copyright JCY 2025")
        self.image_files = [] #generate_image_files(directory)
        self.current_index = 0
        self.zoom_factor = 1 #facteur de zoom
        self.fact_reduc=2 #facteur de réduction d'entrée.
        self.base_opacity = 1.0
        self.threshold = 30  # Seuil initial
        self.blob_size = 32 # taille des taches
        self.blob_min_percentage = 0.15 # pourcentage de pixels rouges
        self.auto=False # true si on essaie de vérifier si l'image suivante est là
        self.diff_image= None
        self.gray_mode = False  # False = couleur, True = noir et blanc
        self.img_sizex=5400 #taille de l'image en x (à priori)
        self.mode_image = 0 # mode image (0 = normal analyse, 1= image 1, 2 image 2) 

        # mémorisation images de base
        self.img1 = None
        self.img2 = None

        def create_widgets():
        # Interface graphique ==================================================================================================
            self.canvas_frame = tk.Frame(self)
            self.canvas_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
            self.canvas_frame_cmd = tk.Frame(self, width=300,height=self.height)
            self.canvas_frame_cmd.pack(side=tk.LEFT, fill=tk.BOTH)

            self.canvas = tk.Canvas(self.canvas_frame, width=self.width, height=self.height, bg="gray")
            self.canvas.grid(row=0, column=0, sticky="nsew")

            self.v_scrollbar = tk.Scrollbar(self.canvas_frame, orient=tk.VERTICAL, command=self.canvas.yview)
            self.v_scrollbar.grid(row=0, column=1, sticky="ns")
            self.h_scrollbar = tk.Scrollbar(self.canvas_frame, orient=tk.HORIZONTAL, command=self.canvas.xview)
            self.h_scrollbar.grid(row=1, column=0, sticky="ew")

            self.canvas.config(yscrollcommand=self.v_scrollbar.set, xscrollcommand=self.h_scrollbar.set)

            # Répertoire à analyser
            self.load_button = tk.Button(self.canvas_frame_cmd, text="Charger", command=self.load_new_directory)
            self.load_button.grid(row=0,column=0, padx=5, pady=10,sticky='w')
            self.directory_var = tk.StringVar(value="img/img0/")  # Répertoire par défaut
            self.dir_entry = tk.Entry(self.canvas_frame_cmd, textvariable=self.directory_var, width=40)
            self.dir_entry.grid(row=0,column=1,columnspan=2, padx=5, pady=20,sticky='w')
            # Bouton check pour le mode auto
            self.auto_var = tk.IntVar(value=self.auto)
            self.auto_check = tk.Checkbutton(self.canvas_frame_cmd, text="AUTO", variable=self.auto_var)
            self.auto_check.grid(row=0, column=3, padx=5, pady=10, sticky='w')
            # Images analysées
            self.label = tk.Label(self.canvas_frame_cmd, text="Images analysées:", font=("Arial", 8), height=2)
            self.label.grid(row=1,column=0,columnspan=4, padx=5,pady=10,sticky='w')

            # Curseur de navigation
            self.label_nav = tk.Label(self.canvas_frame_cmd, text="navigation", font=("Arial", 8))
            self.label_nav.grid(row=2,column=0, padx=10)
            self.slider = tk.Scale(self.canvas_frame_cmd, from_=0, to=len(self.image_files) - 2, orient=tk.HORIZONTAL,length=280)
            self.slider.grid(row=2,column=1,columnspan=3, padx=5)

            # Cuseur de seuil
            self.label_tres = tk.Label(self.canvas_frame_cmd, text="seuil", font=("Arial", 8))
            self.label_tres.grid(row=3,column=0, padx=5)
            self.threshold_slider = tk.Scale(self.canvas_frame_cmd, from_=0, to=100, orient=tk.HORIZONTAL, length=280)
            self.threshold_slider.set(self.threshold)
            self.threshold_slider.grid(row=3,column=1,columnspan=3, padx=5)

            # Ajout du widget liste déroulante pour le facteur de réduction
            self.fact_reduc_var = tk.IntVar(value=self.fact_reduc)
            self.lst_fact_reduc = tk.OptionMenu(self.canvas_frame_cmd, self.fact_reduc_var, 1, 2, 4, 8, 16, command=self.update_fact_reduc)
            self.lst_fact_reduc.grid(row=4, column=1,  padx=5, pady=10, sticky='w')
            self.label_fact_reduc = tk.Label(self.canvas_frame_cmd, text="Facteur de réduction", font=("Arial", 8))
            self.label_fact_reduc.grid(row=4, column=0, padx=5, pady=10, sticky='e')

            # Ajout du widget liste déroulante pour la taille des blocs à détecter
            self.blob_size_var = tk.IntVar(value=self.blob_size)
            self.lst_blob_size = tk.OptionMenu(self.canvas_frame_cmd, self.blob_size_var, 6, 8, 12, 16, 24, 32, 48, 64, 128, command=self.update_blob_size)
            self.lst_blob_size.grid(row=5, column=1, padx=5, pady=10, sticky='w')
            self.label_blob_size = tk.Label(self.canvas_frame_cmd, text="Taille taches (pixels)", font=("Arial", 8))
            self.label_blob_size.grid(row=5, column=0, padx=5, pady=10, sticky='e')

            # Ajout du widget liste déroulante pour la proportion des blocs à détecter
            self.blob_min_percentage_var = tk.IntVar(value=self.blob_min_percentage)
            self.lst_blob_min_percentage = tk.OptionMenu(self.canvas_frame_cmd, self.blob_min_percentage_var, 10,15,20,30,40,50,75,100, command=self.update_blob_min_percentage)
            self.lst_blob_min_percentage.grid(row=6, column=1, padx=5, pady=10, sticky='w')
            self.label_blob_min_percentage = tk.Label(self.canvas_frame_cmd, text="% différence min", font=("Arial", 8))
            self.label_blob_min_percentage.grid(row=6, column=0, padx=5, pady=10, sticky='e')

            # Affichage du nombre de taches détectés
            self.label_nb_blob = tk.Label(self.canvas_frame_cmd, text="Nb taches", font=("Arial", 8))
            self.label_nb_blob.grid(row=7, column=0, columnspan=2,padx=5, pady=10, sticky='w')

            # Bouton fade (N/B clair)
            self.fade_button = tk.Button(self.canvas_frame_cmd, text="Atténuer image", command=self.toggle_fade)
            self.fade_button.grid(row=9,column=0, padx=5, pady=5,sticky='w')

            # Zone d'analyse
            self.cmd_edit_polygon=tk.Button(self.canvas_frame_cmd, text="Définir zone d'analyse \n(clic/clic droit)", command=self.edit_polygon)
            self.cmd_edit_polygon.grid(row=9, column=1, columnspan=3,padx=5, pady=5, sticky='w')
            self.points = np.array([])  # Liste des points (x, y)
            self.editing_polygon = False
            self.temp_lines = []  # Lignes temporaires affichées

            # label d'aide
            self.label_help = tk.Label(self.canvas_frame_cmd, 
                text =  "AIDE: \n 🖰 double clic pour zoomer sur un endroit précis, "
                    + "\n    ascenceurs pour recentrer"
                    +" \n 🖰 clic droit pour dézoomer"
                    +" \n ← → flèches pour naviguer entre les images"
                    +" \n ↓ flèche du bas pour voir les 2 images originales"
                    +" \n ↑ flèche du haut pour retourner à l'analyse de 2 images",
                font=("Arial", 12), anchor='w',  justify='left')
            self.label_help.grid(row=10, column=0, columnspan=4, padx=5, pady=10, sticky="w")


            #Liaison des objets aux évènements ==================================================================================================
            # pour naviguer avec les flèches entre les fichiers, ou autre (touche espace)
            self.bind("<Key>", self.on_key)

            # Lier les événements de la souris
            self.canvas.bind("<Double-Button-1>", self.zoom_in)
            self.canvas.bind("<Button-3>", self.right_click)
            self.canvas.bind("<Button-1>", self.add_point)  # Clic gauche = ajouter un point
            self.canvas.bind("<Motion>", self.preview_polygon)  # Déplacement souris = aperçu
            # Lier les cases à cocher
            self.threshold_slider.bind("<ButtonRelease-1>", self.update_threshold)  # Mise à jour au relâchement du clic
            self.dir_entry.bind('<Return>', lambda event: self.load_new_directory())
            self.slider.bind("<ButtonRelease-1>", lambda event: self.slider_update(self.slider.get()))


        create_widgets()
        self.load_new_directory()

    # fonction de traitement des touches (placée proche des bind)
        # traitement des touches
    def on_key(self, event):
        # touche gauche, reculer d'une image si possible
        if event.keysym == "Left":
            self.slider.set(max(self.slider.get() - 1, self.slider.cget("from")))
            self.slider_update(self.slider.get())

        # touche droite, avancer d'ue image si possible
        elif event.keysym == "Right":
            self.slider.set(min(self.slider.get() + 1, self.slider.cget("to")))
            self.slider_update(self.slider.get())

        # touche espace
        elif event.keysym == "Down":
            self.display_img_mode(event)
        
        # touche flèche bas
        elif event.keysym == "Up" :
            self.update_image()


    #fonctions pour la zone d'analyse ==================================================================================================

    def edit_polygon(self):
        """change le mode d'édition du polygone"""
        self.editing_polygon = not self.editing_polygon
        if self.editing_polygon:#si on passe en édition
            self.cmd_edit_polygon.config(text="Terminer zone d'analyse")
            self.cmd_edit_polygon.config(bg="red")
            self.points = []  # Liste des points (x, y)
            self.reset_zoom(None)
        else:
            self.cmd_edit_polygon.config(text="Définir Zone d'analyse")
            self.cmd_edit_polygon.config(bg="SystemButtonFace")
            print("Zone d'analyse mémorisée :", self.points, "editing_polygon",self.editing_polygon)  # Affichage des coordonnées

    def add_point(self, event):
        """ Ajoute un point et affiche une ligne temporaire. """
        if self.zoom_factor==1 and self.editing_polygon:
            self.points.append([event.x, event.y])

            if len(self.points) > 1:
                ligne = self.canvas.create_line(self.points[-2], self.points[-1], fill="black")
                self.temp_lines.append(ligne)

    def preview_polygon(self, event):
        """ Affiche une ligne temporaire entre le dernier point et la position actuelle. """
        if len(self.points)>0 and self.editing_polygon:
            self.canvas.delete("temp")  # Effacer l'ancienne ligne temporaire
            self.canvas.create_line(self.points[-1], (event.x, event.y), fill="black", tags="temp")

    def finish_polygon(self, event):
        """ Ferme le polygone et l'affiche en remplissant. """

        if len(self.points) > 2 and self.editing_polygon:
            self.canvas.delete("temp")  # Supprimer l'aperçu
            self.display_polygon() #afficher le polygone

            # Supprimer les lignes temporaires
            for ligne in self.temp_lines:
                self.canvas.delete(ligne)
            self.temp_lines.clear()

            #print("Polygone mémorisé :", self.points)  # Affichage des coordonnées
            self.edit_polygon()  # Réinitialisation

    def display_polygon(self):
        #print ("Polygone original",self.points)
        if len(self.points) > 2 :
            # calcul d'un self.points2 à l'échelle
            self.points_scale = copy.deepcopy(self.points)
            for p in self.points_scale :
                p[0]=p[0]*self.zoom_factor
                p[1]=p[1]*self.zoom_factor
            self.canvas.create_polygon(self.points_scale, outline="black", fill="", width=2)
        #print ("Polygone original",self.points)
    
    # Autres fonctions mineures (mise à jour des variables, tritement des touches) ================================================================================
    # mise à jour du facteur de réduction (et relance du processus)
    def update_fact_reduc(self, value):
        self.fact_reduc = int(value)
        self.update_image()
    
    # mise à jour de la taille des blocs 
    def update_blob_size(self, value):
        self.blob_size = int(value)
        self.update_image()

    # mise à jour de la proportion des blocs mini pour être comptabilité
    def update_blob_min_percentage(self, value):
        self.blob_min_percentage = int(value)/100
        self.update_image()

    #sonnerie
    def ring_bell_multiple_times(self,count):
        if count>6:
            count=6
        if count > 0:
            self.bell()
            self.after(700, self.ring_bell_multiple_times, count - 1)

    def update_threshold(self, event):
        """Met à jour le seuil et rafraîchit l’image seulement quand on relâche le curseur."""
        self.threshold = self.threshold_slider.get()
        self.update_image()

    def slider_update(self, val):
        if (val!=self.current_index):
            self.current_index = int(val)
            self.slider.update_idletasks()
            self.update_image()

            
    def toggle_fade(self):
        # Basculer entre couleur et noir & blanc
        self.gray_mode = not self.gray_mode 
        self.update_image()
    
    def right_click(self,event):
        # traitement clic droit (soit on finit le polygone analyse, soit on reset le zoom)
        if self.editing_polygon:
            self.finish_polygon(event)
        else :
            self.reset_zoom(event)


    # Fonction principale qui appelle compare_images ================================================================================
    def update_image(self):
        self.config(cursor="watch")
        self.update_idletasks() #rafraichissement de l'écran tout de suite
        image1_path = self.image_files[self.current_index]
        image2_path = self.image_files[self.current_index + 1]

        print()
        print("Traitement de",image1_path,image2_path,"facteur de différence",self.threshold,"%", "taille des taches",self.blob_size,"pixels", "pourcentage de taches",self.blob_min_percentage*100,"%")
        
        # chargement des images
        start = time.perf_counter() #2.8secondes !!
        self.img1 = cv2.imread(image1_path)
        self.img2 = cv2.imread(image2_path)
        print_time("Lecture images sur le disque :",start)

        # Appliquer un facteur de réduction
        start = time.perf_counter()
        if self.fact_reduc>1:
            self.img1 = cv2.resize(self.img1, (int(self.img1.shape[1]/self.fact_reduc), int(self.img1.shape[0]/self.fact_reduc)),interpolation=cv2.INTER_NEAREST)
            self.img2 = cv2.resize(self.img2, (int(self.img2.shape[1]/self.fact_reduc), int(self.img2.shape[0]/self.fact_reduc)),interpolation=cv2.INTER_NEAREST)
            print_time("Réduction facteur " + str(self.fact_reduc) ,start)


        # Comparer les images et créer l'image de différence
        base_image, self.diff_image, self.img_sizex = compare_images(self.img1, self.img2, self.gray_mode, self.threshold)

        #détection des taches (d'abord on somme), on laisse les bords tranquilles
        start = time.perf_counter() #2.8secondes !!
        self.mvt_blobs=detect_blobs(self.diff_image, self.blob_size, self.blob_min_percentage,self.points)
        print_time("Détection taches :" + str(self.blob_size) + "/" + str(self.blob_min_percentage)+ "=>" + str(len(self.mvt_blobs)),start)
        
        #agglomération des taches
        start = time.perf_counter()
        n=len(self.mvt_blobs)
        if(len(self.mvt_blobs)<1000):
            self.mvt_blobs=agglomerate(self.mvt_blobs)
        print_time("Agglomération des taches :" + str(len( self.mvt_blobs)) + " / " + str(n),start)
            
        self.label_nb_blob.config(text=f"Nb taches: {len(self.mvt_blobs)}")

        # Afficher l'image (le chrono est dans la fonction)
        self.display_image(self.diff_image)

        #affichage des taches
        start = time.perf_counter()
        self.display_blobs()
        print_time("Affichage des taches :",start)

        #affichage de la zone d'exclusion
        self.display_polygon()

        #sonnerie
        n=(int(math.log2(len(self.mvt_blobs)+1)))
        if n>=1:
            self.ring_bell_multiple_times(n)

        self.label.config(text=f"Images analysées : {self.image_files[self.current_index]} - {self.image_files[self.current_index+1]}")

        self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))
        self.config(cursor="")

    # Fonctions affichage (blobs, image) ================================================================================
    # affiche les taches
    def display_blobs(self):
        if len(self.mvt_blobs)<1000: #limite à 100 ronds bleus
            if (self.zoom_factor>=1):
                    factor=self.img_sizex/self.width/self.zoom_factor #/self.fact_reduc
                    for mvt_blob in self.mvt_blobs:
                        self.canvas.create_oval((mvt_blob[1]-self.blob_size)/factor,(mvt_blob[0]-self.blob_size)/factor,(mvt_blob[1]+ mvt_blob[3] + self.blob_size)/factor,(mvt_blob[0]+mvt_blob[2] + self.blob_size)/factor,outline='blue', width=2)

    # affiche l'image (différence avec les taches)
    def display_image(self, diff_image):
        start = time.perf_counter()
        #base_image = base_image.resize((int(900 * self.zoom_factor), int(600 * self.zoom_factor)))
        diff_image = Image.fromarray(diff_image)
        diff_image = diff_image.resize((int(self.width * self.zoom_factor), int(self.height * self.zoom_factor)))
        print_time("préparation de l'image à afficher",start)

        #self.tk_base_image = ImageTk.PhotoImage(base_image)
        start = time.perf_counter()
        self.tk_diff_image = ImageTk.PhotoImage(diff_image)

        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_diff_image)
        print_time("Affichage 900x600, zoom " + str(self.zoom_factor),start)
    
    # affiche une des images originales (par la touche espace)
    def display_img_mode(self, event=None):
        print("\n")
        # Chemin de l'image
        start = time.perf_counter()
        self.mode_image+=1
        if self.mode_image ==3:
            self.mode_image=1
        if self.mode_image == 1 :
            img = self.img1
        else :
            img = self.img2
        #img = cv2.imread(image_path)
        print_time("Lecture image " ,start)
        
        # Vérifier si l'image a été correctement chargée
        if img is None:
            print(f"Erreur : Impossible de charger l'image à partir de {image_path}")
            return
        
        # Convertir l'image de BGR à RGB, onvertir l'image en objet PIL et redimensionner au zoom
        start = time.perf_counter()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img)
        img_pil = img_pil.resize((int(self.width * self.zoom_factor), int(self.height * self.zoom_factor)))
        print_time("Préparation et dimensionnement " ,start)

        # Convertir l'image PIL en PhotoImage
        start = time.perf_counter()
        img_tk = ImageTk.PhotoImage(image=img_pil)
        print_time("Conversion " ,start)
        
        # Supprimer tout contenu précédent du canevas etaffichge
        start = time.perf_counter()
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
        print_time("Affichage " ,start)
        
        # Conserver une référence de l'image pour éviter qu'elle ne soit garbage collected
        self.canvas.image = img_tk

    # Fonctions gestions du zoom ================================================================================

    def zoom_in(self, event):
        #on s'approche, pour l'instant il faut refaire l'analyse totale
        self.old_zoom = self.zoom_factor
        self.oldxview = self.canvas.xview()
        self.oldyview = self.canvas.yview()
        if self.zoom_factor<=8:
            self.zoom_factor*=2
            mouse_x = self.canvas.canvasx(event.x)
            mouse_y = self.canvas.canvasy(event.y)

            self.update_image()
            #self.display_image(self.diff_image)
            #self.display_blobs()
            # Recentrer sur le point cliqué
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()
            self.canvas.xview_moveto((mouse_x/self.old_zoom) / canvas_width*(self.zoom_factor-1)/self.zoom_factor)
            self.canvas.yview_moveto((mouse_y /self.old_zoom) / canvas_height*(self.zoom_factor-1)/self.zoom_factor)


    def reset_zoom(self, event):
        #on s'éloigne, pas besoin de refire l'analyse
        self.zoom_factor = 1.0
        #self.update_image()
        self.display_image(self.diff_image)
        self.display_blobs()
        self.display_polygon()
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)




    def load_new_directory(self):
        # charger un répertoire (gestion du mode AUTO)
        self.auto=self.auto_var.get()
        print ("Auto=",self.auto)
        old_index=self.current_index
        new_directory = self.directory_var.get()      
        if not os.path.isdir(new_directory):
            print("Le répertoire n'existe pas !")
            return
        
        # Trouver toutes les images dans le répertoire
        image_extensions = ("*.jpg", "*.jpeg", "*.png")  # Formats d'image
        self.image_files = []
        for ext in image_extensions:
            self.image_files.extend(sorted(glob.glob(os.path.join(new_directory, ext))))
        
        if len(self.image_files) < 2:
            print("Pas assez d'images pour comparer !")
            return
        else :
            # affichage du nombre total pour savor
            self.label_nav.config(text=f"navigation ({len(self.image_files)-2})")
        
        # Réinitialiser l'index et mettre à jour l'interface
        if self.auto:
            if self.current_index<len(self.image_files)-2:
                self.current_index = self.current_index + 1
        else:
            self.current_index = 0

        # si on a encore qq chose à faire (reste 1 image ou )
        if old_index!=self.current_index or not self.auto:
            self.slider.set(self.current_index)
            if not self.auto:
                self.zoom_factor = 1
            self.slider.config(to=len(self.image_files) - 2)
            self.update_image()

        # en mode auto on charge l'image suivante    
        if (self.auto):
            self.after(4000, self.load_new_directory)




''' 
==================================================================================================================================
Lancement du programme principal
==================================================================================================================================
'''

path="img/img0" #dossier pour les images

app = ImageViewer(path)
app.mainloop()
