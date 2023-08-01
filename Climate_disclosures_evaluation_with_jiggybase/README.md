# Climate Disclosures Evaluation with JiggyBase (English version)

## Data Collection and Preparation

The first step of our project involves collecting ESG disclosures from various sources, including company websites, TCFD hub, and CDP. These reports, typically in PDF format, are then processed to extract textual information and clean the data. This ensures that the data is of high quality and suited for further analysis.

## Creation of an ESG Disclosures Corpus

After cleaning, ESG reports are stored in regularly updated corpora. These corpora provide a rich source of data for evaluating the ESG performance of public companies.

## Vectorization and Integration

To make our ESG disclosures corpus compatible with language models, we need to convert the textual data into vectors - a process known as vectorization. Our proprietary tool, Jiggybase, automatically handles this vectorization step.

## Fact Checking with Jiggybase

Jiggybase is a private ChatGPT interface that extends the OpenAI product by connecting it to our external database containing ESG reports. This allows ChatGPT to access up-to-date information on a large scale, enabling it to provide more accurate responses. We will use Jiggybase for fact-checking, which is a classification problem with three possible outcomes: the fact is supported by the information in the database, it is not, or there is not enough information to make a decision.

## ESG Frameworks and Prompt Engineering

We evaluate ESG disclosures using the ESG framework established by the Transition Pathway Initiative (TPI). To adapt TPI's questions to our model, we use a process known as prompt engineering. This process is critical as large language models can produce very different outputs from small changes in the input.

## Maturity Level Evaluation

After processing the reports and fact-checking, we can assign a maturity level to each company. For example, a company whose 18 facts are supported by our model would receive the highest maturity level (4), while a company whose facts are not supported or cannot be verified would receive a lower maturity level.

The maturity level evaluation helps us quickly and on a large scale understand the current ESG landscape. Our goal is to provide a tool for investors and public institutions that can measure companies' transition capabilities both regionally and globally.


# Méthodologie d'Évaluation des Divulgations ESG (Version francaise)

Notre projet vise à évaluer à grande échelle les divulgations Environnementales, Sociales et de Gouvernance (ESG) des entreprises.

## Collecte et Préparation des Données

La première étape de notre projet consiste à collecter les divulgations ESG à partir de diverses sources, notamment les sites Web d'entreprises, le TCFD hub et le CDP. Ces rapports, généralement sous format PDF, sont ensuite traités pour extraire les informations textuelles et nettoyer les données. Cela garantit que les données sont de haute qualité et adaptées à l'analyse ultérieure.

## Création d'un Corpus de Divulgations ESG

Après le nettoyage, les rapports ESG sont stockés dans des corpus mis à jour régulièrement. Ces corpus fournissent une source riche de données pour évaluer les performances ESG des entreprises publiques.

## Vectorisation et Intégration

Afin de rendre notre corpus de divulgations ESG compatible avec les modèles de langage, nous devons convertir les données textuelles en vecteurs - un processus connu sous le nom de vectorisation. Notre outil propriétaire, Jiggybase, gère automatiquement cette étape de vectorisation.

## Vérification des Faits avec Jiggybase

Jiggybase est une interface privée ChatGPT qui étend le produit OpenAI en le connectant à notre base de données externe contenant les rapports ESG. Cela permet à ChatGPT d'accéder à des informations à jour à grande échelle, lui permettant de fournir des réponses plus précises. Nous utiliserons Jiggybase pour de la vérification des faits, qui est un problème de classification avec trois résultats possibles : le fait est soutenu par l'information dans la base de données, il ne l'est pas, ou il n'y a pas assez d'informations pour prendre une décision.

## Cadres ESG et “Prompt engineering”

Nous évaluons les divulgations ESG en utilisant le cadre ESG établi par l'Initiative de Transition de Trajectoire (TPI). Pour adapter les questions du TPI à notre modèle, nous utilisons un processus connu sous le nom d'ingénierie des prompts. Ce processus est crucial car les grands modèles de langage peuvent produire des sorties très différentes à partir de petits changements dans l'entrée.

## Évaluation du Niveau de Maturité

Après avoir traité les rapports et vérifié les faits, nous pouvons attribuer un niveau de maturité à chaque entreprise. Par exemple, une entreprise dont les 18 faits sont soutenus par notre modèle recevrait le niveau de maturité le plus élevé (4), tandis qu'une entreprise dont les faits ne sont pas soutenus ou ne peuvent être vérifiés recevrait un niveau de maturité inférieur.

L'évaluation du niveau de maturité nous aide à comprendre rapidement et à grande échelle le paysage ESG actuel. Notre objectif est de fournir un outil pour les investisseurs et les institutions publiques qui peut mesurer les capacités de transition des entreprises à la fois au niveau régional et mondial.

