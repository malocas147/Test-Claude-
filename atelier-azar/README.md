# Atelier Azar, site vitrine

Site statique en une page (`index.html`), sans dépendance : ouvrez le fichier ou déposez le dossier sur n'importe quel hébergeur (Netlify, Vercel, OVH, Infomaniak…).

## Remplacer les vidéos par vos films IA

Les fichiers `video/*.mp4` actuels sont des **vidéos de démonstration** (lent zoom sur les visuels du catalogue). Remplacez-les par vos films IA en gardant les mêmes noms :

| Fichier | Emplacement | Format conseillé |
|---|---|---|
| `video/riviera.mp4` | Plein écran d'accueil | 16:9, 1920×1080 |
| `video/terrasse.mp4` | Section « Les films », grand format | 16:9 |
| `video/desert.mp4` | Section « Les films », vertical | 2:3 ou 9:16 |
| `video/bali.mp4` | Section « Les films », vertical | 2:3 ou 9:16 |
| `video/salon.mp4` | En réserve | 16:9 |

Conseils : 8 à 15 s, en boucle, sans son, H.264, 2 à 5 Mo chacune. Compression :

```
ffmpeg -i film.mov -an -c:v libx264 -crf 24 -preset slow -vf scale=1920:-2 -movflags +faststart video/riviera.mp4
```

L'attribut `poster="img/…webp"` de chaque `<video>` est l'image affichée pendant le chargement : remplacez-la par une image tirée du film.

## Formulaire de contact

Le formulaire prépare un e-mail vers info@redzone.ch dans la messagerie du visiteur. Pour recevoir les demandes directement, branchez un service comme Formspree ou Netlify Forms.
