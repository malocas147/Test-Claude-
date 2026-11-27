#!/usr/bin/env python3
"""Build the five Atelier Azar pages from shared header/footer parts.

Edit the page bodies below, then run:  python3 tools/build_atelier.py
Output: atelier-azar/{index,collections,films,atelier,contact}.html
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "atelier-azar"

PAGES = [  # file, menu label, <title>, description
    ("index.html", "Accueil", "Atelier Azar", "Atelier Azar, lampes monumentales de 3 à 4 mètres créées à Genève par Pascal Pupillo."),
    ("collections.html", "Collections", "Collections – Atelier Azar", "Shanghai, Kailedo, Omaya, Saint-Moritz et Bali : cinq lampes monumentales en versions XL (3 m) et XXL (4 m)."),
    ("films.html", "Films & Inspirations", "Films & Inspirations – Atelier Azar", "Les lampes Atelier Azar en situation : films réalisés par IA et mises en scène dans des lieux d'exception."),
    ("atelier.html", "L'Atelier", "L'Atelier – Atelier Azar", "Pascal Pupillo et l'histoire d'Atelier Azar, né à Genève en 2025 : la lumière devient sculpture."),
    ("contact.html", "Contact", "Contact – Atelier Azar", "Parlez-nous de votre lieu : Atelier Azar, Avenue de Châtelaine 36, Genève. +41 22 777 00 70."),
]

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">')


def head(title, desc, preload=""):
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="claude:viewport-fit-sides" content="cover">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="img/hero-poster.webp">
{preload}{FONTS}
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
"""


def header(current):
    links = "".join(
        f'<a href="{f}"{" aria-current=\"page\"" if f == current else ""}>{label}</a>'
        for f, label, *_ in PAGES)
    return f"""<header id="top">
  <button class="pill menu-btn" id="menuBtn" aria-expanded="false" aria-controls="drawer"><i></i><span>Menu</span></button>
  <a class="logo" href="index.html" aria-label="Atelier Azar, accueil"><img class="ll" src="img/logo-light.png" alt="Atelier Azar"><img class="ld" src="img/logo-dark.png" alt=""></a>
  <a class="pill cta" href="contact.html"><span>Contact</span><span aria-hidden="true" style="display:inline">→</span></a>
</header>
<div class="drawer" id="drawer" hidden>
  <button class="pill" id="drawerClose">Fermer</button>
  <nav aria-label="Menu">{links}</nav>
  <aside><p class="info">Atelier Azar Sàrl · Avenue de Châtelaine 36, CH-1203 Genève<br>+41 22 777 00 70 · info@redzone.ch</p></aside>
</div>
"""


FOOTER = """<footer class="band">
  <div class="cols">
    <div><img src="img/logo-dark.png" alt="Atelier Azar" style="margin-bottom:18px"><p>Lampes monumentales et objets hors échelle, imaginés à Genève.</p></div>
    <div><h4>Pages</h4><nav><a href="collections.html">Collections</a><a href="films.html">Films &amp; Inspirations</a><a href="atelier.html">L'Atelier</a><a href="contact.html">Contact</a></nav></div>
    <div><h4>Atelier</h4><p>Avenue de Châtelaine 36<br>CH-1203 Genève, Suisse</p></div>
    <div><h4>Contact</h4><nav><a href="tel:+41227770070">+41 22 777 00 70</a><a href="mailto:info@redzone.ch">info@redzone.ch</a></nav></div>
  </div>
  <div class="legal"><span>© 2026 Atelier Azar Sàrl, Genève</span><span>Films et mises en situation réalisés par IA</span></div>
</footer>
"""

LIGHTBOX = """<div class="lb" id="lb" hidden role="dialog" aria-modal="true" aria-label="Fiche produit">
  <button class="x pill" id="lbClose">Fermer</button>
  <img id="lbImg" alt="">
  <aside id="lbInfo"></aside>
</div>
"""

TAIL = '<script src="assets/site.js"></script>\n</body>\n</html>\n'

INTRO_FLAG = ("<script>try{if(!matchMedia('(prefers-reduced-motion: reduce)').matches&&!sessionStorage.getItem('azarIntro'))"
              "document.documentElement.classList.add('intro-on')}catch(e){document.documentElement.classList.add('intro-on')}</script>\n")


def page_hero(label, title, text, media, short=False):
    return f"""<section class="page-hero{' short' if short else ''}">
  {media}
  <div class="copy"><p class="label">{label}</p><h1>{title}</h1><p>{text}</p></div>
</section>
"""


def cta(title, text, primary=("contact.html", "Parler de votre projet"), secondary=None):
    sec = f'<a class="btn" href="{secondary[0]}">{secondary[1]}</a>' if secondary else ""
    return f"""<section class="band cta-band">
  <div class="wrap">
    <div><h2>{title}</h2><p style="margin:16px 0 0;color:var(--soft);max-width:32em">{text}</p></div>
    <div class="acts"><a class="btn fill" href="{primary[0]}">{primary[1]}</a>{sec}</div>
  </div>
</section>
"""


TEASE = [("shanghai", "Shanghai", "shanghai-xl", "Le piédestal laqué noir aux lignes de pagode."),
         ("kailedo", "Kailedo", "kailedo-champagne-xl", "Trois blocs martelés qui accrochent la lumière."),
         ("omaya", "Omaya", "omaya-silver-xl", "Une colonne miroir creusée d'alvéoles et de LED.")]

HOME = INTRO_FLAG + header("index.html") + """<main>
<section class="hero" id="accueil">
  <!-- Film IA d'accueil : video/riviera.mp4 (ordinateur) et video/riviera-mobile.mp4 (écrans verticaux), montés en aller-retour pour une boucle sans saut -->
  <video class="v" autoplay muted loop playsinline preload="auto" poster="img/hero-poster.webp"><source src="video/riviera-mobile.mp4" type="video/mp4" media="(max-aspect-ratio: 4/5)"><source src="video/riviera.mp4" type="video/mp4"></video>
  <div class="opening" id="intro" aria-hidden="true">
    <img class="mono" src="img/mono-light.png" alt="">
    <svg viewBox="0 0 760 90"><text x="380" y="70" text-anchor="middle">ATELIER AZAR</text></svg>
    <p class="tag">Lampes monumentales, Genève</p>
  </div>
  <div class="copy">
    <div>
      <h1>La lumière devient sculpture</h1>
      <p>Lampes monumentales de trois à quatre mètres, imaginées à Genève pour habiter les lieux d'exception.</p>
    </div>
    <div class="ctl">
      <a class="btn" href="collections.html">Découvrir les collections</a>
      <span><button class="vbtn" id="heroToggle" aria-pressed="false">Pause</button> <span class="ai">Film réalisé par IA</span></span>
    </div>
  </div>
</section>

<section class="band manifesto">
  <div class="wrap">
    <blockquote>Car le hasard n'existe pas… il se provoque, il se construit, il se crée.</blockquote>
    <div class="txt">
      <p class="label">Atelier Azar, un nom qui intrigue</p>
      <p><strong>Des objets architecturaux conçus pour habiter les espaces avec caractère et émotion.</strong> Entre influences méditerranéennes, inspirations asiatiques et minimalisme contemporain, chaque pièce cherche à provoquer un sentiment de puissance, de sérénité et d'émerveillement.</p>
      <p>Ses pièces dépassent la simple fonction décorative. Elles deviennent des présences.</p>
    </div>
  </div>
</section>

<section class="band" style="padding-top:0">
  <div class="wrap">
    <div class="head"><h2>Les collections</h2><p>Cinq silhouettes, chacune en version XL (3 m) ou XXL (4 m), en finitions Black, Silver, Champagne, Woodee ou laque blanche.</p></div>
    <div class="teasers">""" + "".join(
    f'<a class="tcard" href="collections.html#{i}"><div class="ph"><img class="fx" src="img/{img}.webp" alt="{n}, lampe monumentale à côté d\'une personne de 1,80 m" loading="lazy" decoding="async"></div><h3>{n}</h3><p>{d}</p></a>'
    for i, n, img, d in TEASE) + """</div>
    <p style="margin-top:36px"><a class="more" href="collections.html">Voir les cinq collections →</a></p>
  </div>
</section>

<section class="feature">
  <img class="fx" src="img/scene-terrasse.webp" alt="Lampe Omaya Silver sur une terrasse en béton au couchant" loading="lazy" decoding="async">
  <div class="inner">
    <p class="label">Films &amp; Inspirations</p>
    <h2>Chaque pièce se révèle d'abord en film</h2>
    <p>Terrasses au couchant, jardins de palmiers, salons face à la mer : nos films IA projettent chaque lampe dans des lieux qui lui ressemblent.</p>
    <p style="margin-top:24px"><a class="btn" href="films.html">Voir les films</a></p>
  </div>
</section>

<section class="band split">
  <div class="wrap">
    <img class="fx" src="img/scene-salon.webp" alt="Lampe Kailedo dans un salon ouvert sur l'océan au crépuscule" loading="lazy" decoding="async">
    <div class="txt">
      <p class="label">L'Atelier</p>
      <h2 style="margin:12px 0 22px">Pascal Pupillo, rêver grand</h2>
      <p>Né à Dakar en 1978, nourri par Londres, l'Asie et vingt-cinq ans d'expériences visuelles immersives à Genève, Pascal Pupillo fonde Atelier Azar en 2025 avec une idée : des lampes géantes capables de transformer un lieu en émotion.</p>
      <p style="margin-top:24px"><a class="more" href="atelier.html">Découvrir l'histoire →</a></p>
    </div>
  </div>
</section>

<section class="band" style="padding-top:0">
  <div class="wrap">
    <div class="head"><h2>Inspirations</h2><p>Riviera, désert, Méditerranée : les pièces en situation.</p></div>
    <div class="strip">
      <a href="films.html#inspirations"><img class="fx" src="img/scene-riviera.webp" alt="Shanghai Black au bord d'une piscine à débordement" loading="lazy" decoding="async"></a>
      <a href="films.html#inspirations"><img class="fx" src="img/scene-desert-silver.webp" alt="Omaya Silver dans un jardin de palmiers, la nuit" loading="lazy" decoding="async"></a>
      <a href="films.html#inspirations"><img class="fx" src="img/scene-bali-console.webp" alt="Deux lampes Bali sur une console ancienne" loading="lazy" decoding="async"></a>
    </div>
  </div>
</section>
""" + cta("Parlons de votre lieu", "Villa, hôtel, yacht club ou événement : chaque pièce est réalisée à la demande.", secondary=("atelier.html#projet", "Comment ça se passe")) + "</main>\n"

COLLECTIONS = header("collections.html") + "<main>\n" + page_hero(
    "Collections", "Cinq silhouettes, deux échelles",
    "Chaque modèle existe en XL (3 m) et XXL (4 m). Choisissez une finition, puis ouvrez la fiche pour voir les cotes.",
    '<img src="img/scene-bali-console.webp" alt="Deux lampes Bali sur une console ancienne, entre deux palmiers" fetchpriority="high">') + """
<section class="band">
  <div class="wrap"><div class="grid" id="grid"></div></div>
</section>

<section class="band scale" id="echelle" style="padding-top:0">
  <div class="wrap">
    <div>
      <h2>Penser à l'échelle</h2>
      <p style="margin-top:18px">Une lampe Atelier Azar se mesure à l'architecture. Indiquez la hauteur sous plafond de votre lieu pour voir quelle version y respire.</p>
      <div class="ctrl">
        <label for="ceil">Hauteur sous plafond <output id="ceilOut">4,80 m</output></label>
        <input type="range" id="ceil" min="2.5" max="8" step="0.1" value="4.8">
      </div>
      <p class="verdict" id="verdict"></p>
    </div>
    <div class="fig" id="fig" role="img" aria-label="Élévation à l'échelle : personne de 1,80 m, lampe XL de 3 m et lampe XXL de 4 m sous le plafond choisi"></div>
  </div>
</section>
""" + cta("Un modèle vous parle ?", "Dites-nous lequel, avec la hauteur de votre lieu : nous revenons avec une proposition et un premier film.", primary=("contact.html", "Demander un devis"), secondary=("films.html", "Voir les films")) + "</main>\n" + LIGHTBOX

FILMS = header("films.html") + "<main>\n" + page_hero(
    "Films & Inspirations", "La lumière en situation",
    "Chaque pièce est révélée en film, généré par intelligence artificielle, dans des lieux qui lui ressemblent.",
    '<video class="v" autoplay muted loop playsinline preload="auto" poster="img/hero-poster.webp"><source src="video/riviera-mobile.mp4" type="video/mp4" media="(max-aspect-ratio: 4/5)"><source src="video/riviera.mp4" type="video/mp4"></video>') + """
<section class="band films" id="films">
  <div class="wrap">
    <div class="head"><h2>Les films</h2><p>Une terrasse au couchant, un jardin de palmiers, un salon face à la mer.</p></div>
    <figure class="lead">
      <video class="v" muted loop playsinline preload="none" poster="img/scene-terrasse.webp"><source src="video/terrasse.mp4" type="video/mp4"></video>
      <figcaption><p class="label" style="color:#e6dccd">Omaya Silver XXL</p><h3>Une terrasse suspendue au-dessus des collines</h3></figcaption>
    </figure>
    <div class="row">
      <figure><video class="v" muted loop playsinline preload="none" poster="img/scene-desert-champagne.webp" style="height:100%;object-fit:cover"><source src="video/desert.mp4" type="video/mp4"></video></figure>
      <figure><video class="v" muted loop playsinline preload="none" poster="img/scene-bali-terrasse.webp" style="height:100%;object-fit:cover"><source src="video/bali.mp4" type="video/mp4"></video></figure>
      <div class="note">
        <p class="label">Votre lieu, avant la fabrication</p>
        <h3 style="margin:12px 0 16px">Voir la lampe chez soi</h3>
        <p>Envoyez quelques photos de votre espace : nous réalisons un film IA de la pièce choisie, à l'échelle, dans votre décor. Vous validez la proportion et la finition avant que l'atelier ne commence.</p>
        <p><a class="btn fill" href="contact.html">Demander un film</a></p>
      </div>
    </div>
  </div>
</section>

<section class="band" id="inspirations" style="padding-top:0">
  <div class="wrap">
    <div class="head"><h2>Inspirations</h2><p>Riviera, désert, Méditerranée : les pièces en situation. Touchez une image pour l'agrandir.</p></div>
    <div class="mosaic" id="mosaic"></div>
  </div>
</section>
""" + cta("Imaginez-la chez vous", "Nous réalisons un film de la lampe choisie dans votre propre décor.", primary=("contact.html", "Demander un film"), secondary=("collections.html", "Voir les collections")) + "</main>\n" + LIGHTBOX

ATELIER = header("atelier.html") + "<main>\n" + page_hero(
    "L'Atelier", "Rêver grand",
    "Atelier Azar, un nom qui laisse planer le mystère sur ce qui se cache réellement derrière lui.",
    '<img src="img/scene-salon.webp" alt="Lampe Kailedo dans un salon ouvert sur l\'océan au crépuscule" fetchpriority="high">') + """
<section class="band">
  <div class="wrap story">
    <p class="big">Car le hasard n'existe pas… il se provoque, il se construit, il se crée.</p>
    <p>Né à Dakar, au Sénégal, en 1978, Pascal Pupillo grandit entre les cultures, les voyages et les influences du monde. Très jeune déjà, il développe une fascination profonde pour l'architecture, les volumes et les atmosphères hors normes. Depuis l'enfance, une idée ne l'a jamais quitté : rêver grand.</p>
  </div>
</section>

<section class="band split" style="padding-top:0">
  <div class="wrap">
    <img class="fx" src="img/scene-desert-champagne.webp" alt="Lampe Omaya Champagne entre les braseros d'un jardin de palmiers" loading="lazy" decoding="async">
    <div class="txt">
      <p class="label">Le monde comme atelier</p>
      <h2 style="margin:12px 0 22px">De Swissair à l'Asie</h2>
      <p>Son parcours débute dans l'aviation, auprès de la compagnie Swissair, une expérience qui renforce encore son ouverture au monde. Londres, puis l'Asie, à travers d'innombrables voyages en Thaïlande, en Chine, au Japon, en Corée, en Indonésie, aux Philippines et aux États-Unis, deviennent des terrains d'inspiration permanents.</p>
      <p>Chaque destination nourrit son regard, affine sa sensibilité et façonne peu à peu un univers artistique singulier, entre minimalisme architectural, luxe contemporain et émotion lumineuse.</p>
    </div>
  </div>
</section>

<section class="band split rev" style="padding-top:0">
  <div class="wrap">
    <img class="fx" src="img/scene-riviera.webp" alt="Lampe Shanghai Black au bord d'une piscine à débordement" loading="lazy" decoding="async">
    <div class="txt">
      <p class="label">Genève, 2025</p>
      <h2 style="margin:12px 0 22px">La naissance d'Atelier Azar</h2>
      <p>Pendant plus de 25 ans, Pascal Pupillo évolue dans l'événementiel à Genève avec sa société Red Zone, où il imagine des expériences visuelles immersives et spectaculaires. Mais derrière cette aventure, un rêve plus profond continuait de grandir : créer des œuvres monumentales, des lampes géantes et des objets hors échelle capables de transformer un lieu en émotion.</p>
      <p>C'est ainsi qu'est né Atelier Azar, en 2025.</p>
    </div>
  </div>
</section>

<section class="band" style="padding-top:0">
  <div class="wrap">
    <div class="head"><h2>Une signature</h2><p>La lumière devient sculpture, les matières dialoguent avec l'architecture, et chaque création cherche à provoquer un sentiment de puissance, de sérénité et d'émerveillement.</p></div>
    <div class="values">
      <div><p class="label">Méditerranée</p><h3>La lumière du soir</h3><p>Terrasses, pierre chaude et horizons marins : des pièces pensées pour la douceur des fins de journée.</p></div>
      <div><p class="label">Asie</p><h3>Le sens des volumes</h3><p>Lignes de pagode, laques et proportions architecturales, rapportées de longues années de voyages.</p></div>
      <div><p class="label">Minimalisme</p><h3>Des présences</h3><p>Des objets qui dépassent la simple fonction décorative pour habiter les espaces avec caractère et émotion.</p></div>
    </div>
    <p class="lede" style="margin-top:56px">Un luxe différent : émotionnel, intemporel et profondément expérientiel.</p>
  </div>
</section>

<section class="band" id="projet" style="padding-top:0">
  <div class="wrap">
    <div class="head"><h2>Un projet, pas à pas</h2><p>Pour une villa, un hôtel, un yacht club ou un événement.</p></div>
    <div class="steps">
      <div><div class="n">I</div><h3>Rencontre</h3><p>Votre lieu, vos volumes, l'émotion recherchée. Choix du modèle, de la taille et de la finition.</p></div>
      <div><div class="n">II</div><h3>Film de projection</h3><p>Un film IA de la lampe dans votre espace, pour valider l'échelle et la lumière.</p></div>
      <div><div class="n">III</div><h3>Création</h3><p>Fabrication de la pièce, abat-jour et éclairage LED sur mesure.</p></div>
      <div><div class="n">IV</div><h3>Installation</h3><p>Livraison et mise en lumière sur place, en intérieur comme en extérieur.</p></div>
    </div>
  </div>
</section>
""" + cta("Commençons par votre lieu", "Une première conversation suffit pour choisir le modèle et l'échelle.", secondary=("collections.html", "Voir les collections")) + "</main>\n"

CONTACT = header("contact.html") + "<main>\n" + page_hero(
    "Contact", "Parlons de votre lieu",
    "Chaque pièce est réalisée à la demande. Décrivez votre projet, nous revenons vers vous avec une proposition et un premier film.",
    '<img src="img/scene-desert-silver.webp" alt="Lampe Omaya Silver dans un jardin de palmiers, la nuit" fetchpriority="high" style="object-position:50% 40%">',
    short=True) + """
<section class="band contact">
  <div class="wrap">
    <div>
      <h2>Atelier Azar</h2>
      <address>
        Atelier Azar Sàrl<br>
        Avenue de Châtelaine 36<br>
        CH-1203 Genève, Suisse<br>
        <a href="tel:+41227770070">+41 22 777 00 70</a><br>
        <a href="mailto:info@redzone.ch">info@redzone.ch</a>
      </address>
      <p class="label" style="margin-top:36px">Utile pour une première réponse</p>
      <ul class="checklist">
        <li>Le lieu : villa, hôtel, terrasse, événement</li>
        <li>La hauteur sous plafond, ou « extérieur »</li>
        <li>Le modèle et la finition qui vous attirent</li>
        <li>Quelques photos de l'espace, pour votre film</li>
        <li>Le délai souhaité</li>
      </ul>
    </div>
    <form id="form" novalidate>
      <div><label for="f-name">Nom</label><input id="f-name" name="name" autocomplete="name" required></div>
      <div><label for="f-mail">E-mail</label><input id="f-mail" name="email" type="email" autocomplete="email" required></div>
      <div><label for="f-tel">Téléphone</label><input id="f-tel" name="tel" type="tel" autocomplete="tel"></div>
      <div><label for="f-model">Modèle</label><select id="f-model" name="model"><option>Je ne sais pas encore</option></select></div>
      <div class="full"><label for="f-msg">Votre projet</label><textarea id="f-msg" name="msg" placeholder="Lieu, hauteur sous plafond, intérieur ou extérieur, délai…"></textarea></div>
      <div class="full"><button class="btn fill" type="submit">Envoyer la demande</button></div>
    </form>
  </div>
</section>
</main>
"""

BODIES = {"index.html": HOME, "collections.html": COLLECTIONS, "films.html": FILMS, "atelier.html": ATELIER, "contact.html": CONTACT}
PRELOAD = {"index.html": '<link rel="preload" as="image" href="img/hero-poster.webp" fetchpriority="high">\n'}

for f, _, title, desc in PAGES:
    html = head(title, desc, PRELOAD.get(f, "")) + BODIES[f] + FOOTER + TAIL
    (OUT / f).write_text(html, encoding="utf-8")
    print(f, len(html.splitlines()), "lines")
