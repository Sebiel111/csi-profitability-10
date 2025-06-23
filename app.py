
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

# Select language
language = st.selectbox(labels["English"]["language"], list(labels.keys()))
L = labels[language]

# Title
st.title(L["title"])

# Simulation logic
def get_csi_percentages(score):
    if score >= 901: return 0.74, 0.35
    if score >= 801: return 0.51, 0.24
    if score >= 701: return 0.32, 0.19
    return 0.14, 0.16

def simulate(csi, count, s_profit, own_years, warranty, v_profit):
    years = list(range(2026, 2041))
    service = {y:0 for y in years}
    repeat = {y:0 for y in years}
    total = {y:0 for y in years}
    waves = [{"year":2025, "count":count, "repeated":False}]
    s_pct, r_pct = get_csi_percentages(csi)
    for y in years:
        new = []
        for w in waves:
            age = y - w["year"]
            if 1 <= age <= warranty:
                service[y] += w["count"] * s_pct
            if not w["repeated"] and age >= own_years:
                r = w["count"] * r_pct
                repeat[y] += r
                w["repeated"] = True
                new.append({"year":y, "count":r, "repeated":False})
        waves.extend(new)
        total[y] = round(service[y]) * s_profit + round(repeat[y]) * v_profit

    df = pd.DataFrame({
        L["year"]: years,
        L["service_customers"]: [round(service[y]) for y in years],
        L["repeat_purchases"]: [round(repeat[y]) for y in years],
        L["total_profit"]: [round(total[y]) for y in years]
    })
    totals = {
        L["year"]: L["total"],
        L["service_customers"]: int(df[L["service_customers"]].sum()),
        L["repeat_purchases"]: int(df[L["repeat_purchases"]].sum()),
        L["total_profit"]: int(df[L["total_profit"]].sum())
    }
    df = pd.concat([pd.DataFrame([totals]), df], ignore_index=True)
    return df

def format_number(n):
    if language == "Svenska":
        return f"{n:,}".replace(",", " ")
    if language == "English":
        return f"{n:,}"
    return f"{n:,}".replace(",", "X").replace(".", ",").replace("X", ".")

def render_table(df):
    html = "<table class='custom'><thead><tr>"
    for col in df.columns:
        html += f"<th>{col}</th>"
    html += "</tr></thead><tbody>"
    for _, row in df.iterrows():
        cls = " class='total-row'" if row[df.columns[0]] == L["total"] else ""
        html += f"<tr{cls}><td class='left'>{row[df.columns[0]]}</td>"
        for val in row.iloc[1:]:
            html += f"<td>{format_number(val)}</td>"
        html += "</tr>"
    html += "</tbody></table>"
    return html

with st.form("form"):
    csi = st.slider(L["csi_score"], 0, 1000, 870)
    # Inputs inline with labels in specified order
    sample_col, own_col, vp_col, warrant_col, sp_col = st.columns([2,2,2,2,2])
    sample = sample_col.text_input(L["sample_size"], value=format_number(100), key="sample")
    own = own_col.text_input(L["ownership_duration"], value=str(2), key="own")
    vp = vp_col.text_input(L["vehicle_profit"], value=format_number(1225), key="vp")
    warranty = warrant_col.text_input(L["warranty_duration"], value=str(3), key="warranty")
    sp = sp_col.text_input(L["service_profit"], value=format_number(350), key="sp")
    go = st.form_submit_button(L["run"])

if go:
    count = int(sample.replace(" ","").replace(",",""))
    own_years = float(own.replace(",",".")) 
    warranty_years = float(warranty.replace(",",".")) 
    vprofit = int(vp.replace(" ","").replace(",",""))
    sprofit = int(sp.replace(" ","").replace(",",""))
    df = simulate(csi, count, sprofit, own_years, warranty_years, vprofit)
    st.subheader(L["results"])
    st.markdown(render_table(df), unsafe_allow_html=True)
    st.download_button(L["download"], df.to_csv(index=False).encode("utf-8"), "csi_profitability.csv", "text/csv")
