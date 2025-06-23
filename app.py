
import streamlit as st
import pandas as pd

# CSS styling
st.markdown('''
    <style>
        body, html { background-color: #f9f9f9; }
        .block-container { padding: 2rem; font-size: 20px; }
        h1 { color: #1c1c1e; }
        .stSlider label, .stSlider, .stTextInput input, .stTextInput label {
            font-size: 1.5rem !important;
        }
        .stTextInput input {
            text-align: right;
            font-size: 1.5rem !important;
        }
        .stButton button {
            background-color: #4F46E5;
            color: white;
            font-weight: bold;
            border-radius: 0.5rem;
            padding: 1rem 2rem;
            font-size: 1.5rem;
        }
        table.custom { width:100%; border-collapse: collapse; font-size:22px; }
        table.custom th { text-align:center; font-weight:bold; border-bottom:1px solid #ccc; padding:10px; }
        table.custom td { text-align:right; padding:10px; border-bottom:1px solid #eee; }
        table.custom td.left { text-align:left; }
        table.custom tr.total-row { font-weight:bold; background-color: #eeeeee; }
    </style>
''', unsafe_allow_html=True)

# Translation labels
labels = {
    "English": {"language": "Language", "title": "CSI Profitability Simulator",
                "csi_score": "CSI score (out of 1,000)", "sample_size": "Sample size (Volvo Selekt sales)",
                "ownership_duration": "Ownership duration (years)", "warranty_duration": "Volvo Selekt warranty (years)",
                "vehicle_profit": "Vehicle sale profit", "service_profit": "Service profit per year per customer",
                "run": "Run simulation", "results": "Results", "year": "Year",
                "service_customers": "Service customers", "repeat_purchases": "Repeat purchases",
                "total_profit": "Total profit", "total": "Total", "download": "Download CSV"},
    "Español": {"language": "Idioma", "title": "Simulador de rentabilidad CSI",
                "csi_score": "Puntuación CSI (de 1 000)", "sample_size": "Volumen de ventas Volvo Selekt",
                "ownership_duration": "Duración de propiedad (años)", "warranty_duration": "Garantía Volvo Selekt (años)",
                "vehicle_profit": "Beneficio por venta de vehículo", "service_profit": "Beneficio de servicio por cliente y año",
                "run": "Ejecutar simulación", "results": "Resultados", "year": "Año",
                "service_customers": "Clientes de servicio", "repeat_purchases": "Recompras",
                "total_profit": "Beneficio total", "total": "Total", "download": "Descargar CSV"},
    "Português": {"language": "Idioma", "title": "Simulador de rentabilidade CSI",
                  "csi_score": "Pontuação CSI (de 1 000)", "sample_size": "Vendas Volvo Selekt",
                  "ownership_duration": "Duração de propriedade (anos)", "warranty_duration": "Garantia Volvo Selekt (anos)",
                  "vehicle_profit": "Lucro por venda de veículo", "service_profit": "Lucro de serviço por cliente por ano",
                  "run": "Executar simulação", "results": "Resultados", "year": "Ano",
                  "service_customers": "Clientes de serviço", "repeat_purchases": "Recompras",
                  "total_profit": "Lucro total", "total": "Total", "download": "Baixar CSV"},
    "Français": {"language": "Langue", "title": "Simulateur de rentabilité CSI",
                 "csi_score": "Score CSI (sur 1 000)", "sample_size": "Nombre de ventes Volvo Selekt",
                 "ownership_duration": "Durée de possession (ans)", "warranty_duration": "Garantie Volvo Selekt (ans)",
                 "vehicle_profit": "Profit par vente de véhicule", "service_profit": "Profit service par client et par an",
                 "run": "Lancer la simulation", "results": "Résultats", "year": "Année",
                 "service_customers": "Clients service", "repeat_purchases": "Achats répétés",
                 "total_profit": "Profit total", "total": "Total", "download": "Télécharger CSV"},
    "Deutsch": {"language": "Sprache", "title": "CSI-Ertragsimulator",
                "csi_score": "CSI-Wert (von 1 000)", "sample_size": "Volvo Selekt-Verkäufe",
                "ownership_duration": "Besitzdauer (Jahre)", "warranty_duration": "Volvo Selekt-Garantie (Jahre)",
                "vehicle_profit": "Gewinn pro Fahrzeugverkauf", "service_profit": "Servicegewinn pro Kunde und Jahr",
                "run": "Simulation starten", "results": "Ergebnisse", "year": "Jahr",
                "service_customers": "Servicekunden", "repeat_purchases": "Wiederholungskäufe",
                "total_profit": "Gesamtgewinn", "total": "Gesamt", "download": "CSV herunterladen"},
    "Italiano": {"language": "Lingua", "title": "Simulatore di redditività CSI",
                 "csi_score": "Punteggio CSI (su 1 000)", "sample_size": "Vendite Volvo Selekt",
                 "ownership_duration": "Durata proprietà (anni)", "warranty_duration": "Garanzia Volvo Selekt (anni)",
                 "vehicle_profit": "Profitto per vendita veicolo", "service_profit": "Profitto assistenza per cliente all'anno",
                 "run": "Esegui simulazione", "results": "Risultati", "year": "Anno",
                 "service_customers": "Clienti assistenza", "repeat_purchases": "Riacquisti",
                 "total_profit": "Profitto totale", "total": "Totale", "download": "Scarica CSV"},
    "Svenska": {"language": "Språk", "title": "CSI Lönsamhetssimulator",
                "csi_score": "CSI-poäng (av 1 000)", "sample_size": "Volvo Selekt-försäljning",
                "ownership_duration": "Ägarperiod (år)", "warranty_duration": "Volvo Selekt-garanti (år)",
                "vehicle_profit": "Vinst per bilförsäljning", "service_profit": "Servicevinst per kund och år",
                "run": "Kör simulering", "results": "Resultat", "year": "År",
                "service_customers": "Servicekunder", "repeat_purchases": "Återköp",
                "total_profit": "Total vinst", "total": "Totalt", "download": "Ladda ner CSV"}
}

# UI
language = st.selectbox(labels["English"]["language"], list(labels.keys()))
L = labels[language]

st.title(L["title"])
# ... rest of the code unchanged ...
