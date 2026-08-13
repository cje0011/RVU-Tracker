import streamlit as st

master_codes = {
    "D0120": {"points": 6, "desc": "Periodic oral evaluation"},
    "D0120.3": {"points": 0, "desc": "Re-Evaluation Of Periodontal Therapy (NC predoc)"},
    "D0140": {"points": 6, "desc": "Limited Oral Eval-Prob Focused (New Patient)"},
    "D0140.1": {"points": 6, "desc": "Limited Oral Eval, Problem Focused (Inactive/Current Pt)"},
    "D0140.3": {"points": 0, "desc": "Limited Oral Evaluation-Problem Focused (Board Pt Screen)"},
    "D0150": {"points": 9, "desc": "Comprehensive oral evaluation"},
    "D0170": {"points": 4, "desc": "Re-eval-limited-prob focused"},
    "D0180": {"points": 3, "desc": "Comprehensive periodontal eval-new or established patient"},
    "D0210": {"points": 6, "desc": "Intraoral - Comprehensive Series - Display full dentition"},
    "D0220": {"points": 1, "desc": "Intraoral-periapical 1st film"},
    "D0220.1": {"points": 1, "desc": "First Periapical N/C"},
    "D0220.2": {"points": 1, "desc": "Additional Periapicals N/C"},
    "D0230": {"points": 1, "desc": "Intraoral-periapical addı film"},
    "D0240": {"points": 0, "desc": "Intraoral occlusal film"},
    "D0270": {"points": 1, "desc": "Bitewing - single film"},
    "D0272": {"points": 2, "desc": "Bitewing - 2 films"},
    "D0273": {"points": 3, "desc": "Bitewing, 3 films"},
    "D0274": {"points": 4, "desc": "Bitewing - 4 films"},
    "D0277": {"points": 4, "desc": "Vertical bitewing - 7-8 films"},
    "D0330": {"points": 2, "desc": "Panoramic film"},
    "D0460": {"points": 0, "desc": "Pulp vitality tests (NC)"},
    "D0460.1": {"points": 0, "desc": "Pulp Vitality Tests (DWP)"},
    "D0470": {"points": 2, "desc": "Diagnostic casts"},
    "D0470.3": {"points": 2, "desc": "Diagnostic Cast - from digital impression"},
    "D0999": {"points": 0, "desc": "Unspecified diagnostic procedure, by report-enter fee or NC"},
    "D0999.5": {"points": 0, "desc": "Facebow Transfer & Interocclusal Records"},
    "D1110": {"points": 6, "desc": "Prophy - adult"},
    "D1110.2": {"points": 6, "desc": "Prophylaxis - Pediatric (13 And Older)"},
    "D1120": {"points": 3, "desc": "Prophylaxis - Child (12 yrs and under)"},
    "D1206": {"points": 1, "desc": "Fluoride varnish"},
    "D1330": {"points": 1, "desc": "Oral Hygiene Instruction (Complex)"},
    "D1330.1": {"points": 1, "desc": "Oral Hygiene Instruction/Simple (NC)"},
    "D1351": {"points": 2, "desc": "Sealant per tooth"},
    "D1354": {"points": 2, "desc": "Caries arresting med (Silver Diamine Fluoride) Per Tooth"},
    "D2140": {"points": 6, "desc": "Amalgam 1 surface"},
    "D2140.2": {"points": 8, "desc": "Crown Margin Repair, One Surface Amalgam"},
    "D2150": {"points": 8, "desc": "Amalgam - 2 surfaces"},
    "D2150.2": {"points": 12, "desc": "Crown Margin Repair, Two surface Amalgam"},
    "D2160": {"points": 12, "desc": "Amalgam 3 surfaces"},
    "D2161": {"points": 15, "desc": "Amalgam 4 or more surfaces"},
    "D2330": {"points": 6, "desc": "Resin-based comp-1 surf, ant."},
    "D2330.1": {"points": 5, "desc": "Glass lonomer Restoration-1 Surface/Ant"},
    "D2330.2": {"points": 7, "desc": "Crown Margin Repair, One Surf Anter Comp"},
    "D2330.3": {"points": 7, "desc": "Crown Margin Repair - Implant restoration"},
    "D2331": {"points": 8, "desc": "Resin-based comp-2 surf, ant."},
    "D2331.1": {"points": 7, "desc": "Glass lonomer Restoration-2 Surfaces/Ant"},
    "D2331.2": {"points": 9, "desc": "Crown Margin Repair, Two Surf Anter Comp"},
    "D2332": {"points": 10, "desc": "Resin-based comp-3 surf, ant."},
    "D2332.1": {"points": 9, "desc": "Glass lonomer Restoration-3 Surfaces/Ant"},
    "D2335": {"points": 12, "desc": "Resin-based comp-4+surf, ant."},
    "D2335.1": {"points": 10, "desc": "Glass lonomer Restoration - four or more surfaces, anterior"},
    "D2391": {"points": 6, "desc": "Resin-based comp-1 surf, post."},
    "D2391.1": {"points": 5, "desc": "Glass lonomer 1 Surface Posterior"},
    "D2391.2": {"points": 7, "desc": "Crown Margin Repair One Surf Poster Comp"},
    "D2392": {"points": 12, "desc": "Resin-based comp-2 surf, post."},
    "D2392.1": {"points": 11, "desc": "Glass lonomer 2 Surface Posterior"},
    "D2392.2": {"points": 9, "desc": "Crown Margin Repair Two Surf Poster Comp"},
    "D2393": {"points": 15, "desc": "Resin-based comp-3 surf, post."},
    "D2393.1": {"points": 14, "desc": "Glass lonomer 3 Surface Posterior"},
    "D2394": {"points": 18, "desc": "Resin-based comp-4+surf, post."},
    "D2394.1": {"points": 15, "desc": "Glass lonomer 4 or more Surface Posterior"},
    "D2394.2": {"points": 18, "desc": "Resin-Based Composite 5 Surface Posterio"},
    "D2510": {"points": 30, "desc": "Inlay - metallic - 1 surface"},
    "D2520": {"points": 35, "desc": "Inlay - metallic - 2 surfaces"},
    "D2530": {"points": 40, "desc": "Inlay - metallic - 3 or more"},
    "D2543": {"points": 40, "desc": "Onlay metallic - 3 surfaces"},
    "D2544": {"points": 40, "desc": "Onlay - metallic - 4 or more"},
    "D2610": {"points": 30, "desc": "Inlay - porc/cer - 1 surface"},
    "D2620": {"points": 35, "desc": "Inlay - porc/cer - 2 surfaces"},
    "D2630": {"points": 40, "desc": "Inlay - porc/cer - 3 or more"},
    "D2642": {"points": 40, "desc": "Onlay - porc/cer - 2 surfaces"},
    "D2643": {"points": 40, "desc": "Onlay - porc/cer - 3 surfaces"},
    "D2644": {"points": 40, "desc": "Onlay - porc/cer - 4 or more"},
    "D2650": {"points": 30, "desc": "Inlay resin 1 surface"},
    "D2651": {"points": 35, "desc": "Inlay - resin - 2 surfaces"},
    "D2652": {"points": 40, "desc": "Inlay - resin - 3 or more"},
    "D2662": {"points": 40, "desc": "Onlay resin - 2 surfaces"},
    "D2663": {"points": 40, "desc": "Onlay - resin - 3 surfaces"},
    "D2664": {"points": 40, "desc": "Onlay - resin - 4 or more"},
    "D2740": {"points": 40, "desc": "Crown - porcelain/ceramic subs"},
    "D2750": {"points": 40, "desc": "Crown - PFM high noble metal"},
    "D2750.1": {"points": 40, "desc": "Crown - PFM high noble metal (Survey Crown)"},
    "D2751": {"points": 40, "desc": "Crown - PFM predom. base metal"},
    "D2751.1": {"points": 40, "desc": "Crown - PFM predom. base metal (Survey Crown)"},
    "D2752": {"points": 40, "desc": "Crown - PFM noble metal"},
    "D2752.1": {"points": 40, "desc": "Crown - PFM noble metal (Survey Crown)"},
    "D2780": {"points": 45, "desc": "Crown - 3/4 cast high noble mt"},
    "D2781": {"points": 45, "desc": "Crown - 3/4 cast predominantly base metal (DWP)"},
    "D2782": {"points": 45, "desc": "Crown 3/4 cast noble metal"},
    "D2790": {"points": 40, "desc": "Crown - full cast high noble metal"},
    "D2790.1": {"points": 40, "desc": "Crown - full cast high noble metal (Survey Crown)"},
    "D2791": {"points": 40, "desc": "Crown -Full cast pred base mtl"},
    "D2791.1": {"points": 40, "desc": "Crown- full cast pred base mtl (Survey Crown)"},
    "D2792": {"points": 40, "desc": "Crown -Full cast noble metal"},
    "D2792.1": {"points": 40, "desc": "Crown - full cast noble metal (Survey Crown)"},
    "D2799": {"points": 12, "desc": "Provisional crown - further treatment or completion of diag"},
    "D2910": {"points": 6, "desc": "Recement Inlay"},
    "D2915": {"points": 6, "desc": "Recement post and core"},
    "D2920": {"points": 6, "desc": "Recement crown"},
    "D2931": {"points": 12, "desc": "Prefab SS crown - perm. tooth"},
    "D2940": {"points": 6, "desc": "placement of interim direct restoration"},
    "D2940.1": {"points": 6, "desc": "STEPWISE Caries Remain Needs Re-eval"},
    "D2940.2": {"points": 6, "desc": "Sedative Filling Caries Removed, Need Final Rest"},
    "D2949": {"points": 15, "desc": "Restorative foundation for an indirect restoration"},
    "D2950": {"points": 15, "desc": "Core buildup, including any pins when required"},
    "D2951": {"points": 1, "desc": "Pin retention - per tooth"},
    "D2952": {"points": 30, "desc": "Cast post and core, w/ crown"},
    "D2954": {"points": 20, "desc": "Prefab post and core, w/ crown"},
    "D2960": {"points": 14, "desc": "Labial veneer, resin - Direct"},
    "D2961": {"points": 40, "desc": "Labial veneer, resin - Indirect"},
    "D2962": {"points": 40, "desc": "Labial veneer, porcelain - Indirect"},
    "D2999": {"points": 0, "desc": "Unspecified restorative proc."},
    "D3110": {"points": 2, "desc": "Pulp cap - direct"},
    "D3120": {"points": 2, "desc": "Pulp cap - indirect"},
    "D3120.1": {"points": 0, "desc": "Indirect Pulp Cap (Pedo) NC"},
    "D3220": {"points": 6, "desc": "Theraputic Pulpotomy-Primary or Permanent tooth"},
    "D3221": {"points": 6, "desc": "Pulpal debridement, prim/perm"},
    "D3310": {"points": 25, "desc": "Endo therapy - anterior"},
    "D3320": {"points": 30, "desc": "Endo therapy - bicuspid"},
    "D3330": {"points": 45, "desc": "Endo therapy - molar"},
    "D3330.1": {"points": 45, "desc": "Endo therapy - molar 4 Canals"},
    "D3332": {"points": 6, "desc": "Incomplete endo therapy, inoperable, unrestorable or fractured"},
    "D3346": {"points": 25, "desc": "Retreatment - Anterior"},
    "D3347": {"points": 30, "desc": "Retreatment - Bicuspid"},
    "D3348": {"points": 45, "desc": "Retreatment - Molar"},
    "D4210": {"points": 30, "desc": "Gingivectomy or gingivoplasty - 4 or more teeth per quadrant"},
    "D4211": {"points": 6, "desc": "Gingivectomy or gingivoplasty - 1-3 teeth per quadrant"},
    "D4212": {"points": 3, "desc": "Gingivectomy/gingivoplasty to allow access for restorative"},
    "D4240": {"points": 30, "desc": "Gingival flap, inc root planing - 4 or more teeth per quad"},
    "D4241": {"points": 30, "desc": "Gingival flap, including root planing 1-3 teeth per quaq"},
    "D4245": {"points": 30, "desc": "Apically positioned flap"},
    "D4249": {"points": 30, "desc": "Clinical crown lengthening - hard tissue"},
    "D4260": {"points": 30, "desc": "Osseous surgery, including flap - 4 or more teeth per quad"},
    "D4261": {"points": 30, "desc": "Osseous surgery, including flap - 1-3 teeth per quadrant"},
    "D4274": {"points": 30, "desc": "Distal or proximal wedge"},
    "D4341": {"points": 0, "desc": "Periodontal scaling & root planing 4 or more teeth per quad"},
    "D4342": {"points": 0, "desc": "Periodontal scaling and root planing 1-3 teeth per quad"},
    "D4346": {"points": 6, "desc": "Scaling in presence of gingival inflammation - full mouth"},
    "D4355": {"points": 6, "desc": "Full mouth debridement to enable comp eval and diagnosis"},
    "D4910": {"points": 9, "desc": "Periodontal maintenance"},
    "D4999": {"points": 0, "desc": "Unspecified periodontal procedure, by report-Enter fee or NC"},
    "D4999.1": {"points": 0, "desc": "Laser Disposable Tip"},
    "D5110": {"points": 75, "desc": "Complete denture - maxillary"},
    "D5120": {"points": 75, "desc": "Complete denture - mandibular"},
    "D5130": {"points": 80, "desc": "Immediate denture - maxillary"},
    "D5211": {"points": 15, "desc": "Upper Partial - Acrylic Base (use only as final prosthesis)"},
    "D5212": {"points": 15, "desc": "Lower Partial - Acrylic Base (use only as final prosthesis)"},
    "D5213": {"points": 80, "desc": "Max partial cast metal frame"},
    "D5214": {"points": 80, "desc": "Mand partial-cast metal frame"},
    "D5410": {"points": 6, "desc": "Adjust complete denture - Max"},
    "D5410.1": {"points": 20, "desc": "Remount And Adjust Occlusion"},
    "D5411": {"points": 6, "desc": "Adjust complete denture - Mand"},
    "D5421": {"points": 6, "desc": "Adjust partial denture - Max"},
    "D5422": {"points": 6, "desc": "Adjust partial denture - Mand"},
    "D5520": {"points": 5, "desc": "Replace teeth - per tooth"},
    "D5520.1": {"points": 5, "desc": "Replace Additional Teeth - Each Tooth"},
    "D5630": {"points": 5, "desc": "Repair or replace broken clasp"},
    "D5640": {"points": 5, "desc": "Replace teeth - per tooth"},
    "D5640.1": {"points": 5, "desc": "Replace Additional Teeth/Per Tooth"},
    "D5650": {"points": 5, "desc": "Add tooth to existing partial"},
    "D5660": {"points": 5, "desc": "Add clasp to existing partial"},
    "D5710": {"points": 40, "desc": "Rebase complete maxillary denture"},
    "D5711": {"points": 40, "desc": "Rebase complete mandibular denture"},
    "D5720": {"points": 20, "desc": "Rebase max. partial denture"},
    "D5721": {"points": 20, "desc": "Rebase mand. partial denture"},
    "D5730": {"points": 20, "desc": "Reline comp max - Direct"},
    "D5731": {"points": 20, "desc": "Reline comp mand - Direct"},
    "D5740": {"points": 20, "desc": "Reline max part - Direct"},
    "D5741": {"points": 20, "desc": "Reline mand part - Direct"},
    "D5750": {"points": 30, "desc": "Reline comp max - Indirect"},
    "D5750.1": {"points": 30, "desc": "Soft Liner Upper Denture Reline (Processed)"},
    "D5751": {"points": 30, "desc": "Reline comp mand - Indirect"},
    "D5751.1": {"points": 30, "desc": "Soft Liner Lower Denture Reline (Processed)"},
    "D5760": {"points": 30, "desc": "Reline max part - Indirect"},
    "D5761": {"points": 30, "desc": "Reline mand part - Indirect"},
    "D5820": {"points": 15, "desc": "Interim partial denture Maxillary"},
    "D5820.1": {"points": 15, "desc": "Essex interim appliance - maxillary"},
    "D5821": {"points": 15, "desc": "Interim partial denture Mandibular"},
    "D5821.1": {"points": 15, "desc": "Essex interim appliance mandibular"},
    "D5850": {"points": 3, "desc": "Tissue conditioning - Max."},
    "D5851": {"points": 6, "desc": "Tissue conditioning - Mand."},
    "D5863": {"points": 65, "desc": "Overdenture - complete maxillary"},
    "D5864": {"points": 80, "desc": "Overdenture - partial maxillary"},
    "D5865": {"points": 65, "desc": "Overdenture - complete mandibular"},
    "D5866": {"points": 80, "desc": "Overdenture - partial mandibular"},
    "D5875": {"points": 12, "desc": "Mod of rem prosth after implnt"},
    "D5899": {"points": 0, "desc": "Unspecified removable prosth proc - Enter fee or NC"},
    "D5986": {"points": 5, "desc": "Fluoride gel carrier"},
    "D5999.1": {"points": 0, "desc": "Surg Guide/Prosthetic Appliance/Imm Dent"},
    "D6010.3": {"points": 0, "desc": "Surgical placement of implant body endosteal implant PREDOC"},
    "D6056": {"points": 2, "desc": "Prefabricated abutment - includes placement"},
    "D6056.1": {"points": 4, "desc": "Prefab Implant Abutment-Overdenture bar-per implant"},
    "D6056.2": {"points": 2, "desc": "Prefabricated Abutment - includes placement (Fee Class)"},
    "D6057": {"points": 2, "desc": "Abutment Custom"},
    "D6058": {"points": 40, "desc": "Crown - Abutment supported porc/ceramic"},
    "D6059": {"points": 40, "desc": "Crown - Abutment supported PFM (high noble metal)"},
    "D6060": {"points": 40, "desc": "Crown - Abutment supported, PFM, based metal"},
    "D6061": {"points": 40, "desc": "Crown - abutment supported - PFM, noble metal"},
    "D6062": {"points": 40, "desc": "Crown - Abutment-cast metal, high noble"},
    "D6063": {"points": 40, "desc": "Crown - Abutment-cast metal, based metl"},
    "D6064": {"points": 40, "desc": "Crown - Abutment supported cast metal, noble metl"},
    "D6065": {"points": 40, "desc": "Crown - Implant supported - porc/ceramic"},
    "D6066": {"points": 40, "desc": "Crown - Implant supported - PFM, high noble metal"},
    "D6067": {"points": 40, "desc": "Crown - Implant supported -metal, high noble"},
    "D6190": {"points": 12, "desc": "Surgical Guide"},
    "D6190.2": {"points": 12, "desc": "Surg implant guide (Fee Class)"},
    "D6190.4": {"points": 12, "desc": "3D printed Surgical Implant Guide"},
    "D6205.2": {"points": 25, "desc": "Pontic - Indirect - Maryland Bridge - Resin Based composite"},
    "D6210": {"points": 25, "desc": "Pontic - cast high noble metal"},
    "D6210.2": {"points": 25, "desc": "Pontic - Maryland Bridge Cast High Nobel Metal"},
    "D6212": {"points": 25, "desc": "Pontic cast noble metal"},
    "D6212.2": {"points": 25, "desc": "Pontic - Maryland Bridge - cast noble metal"},
    "D6240": {"points": 25, "desc": "Pontic - Porcelain fused to high noble metal"},
    "D6240.2": {"points": 25, "desc": "Pontic - Maryland Bridge - Proc. Fused to high nobel metal"},
    "D6241": {"points": 25, "desc": "Pontic - Porc fused to base metal (Acid Etch Bridge)"},
    "D6242": {"points": 25, "desc": "Pontic-porc fuse to noble metl"},
    "D6245": {"points": 25, "desc": "Pontic-porcelain/ceramic"},
    "D6245.2": {"points": 25, "desc": "Pontic-Maryland Bridge - porcelain/ceramic"},
    "D6253": {"points": 0, "desc": "Interim pontic - further treatment or completion of diag"},
    "D6545": {"points": 25, "desc": "Maryland Bridge - Metal Wing (Acid Etch Bridge)"},
    "D6548": {"points": 25, "desc": "Maryland Bridge - Ceramic/Porcelain Wing (Acid Etch Bridge)"},
    "D6549": {"points": 25, "desc": "Maryland Bridge - Resin Wing (Acid Etch Bridge)"},
    "D6610": {"points": 40, "desc": "Onlay high noble mtl, 2 surf"},
    "D6611": {"points": 40, "desc": "Onlay - high noble mtl, 3+ sur"},
    "D6614": {"points": 40, "desc": "Onlay - cast noble mtl, 2 surf"},
    "D6615": {"points": 40, "desc": "Onlay - cast noble mtl, 3+ sur"},
    "D6710": {"points": 40, "desc": "Retainer crown - indirect resin based composite"},
    "D6720": {"points": 40, "desc": "Retainer crown - resin with high noble metal"},
    "D6722": {"points": 40, "desc": "Retainer crown - resin with noble metal"},
    "D6740": {"points": 40, "desc": "Retainer crown - porcelain/ceramic"},
    "D6750": {"points": 40, "desc": "Retainer crown - porcelain fused to high noble metal"},
    "D6752": {"points": 40, "desc": "Retainer crown - porcelain fused - noble metal"},
    "D6780": {"points": 40, "desc": "Retainer crown - 3/4 cast high noble metal"},
    "D6782": {"points": 40, "desc": "Retainer Crown - 3/4 cast noble metal"},
    "D6790": {"points": 40, "desc": "Retainer crown -full cast high noble mtl"},
    "D6792": {"points": 40, "desc": "Retainer Crown - full cast noble metal"},
    "D6793": {"points": 0, "desc": "Interim retainer crown - further treatment or completion"},
    "D6794": {"points": 0, "desc": "Retainer crown - titanium"},
    "D6930": {"points": 6, "desc": "Recement FPD"},
    "D6980": {"points": 6, "desc": "FPD repair"},
    "D6999": {"points": 0, "desc": "Unspecified fixed prosthodontic procedure, Enter fee or NC"},
    "D6999.2": {"points": 0, "desc": "Characterizing/Staining/Porcelain Restn"},
    "D7111": {"points": 0, "desc": "Extraction, coronal remnants - deciduous tooth"},
    "D7140": {"points": 0, "desc": "Extraction, eruptd tth/ exp rt"},
    "D7140.1": {"points": 0, "desc": "Extraction, Erupted Tooth-Primary Tooth"},
    "D7210": {"points": 0, "desc": "Surg extraction of erupted tooth"},
    "D7250": {"points": 0, "desc": "Extraction of residual tth roots"},
    "D7285": {"points": 0, "desc": "Biopsy of oral tissue - hard"},
    "D7286": {"points": 6, "desc": "Biopsy of oral tissue - soft"},
    "D7286.1": {"points": 6, "desc": "Biopsy Soft Tissue - Incisional"},
    "D7310": {"points": 0, "desc": "Alveoloplasty with extractions"},
    "D7311": {"points": 0, "desc": "Alveoloplasty inc ext: 1-3 tth"},
    "D7320": {"points": 0, "desc": "Alveoloplasty w/o extractions"},
    "D7320.1": {"points": 0, "desc": "Mylohyoid Rdg/Endoalveolar Crest Reductn"},
    "D7321": {"points": 0, "desc": "Alveoloplasty no ext: 1-3 tth"},
    "D7410": {"points": 0, "desc": "Excision, benign lesion<1.25cm"},
    "D7411": {"points": 0, "desc": "Excision, benign lesion>1.25cm"},
    "D7471.2": {"points": 0, "desc": "Removal of lateral exostosis - Mandible"},
    "D7473": {"points": 0, "desc": "Removal of torus mandibularis"},
    "D7473.1": {"points": 0, "desc": "Removal of torus mandibularis (HDI only)"},
    "D7485": {"points": 0, "desc": "Surg reduct of osseous tuberos"},
    "D7510": {"points": 0, "desc": "Incision/drainage, abscess-intr"},
    "D7880": {"points": 25, "desc": "Occlusal orthotic device"},
    "D7880.1": {"points": 25, "desc": "Therapeutic Occlusal Appliance"},
    "D7880.2": {"points": 25, "desc": "Diagnostic Occlusal Splint Or Bite Plane"},
    "D7970": {"points": 0, "desc": "Excision - hyperplastic tiss"},
    "D7972": {"points": 0, "desc": "Surg reduct, fibrs. tuberosity"},
    "D9110": {"points": 4, "desc": "Palliative Tx of dental pain per visit"},
    "D9110.3": {"points": 0, "desc": "Necrotizng Ulcerative Gingivitus/Specify"},
    "D9110.4": {"points": 0, "desc": "Emergency Tx/Acute Ulcerative Lesions"},
    "D9120": {"points": 3, "desc": "Fixed partial denture sectioning"},
    "D9310": {"points": 0, "desc": "Consultation"},
    "D9310.1": {"points": 0, "desc": "Bleaching Consultation, Initial Visit (NC)"},
    "D9310.5": {"points": 6, "desc": "Implant Screening - Predoc (NC)"},
    "D9430": {"points": 0, "desc": "Office visit -observation only"},
    "D9430.1": {"points": 0, "desc": "Endo Recall-Office Visit For Observation (NC)"},
    "D9430.2": {"points": 0, "desc": "Observation/Re-Evaluation Visit (NC)"},
    "D9630": {"points": 0, "desc": "Other drugs and/or medicaments, by report (Enter fee)"},
    "D9630.4": {"points": 0, "desc": "Oral Antibiotic - Amoxicillin"},
    "D9630.5": {"points": 0, "desc": "Oral Antibiotic - Clindamycin"},
    "D9630.6": {"points": 0, "desc": "Oral Antibiotic - Azithromycin"},
    "D9910": {"points": 2, "desc": "Application of desensitizing medicament"},
    "D9911": {"points": 0, "desc": "Appl of desensitizing resin - cervical/root surface/per tth"},
    "D9941": {"points": 6, "desc": "Fabrication of athl mouthguard"},
    "D9942": {"points": 0, "desc": "Repair/reline occlusal guard"},
    "D9944": {"points": 30, "desc": "Occlusal guard - hard appliance, full arch (bruxism)"},
    "D9945": {"points": 15, "desc": "Occlusal guard - soft appliance, full arch (bruxism)"},
    "D9950": {"points": 15, "desc": "Occlusion analysis-mountd case"},
    "D9951": {"points": 3, "desc": "Occlusal adjustment - limited"},
    "D9952": {"points": 15, "desc": "Occlusal adjustment - complete"},
    "D9952.1": {"points": 15, "desc": "Occlusal Equilibration (Add Fee)"},
    "D9970": {"points": 1, "desc": "Enamel microabrasion"},
    "D9971": {"points": 0, "desc": "Odontoplasty per tooth"},
    "D9973": {"points": 0, "desc": "External bleaching - per tooth"},
    "D9974": {"points": 6, "desc": "Internal bleaching - per tooth"},
    "D9975": {"points": 9, "desc": "External bleaching - external bleaching system per arch"},
    "D9975.1": {"points": 0, "desc": "Additional Bleaching tubes"},
    "I0150": {"points": 9, "desc": "Comprehensive Oral Re-Evaluation-Cont Tx"},
    "I0170": {"points": 0, "desc": "Departmental Screening Or Examination"},
    "I0210": {"points": 12, "desc": "Smile Analysis"},
    "I0220": {"points": 2, "desc": "Occlusal Analysis"},
    "I0520": {"points": 6, "desc": "Treatment Plan"},
    "I2190": {"points": 0, "desc": "Restoration Polish - Per Quad/Arch"},
    "I7999": {"points": 0, "desc": "Post Operative Procedure"},
    "I9800": {"points": 6, "desc": "Exit Examination"},
    "I9990": {"points": 0, "desc": "Duplication of Radiographs"},
    "I9996": {"points": 1, "desc": "Intraoral camera use FAMD"},
    "I9996.2": {"points": 4, "desc": "SLR photographs for case presentation FAMD"},
    "I9996.3": {"points": 1, "desc": "Patient education (iPad use) FAMD"},
    "I9997": {"points": 0, "desc": "Record Duplication"},
    "T1013": {"points": 0, "desc": "Interpretation Service Sign Language"}
}

# Initialize session state variables
if 'running_total' not in st.session_state:
    st.session_state.running_total = 0
if 'history' not in st.session_state:
    st.session_state.history = []
if 'entry_counter' not in st.session_state:
    st.session_state.entry_counter = 0

# Define a function to handle deleting an entry
def delete_entry(item_id):
    # Filter out the item that matches the unique ID
    st.session_state.history = [item for item in st.session_state.history if item[0] != item_id]
    # Recalculate the running total from the remaining items
    st.session_state.running_total = sum(item[4] for item in st.session_state.history)

st.title("Code Point Tracker")

# Create a form so the user can press Enter to submit
with st.form(key='code_entry_form', clear_on_submit=True):
    user_code = st.text_input("Enter a code:")
    submit_button = st.form_submit_button("Submit")

# Process the code when submitted
if submit_button and user_code:
    parts = user_code.strip().upper().split()
    
    if len(parts) > 2:
        st.error("Format not recognized. Please use 'CODE' or 'CODE QUANTITY'.")
    else:
        clean_code = parts[0]
        qty_is_valid = True
        qty = 1
        
        if len(parts) == 2:
            try:
                qty = int(parts[1])
            except ValueError:
                st.error("Please enter a valid number for the quantity (e.g., 'D0140 3').")
                qty_is_valid = False
        
        if qty_is_valid:
            if clean_code in master_codes:
                base_points = master_codes[clean_code]["points"]
                description = master_codes[clean_code]["desc"]
                total_points = base_points * qty
                
                # Update total and counter
                st.session_state.running_total += total_points
                st.session_state.entry_counter += 1
                
                # Add to history with a unique ID at the beginning of the tuple
                st.session_state.history.append((
                    st.session_state.entry_counter, 
                    clean_code, 
                    qty, 
                    description, 
                    total_points
                ))
                
                if qty > 1:
                    st.success(f"Success! Added {qty}x {clean_code} - {description} ({total_points} total points).")
                else:
                    st.success(f"Success! {clean_code} - {description} is worth {total_points} points.")
            else:
                st.error(f"Code '{clean_code}' not found in the master list.")

# Display the running total prominently
st.metric(label="Total Points", value=st.session_state.running_total)

# Display the log of what has been entered
if st.session_state.history:
    st.write("---")
    st.subheader("Entry History")
    
    # Iterate through the history in reverse order
    for item_id, code, q, desc, pts in reversed(st.session_state.history):
        # Create two columns: a wide one for text, a narrow one for the button
        col1, col2 = st.columns([9, 1])
        
        with col1:
            if q > 1:
                st.write(f"- **{code}** (x{q}): {desc} ({pts} points)")
            else:
                st.write(f"- **{code}**: {desc} ({pts} points)")
                
        with col2:
            # When clicked, this button triggers the delete_entry function
            st.button("❌", key=f"del_{item_id}", on_click=delete_entry, args=(item_id,))
