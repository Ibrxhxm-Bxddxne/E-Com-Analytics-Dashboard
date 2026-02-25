##📊 E-Com Analytics Dashboard
Un tableau de bord analytique haute performance permettant de visualiser, gérer et analyser des données de ventes e-commerce. Ce projet transforme des données brutes issues de fichiers CSV en insights exploitables grâce à une interface moderne et réactive.

✨ Fonctionnalités
📈 Visualisation de Données : Graphiques interactifs (Area, Bar, Pie) avec ApexCharts pour suivre l'évolution des revenus.

💎 Interface "Glassmorphism" : Design épuré et moderne utilisant Tailwind CSS 4.0.

🔒 Sécurité JWT : Authentification robuste via JSON Web Tokens pour protéger les données sensibles.

🛠️ CRUD Complet : Interface de gestion permettant de créer, lire, mettre à jour et supprimer des transactions en temps réel.

📊 Statistiques Automatisées : Calcul instantané du CA total, des profits et des indicateurs de performance (KPIs) via le backend Django.

📱 Entièrement Responsive : Optimisé pour une utilisation sur desktop, tablette et mobile.

🛠️ Stack Technique
Frontend
Vue 3 (Composition API) & TypeScript

Vite (Build tool ultra-rapide)

Pinia (Gestion d'état globale)

ApexCharts (Moteur de rendu graphique)

Axios (Communication API avec intercepteurs de tokens)

Backend
Django 5 & Django REST Framework (DRF)

SimpleJWT (Gestion de l'authentification)

Pandas (Traitement initial des données CSV)

SQLite (Base de données par défaut)

🚀 Installation et Lancement
1. Cloner le projet
Bash
git clone https://github.com/votre-username/DashboardEcom.git
cd DashboardEcom
2. Configuration du Backend (Django)
Bash
cd backend
python -m venv venv
# Windows: venv\Scripts\activate | Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # Pour accéder à l'admin
python manage.py runserver
3. Configuration du Frontend (Vue.js)
Bash
cd ../frontend
npm install
npm run dev
Accédez à l'application sur : http://localhost:5173

📂 Structure du Projet
Plaintext
├── backend/            # API Django REST
│   ├── core/           # Configuration du projet
│   ├── sales/          # Application de gestion des ventes (Modèles, Vues, Serializers)
│   └── manage.py
├── frontend/           # Application Vue.js
│   ├── src/
│   │   ├── api.ts      # Configuration Axios
│   │   ├── stores/     # Pinia (Auth store)
│   │   ├── views/      # Dashboard & Login
│   │   └── types/      # Interfaces TypeScript
│   └── tailwind.config.js
└── README.md
