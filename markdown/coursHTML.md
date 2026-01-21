### Le langage HTML

1. HTML

HyperText Markup *Langage de balises hypertexte*

un fichier `.html` est un fichier de texte (comme le markdown par exemple). On ouvre un fichier de 2 façons:
-le développeur => avec un éditeur de code (ex: VisualStudioCode)
- l'utilisateur => avec un navigateur (ex: firefox)

le plus souvent les balises html sont en couple (ouvrante/fermante) mais il existe aussi des balises *orpheline*:
- `<MaBalise></MaBalise>`
- `<Mabalise>`

la structure minimale d'une page web est:

```html
<!DOCTYPE html>
<html>
<head></head>
<body></body>
</html>
```

Le site de référence pour les langages du WEB des développeurs de Mozilla.
[https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements)

Quelques balises à connaître:
- <body></body> 
- <head></head> contient ce qui n'est pas visible sur la page
- `<hl></hl>`permet de faire de titres sur la page
- `<p></p>`permet de faire un paragraphe
- `<a href=""></a>` permet d'accrocher ;e curseur pour cliquer vers un lien
- `<img src="">` pour insérer une image
- `<br>` pour casser la ligne
- `<ul></ul>` pour réakser une liste sans ordre
- `<ol></ul>` pour réaliser une liste ordonnée
- `<li></li>` pour insérer des items dans une liste


les balises ouvrantes peuvent contenir des attributs définis sur le site de référence ou l'attribut `clas=""`:<br>
`<maBalise attribut=""></maBalise>`

----------------
Pour donner le chemin relatif vers un fichier, on utilise:
- `,/` pour chercher dans le dossier courant
- `,./` pour chercher dans le dossier du dessus


2. Le CSS
Cascading Style Sheet *feuille de style en cascade*
[https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties)

Pour définir du style, il faut un sélecteur (element HTML ou class), des accolades, une propriété, une valeur.

```css
selecteur{
    propriete:valeur;
}

```

On peut écrire le CSS:
-dans le fichier html entre les balises `<style></style>`
dans un fichier dédié avec l'extension`.css`; il faut ajouter
une balise`<link rel="stylesheet" href="">`


Il existe plus de 500 propriétés et encore davantage de valeur possibles mais souvent, les valeurs sont :
- des couleurs (soit un nom soit un code comme rgb(0-255,0-255,0-255))
- des tailles : plusieurs unités sont possible
    -`px` pour pixels
    -`em` relatif à la taille de la police
    -`%`relatif à la taille du contenant 


Rem: Quand le sélecteur css est un élément HTML (par exemple `p`) alors les propriétés s'appliquent à tous les éléments du même type.

Pour différencier des éléments de même nature, on peut utiliser l'attribut `class` ou `id`. Dans ce cas, le sélecteur est le nom de la classe précédé d'un `.` ou le nom l'identifiant précédé d'un `#`


Rem: le contenu d'un élément HTML suit le principe du modèle en boite
[https://www.w3schools.com/css/css_boxmodel.asp](https://www.w3schools.com/css/css_boxmodel.asp)


Trois propriétés importantes sont liées à ce modèle:
- `border` pour le style de la bordure 
- `padding` pour l'espace interne
- `margin` pour la marge autour de la bordure


Rem: il existe des propriétés spécifiques au texte, en particulier:
- `text-align` pour justifier le texte.
- `font` pour la policee de charactères



Ils existes deux balises HTML universelles qui permettent de grouper des éléments ou du texte:
- `<div></div>`
- `<span></span>`

3.Javascript

Il s'agit d'un language de programation comme Python mais initialement dédié au WEB.

C'est un language prévu pour interagir avec une page html: le document peut se représenter ainsi:
image du DOM (Document Object Model:)
window
 ├── alert()
 └── document
      ├── getElementById()
      └── querySelector()
            ↓
         élément HTML
            ├── innerHTML
            ├── style
            │     ├── color
            │     ├── backgroundColor
            │     └── display
            └── addEventListener()

Le JS permet de rendre une page HTML plus dinamique notament grace au formulaire `<from></from>`

les élement Html interactifs sont généralement des `<imput type="">`
-button
-check box
-text
-range
-password


Pour écrire du JS on utilise les balises`<script></script>` et :
-on écrit directement le code dans le fichier 

Pour attraper un élément sur la page afin de la manipuler avec JS, on peut utiliser:
-`querySelector()`
-`getElementById()`


On écrira :
```js
let elementHTML = document.querySelector(""); // avec un sélecteur css
let elementHTML = document.getElementById("") //avec un id
```


la plupart des élément HTML interactifs ont une propriété `value`.

```js
console.log(elementHTML.value);
```

JS est capable d'associer un évènement à un élément HTML:
-click
-change
-input
-mouseover ....

on utilise la méthode `addEventListener()`

```js
elementHTML.addEventListener("event", function(){
    //faire quelquechose
});
```