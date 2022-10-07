# La recette secrète

## Write-up

En observant le site web, il y a une page `Mes recettes`. En y allant, on découvre qu’on a seulement accès à quelques recettes. Il n’y a pas celle qui nous intéresse : la recette du Coke original.

Lorsqu’on clique sur le lien d’une des recettes, on voit dans l’URL de celle-ci un numéro qui correspond au numéro de la recette.

Si l’on change le numéro pour `1`, on obtient l’URL qui termine par `/recette/1`.

Cette vulnérabilité est nommée `référence directe non sécurisée à un objet` ([IDOR en anglais](https://highon.coffee/blog/insecure-direct-object-reference-idor/))

## Flag

`FLAG-F0R-Y0UR-3Y35-0N1Y`
