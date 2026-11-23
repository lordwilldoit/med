"""Generates DoseCalc/Drugs.json. Lists inside a field are separated by ' | '."""
import json, sys

CATS = ["cardio", "blood", "endo", "gi", "pain", "neuro", "psych", "resp", "infection", "vitamins", "other"]
drugs = []

def D(id, cat, name_fr, name_en, brands, cls_fr, cls_en, why_fr, why_en, side_fr, side_en, watch_fr="", watch_en=""):
    sp = lambda s: [x.strip() for x in s.split("|") if x.strip()]
    assert cat in CATS, id
    drugs.append({
        "id": id, "category": cat,
        "name": {"fr": name_fr, "en": name_en},
        "brands": sp(brands),
        "drugClass": {"fr": cls_fr, "en": cls_en},
        "why": {"fr": sp(why_fr), "en": sp(why_en)},
        "sideEffects": {"fr": sp(side_fr), "en": sp(side_en)},
        "watch": {"fr": sp(watch_fr), "en": sp(watch_en)},
    })

# ---------------- Cardio ----------------
D("amlodipine", "cardio", "Amlodipine", "Amlodipine", "Norvasc",
  "Bloqueur des canaux calciques (BCC)", "Calcium channel blocker (CCB)",
  "Hypertension artérielle (HTA) | Angine de poitrine", "High blood pressure | Angina",
  "Œdème des chevilles | Maux de tête | Bouffées de chaleur | Étourdissements | Fatigue",
  "Ankle swelling | Headache | Flushing | Dizziness | Fatigue",
  "Prendre la TA avant | Hypotension orthostatique : se lever lentement",
  "Check BP before giving | Orthostatic hypotension: get up slowly")
D("diltiazem", "cardio", "Diltiazem", "Diltiazem", "Cardizem | Tiazac",
  "Bloqueur des canaux calciques (non dihydropyridine)", "Calcium channel blocker (non-dihydropyridine)",
  "HTA | Angine | Fibrillation auriculaire (contrôle de la fréquence)", "High blood pressure | Angina | Atrial fibrillation (rate control)",
  "Bradycardie | Hypotension | Œdème | Maux de tête | Constipation",
  "Slow heart rate | Low blood pressure | Swelling | Headache | Constipation",
  "Prendre FC et TA avant | Ne pas écraser les formes à libération prolongée",
  "Check HR and BP before giving | Don't crush extended-release forms")
D("ramipril", "cardio", "Ramipril", "Ramipril", "Altace",
  "Inhibiteur de l'enzyme de conversion (IECA)", "ACE inhibitor",
  "HTA | Insuffisance cardiaque | Après un infarctus | Protection des reins (diabète)",
  "High blood pressure | Heart failure | After a heart attack | Kidney protection (diabetes)",
  "Toux sèche | Étourdissements | Hyperkaliémie (K+ élevé) | Hypotension | Angiœdème (rare, urgence)",
  "Dry cough | Dizziness | High potassium | Low blood pressure | Angioedema (rare, emergency)",
  "TA, potassium et créatinine | Enflure du visage, des lèvres ou de la langue : aviser immédiatement",
  "BP, potassium and creatinine | Swelling of face, lips or tongue: report immediately")
D("perindopril", "cardio", "Périndopril", "Perindopril", "Coversyl",
  "Inhibiteur de l'enzyme de conversion (IECA)", "ACE inhibitor",
  "HTA | Maladie coronarienne | Insuffisance cardiaque", "High blood pressure | Coronary artery disease | Heart failure",
  "Toux sèche | Étourdissements | Hyperkaliémie | Hypotension | Angiœdème (rare)",
  "Dry cough | Dizziness | High potassium | Low blood pressure | Angioedema (rare)",
  "TA, potassium et créatinine", "BP, potassium and creatinine")
D("losartan", "cardio", "Losartan", "Losartan", "Cozaar",
  "Antagoniste des récepteurs de l'angiotensine (ARA)", "Angiotensin receptor blocker (ARB)",
  "HTA | Insuffisance cardiaque | Protection des reins (diabète)", "High blood pressure | Heart failure | Kidney protection (diabetes)",
  "Étourdissements | Hyperkaliémie | Hypotension | Fatigue",
  "Dizziness | High potassium | Low blood pressure | Fatigue",
  "TA, potassium et créatinine | Moins de toux qu'avec un IECA", "BP, potassium and creatinine | Less cough than ACE inhibitors")
D("metoprolol", "cardio", "Métoprolol", "Metoprolol", "Lopresor | Betaloc",
  "Bêtabloquant (cardiosélectif)", "Beta blocker (cardioselective)",
  "HTA | Angine | Après un infarctus | Fibrillation auriculaire (contrôle de la fréquence) | Insuffisance cardiaque",
  "High blood pressure | Angina | After a heart attack | Atrial fibrillation (rate control) | Heart failure",
  "Bradycardie | Fatigue | Étourdissements | Hypotension | Mains et pieds froids",
  "Slow heart rate | Fatigue | Dizziness | Low blood pressure | Cold hands and feet",
  "Prendre FC et TA avant; retenir et aviser selon les paramètres de l'ordonnance | Ne pas cesser brusquement | Peut masquer les signes d'hypoglycémie",
  "Check HR and BP first; hold and report per the order's parameters | Don't stop suddenly | Can mask low blood sugar signs")
D("bisoprolol", "cardio", "Bisoprolol", "Bisoprolol", "Monocor",
  "Bêtabloquant (cardiosélectif)", "Beta blocker (cardioselective)",
  "HTA | Insuffisance cardiaque | Angine | Fibrillation auriculaire",
  "High blood pressure | Heart failure | Angina | Atrial fibrillation",
  "Bradycardie | Fatigue | Étourdissements | Hypotension",
  "Slow heart rate | Fatigue | Dizziness | Low blood pressure",
  "Prendre FC et TA avant | Ne pas cesser brusquement", "Check HR and BP before giving | Don't stop suddenly")
D("furosemide", "cardio", "Furosémide", "Furosemide", "Lasix",
  "Diurétique de l'anse", "Loop diuretic",
  "Œdème | Insuffisance cardiaque | Œdème pulmonaire | HTA", "Swelling (edema) | Heart failure | Fluid in the lungs | High blood pressure",
  "Mictions fréquentes | Hypokaliémie (K+ bas) | Déshydratation | Hypotension | Étourdissements | Ototoxicité (doses IV élevées)",
  "Frequent urination | Low potassium | Dehydration | Low blood pressure | Dizziness | Hearing damage (high IV doses)",
  "Poids quotidien, ingesta/excreta | Potassium | Donner le matin pour éviter les mictions la nuit",
  "Daily weight, intake/output | Potassium | Give in the morning to avoid night-time urination")
D("hctz", "cardio", "Hydrochlorothiazide", "Hydrochlorothiazide", "HCTZ",
  "Diurétique thiazidique", "Thiazide diuretic",
  "HTA | Œdème", "High blood pressure | Swelling (edema)",
  "Hypokaliémie | Hyponatrémie | Hyperglycémie | Goutte | Photosensibilité | Étourdissements",
  "Low potassium | Low sodium | High blood sugar | Gout | Sun sensitivity | Dizziness",
  "Électrolytes | Donner le matin", "Electrolytes | Give in the morning")
D("spironolactone", "cardio", "Spironolactone", "Spironolactone", "Aldactone",
  "Diurétique épargneur de potassium (antagoniste de l'aldostérone)", "Potassium-sparing diuretic (aldosterone antagonist)",
  "Insuffisance cardiaque | Ascite (cirrhose) | HTA résistante", "Heart failure | Ascites (cirrhosis) | Hard-to-control high blood pressure",
  "Hyperkaliémie (K+ élevé) | Gynécomastie | Étourdissements | Troubles digestifs",
  "High potassium | Breast enlargement in men | Dizziness | Stomach upset",
  "Potassium (surtout avec un IECA ou ARA) | Éviter les suppléments de potassium sauf si prescrits",
  "Potassium (especially with ACE inhibitor or ARB) | Avoid potassium supplements unless ordered")
D("digoxin", "cardio", "Digoxine", "Digoxin", "Lanoxin | Toloxin",
  "Glycoside cardiaque (digitalique)", "Cardiac glycoside",
  "Insuffisance cardiaque | Fibrillation auriculaire (contrôle de la fréquence)", "Heart failure | Atrial fibrillation (rate control)",
  "Toxicité : nausées, vomissements, perte d'appétit | Vision jaune-verte ou halos | Bradycardie | Arythmies | Confusion",
  "Toxicity: nausea, vomiting, loss of appetite | Yellow-green vision or halos | Slow heart rate | Irregular heartbeat | Confusion",
  "Pouls apical 1 minute complète avant; retenir et aviser selon les paramètres de l'ordonnance (souvent < 60) | K+ bas augmente le risque de toxicité | Marge thérapeutique étroite (digoxinémie)",
  "Apical pulse for a full minute first; hold and report per order parameters (often < 60) | Low potassium raises toxicity risk | Narrow therapeutic range (digoxin level)")
D("nitroglycerin", "cardio", "Nitroglycérine", "Nitroglycerin", "Nitrolingual (vaporisateur) | Trinipatch (timbre)",
  "Dérivé nitré (vasodilatateur)", "Nitrate (vasodilator)",
  "Crise d'angine (sublingual) | Prévention de l'angine (timbre)", "Angina attack (under the tongue) | Angina prevention (patch)",
  "Maux de tête | Hypotension | Étourdissements | Bouffées de chaleur",
  "Headache | Low blood pressure | Dizziness | Flushing",
  "Faire asseoir le patient | Sublingual : selon le protocole, habituellement 1 dose aux 5 min, max 3; appeler à l'aide si la douleur persiste | Contre-indiqué avec sildénafil/tadalafil | Timbre : retirer la nuit si prescrit, alterner les sites",
  "Have the patient sit | Under the tongue: per protocol, usually 1 dose every 5 min, max 3; call for help if pain persists | Not with sildenafil/tadalafil | Patch: remove at night if ordered, rotate sites")
D("atorvastatin", "cardio", "Atorvastatine", "Atorvastatin", "Lipitor",
  "Statine (hypolipémiant)", "Statin (cholesterol-lowering)",
  "Cholestérol élevé | Prévention de l'infarctus et de l'AVC", "High cholesterol | Preventing heart attack and stroke",
  "Douleurs musculaires | Troubles digestifs | Maux de tête | Hausse des enzymes du foie | Rhabdomyolyse (rare)",
  "Muscle pain | Stomach upset | Headache | Raised liver enzymes | Muscle breakdown (rare)",
  "Signaler douleurs ou faiblesse musculaires inexpliquées", "Report unexplained muscle pain or weakness")
D("rosuvastatin", "cardio", "Rosuvastatine", "Rosuvastatin", "Crestor",
  "Statine (hypolipémiant)", "Statin (cholesterol-lowering)",
  "Cholestérol élevé | Prévention de l'infarctus et de l'AVC", "High cholesterol | Preventing heart attack and stroke",
  "Douleurs musculaires | Maux de tête | Nausées | Hausse des enzymes du foie",
  "Muscle pain | Headache | Nausea | Raised liver enzymes",
  "Signaler douleurs musculaires inexpliquées", "Report unexplained muscle pain")

# ---------------- Blood (antiplatelets / anticoagulants) ----------------
D("asa", "blood", "Acide acétylsalicylique (AAS)", "Acetylsalicylic acid (ASA)", "Aspirin | Entrophen | Asaphen",
  "Antiplaquettaire (à faible dose) / AINS", "Antiplatelet (low dose) / NSAID",
  "Prévention de l'infarctus et de l'AVC (80 mg) | Après un stent | Douleur et fièvre (doses plus fortes)",
  "Preventing heart attack and stroke (80 mg) | After a stent | Pain and fever (higher doses)",
  "Brûlures d'estomac | Saignements digestifs | Ecchymoses (bleus)",
  "Heartburn | Stomach bleeding | Bruising",
  "Surveiller saignements, selles noires | Avec nourriture | Comprimés entérosolubles : ne pas écraser",
  "Watch for bleeding, black stools | Give with food | Enteric-coated: don't crush")
D("clopidogrel", "blood", "Clopidogrel", "Clopidogrel", "Plavix",
  "Antiplaquettaire", "Antiplatelet",
  "Après un stent ou un syndrome coronarien aigu | Prévention de l'AVC | Maladie artérielle périphérique",
  "After a stent or heart attack | Stroke prevention | Peripheral artery disease",
  "Saignements | Ecchymoses | Diarrhée | Éruption cutanée",
  "Bleeding | Bruising | Diarrhea | Rash",
  "Surveiller les saignements | Ne pas cesser sans l'avis du médecin (risque de thrombose du stent)",
  "Watch for bleeding | Don't stop without the doctor (stent clot risk)")
D("warfarin", "blood", "Warfarine", "Warfarin", "Coumadin",
  "Anticoagulant (antagoniste de la vitamine K)", "Anticoagulant (vitamin K antagonist)",
  "Fibrillation auriculaire | Thrombose veineuse profonde (TVP) / embolie pulmonaire (EP) | Valve cardiaque mécanique",
  "Atrial fibrillation | Deep vein clot (DVT) / lung clot (PE) | Mechanical heart valve",
  "Saignements (gencives, nez, urine, selles) | Ecchymoses",
  "Bleeding (gums, nose, urine, stool) | Bruising",
  "RNI (INR) régulier; dose ajustée selon le résultat | Beaucoup d'interactions (antibiotiques, AINS...) | Apport en vitamine K constant | Antidote : vitamine K",
  "Regular INR; dose adjusted to the result | Many interactions (antibiotics, NSAIDs...) | Keep vitamin K intake steady | Antidote: vitamin K")
D("apixaban", "blood", "Apixaban", "Apixaban", "Eliquis",
  "Anticoagulant oral direct (inhibiteur du facteur Xa)", "Direct oral anticoagulant (factor Xa inhibitor)",
  "Fibrillation auriculaire (prévention de l'AVC) | TVP / EP : traitement et prévention",
  "Atrial fibrillation (stroke prevention) | DVT / PE: treatment and prevention",
  "Saignements | Ecchymoses | Nausées",
  "Bleeding | Bruising | Nausea",
  "Deux fois par jour, à heure fixe | Surveiller les saignements | Pas de suivi RNI",
  "Twice a day at set times | Watch for bleeding | No INR needed")
D("rivaroxaban", "blood", "Rivaroxaban", "Rivaroxaban", "Xarelto",
  "Anticoagulant oral direct (inhibiteur du facteur Xa)", "Direct oral anticoagulant (factor Xa inhibitor)",
  "Fibrillation auriculaire (prévention de l'AVC) | TVP / EP | Prévention après une chirurgie orthopédique",
  "Atrial fibrillation (stroke prevention) | DVT / PE | Prevention after orthopedic surgery",
  "Saignements | Ecchymoses | Anémie",
  "Bleeding | Bruising | Anemia",
  "Doses de 15 et 20 mg : avec un repas | Surveiller les saignements",
  "15 and 20 mg doses: give with a meal | Watch for bleeding")
D("enoxaparin", "blood", "Énoxaparine", "Enoxaparin", "Lovenox | Redesca",
  "Héparine de faible poids moléculaire (HFPM)", "Low-molecular-weight heparin (LMWH)",
  "Prévention des caillots (immobilisation, chirurgie) | Traitement de la TVP / EP",
  "Preventing clots (bedrest, surgery) | Treating DVT / PE",
  "Saignements | Ecchymoses ou hématome au site d'injection | Thrombocytopénie",
  "Bleeding | Bruising or lump at injection site | Low platelets",
  "Sous-cutané dans l'abdomen, à 5 cm du nombril, alterner les côtés | Ne pas expulser la bulle d'air, ne pas frotter | Plaquettes",
  "Subcutaneous in the abdomen, 5 cm from the navel, alternate sides | Don't expel the air bubble, don't rub | Platelets")
D("heparin", "blood", "Héparine", "Heparin", "",
  "Anticoagulant (héparine non fractionnée)", "Anticoagulant (unfractionated heparin)",
  "Prévention des caillots (sous-cutané) | Traitement de la TVP / EP (perfusion IV)",
  "Preventing clots (subcutaneous) | Treating DVT / PE (IV drip)",
  "Saignements | Ecchymoses | Thrombocytopénie induite par l'héparine (TIH)",
  "Bleeding | Bruising | Heparin-induced low platelets (HIT)",
  "Médicament de haute alerte : double vérification | IV : selon le protocole (TCA / aPTT) | Plaquettes | Antidote : protamine",
  "High-alert drug: independent double check | IV: per protocol (aPTT) | Platelets | Antidote: protamine")

# ---------------- Endocrine ----------------
D("metformin", "endo", "Metformine", "Metformin", "Glucophage | Glumetza",
  "Antidiabétique (biguanide)", "Diabetes medication (biguanide)",
  "Diabète de type 2", "Type 2 diabetes",
  "Diarrhée, nausées, crampes | Goût métallique | Carence en vitamine B12 (long terme) | Acidose lactique (rare)",
  "Diarrhea, nausea, cramps | Metallic taste | Low vitamin B12 (long term) | Lactic acidosis (rare)",
  "Avec les repas | Fonction rénale | Souvent suspendue avant un examen avec contraste iodé (selon protocole) | Ne cause pas d'hypoglycémie seule",
  "With meals | Kidney function | Often held before iodine contrast tests (per protocol) | Doesn't cause low blood sugar on its own")
D("gliclazide", "endo", "Gliclazide", "Gliclazide", "Diamicron",
  "Antidiabétique (sulfonylurée)", "Diabetes medication (sulfonylurea)",
  "Diabète de type 2", "Type 2 diabetes",
  "Hypoglycémie | Gain de poids | Nausées",
  "Low blood sugar | Weight gain | Nausea",
  "Glycémie | Avec le déjeuner; aviser si le patient ne mange pas (risque d'hypoglycémie)",
  "Blood sugar | Give with breakfast; report if the patient isn't eating (low sugar risk)")
D("empagliflozin", "endo", "Empagliflozine", "Empagliflozin", "Jardiance",
  "Antidiabétique (inhibiteur du SGLT2)", "Diabetes medication (SGLT2 inhibitor)",
  "Diabète de type 2 | Insuffisance cardiaque | Insuffisance rénale chronique",
  "Type 2 diabetes | Heart failure | Chronic kidney disease",
  "Infections urinaires et génitales (champignons) | Mictions fréquentes | Déshydratation | Acidocétose (rare)",
  "Urinary and genital (yeast) infections | Frequent urination | Dehydration | Ketoacidosis (rare)",
  "Hydratation | Hygiène génitale | Souvent suspendu si le patient est à jeun ou malade (selon protocole)",
  "Hydration | Genital hygiene | Often held when NPO or acutely ill (per protocol)")
D("sitagliptin", "endo", "Sitagliptine", "Sitagliptin", "Januvia | Janumet (avec metformine)",
  "Antidiabétique (inhibiteur de la DPP-4)", "Diabetes medication (DPP-4 inhibitor)",
  "Diabète de type 2", "Type 2 diabetes",
  "Maux de tête | Rhume / mal de gorge | Pancréatite (rare)",
  "Headache | Cold symptoms / sore throat | Pancreatitis (rare)",
  "Peu d'hypoglycémie seule | Douleur abdominale intense : aviser", "Little low-sugar risk alone | Severe stomach pain: report")
D("insulin-glargine", "endo", "Insuline glargine (longue action)", "Insulin glargine (long-acting)", "Lantus | Basaglar | Toujeo",
  "Insuline basale (longue action)", "Basal insulin (long-acting)",
  "Diabète type 1 et type 2 : contrôle de la glycémie sur 24 h", "Type 1 and 2 diabetes: 24-hour blood sugar control",
  "Hypoglycémie | Réaction au site d'injection | Gain de poids",
  "Low blood sugar | Injection site reaction | Weight gain",
  "Médicament de haute alerte : double vérification | Glycémie | Une fois par jour à la même heure, pas de pic | Ne jamais mélanger avec une autre insuline | Connaître les signes d'hypoglycémie",
  "High-alert drug: double check | Blood sugar | Once a day at the same time, no peak | Never mix with another insulin | Know the signs of low blood sugar")
D("insulin-rapid", "endo", "Insuline rapide (lispro, asparte)", "Rapid-acting insulin (lispro, aspart)", "Humalog | NovoRapid | Admelog | Fiasp",
  "Insuline prandiale (action rapide)", "Mealtime insulin (rapid-acting)",
  "Diabète : couvrir les repas | Corriger une glycémie élevée (échelle)", "Diabetes: cover meals | Correct high blood sugar (sliding scale)",
  "Hypoglycémie | Réaction au site d'injection | Hypokaliémie",
  "Low blood sugar | Injection site reaction | Low potassium",
  "Médicament de haute alerte : double vérification | Glycémie avant | Donner juste avant le repas (0–15 min); le repas doit être disponible",
  "High-alert drug: double check | Check blood sugar first | Give right before the meal (0–15 min); the meal must be there")
D("levothyroxine", "endo", "Lévothyroxine", "Levothyroxine", "Synthroid | Eltroxin",
  "Hormone thyroïdienne", "Thyroid hormone",
  "Hypothyroïdie", "Underactive thyroid (hypothyroidism)",
  "Si dose trop forte : palpitations, tachycardie, insomnie, nervosité, perte de poids, intolérance à la chaleur",
  "If the dose is too high: palpitations, fast heart rate, insomnia, nervousness, weight loss, heat intolerance",
  "À jeun, 30–60 min avant le déjeuner, avec de l'eau | Séparer de 4 h du calcium, du fer et des antiacides",
  "On an empty stomach, 30–60 min before breakfast, with water | Separate by 4 h from calcium, iron and antacids")
D("prednisone", "endo", "Prednisone", "Prednisone", "",
  "Corticostéroïde", "Corticosteroid",
  "Exacerbation de MPOC ou d'asthme | Inflammation (arthrite, maladies auto-immunes) | Réactions allergiques",
  "COPD or asthma flare | Inflammation (arthritis, autoimmune disease) | Allergic reactions",
  "Hyperglycémie | Insomnie | Changements d'humeur | Appétit augmenté | Rétention d'eau | Infections | Ostéoporose (long terme)",
  "High blood sugar | Insomnia | Mood changes | Increased appetite | Fluid retention | Infections | Weak bones (long term)",
  "Le matin avec nourriture | Glycémie chez le diabétique | Ne pas cesser brusquement après un usage prolongé",
  "In the morning with food | Blood sugar in diabetics | Don't stop suddenly after long-term use")

# ---------------- GI ----------------
D("pantoprazole", "gi", "Pantoprazole", "Pantoprazole", "Pantoloc | Tecta",
  "Inhibiteur de la pompe à protons (IPP)", "Proton pump inhibitor (PPI)",
  "Reflux gastro-œsophagien (RGO) | Ulcère d'estomac | Protection de l'estomac (AINS, corticos)",
  "Acid reflux (GERD) | Stomach ulcer | Stomach protection (NSAIDs, steroids)",
  "Maux de tête | Diarrhée | Douleur abdominale | Long terme : C. difficile, ↓ B12 et magnésium, fractures",
  "Headache | Diarrhea | Stomach pain | Long term: C. difficile, low B12 and magnesium, fractures",
  "30–60 min avant le déjeuner | Ne pas écraser ni croquer", "30–60 min before breakfast | Don't crush or chew")
D("famotidine", "gi", "Famotidine", "Famotidine", "Pepcid",
  "Antihistaminique H2 (anti-acide)", "H2 blocker (acid reducer)",
  "RGO | Brûlures d'estomac | Ulcère", "Acid reflux | Heartburn | Ulcer",
  "Maux de tête | Étourdissements | Confusion chez la personne âgée",
  "Headache | Dizziness | Confusion in older adults",
  "Dose réduite si fonction rénale diminuée", "Lower dose if kidney function is reduced")
D("sennosides", "gi", "Sennosides", "Sennosides", "Senokot",
  "Laxatif stimulant", "Stimulant laxative",
  "Constipation (souvent avec les opioïdes)", "Constipation (often with opioids)",
  "Crampes abdominales | Diarrhée | Urine plus foncée",
  "Stomach cramps | Diarrhea | Darker urine",
  "Agit en 6–12 h : souvent donné au coucher | Noter les selles", "Works in 6–12 h: often given at bedtime | Track bowel movements")
D("docusate", "gi", "Docusate sodique", "Docusate sodium", "Colace | Soflax",
  "Émollient des selles", "Stool softener",
  "Prévenir les selles dures", "Preventing hard stools",
  "Peu d'effets | Crampes légères | Goût amer (liquide)",
  "Few side effects | Mild cramps | Bitter taste (liquid)",
  "Efficacité limitée seul : souvent combiné à un laxatif", "Limited effect on its own: often combined with a laxative")
D("peg3350", "gi", "Polyéthylène glycol 3350 (PEG)", "Polyethylene glycol 3350 (PEG)", "Lax-A-Day | RestoraLAX",
  "Laxatif osmotique", "Osmotic laxative",
  "Constipation", "Constipation",
  "Ballonnements | Gaz | Diarrhée | Nausées",
  "Bloating | Gas | Diarrhea | Nausea",
  "Dissoudre la poudre dans 125–250 mL de liquide | Effet en 1–3 jours | Noter les selles",
  "Dissolve the powder in 125–250 mL of liquid | Works in 1–3 days | Track bowel movements")
D("lactulose", "gi", "Lactulose", "Lactulose", "",
  "Laxatif osmotique", "Osmotic laxative",
  "Constipation | Encéphalopathie hépatique (diminue l'ammoniac)", "Constipation | Hepatic encephalopathy (lowers ammonia)",
  "Gaz | Ballonnements | Crampes | Diarrhée | Goût très sucré",
  "Gas | Bloating | Cramps | Diarrhea | Very sweet taste",
  "Peut être mélangé à du jus | Encéphalopathie : viser 2–3 selles molles par jour (selon l'ordonnance) | Surveiller hydratation et électrolytes",
  "Can be mixed with juice | Encephalopathy: aim for 2–3 soft stools a day (per order) | Watch hydration and electrolytes")
D("ondansetron", "gi", "Ondansétron", "Ondansetron", "Zofran",
  "Antiémétique (antagoniste 5-HT3)", "Anti-nausea (5-HT3 antagonist)",
  "Nausées et vomissements (chimiothérapie, après une chirurgie)", "Nausea and vomiting (chemo, after surgery)",
  "Maux de tête | Constipation | Étourdissements | Allongement du QT",
  "Headache | Constipation | Dizziness | QT prolongation",
  "Comprimé orodispersible : sur la langue, mains sèches", "Dissolving tablet: on the tongue, with dry hands")
D("metoclopramide", "gi", "Métoclopramide", "Metoclopramide", "Metonia",
  "Antiémétique / prokinétique", "Anti-nausea / gut motility drug",
  "Nausées et vomissements | Gastroparésie (estomac lent) | RGO", "Nausea and vomiting | Gastroparesis (slow stomach) | Acid reflux",
  "Somnolence | Agitation | Symptômes extrapyramidaux | Dyskinésie tardive (usage prolongé)",
  "Drowsiness | Restlessness | Extrapyramidal symptoms | Tardive dyskinesia (long-term use)",
  "30 min avant les repas | Signaler mouvements involontaires", "30 min before meals | Report involuntary movements")
D("dimenhydrinate", "gi", "Dimenhydrinate", "Dimenhydrinate", "Gravol",
  "Antiémétique (antihistaminique)", "Anti-nausea (antihistamine)",
  "Nausées et vomissements | Mal des transports | Vertiges", "Nausea and vomiting | Motion sickness | Vertigo",
  "Somnolence | Bouche sèche | Vision trouble | Confusion chez la personne âgée | Rétention urinaire",
  "Drowsiness | Dry mouth | Blurred vision | Confusion in older adults | Urinary retention",
  "Risque de chute | Prudence chez la personne âgée (effets anticholinergiques)", "Fall risk | Caution in older adults (anticholinergic effects)")

# ---------------- Pain ----------------
D("acetaminophen", "pain", "Acétaminophène", "Acetaminophen", "Tylenol | Atasol",
  "Analgésique / antipyrétique", "Pain reliever / fever reducer",
  "Douleur légère à modérée | Fièvre", "Mild to moderate pain | Fever",
  "Rares aux doses habituelles | Atteinte du foie en cas de surdose",
  "Rare at usual doses | Liver damage in overdose",
  "Respecter la dose max quotidienne de l'ordonnance (adulte : souvent 4 g/jour, moins chez la personne âgée ou l'alcoolique) | Compter TOUTES les sources (ex. Tylenol + Percocet) | Réévaluer la douleur ou la température",
  "Respect the order's max daily dose (adults: often 4 g/day, less in older adults or with alcohol use) | Count ALL sources (e.g. Tylenol + Percocet) | Reassess pain or temperature")
D("ibuprofen", "pain", "Ibuprofène", "Ibuprofen", "Advil | Motrin",
  "Anti-inflammatoire non stéroïdien (AINS)", "Non-steroidal anti-inflammatory (NSAID)",
  "Douleur | Inflammation | Fièvre", "Pain | Inflammation | Fever",
  "Brûlures d'estomac | Ulcère et saignement digestif | Atteinte des reins | Hausse de la TA | Rétention d'eau",
  "Heartburn | Stomach ulcer and bleeding | Kidney damage | Higher blood pressure | Fluid retention",
  "Avec nourriture | Prudence : personne âgée, insuffisance rénale ou cardiaque, anticoagulants",
  "Give with food | Caution: older adults, kidney or heart failure, blood thinners")
D("naproxen", "pain", "Naproxène", "Naproxen", "Naprosyn | Aleve",
  "Anti-inflammatoire non stéroïdien (AINS)", "Non-steroidal anti-inflammatory (NSAID)",
  "Douleur | Arthrite | Inflammation", "Pain | Arthritis | Inflammation",
  "Brûlures d'estomac | Saignement digestif | Atteinte des reins | Rétention d'eau",
  "Heartburn | Stomach bleeding | Kidney damage | Fluid retention",
  "Avec nourriture | Mêmes précautions que l'ibuprofène", "Give with food | Same cautions as ibuprofen")
D("morphine", "pain", "Morphine", "Morphine", "Statex | M-Eslon | MS Contin",
  "Analgésique opioïde (stupéfiant)", "Opioid pain reliever (narcotic)",
  "Douleur modérée à sévère | Dyspnée en soins palliatifs", "Moderate to severe pain | Shortness of breath in palliative care",
  "Constipation | Nausées | Somnolence | Dépression respiratoire | Confusion | Démangeaisons | Rétention urinaire",
  "Constipation | Nausea | Drowsiness | Slowed breathing | Confusion | Itching | Urinary retention",
  "Avant et après : douleur, FR, niveau de sédation (échelle POSS) | Stupéfiant : registre et décompte | Libération prolongée : ne pas écraser | Laxatif souvent prescrit | Antidote : naloxone",
  "Before and after: pain, RR, sedation level (POSS) | Narcotic: register and count | Extended-release: don't crush | Laxative often ordered | Antidote: naloxone")
D("hydromorphone", "pain", "Hydromorphone", "Hydromorphone", "Dilaudid | Hydromorph Contin",
  "Analgésique opioïde (stupéfiant)", "Opioid pain reliever (narcotic)",
  "Douleur modérée à sévère", "Moderate to severe pain",
  "Constipation | Nausées | Somnolence | Dépression respiratoire | Confusion",
  "Constipation | Nausea | Drowsiness | Slowed breathing | Confusion",
  "Environ 5 fois plus puissant que la morphine : ne jamais confondre les deux | Médicament de haute alerte | FR et sédation (POSS) | Antidote : naloxone",
  "About 5 times stronger than morphine: never mix them up | High-alert drug | RR and sedation (POSS) | Antidote: naloxone")
D("oxycodone", "pain", "Oxycodone", "Oxycodone", "Supeudol | OxyNEO | Percocet (avec acétaminophène)",
  "Analgésique opioïde (stupéfiant)", "Opioid pain reliever (narcotic)",
  "Douleur modérée à sévère", "Moderate to severe pain",
  "Constipation | Nausées | Somnolence | Dépression respiratoire | Étourdissements",
  "Constipation | Nausea | Drowsiness | Slowed breathing | Dizziness",
  "FR et sédation (POSS) | Percocet contient de l'acétaminophène : compter dans le total quotidien | Libération prolongée : ne pas écraser",
  "RR and sedation (POSS) | Percocet contains acetaminophen: count it in the daily total | Extended-release: don't crush")
D("tramadol", "pain", "Tramadol", "Tramadol", "Ultram | Tridural | Tramacet (avec acétaminophène)",
  "Analgésique opioïde faible (aussi effet sur la sérotonine)", "Weak opioid pain reliever (also acts on serotonin)",
  "Douleur modérée", "Moderate pain",
  "Nausées | Étourdissements | Constipation | Somnolence | Convulsions (rare) | Syndrome sérotoninergique avec certains antidépresseurs",
  "Nausea | Dizziness | Constipation | Drowsiness | Seizures (rare) | Serotonin syndrome with some antidepressants",
  "Vérifier les antidépresseurs (ISRS, IRSN) | Risque de chute", "Check for antidepressants (SSRIs, SNRIs) | Fall risk")
D("gabapentin", "pain", "Gabapentine", "Gabapentin", "Neurontin",
  "Anticonvulsivant (utilisé pour la douleur neuropathique)", "Anticonvulsant (used for nerve pain)",
  "Douleur neuropathique | Épilepsie", "Nerve pain | Epilepsy",
  "Somnolence | Étourdissements | Démarche instable | Œdème des jambes",
  "Drowsiness | Dizziness | Unsteady walking | Leg swelling",
  "Risque de chute | Dose réduite si fonction rénale diminuée | Ne pas cesser brusquement",
  "Fall risk | Lower dose with reduced kidney function | Don't stop suddenly")
D("pregabalin", "pain", "Prégabaline", "Pregabalin", "Lyrica",
  "Anticonvulsivant (utilisé pour la douleur neuropathique)", "Anticonvulsant (used for nerve pain)",
  "Douleur neuropathique (diabète, zona, moelle) | Fibromyalgie | Anxiété généralisée",
  "Nerve pain (diabetes, shingles, spinal cord) | Fibromyalgia | Generalized anxiety",
  "Somnolence | Étourdissements | Gain de poids | Œdème | Vision trouble | Bouche sèche",
  "Drowsiness | Dizziness | Weight gain | Swelling | Blurred vision | Dry mouth",
  "Souvent au coucher | Risque de chute | Ne pas cesser brusquement",
  "Often at bedtime | Fall risk | Don't stop suddenly")
D("naloxone", "pain", "Naloxone", "Naloxone", "Narcan",
  "Antagoniste des opioïdes (antidote)", "Opioid antagonist (antidote)",
  "Surdose d'opioïdes (dépression respiratoire, sédation profonde)", "Opioid overdose (slowed breathing, deep sedation)",
  "Sevrage aigu : agitation, douleur, nausées, vomissements, tachycardie",
  "Sudden withdrawal: agitation, pain, nausea, vomiting, fast heart rate",
  "Agit moins longtemps que la plupart des opioïdes : surveiller la re-sédation | Suivre le protocole d'urgence",
  "Wears off before most opioids: watch for re-sedation | Follow the emergency protocol")

# ---------------- Neuro ----------------
D("divalproex", "neuro", "Divalproex sodique", "Divalproex sodium", "Epival",
  "Anticonvulsivant / thymorégulateur", "Anticonvulsant / mood stabilizer",
  "Épilepsie | Trouble bipolaire | Prévention de la migraine | Parfois troubles de comportement",
  "Epilepsy | Bipolar disorder | Migraine prevention | Sometimes behaviour problems",
  "Nausées, troubles digestifs | Maux de tête | Tremblements | Somnolence | Gain de poids | Perte de cheveux | Rare : atteinte du foie, pancréatite, ↓ plaquettes",
  "Nausea, stomach upset | Headache | Tremor | Drowsiness | Weight gain | Hair loss | Rare: liver damage, pancreatitis, low platelets",
  "Entérosoluble : ne pas écraser ni croquer | Médicament dangereux (tératogène) : manipuler selon la politique | Taux sérique, enzymes du foie, plaquettes",
  "Enteric-coated: don't crush or chew | Hazardous drug (causes birth defects): handle per policy | Blood level, liver enzymes, platelets")
D("levetiracetam", "neuro", "Lévétiracétam", "Levetiracetam", "Keppra",
  "Anticonvulsivant", "Anticonvulsant",
  "Épilepsie (crises convulsives)", "Epilepsy (seizures)",
  "Somnolence | Étourdissements | Fatigue | Irritabilité, changements d'humeur",
  "Drowsiness | Dizziness | Fatigue | Irritability, mood changes",
  "À heure fixe | Ne pas cesser brusquement | Signaler changements de comportement",
  "At set times | Don't stop suddenly | Report behaviour changes")
D("phenytoin", "neuro", "Phénytoïne", "Phenytoin", "Dilantin",
  "Anticonvulsivant", "Anticonvulsant",
  "Épilepsie", "Epilepsy",
  "Hyperplasie des gencives | Nystagmus | Démarche instable | Confusion | Éruption cutanée",
  "Gum overgrowth | Jerky eye movements | Unsteady walking | Confusion | Rash",
  "Marge thérapeutique étroite : taux sérique | Hygiène buccale | Bien agiter la suspension",
  "Narrow therapeutic range: blood level | Oral hygiene | Shake the suspension well")
D("donepezil", "neuro", "Donépézil", "Donepezil", "Aricept",
  "Inhibiteur de la cholinestérase", "Cholinesterase inhibitor",
  "Maladie d'Alzheimer (ralentir les symptômes)", "Alzheimer's disease (slow the symptoms)",
  "Nausées | Diarrhée | Perte d'appétit | Insomnie, rêves intenses | Bradycardie",
  "Nausea | Diarrhea | Loss of appetite | Insomnia, vivid dreams | Slow heart rate",
  "Habituellement au coucher (le matin si rêves gênants) | Fréquence cardiaque | Poids",
  "Usually at bedtime (morning if dreams are a problem) | Heart rate | Weight")
D("levodopa", "neuro", "Lévodopa-carbidopa", "Levodopa-carbidopa", "Sinemet | Prolopa (lévodopa-bensérazide)",
  "Antiparkinsonien (précurseur de la dopamine)", "Parkinson's medication (dopamine precursor)",
  "Maladie de Parkinson", "Parkinson's disease",
  "Nausées | Hypotension orthostatique | Mouvements involontaires (dyskinésies) | Hallucinations, confusion",
  "Nausea | Orthostatic hypotension | Involuntary movements | Hallucinations, confusion",
  "Donner à l'heure exacte : un retard aggrave la rigidité | Les repas riches en protéines diminuent l'effet | Risque de chute",
  "Give exactly on time: delays worsen stiffness | High-protein meals reduce the effect | Fall risk")

# ---------------- Psych ----------------
D("risperidone", "psych", "Rispéridone", "Risperidone", "Risperdal",
  "Antipsychotique atypique (2e génération)", "Atypical antipsychotic (2nd generation)",
  "Schizophrénie | Trouble bipolaire | Agressivité grave dans la démence (court terme)",
  "Schizophrenia | Bipolar disorder | Severe aggression in dementia (short term)",
  "Symptômes extrapyramidaux (raideur, tremblements, agitation) | Somnolence | Gain de poids | Hypotension orthostatique | Agitation | Insomnie | Maux de tête",
  "Extrapyramidal symptoms (stiffness, tremor, restlessness) | Drowsiness | Weight gain | Orthostatic hypotension | Agitation | Insomnia | Headache",
  "Personne âgée avec démence : risque accru d'AVC et de décès | Risque de chute | Signaler mouvements anormaux",
  "Older adults with dementia: higher stroke and death risk | Fall risk | Report abnormal movements")
D("quetiapine", "psych", "Quétiapine", "Quetiapine", "Seroquel",
  "Antipsychotique atypique (2e génération)", "Atypical antipsychotic (2nd generation)",
  "Schizophrénie | Trouble bipolaire | Dépression (en ajout)", "Schizophrenia | Bipolar disorder | Depression (add-on)",
  "Somnolence | Étourdissements | Hypotension orthostatique | Gain de poids | Hyperglycémie | Bouche sèche | Constipation",
  "Drowsiness | Dizziness | Orthostatic hypotension | Weight gain | High blood sugar | Dry mouth | Constipation",
  "Risque de chute | Personne âgée avec démence : risque accru d'AVC et de décès | Libération prolongée (XR) : ne pas écraser",
  "Fall risk | Older adults with dementia: higher stroke and death risk | Extended-release (XR): don't crush")
D("olanzapine", "psych", "Olanzapine", "Olanzapine", "Zyprexa | Zydis (orodispersible)",
  "Antipsychotique atypique (2e génération)", "Atypical antipsychotic (2nd generation)",
  "Schizophrénie | Trouble bipolaire | Agitation", "Schizophrenia | Bipolar disorder | Agitation",
  "Gain de poids important | Somnolence | Hyperglycémie | Cholestérol élevé | Bouche sèche",
  "Significant weight gain | Drowsiness | High blood sugar | High cholesterol | Dry mouth",
  "Poids et glycémie | Personne âgée avec démence : risque accru d'AVC et de décès",
  "Weight and blood sugar | Older adults with dementia: higher stroke and death risk")
D("haloperidol", "psych", "Halopéridol", "Haloperidol", "Haldol",
  "Antipsychotique typique (1re génération)", "Typical antipsychotic (1st generation)",
  "Psychose | Agitation grave, délirium | Nausées en soins palliatifs",
  "Psychosis | Severe agitation, delirium | Nausea in palliative care",
  "Symptômes extrapyramidaux marqués | Dyskinésie tardive | Sédation | Allongement du QT | Syndrome malin des neuroleptiques (rare : fièvre, rigidité)",
  "Strong extrapyramidal symptoms | Tardive dyskinesia | Sedation | QT prolongation | Neuroleptic malignant syndrome (rare: fever, rigidity)",
  "Signaler rigidité, fièvre, mouvements anormaux | Risque de chute",
  "Report stiffness, fever, abnormal movements | Fall risk")
D("sertraline", "psych", "Sertraline", "Sertraline", "Zoloft",
  "Antidépresseur (ISRS)", "Antidepressant (SSRI)",
  "Dépression | Troubles anxieux | Trouble obsessionnel-compulsif | Stress post-traumatique",
  "Depression | Anxiety disorders | OCD | PTSD",
  "Nausées | Diarrhée | Maux de tête | Insomnie ou somnolence | Troubles sexuels | Hyponatrémie (personne âgée) | ↑ risque de saignement",
  "Nausea | Diarrhea | Headache | Insomnia or drowsiness | Sexual side effects | Low sodium (older adults) | Higher bleeding risk",
  "Effet complet en 4–6 semaines | Surveiller l'humeur et les idées suicidaires au début | Ne pas cesser brusquement",
  "Full effect in 4–6 weeks | Watch mood and suicidal thoughts at the start | Don't stop suddenly")
D("citalopram", "psych", "Citalopram", "Citalopram", "Celexa",
  "Antidépresseur (ISRS)", "Antidepressant (SSRI)",
  "Dépression | Anxiété", "Depression | Anxiety",
  "Nausées | Somnolence | Bouche sèche | Transpiration | Allongement du QT | Hyponatrémie",
  "Nausea | Drowsiness | Dry mouth | Sweating | QT prolongation | Low sodium",
  "Dose limitée chez la personne âgée (risque cardiaque) | Ne pas cesser brusquement",
  "Dose limited in older adults (heart risk) | Don't stop suddenly")
D("escitalopram", "psych", "Escitalopram", "Escitalopram", "Cipralex",
  "Antidépresseur (ISRS)", "Antidepressant (SSRI)",
  "Dépression | Anxiété généralisée | Trouble panique", "Depression | Generalized anxiety | Panic disorder",
  "Nausées | Insomnie ou somnolence | Transpiration | Troubles sexuels | Hyponatrémie",
  "Nausea | Insomnia or drowsiness | Sweating | Sexual side effects | Low sodium",
  "Surveiller l'humeur | Ne pas cesser brusquement", "Watch mood | Don't stop suddenly")
D("mirtazapine", "psych", "Mirtazapine", "Mirtazapine", "Remeron",
  "Antidépresseur (NaSSA)", "Antidepressant (NaSSA)",
  "Dépression (utile si insomnie ou perte d'appétit)", "Depression (helpful with insomnia or poor appetite)",
  "Somnolence | Appétit augmenté | Gain de poids | Bouche sèche | Constipation",
  "Drowsiness | Increased appetite | Weight gain | Dry mouth | Constipation",
  "Au coucher | Risque de chute", "At bedtime | Fall risk")
D("trazodone", "psych", "Trazodone", "Trazodone", "Desyrel",
  "Antidépresseur (souvent utilisé à faible dose pour dormir)", "Antidepressant (often used at low dose for sleep)",
  "Insomnie | Dépression", "Insomnia | Depression",
  "Somnolence | Étourdissements | Hypotension orthostatique | Bouche sèche | Priapisme (rare, urgence)",
  "Drowsiness | Dizziness | Orthostatic hypotension | Dry mouth | Priapism (rare, emergency)",
  "Au coucher | Risque de chute", "At bedtime | Fall risk")
D("lorazepam", "psych", "Lorazépam", "Lorazepam", "Ativan",
  "Benzodiazépine (anxiolytique)", "Benzodiazepine (anti-anxiety)",
  "Anxiété | Agitation | Insomnie (court terme) | Convulsions | Sevrage d'alcool",
  "Anxiety | Agitation | Insomnia (short term) | Seizures | Alcohol withdrawal",
  "Somnolence | Confusion | Chutes | Dépression respiratoire (surtout avec opioïdes) | Dépendance",
  "Drowsiness | Confusion | Falls | Slowed breathing (especially with opioids) | Dependence",
  "Peut être donné sublingual | Risque de chute, surtout chez la personne âgée | Drogue contrôlée : registre",
  "Can be given under the tongue | Fall risk, especially in older adults | Controlled drug: register")
D("zopiclone", "psych", "Zopiclone", "Zopiclone", "Imovane",
  "Hypnotique (somnifère)", "Hypnotic (sleeping pill)",
  "Insomnie (court terme)", "Insomnia (short term)",
  "Goût amer ou métallique | Somnolence le lendemain | Confusion | Chutes",
  "Bitter or metallic taste | Next-day drowsiness | Confusion | Falls",
  "Donner juste avant le coucher | Risque de chute", "Give right at bedtime | Fall risk")
D("lithium", "psych", "Lithium", "Lithium", "Carbolith | Lithane",
  "Thymorégulateur", "Mood stabilizer",
  "Trouble bipolaire", "Bipolar disorder",
  "Tremblements fins | Soif, mictions fréquentes | Nausées | Gain de poids | Hypothyroïdie | Toxicité : diarrhée, vomissements, gros tremblements, démarche instable, confusion",
  "Fine tremor | Thirst, frequent urination | Nausea | Weight gain | Underactive thyroid | Toxicity: diarrhea, vomiting, coarse tremor, unsteady walking, confusion",
  "Marge thérapeutique étroite : lithémie | Hydratation et sel constants | AINS, diurétiques et IECA augmentent le taux",
  "Narrow therapeutic range: lithium level | Keep fluids and salt steady | NSAIDs, diuretics and ACE inhibitors raise the level")

# ---------------- Respiratory ----------------
D("salbutamol", "resp", "Salbutamol", "Salbutamol", "Ventolin | Airomir",
  "Bronchodilatateur bêta-2 à courte action (BACA)", "Short-acting beta-2 bronchodilator (SABA)",
  "Soulagement rapide du bronchospasme (asthme, MPOC) — médicament de secours",
  "Quick relief of bronchospasm (asthma, COPD) — rescue inhaler",
  "Tremblements | Tachycardie, palpitations | Nervosité | Hypokaliémie",
  "Tremor | Fast heart rate, palpitations | Nervousness | Low potassium",
  "Agiter l'inhalateur; utiliser une chambre d'espacement | FC et respiration avant et après",
  "Shake the inhaler; use a spacer | HR and breathing before and after")
D("ipratropium", "resp", "Ipratropium", "Ipratropium", "Atrovent",
  "Bronchodilatateur anticholinergique à courte action", "Short-acting anticholinergic bronchodilator",
  "MPOC | Bronchospasme (souvent avec le salbutamol)", "COPD | Bronchospasm (often with salbutamol)",
  "Bouche sèche | Toux | Goût amer | Vision trouble si contact avec les yeux",
  "Dry mouth | Cough | Bitter taste | Blurred vision if it gets in the eyes",
  "Éviter le contact avec les yeux (nébulisation)", "Keep out of the eyes (nebulizer)")
D("tiotropium", "resp", "Tiotropium", "Tiotropium", "Spiriva",
  "Anticholinergique à longue action (AMLA)", "Long-acting anticholinergic (LAMA)",
  "MPOC (traitement d'entretien quotidien)", "COPD (daily maintenance)",
  "Bouche sèche | Constipation | Rétention urinaire | Mal de gorge",
  "Dry mouth | Constipation | Urinary retention | Sore throat",
  "Une fois par jour | Pas un médicament de secours | Capsules HandiHaler : à inhaler, ne pas avaler",
  "Once a day | Not a rescue inhaler | HandiHaler capsules: inhale, don't swallow")
D("fluticasone-salmeterol", "resp", "Fluticasone + salmétérol", "Fluticasone + salmeterol", "Advair",
  "Corticostéroïde inhalé + bronchodilatateur à longue action", "Inhaled corticosteroid + long-acting bronchodilator",
  "Asthme | MPOC (traitement d'entretien)", "Asthma | COPD (maintenance)",
  "Muguet (candidose buccale) | Voix rauque | Maux de tête | Tremblements | Pneumonie (MPOC)",
  "Oral thrush | Hoarse voice | Headache | Tremor | Pneumonia (COPD)",
  "Rincer la bouche et cracher après | Pas un médicament de secours",
  "Rinse mouth and spit after use | Not a rescue inhaler")

# ---------------- Infection ----------------
D("amoxicillin", "infection", "Amoxicilline", "Amoxicillin", "Amoxil",
  "Antibiotique (pénicilline)", "Antibiotic (penicillin)",
  "Infections ORL (oreilles, gorge, sinus) | Pneumonie | Infections urinaires | H. pylori",
  "Ear, throat and sinus infections | Pneumonia | Urinary infections | H. pylori",
  "Diarrhée | Nausées | Éruption cutanée | Allergie (anaphylaxie rare)",
  "Diarrhea | Nausea | Rash | Allergy (rare anaphylaxis)",
  "Vérifier l'allergie à la pénicilline AVANT | Respecter l'horaire et terminer le traitement",
  "Check for penicillin allergy BEFORE | Keep to the schedule and finish the course")
D("amox-clav", "infection", "Amoxicilline-clavulanate", "Amoxicillin-clavulanate", "Clavulin",
  "Antibiotique (pénicilline + inhibiteur de bêta-lactamase)", "Antibiotic (penicillin + beta-lactamase inhibitor)",
  "Pneumonie | Sinusite | Infections de la peau et morsures | Infections urinaires",
  "Pneumonia | Sinusitis | Skin infections and bites | Urinary infections",
  "Diarrhée (fréquente) | Nausées | Éruption cutanée | Infection à levures",
  "Diarrhea (common) | Nausea | Rash | Yeast infection",
  "Vérifier l'allergie à la pénicilline | Avec un repas", "Check for penicillin allergy | Give with a meal")
D("cephalexin", "infection", "Céphalexine", "Cephalexin", "Keflex",
  "Antibiotique (céphalosporine 1re génération)", "Antibiotic (1st-generation cephalosporin)",
  "Infections de la peau (cellulite) | Infections urinaires | Infections des os",
  "Skin infections (cellulitis) | Urinary infections | Bone infections",
  "Diarrhée | Nausées | Éruption cutanée",
  "Diarrhea | Nausea | Rash",
  "Vérifier les allergies (faible risque croisé avec la pénicilline)", "Check allergies (small cross-reaction risk with penicillin)")
D("ciprofloxacin", "infection", "Ciprofloxacine", "Ciprofloxacin", "Cipro",
  "Antibiotique (fluoroquinolone)", "Antibiotic (fluoroquinolone)",
  "Infections urinaires compliquées | Infections digestives | Infections des os",
  "Complicated urinary infections | Gut infections | Bone infections",
  "Nausées | Diarrhée | Étourdissements, confusion | Photosensibilité | Tendinite ou rupture de tendon | Allongement du QT",
  "Nausea | Diarrhea | Dizziness, confusion | Sun sensitivity | Tendon pain or rupture | QT prolongation",
  "Séparer du calcium, fer, magnésium et antiacides (2 h avant ou 6 h après) | Signaler douleur au tendon (surtout personne âgée ou sous cortico)",
  "Separate from calcium, iron, magnesium and antacids (2 h before or 6 h after) | Report tendon pain (especially older adults or on steroids)")
D("nitrofurantoin", "infection", "Nitrofurantoïne", "Nitrofurantoin", "Macrobid",
  "Antibiotique urinaire", "Urinary antibiotic",
  "Cystite (infection urinaire basse)", "Bladder infection (cystitis)",
  "Nausées | Maux de tête | Urine brun foncé (sans danger) | Réactions pulmonaires (rare)",
  "Nausea | Headache | Dark brown urine (harmless) | Lung reactions (rare)",
  "Avec nourriture | Évité si la fonction rénale est diminuée", "Give with food | Avoided with reduced kidney function")
D("smx-tmp", "infection", "Sulfaméthoxazole-triméthoprime", "Sulfamethoxazole-trimethoprim", "Septra | Bactrim",
  "Antibiotique (sulfamide)", "Antibiotic (sulfonamide)",
  "Infections urinaires | Infections de la peau (SARM) | Prévention de la pneumonie à Pneumocystis",
  "Urinary infections | Skin infections (MRSA) | Preventing Pneumocystis pneumonia",
  "Éruption cutanée (peut être grave) | Nausées | Hyperkaliémie | Photosensibilité",
  "Rash (can be severe) | Nausea | High potassium | Sun sensitivity",
  "Vérifier l'allergie aux sulfas | Bien s'hydrater | Interaction importante avec la warfarine",
  "Check for sulfa allergy | Drink plenty of fluids | Major interaction with warfarin")
D("metronidazole", "infection", "Métronidazole", "Metronidazole", "Flagyl",
  "Antibiotique / antiparasitaire", "Antibiotic / antiparasitic",
  "C. difficile | Infections abdominales (anaérobies) | Vaginose bactérienne",
  "C. difficile | Abdominal infections (anaerobes) | Bacterial vaginosis",
  "Goût métallique | Nausées | Urine foncée | Neuropathie (long terme)",
  "Metallic taste | Nausea | Dark urine | Nerve damage (long term)",
  "Aucun alcool pendant et 48 h après (réaction violente)", "No alcohol during and for 48 h after (severe reaction)")
D("vancomycin", "infection", "Vancomycine", "Vancomycin", "Vancocin",
  "Antibiotique (glycopeptide)", "Antibiotic (glycopeptide)",
  "Infections à SARM (IV) | C. difficile (par la bouche)", "MRSA infections (IV) | C. difficile (by mouth)",
  "Atteinte des reins | Atteinte de l'audition | Syndrome de l'homme rouge (rougeur si perfusion trop rapide)",
  "Kidney damage | Hearing damage | Red man syndrome (flushing if infused too fast)",
  "IV : perfuser lentement (au moins 60 min) | Taux sérique et créatinine",
  "IV: infuse slowly (at least 60 min) | Blood level and creatinine")

# ---------------- Vitamins / minerals ----------------
D("thiamine", "vitamins", "Thiamine (vitamine B1)", "Thiamine (vitamin B1)", "",
  "Vitamine", "Vitamin",
  "Carence en B1 | Alcoolisme (prévenir l'encéphalopathie de Wernicke) | Malnutrition",
  "Vitamin B1 deficiency | Alcohol use disorder (prevent Wernicke's encephalopathy) | Malnutrition",
  "Rares | Réaction au site d'injection (IM/IV)", "Rare | Injection site reaction (IM/IV)",
  "Souvent donnée AVANT le glucose chez la personne alcoolique", "Often given BEFORE glucose in people with alcohol use disorder")
D("vitamin-d", "vitamins", "Cholécalciférol (vitamine D3)", "Cholecalciferol (vitamin D3)", "D-Tabs | Euro-D",
  "Vitamine", "Vitamin",
  "Prévenir ou traiter la carence en vitamine D | Ostéoporose (avec calcium) | Prévention des chutes et fractures",
  "Prevent or treat low vitamin D | Osteoporosis (with calcium) | Preventing falls and fractures",
  "Rares | Surdose : hypercalcémie (nausées, constipation, confusion)",
  "Rare | Overdose: high calcium (nausea, constipation, confusion)",
  "Vérifier la fréquence : 1 000 UI est souvent quotidien, 10 000 ou 50 000 UI souvent hebdomadaire ou mensuel",
  "Check the frequency: 1,000 IU is often daily; 10,000 or 50,000 IU is often weekly or monthly")
D("vitamin-b12", "vitamins", "Cyanocobalamine (vitamine B12)", "Cyanocobalamin (vitamin B12)", "",
  "Vitamine", "Vitamin",
  "Carence en B12 | Anémie pernicieuse | Carence due à la metformine ou aux IPP",
  "Vitamin B12 deficiency | Pernicious anemia | Deficiency from metformin or PPIs",
  "Rares | Douleur au site d'injection", "Rare | Injection site pain",
  "Par la bouche, sublingual ou injection (IM/SC) selon l'ordonnance", "By mouth, under the tongue or by injection (IM/SC) per the order")
D("folic-acid", "vitamins", "Acide folique (vitamine B9)", "Folic acid (vitamin B9)", "",
  "Vitamine", "Vitamin",
  "Carence en folates, anémie | Grossesse | Avec le méthotrexate | Alcoolisme",
  "Folate deficiency, anemia | Pregnancy | With methotrexate | Alcohol use disorder",
  "Rares", "Rare")
D("calcium", "vitamins", "Carbonate de calcium", "Calcium carbonate", "Caltrate | Os-Cal | Tums",
  "Supplément de calcium / antiacide", "Calcium supplement / antacid",
  "Ostéoporose (avec vitamine D) | Faible apport en calcium | Brûlures d'estomac",
  "Osteoporosis (with vitamin D) | Low calcium intake | Heartburn",
  "Constipation | Ballonnements | Gaz",
  "Constipation | Bloating | Gas",
  "Avec les repas | Séparer de la lévothyroxine, du fer et des quinolones",
  "With meals | Separate from levothyroxine, iron and quinolones")
D("ferrous-sulfate", "vitamins", "Sulfate ferreux (fer)", "Ferrous sulfate (iron)", "Fer-In-Sol | Palafer (fumarate)",
  "Supplément de fer", "Iron supplement",
  "Anémie par manque de fer", "Iron-deficiency anemia",
  "Selles noires (normal) | Constipation | Nausées | Douleurs d'estomac",
  "Black stools (normal) | Constipation | Nausea | Stomach pain",
  "Mieux absorbé à jeun ou avec de la vitamine C; avec nourriture si mal toléré | Séparer du calcium, des antiacides, de la lévothyroxine | Liquide : paille (tache les dents)",
  "Best absorbed on an empty stomach or with vitamin C; with food if not tolerated | Separate from calcium, antacids, levothyroxine | Liquid: use a straw (stains teeth)")
D("potassium-chloride", "vitamins", "Chlorure de potassium (KCl)", "Potassium chloride (KCl)", "K-Dur | Micro-K | K-Lyte",
  "Supplément d'électrolyte", "Electrolyte supplement",
  "Hypokaliémie (K+ bas), souvent avec les diurétiques", "Low potassium, often with diuretics",
  "Irritation d'estomac | Nausées | Diarrhée | Hyperkaliémie (trop de K+)",
  "Stomach irritation | Nausea | Diarrhea | High potassium (too much)",
  "Avec nourriture et un grand verre d'eau | Libération prolongée : ne pas écraser | IV : médicament de haute alerte, jamais en bolus | Potassium sanguin",
  "With food and a full glass of water | Extended-release: don't crush | IV: high-alert, never as a push | Blood potassium")

# ---------------- Other ----------------
D("tamsulosin", "other", "Tamsulosine", "Tamsulosin", "Flomax",
  "Alpha-bloquant", "Alpha blocker",
  "Hypertrophie bénigne de la prostate (difficulté à uriner) | Aider à passer un calcul rénal",
  "Enlarged prostate (trouble urinating) | Helping pass a kidney stone",
  "Hypotension orthostatique | Étourdissements | Congestion nasale | Troubles de l'éjaculation",
  "Orthostatic hypotension | Dizziness | Stuffy nose | Ejaculation problems",
  "Ne pas ouvrir ni écraser la capsule | 30 min après le même repas chaque jour | Risque de chute",
  "Don't open or crush the capsule | 30 min after the same meal each day | Fall risk")
D("oxybutynin", "other", "Oxybutynine", "Oxybutynin", "Ditropan",
  "Anticholinergique (antispasmodique urinaire)", "Anticholinergic (bladder antispasmodic)",
  "Vessie hyperactive (urgences, incontinence)", "Overactive bladder (urgency, incontinence)",
  "Bouche sèche | Constipation | Vision trouble | Rétention urinaire | Confusion chez la personne âgée",
  "Dry mouth | Constipation | Blurred vision | Urinary retention | Confusion in older adults",
  "Prudence chez la personne âgée (effets anticholinergiques)", "Caution in older adults (anticholinergic effects)")
D("allopurinol", "other", "Allopurinol", "Allopurinol", "Zyloprim",
  "Inhibiteur de la xanthine oxydase (baisse l'acide urique)", "Xanthine oxidase inhibitor (lowers uric acid)",
  "Prévention des crises de goutte | Acide urique élevé", "Preventing gout attacks | High uric acid",
  "Éruption cutanée (peut être grave) | Troubles digestifs | Crise de goutte au début du traitement",
  "Rash (can be severe) | Stomach upset | Gout flare when starting",
  "Signaler toute éruption cutanée immédiatement | Bien s'hydrater | Après un repas",
  "Report any rash right away | Drink plenty of fluids | After a meal")
D("alendronate", "other", "Alendronate", "Alendronate", "Fosamax",
  "Bisphosphonate", "Bisphosphonate",
  "Ostéoporose (prévenir les fractures)", "Osteoporosis (preventing fractures)",
  "Brûlures de l'œsophage | Brûlures d'estomac | Douleurs musculaires ou osseuses | Ostéonécrose de la mâchoire (rare)",
  "Esophagus irritation | Heartburn | Muscle or bone pain | Jaw bone damage (rare)",
  "Le matin à jeun avec un grand verre d'eau | Rester assis ou debout 30 min et ne rien manger avant | Souvent 1 fois par semaine",
  "In the morning on an empty stomach with a full glass of water | Stay upright 30 min and eat nothing first | Often once a week")

# ================= Added in v3 (from the stage FADM + common unit meds) =================

# --- From the FADM ---
D("piperacillin-tazobactam", "infection", "Pipéracilline-tazobactam", "Piperacillin-tazobactam", "Tazocin",
  "Antibiotique (pénicilline à large spectre + inhibiteur de bêta-lactamase)", "Antibiotic (broad-spectrum penicillin + beta-lactamase inhibitor)",
  "Pneumonie grave ou acquise à l'hôpital | Infections abdominales compliquées | Infections graves de la peau | Sepsis, neutropénie fébrile",
  "Severe or hospital-acquired pneumonia | Complicated abdominal infections | Severe skin infections | Sepsis, febrile neutropenia",
  "Diarrhée (risque de C. difficile) | Nausées | Éruption cutanée | Irritation de la veine au site IV | Hypokaliémie | Atteinte des reins (surtout avec la vancomycine)",
  "Diarrhea (C. difficile risk) | Nausea | Rash | Vein irritation at the IV site | Low potassium | Kidney damage (especially with vancomycin)",
  "Vérifier l'allergie à la pénicilline AVANT | Respecter les heures exactes (ex. q6h) | Site IV et signes d'allergie pendant la perfusion",
  "Check for penicillin allergy BEFORE | Keep to exact times (e.g. q6h) | IV site and allergy signs during the infusion")
D("sulfasalazine", "other", "Sulfasalazine", "Sulfasalazine", "Salazopyrin | Salazopyrin En-Tabs",
  "Anti-inflammatoire (aminosalicylé) / antirhumatismal (ARMM)", "Anti-inflammatory (aminosalicylate) / antirheumatic (DMARD)",
  "Polyarthrite rhumatoïde | Colite ulcéreuse | Maladie de Crohn (côlon)",
  "Rheumatoid arthritis | Ulcerative colitis | Crohn's disease (colon)",
  "Nausées, perte d'appétit | Maux de tête | Urine (et parfois peau) jaune-orange, sans danger | Photosensibilité | Éruption cutanée | Baisse des globules (rare)",
  "Nausea, loss of appetite | Headache | Yellow-orange urine (sometimes skin), harmless | Sun sensitivity | Rash | Low blood counts (rare)",
  "Vérifier l'allergie aux sulfas et à l'AAS | Entérosoluble : ne pas écraser | Après les repas avec un grand verre d'eau | Formule sanguine et foie",
  "Check for sulfa and ASA allergy | Enteric-coated: don't crush | After meals with a full glass of water | Blood counts and liver")
D("ipratropium-salbutamol", "resp", "Ipratropium + salbutamol", "Ipratropium + salbutamol", "Combivent",
  "Bronchodilatateurs combinés (anticholinergique + bêta-2 à courte action)", "Combined bronchodilators (anticholinergic + short-acting beta-2)",
  "MPOC | Bronchospasme", "COPD | Bronchospasm",
  "Bouche sèche | Tremblements | Tachycardie, palpitations | Toux | Nervosité",
  "Dry mouth | Tremor | Fast heart rate, palpitations | Cough | Nervousness",
  "Nébulisation : éviter le contact avec les yeux | FC, FR, saturation et respiration avant et après",
  "Nebulizer: keep out of the eyes | HR, RR, oxygen saturation and breathing before and after")
D("glycerin", "gi", "Glycérine (suppositoire)", "Glycerin (suppository)", "",
  "Laxatif (suppositoire)", "Laxative (suppository)",
  "Constipation", "Constipation",
  "Irritation rectale | Crampes", "Rectal irritation | Cramps",
  "Agit en 15–60 min | Patient couché sur le côté gauche; insérer contre la paroi du rectum, pas dans les selles | Noter le résultat",
  "Works in 15–60 min | Patient on the left side; insert against the rectal wall, not into stool | Record the result")
D("bisacodyl", "gi", "Bisacodyl", "Bisacodyl", "Dulcolax",
  "Laxatif stimulant", "Stimulant laxative",
  "Constipation | Préparation de l'intestin avant un examen", "Constipation | Bowel prep before a procedure",
  "Crampes abdominales | Diarrhée | Irritation rectale (suppositoire)",
  "Stomach cramps | Diarrhea | Rectal irritation (suppository)",
  "Suppositoire : agit en 15–60 min | Comprimé : agit en 6–12 h, entérosoluble, ne pas écraser; pas avec du lait ou un antiacide (1 h) | Noter le résultat",
  "Suppository: works in 15–60 min | Tablet: works in 6–12 h, enteric-coated, don't crush; not with milk or antacids (1 h) | Record the result")
D("codeine", "pain", "Codéine", "Codeine", "Tylenol #3 (avec acétaminophène)",
  "Analgésique opioïde faible / antitussif", "Weak opioid pain reliever / cough suppressant",
  "Douleur légère à modérée | Toux", "Mild to moderate pain | Cough",
  "Constipation | Nausées | Somnolence | Dépression respiratoire",
  "Constipation | Nausea | Drowsiness | Slowed breathing",
  "Le foie la transforme en morphine; l'effet varie beaucoup d'une personne à l'autre | Une « allergie » à la codéine est souvent une intolérance (nausées) : vérifier le type de réaction | Tylenol #3 contient de l'acétaminophène",
  "The liver turns it into morphine; the effect varies a lot between people | A codeine \"allergy\" is often an intolerance (nausea): check what reaction it was | Tylenol #3 contains acetaminophen")

# --- Other common unit meds ---
D("magnesium-hydroxide", "gi", "Hydroxyde de magnésium (lait de magnésie)", "Magnesium hydroxide (milk of magnesia)", "Lait de magnésie | Phillips",
  "Laxatif osmotique / antiacide", "Osmotic laxative / antacid",
  "Constipation | Brûlures d'estomac", "Constipation | Heartburn",
  "Diarrhée | Crampes | Magnésium élevé en cas d'insuffisance rénale",
  "Diarrhea | Cramps | High magnesium with kidney failure",
  "Évité en insuffisance rénale | Agit en 30 min à 6 h | Séparer des autres médicaments (2 h)",
  "Avoided with kidney failure | Works in 30 min to 6 h | Separate from other meds (2 h)")
D("oxazepam", "psych", "Oxazépam", "Oxazepam", "Serax",
  "Benzodiazépine (anxiolytique)", "Benzodiazepine (anti-anxiety)",
  "Anxiété | Insomnie | Sevrage d'alcool", "Anxiety | Insomnia | Alcohol withdrawal",
  "Somnolence | Confusion | Chutes | Dépendance",
  "Drowsiness | Confusion | Falls | Dependence",
  "Souvent choisi chez la personne âgée ou si le foie est atteint | Risque de chute | Drogue contrôlée",
  "Often chosen for older adults or liver disease | Fall risk | Controlled drug")
D("clonazepam", "psych", "Clonazépam", "Clonazepam", "Rivotril",
  "Benzodiazépine (longue action)", "Benzodiazepine (long-acting)",
  "Trouble panique | Épilepsie | Anxiété", "Panic disorder | Epilepsy | Anxiety",
  "Somnolence | Démarche instable | Confusion | Chutes | Dépendance",
  "Drowsiness | Unsteady walking | Confusion | Falls | Dependence",
  "Ne pas cesser brusquement (risque de convulsions) | Risque de chute | Drogue contrôlée",
  "Don't stop suddenly (seizure risk) | Fall risk | Controlled drug")
D("temazepam", "psych", "Témazépam", "Temazepam", "Restoril",
  "Benzodiazépine (hypnotique)", "Benzodiazepine (sleeping pill)",
  "Insomnie (court terme)", "Insomnia (short term)",
  "Somnolence le lendemain | Confusion | Chutes | Dépendance",
  "Next-day drowsiness | Confusion | Falls | Dependence",
  "Au coucher | Risque de chute | Drogue contrôlée", "At bedtime | Fall risk | Controlled drug")
D("venlafaxine", "psych", "Venlafaxine", "Venlafaxine", "Effexor XR",
  "Antidépresseur (IRSN)", "Antidepressant (SNRI)",
  "Dépression | Anxiété généralisée | Trouble panique", "Depression | Generalized anxiety | Panic disorder",
  "Nausées | Transpiration | Hausse de la TA | Insomnie | Troubles sexuels | Symptômes d'arrêt marqués",
  "Nausea | Sweating | Higher blood pressure | Insomnia | Sexual side effects | Strong withdrawal symptoms",
  "TA | Avec nourriture | Ne pas cesser brusquement | Surveiller l'humeur",
  "Blood pressure | With food | Don't stop suddenly | Watch mood")
D("duloxetine", "psych", "Duloxétine", "Duloxetine", "Cymbalta",
  "Antidépresseur (IRSN)", "Antidepressant (SNRI)",
  "Dépression | Anxiété généralisée | Douleur neuropathique (diabète) | Douleur chronique",
  "Depression | Generalized anxiety | Diabetic nerve pain | Chronic pain",
  "Nausées | Bouche sèche | Somnolence | Constipation | Transpiration",
  "Nausea | Dry mouth | Drowsiness | Constipation | Sweating",
  "Ne pas ouvrir ni écraser la capsule | Ne pas cesser brusquement",
  "Don't open or crush the capsule | Don't stop suddenly")
D("bupropion", "psych", "Bupropion", "Bupropion", "Wellbutrin | Zyban",
  "Antidépresseur (IRND)", "Antidepressant (NDRI)",
  "Dépression | Aide à l'arrêt du tabac", "Depression | Help to quit smoking",
  "Insomnie | Bouche sèche | Maux de tête | Agitation | Risque de convulsions",
  "Insomnia | Dry mouth | Headache | Agitation | Seizure risk",
  "Pas au coucher (insomnie) | Ne pas écraser | Évité si convulsions ou trouble alimentaire",
  "Not at bedtime (insomnia) | Don't crush | Avoided with seizures or eating disorders")
D("ceftriaxone", "infection", "Ceftriaxone", "Ceftriaxone", "Rocephin",
  "Antibiotique (céphalosporine 3e génération)", "Antibiotic (3rd-generation cephalosporin)",
  "Pneumonie | Pyélonéphrite | Méningite | Sepsis | Gonorrhée",
  "Pneumonia | Kidney infection | Meningitis | Sepsis | Gonorrhea",
  "Diarrhée | Éruption cutanée | Douleur au site d'injection | Hausse des enzymes du foie",
  "Diarrhea | Rash | Injection site pain | Raised liver enzymes",
  "Vérifier les allergies | Ne pas donner en même temps qu'une solution IV contenant du calcium | IM : souvent diluée avec de la lidocaïne",
  "Check allergies | Don't give at the same time as IV solutions containing calcium | IM: often mixed with lidocaine")
D("azithromycin", "infection", "Azithromycine", "Azithromycin", "Zithromax",
  "Antibiotique (macrolide)", "Antibiotic (macrolide)",
  "Pneumonie | Exacerbation de MPOC | Infections ORL | Chlamydia",
  "Pneumonia | COPD flare | Ear, nose and throat infections | Chlamydia",
  "Diarrhée | Nausées | Douleurs abdominales | Allongement du QT",
  "Diarrhea | Nausea | Stomach pain | QT prolongation",
  "Traitement court (souvent 3–5 jours) | Prudence avec les autres médicaments qui allongent le QT",
  "Short course (often 3–5 days) | Caution with other drugs that prolong QT")
D("amiodarone", "cardio", "Amiodarone", "Amiodarone", "Cordarone",
  "Antiarythmique", "Antiarrhythmic",
  "Fibrillation auriculaire | Arythmies ventriculaires", "Atrial fibrillation | Ventricular arrhythmias",
  "Bradycardie | Hypotension (IV) | Photosensibilité, peau gris-bleu | Troubles de la thyroïde | Toxicité pulmonaire | Atteinte du foie",
  "Slow heart rate | Low blood pressure (IV) | Sun sensitivity, blue-grey skin | Thyroid problems | Lung toxicity | Liver damage",
  "FC et ECG | Thyroïde, foie et poumons (long terme) | Augmente l'effet de la warfarine et de la digoxine",
  "HR and ECG | Thyroid, liver and lungs (long term) | Increases the effect of warfarin and digoxin")
D("candesartan", "cardio", "Candésartan", "Candesartan", "Atacand",
  "Antagoniste des récepteurs de l'angiotensine (ARA)", "Angiotensin receptor blocker (ARB)",
  "HTA | Insuffisance cardiaque", "High blood pressure | Heart failure",
  "Étourdissements | Hyperkaliémie | Hypotension",
  "Dizziness | High potassium | Low blood pressure",
  "TA, potassium et créatinine", "BP, potassium and creatinine")
D("fentanyl-patch", "pain", "Fentanyl (timbre)", "Fentanyl (patch)", "Duragesic",
  "Analgésique opioïde puissant (transdermique)", "Strong opioid pain reliever (skin patch)",
  "Douleur chronique sévère et stable, chez un patient déjà habitué aux opioïdes",
  "Severe, stable chronic pain in a patient already used to opioids",
  "Constipation | Nausées | Somnolence | Dépression respiratoire | Irritation de la peau",
  "Constipation | Nausea | Drowsiness | Slowed breathing | Skin irritation",
  "Changé habituellement aux 72 h : retirer l'ancien timbre | La chaleur (fièvre, coussin chauffant) augmente l'absorption | Ne pas couper | Plier côté collant ensemble pour jeter; noter date et site",
  "Usually changed every 72 h: remove the old patch | Heat (fever, heating pad) increases absorption | Don't cut | Fold sticky sides together to discard; record date and site")
D("budesonide-formoterol", "resp", "Budésonide + formotérol", "Budesonide + formoterol", "Symbicort",
  "Corticostéroïde inhalé + bronchodilatateur à longue action", "Inhaled corticosteroid + long-acting bronchodilator",
  "Asthme | MPOC", "Asthma | COPD",
  "Muguet (candidose buccale) | Voix rauque | Tremblements | Palpitations",
  "Oral thrush | Hoarse voice | Tremor | Palpitations",
  "Rincer la bouche et cracher après | Dans l'asthme, parfois aussi utilisé au besoin (selon l'ordonnance)",
  "Rinse mouth and spit after | In asthma, sometimes also used as needed (per the order)")
D("montelukast", "resp", "Montélukast", "Montelukast", "Singulair",
  "Antagoniste des leucotriènes", "Leukotriene receptor antagonist",
  "Asthme (prévention) | Rhinite allergique", "Asthma (prevention) | Allergies (allergic rhinitis)",
  "Maux de tête | Douleur abdominale | Changements d'humeur, cauchemars",
  "Headache | Stomach pain | Mood changes, nightmares",
  "Le soir | Signaler changements d'humeur ou de comportement | Pas pour une crise aiguë",
  "In the evening | Report mood or behaviour changes | Not for an acute attack")
D("memantine", "neuro", "Mémantine", "Memantine", "Ebixa",
  "Antagoniste des récepteurs NMDA", "NMDA receptor antagonist",
  "Maladie d'Alzheimer modérée à sévère", "Moderate to severe Alzheimer's disease",
  "Étourdissements | Maux de tête | Confusion | Constipation | Somnolence",
  "Dizziness | Headache | Confusion | Constipation | Drowsiness",
  "Dose réduite si fonction rénale diminuée | Risque de chute", "Lower dose with reduced kidney function | Fall risk")
D("insulin-nph", "endo", "Insuline NPH (action intermédiaire)", "NPH insulin (intermediate-acting)", "Humulin N | Novolin ge NPH",
  "Insuline à action intermédiaire", "Intermediate-acting insulin",
  "Diabète : contrôle de base de la glycémie (souvent 1–2 fois par jour)", "Diabetes: background blood sugar control (often once or twice a day)",
  "Hypoglycémie (surtout au pic, 4–12 h après) | Réaction au site d'injection | Gain de poids",
  "Low blood sugar (especially at peak, 4–12 h after) | Injection site reaction | Weight gain",
  "Médicament de haute alerte : double vérification | Suspension trouble : rouler doucement entre les mains pour mélanger, ne pas secouer | Glycémie",
  "High-alert drug: double check | Cloudy suspension: roll gently between the hands to mix, don't shake | Blood sugar")
D("glucagon", "endo", "Glucagon", "Glucagon", "GlucaGen | Baqsimi (nasal)",
  "Hormone qui augmente la glycémie", "Hormone that raises blood sugar",
  "Hypoglycémie sévère quand le patient ne peut rien prendre par la bouche", "Severe low blood sugar when the patient can't take anything by mouth",
  "Nausées | Vomissements", "Nausea | Vomiting",
  "Suivre le protocole d'hypoglycémie | Coucher sur le côté (risque de vomissement) | Donner des glucides par la bouche dès que le patient peut avaler",
  "Follow the low blood sugar protocol | Turn on the side (vomiting risk) | Give carbohydrates by mouth as soon as the patient can swallow")
D("dexamethasone", "endo", "Dexaméthasone", "Dexamethasone", "Decadron",
  "Corticostéroïde (puissant)", "Corticosteroid (potent)",
  "Œdème cérébral | Nausées (chimiothérapie, soins palliatifs) | Inflammation grave | Croup",
  "Brain swelling | Nausea (chemo, palliative care) | Severe inflammation | Croup",
  "Hyperglycémie | Insomnie, agitation | Appétit augmenté | Infections | Rétention d'eau",
  "High blood sugar | Insomnia, agitation | Increased appetite | Infections | Fluid retention",
  "Le matin avec nourriture | Glycémie | Ne pas cesser brusquement après un usage prolongé",
  "In the morning with food | Blood sugar | Don't stop suddenly after long-term use")
D("magnesium-oxide", "vitamins", "Oxyde de magnésium", "Magnesium oxide", "Mag-Ox",
  "Supplément de minéral", "Mineral supplement",
  "Magnésium bas (hypomagnésémie)", "Low magnesium",
  "Diarrhée | Crampes", "Diarrhea | Cramps",
  "Séparer de la lévothyroxine et des quinolones | Prudence en insuffisance rénale",
  "Separate from levothyroxine and quinolones | Caution with kidney failure")
D("nicotine-patch", "other", "Nicotine (timbre)", "Nicotine (patch)", "Nicoderm | Habitrol",
  "Thérapie de remplacement de la nicotine", "Nicotine replacement therapy",
  "Arrêt du tabac | Prévenir le sevrage de nicotine à l'hôpital", "Quitting smoking | Preventing nicotine withdrawal in hospital",
  "Irritation de la peau | Rêves intenses, insomnie | Nausées | Maux de tête",
  "Skin irritation | Vivid dreams, insomnia | Nausea | Headache",
  "Retirer l'ancien timbre | Alterner les sites | Peut être retiré au coucher si troubles de sommeil (selon l'ordonnance)",
  "Remove the old patch | Rotate sites | Can be removed at bedtime for sleep problems (per the order)")

# --- Extra brand names seen on the FADM ---
_extra_brands = {"enoxaparin": ["Noromby"], "prednisone": ["Deltasone", "Winpred"]}
for _d in drugs:
    _d["brands"] += [b for b in _extra_brands.get(_d["id"], []) if b not in _d["brands"]]

# ---------------- checks ----------------
ids = [d["id"] for d in drugs]
assert len(ids) == len(set(ids)), "duplicate ids"
for d in drugs:
    for k in ("name", "drugClass"):
        assert d[k]["fr"] and d[k]["en"], (d["id"], k)
    for k in ("why", "sideEffects"):
        assert d[k]["fr"] and d[k]["en"], (d["id"], k)
        assert len(d[k]["fr"]) == len(d[k]["en"]), (d["id"], k, "fr/en length mismatch")
    assert len(d["watch"]["fr"]) == len(d["watch"]["en"]), (d["id"], "watch mismatch")

out = sys.argv[1]
with open(out, "w", encoding="utf-8") as f:
    json.dump(drugs, f, ensure_ascii=False, indent=1)
from collections import Counter
print(len(drugs), "drugs", dict(Counter(d["category"] for d in drugs)))
