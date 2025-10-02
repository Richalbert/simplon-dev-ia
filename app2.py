import plotly.express as px
import pandas as pd

donnees = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv') # Note the variable name change here

figure = px.pie(donnees, values='qte', names='produit', title='quantité vendue par produit') # Updated variable name here

figure.write_html('ventes-par-produit.html') # Updated filename here

print('ventes-par-produit.html généré avec succès !') # Updated message here    