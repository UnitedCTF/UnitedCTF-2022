const express = require("express");
const path = require('path');
const app = express();
const port = 3000;

app.set('views', path.join(__dirname, '/views'));
app.set('view engine', 'pug');

app.listen(port, () => {
  console.log("Server Started...");
})

// Fake DB
const lstRecette = [
  { id: 0, titre: "Dasani", source: "https://www.dasani.com/products/water", lstIngredient: ["eau purifiée", " sulfate de magnésium", " chlorure de potassium", " sel"], image: "https://www.dasani.com/content/dam/nagbrands/us/dasani/en/products/dasani-pdp-20oz.png" },
  { id: 1, titre: "Coke original", source: "https://highon.coffee/blog/insecure-direct-object-reference-idor/", lstIngredient: ["FLAG-F0R-Y0UR-3Y35-0N1Y"], image: "https://us.coca-cola.com/content/dam/nagbrands/us/coke/en/products/coca-cola-original/desktop/coca-cola-original-12oz.jpg" },
  { id: 2, titre: "Fresca", source: "https://www.fresca.com/products/peach-citrus", lstIngredient: ["eau gazéifiée", " acide citrique", " arômes naturels", " citrate de potassium", " jus de pamplemousse concentré", " aspartame", " sorbate de potassium (pour protéger le goût)", " acésulfame de potassium", " gomme d'acacia", " benzoate de potassium (pour protéger le goût)", " ester glycérolique de résine", " edta de calcium disodique (pour protect goût)", " gomme de caroube"], image: "https://www.fresca.com/content/dam/nagbrands/us/fresca/en/products/heros/peach-citrus-hero_desktop.jpg" },
  { id: 3, titre: "Jus d'orange original premium", source: "https://www.minutemaid.com/products/orange-juice/premium-original-orange-juice/", lstIngredient: ["eau pure filtrée", " jus d'orange concentré premium"], image: "https://www.minutemaid.com/content/dam/nagbrands/us/minutemaidus/en/products/orange-juice/premium-original-oj/Minute-Maid_Orange-Juice_Original-Low-Pulp_59oz.png" },
]

const db = {
  "Eve": { recette: [lstRecette[2], lstRecette[3]] }
}

app.get("/", (req, res) => {
  res.set('Super-Secret', 'FLAG-N0-M0R3-53CR3T')
  res.cookie('Secret here','FLAG-N0-F00D-H3R3')
  res.render('home', { title: 'Coca-Cola' });
});

app.get("/recettes", (req, res) => {
  res.render('recettes', { title: 'Recettes de la maison', lstRecette: db.Eve.recette });
});

app.get("/recette/:id", (req, res) => {
  if (!isNaN(req.params.id) && 0 <= req.params.id && req.params.id < lstRecette.length) {
    res.render('recette', { recette: lstRecette[req.params.id], title: lstRecette[req.params.id].titre });
  }
  res.status(404).render('404');
});

app.use(express.static('public'))

app.get("/robots.txt", (req, res) => {
  res.sendFile('robots.txt', { root: path.join(__dirname) });
});

app.get("*", (req, res) => {
  res.status(404).render('404');
});