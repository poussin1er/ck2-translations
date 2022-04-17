init python:
    achievements = []


    class Achievement:
        """
        Achievement data class for storing and managing the creation, syncing and managing of in-game achievements

        Args:
            _achievement (str): Programic name for the achievement, should be same as steam api name
            text (str): Short description of achievement
        """

        def __init__(self, _achievement, text):
            self.achievement = _achievement
            self.text = text

            self.display_name = _achievement.replace("_", " ")

            achievements.append(self)

            # Add achievements to renpy/steam
            achievement.register(_achievement)
            achievement.sync()

        def checkCondition(self):
            return getattr(store, self.condition)


    def grant_achievement(_achievement):
        if path_builder or _in_replay:
            return

        renpy.show(_achievement, [achievementShow])
        achievement.grant(_achievement)
        achievement.sync()


# ACHIEVEMENT ITEMS HERE
    #v1
    # Achievement("troisieme_joueur_pret", "Trio avec Riley et Aubrey") -- CK1 achievement
    # Achievement("sauver_le_soldat_ryan", "Ne laisse pas Ryan attraper une MST") -- CK1 achievement
    Achievement("beastie_boy", "Sabote la vente de pâtisseries")
    Achievement("agent_double", "Aide les campagnes de Chloé et de Lindsey")
    Achievement("accepte_de_ne_pas_etre_d'accord", "Chris n'aide pas Chloé")
    Achievement("comment_t'as_su", "Achète à Amber ses bonbons préférés")
    Achievement("confiance_fondee", "Fais confiance à ta petite amie Chloé avec son ex")
    Achievement("colere_de_pen", "Pénélope fait un scandale au restaurant")
    Achievement("tes_paupieres_sont_lourdes", "Lauren utilise ses pouvoirs d'hypnose pour faire le bien")
    Achievement("dis_cuicui", "Prends une photo avec l'oiseau")
    Achievement("grand_theft_chloe", "Vole le journal intime et tout l'argent")
    Achievement("nettoie-les", "Avoir une influence positive sur Amber et Samantha")

    #v2
    Achievement("en_rut", "Mate Autumn") #s4
    Achievement("da_ba_dee_da_ba_dai", "I'm Blue") #s4
    Achievement("contre-espionnage", "Lindsey s'attendait à cette stratégie") #s12
    Achievement("huumm_un_donut", "Mange le donut") #s13
    Achievement("ours_a_miel", "Lèche les pancakes de Mme Rose") #s15
    Achievement("saison_des_citrouilles", "Tu aimes vraiment cette citrouille, hein ?") #s18
    Achievement("souvenirs_d'enfance", "Surprends la fille qui fête son anniversaire") #s18
    Achievement("maitre_d'oeuvre", "termine la checklist") #s18
    Achievement("trop_d'informations", "Vérifie souvent tes notes de réunion") #s21
    Achievement("chantage_emotionnel", "Menace Mme Rose") #s21
    Achievement("karen", "Où est votre responsable ?!") #s24
    Achievement("polycurieux", "La monogamie est surfaite") #s26
    Achievement("fromage_bleu_et_sambuca", "Le pire traiteur de mariage de tous les temps") #s33
    Achievement("qu'est-ce_qui_se_passe", "Aubrey goûte à sa propre médecine au mariage") #s33
    Achievement("encore_une_chose", "Découvre toutes les pistes et résous l'affaire") #s46

    #v3
    Achievement("la_reponse_a_tout", "La bonne réponse était Milton Friedman") #s10
    Achievement("edition_speciale", "Postule pour l'équipe de journalistes") #s11
    Achievement("doit_resister_a_la_tentation", "Reste concentré au parc") #s14
    Achievement("simplement_curieux_a_ton_sujet", "Dis à Amber que tu as regardé dans ses affaires") #s22
    Achievement("Planning_charge", "Jongle avec un planning chargé") #27
    Achievement("rencard_parfait", "Incroyable premier rencard officiel avec Aubrey  ") #s40
    Achievement("Une_foule_de_trois", "Petite amie numéro trois") #s41
    Achievement("defenestre", "Je ne sais même pas ce que ce mot signifie") #s48
    Achievement("Pris_en_flagrant_délit", "Ne pas faire de dons te retombe dessus") #s55
    Achievement("eloge_en_chanson", "Obtiens l'approbation de Polly") #s59
    Achievement("journée_de_mauvais_poil", "Les photos du DMV sont terribles") #s65
