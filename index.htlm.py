html_content = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Accueil - Versus</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            margin: 0;
            padding: 0;
            text-align: center;
            background-color: #000000;
            color: #fff;
        }
        h1 {
            margin-top: 100px;
            color: #f09db8;
            font-size: 3em;
        }
        h1 span {
            color: white;
        }
        img {
            width: 50%;
            height: auto;
            margin: 10px 0;
            border-radius: 10px;
        }
        .product {
            margin: 10px;
            padding: 10px;
            border: 1px solid #f09db8;
            border-radius: 10px;
            background-color: #333;
            width: 200px;
            text-align: center;
        }
        .product h2 {
            color: #f09db8;
        }
        #products {
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap; /* Pour permettre aux produits de passer à la ligne si l'espace est insuffisant */
        }
        .footer {
            margin-top: 50px;
            background-color: #333;
            padding: 20px;
            color: #fff;
        }
        .footer a {
            color: #f09db8;
            text-decoration: none;
            margin: 0 15px;
        }
        nav ul {
            list-style-type: none;
            padding: 0;
            text-align: center;
            background-color: #333;
        }
        nav ul li {
            display: inline;
            margin-right: 20px;
        }
        nav ul li a {
            color: #fff;
            text-decoration: none;
            padding: 10px 15px;
        }
        nav ul li a:hover {
            background-color: #f09db8;
        }
        #main-content {
            display: block;
        }
        .faq-section {
            background-color: #333;
            padding: 30px;
            margin-top: 30px;
            border-radius: 10px;
        }
        .faq-section h2 {
            color: #f09db8;
        }
        .faq-item {
            margin: 15px 0;
        }
        .faq-item p {
            margin: 5px 0;
        }
    </style>
    <script>
        function acheter(id) {
            var stockElement = document.getElementById(id);
            var stock = parseInt(stockElement.textContent);
            if (stock > 0) {
                stock--;
                stockElement.textContent = stock;
                alert("Achat réussi !");
            } else {
                alert("Stock épuisé !");
            }
        }
    </script>
</head>
<body>
    <div id="main-content">
        <h1><span>Bienvenue sur</span> VERSUS</h1>
        <nav>
            <ul>
                <li><a href="#home">Accueil</a></li>
                <li><a href="#products">Produits</a></li>
                <li><a href="#faq">FAQ</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
        <div id="products">
            <div class="product">
                <h2>Jog</h2>
                <img src="file:///C:/Users/Eleve/Pictures/Vaisseau.png" alt="Vaisseau">
                <p>Stock: <span id="stock1">5</span></p>
                <button onclick="acheter('stock1')">Acheter</button>
            </div>
            <div class="product">
                <h2>Pull 2</h2>
                <img src="file:///C:/Users/Eleve/Pictures/Vaisseau.png" alt="Vaisseau">
                <p>Stock: <span id="stock2">2</span></p>
                <button onclick="acheter('stock2')">Acheter</button>
            </div>
            <div class="product">
                <h2>T-shirt</h2>
                <img src="file:///C:/Users/Eleve/Pictures/Vaisseau.png" alt="Vaisseau">
                <p>Stock: <span id="stock3">0</span></p>
                <button onclick="acheter('stock3')">Acheter</button>
            </div>
        </div>
        <div id="faq" class="faq-section">
            <h2>Foire aux questions (FAQ)</h2>
            <div class="faq-item">
                <h3><strong>Fournisseurs:</strong> Avez-vous rencontré des difficultés à trouver un fournisseur ? Avec quel fournisseur avez-vous finalement décidé de collaborer ? Comment avez-vous fait pour créer les t-shirts ? (sérigraphie, broderie) Avez-vous reçu des prototypes ? Si oui, où peut-on les voir ?</h3>
                <p><strong>Réseaux :</strong> Quelle procédure utilisez-vous pour faire connaître la marque ? (Flyer, vidéo sur internet, etc.) Sur quels réseaux peut-on retrouver la marque ? Combien de posts sur les différents réseaux par semaine ? Comment gérez-vous les différents réseaux ? (montage, post, qui gère les comptes)</p>
            </div>
            <div class="faq-item">
                <h3><strong>Site internet :</strong> Comment avez-vous créé le site ? Comment le site marchera-t-il ? (drop, constamment en ventes) Est-ce qu’on peut déjà accéder au site ? Si oui, quelle est l’adresse internet ?</h3>
                <p><strong>RH :</strong> En quoi consiste votre rôle dans la mini entreprise ?</p>
            </div>
            <div class="faq-item">
                <h3><strong>Comment puis-je contacter le support ?</strong></h3>
                <p>Vous pouvez nous contacter par email à <a href="mailto:versus.core9@gmail.com">versus.core9@gmail.com</a>.</p>
            </div>
        </div>
        <div id="contact" class="footer">
            <p>Contactez-nous à : <a href="mailto:versus.core9@gmail.com">versus.core9@gmail.com</a></p>
            <p>Suivez-nous sur :</p>
            <p>
                <a href="https://www.tiktok.com/@versus.core">TikTok</a>
                <a href="https://www.instagram.com/versus.core">Instagram</a>
            </p>
        </div>
    </div>
</body>
</html>

"""

# Enregistrer dans un fichier HTML
file_name = 'accueil_page.html'
with open(file_name, 'w') as file:
    file.write(html_content)
print(f"Le fichier HTML a été généré sous le nom '{file_name}' avec succès !")
