# Utilisation de l'API cryptocompare pour récupérer les données

## Frontend
L'interface utilisateur est construite avec du bootstrap. 
Elle affiche les articles récupérés de CryptoCompare, probablement dans un format `card` avec des images, des titres et 
des résumés des articles.

## Backend
Le backend est développé avec Django, un framework web Python. Il gère les requêtes HTTP, interagit avec l'API de 
CryptoCompare pour récupérer les articles, et envoie les données au frontend.

## Intégration de l'API
Utilisation de l'API de CryptoCompare pour obtenir les dernièrs articles sur les crypto-monnaies.
Possibilité d'inclure des fonctionnalités telles que le filtrage par catégorie de nouvelles, la recherche par mot-clé, ou 
le tri par date.

## Déploiement
Le projet est déployé sur un serveur web, avec une attention particulière à la sécurité, à la performance, et à la 
scalabilité. Il nécessite une maintenance régulière pour s'assurer que l'intégration avec l'API de CryptoCompare 
fonctionne correctement et que le site reste à jour avec les dernières pratiques de développement web.