import joblib
import pandas as pd

# Charger le modèle
reg_model = joblib.load('model_ml/model_valeurs.pkl')

# Si tu as le classifieur pluie/pas pluie
clf_model = joblib.load('model_ml/models_ml/model_pluie.pkl')  # si tu as sauvegardé ton RandomForestClassifier
def predict_weather(lon, lat, year, month, day):
    # Créer le dataframe pour le modèle
    X_future = pd.DataFrame([{
        'Longitude': lon,
        'Latitude': lat,
        'Year': year,
        'Month': month,
        'Day': day
    }])
    
    # Prédiction des valeurs continues
    y_future = reg_model.predict(X_future)
    targets = ['Temp_Moyenne','Humidite','Vent','Rayonnement_Total','Rayonnement_Ciel_Clair','Precipitation']
    df_future = pd.DataFrame(y_future, columns=targets)
    
    # Prédiction pluie/non pluie
    rain_pred = clf_model.predict(df_future)[0]
    rain_proba = clf_model.predict_proba(df_future)[0][1]
    
    # Retourner un dictionnaire
    result = df_future.iloc[0].to_dict()
    result['Rain'] = int(rain_pred)
    result['Rain_Probability'] = float(rain_proba)
    
    return result
