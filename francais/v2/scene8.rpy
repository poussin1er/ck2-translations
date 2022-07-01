# TODO: Translation updated at 2022-03-17 15:15

# game/v2/scene8.rpy:22
translate francais v2s8_ce82b4c9:

    # cl "So, for phase two, we're stepping things up."
    cl "Donc, pour la phase deux, on va intensifier les choses."

# game/v2/scene8.rpy:27
translate francais v2s8_c222cd55:

    # u "Sounds good. I'm up for anything... Besides murder."
    u "C'est bien. Je suis prêt à tout... À part le meurtre."

# game/v2/scene8.rpy:32
translate francais v2s8_71fee5cb:

    # cl "Haha! Okay, no murder... Got it."
    cl "Haha ! Bon, pas de meurtre... C'est noté."

# game/v2/scene8.rpy:34
translate francais v2s8_522e50de:

    # cl "Except for political murder. *Laughs* We're winning no matter what it takes."
    cl "Sauf pour ce qui est des meurtres politiques. *Rire* On va gagner quoi qu'il en coûte."

# game/v2/scene8.rpy:39
translate francais v2s8_574851b5:

    # u "Yes, ma'am."
    u "Oui, m'dame."

# game/v2/scene8.rpy:45
translate francais v2s8_1c61f5c9:

    # cl "Eww, no... I like it when you're in charge... *Chuckles*"
    cl "Euh, non... J'aime bien quand c'est toi qui commande... *Rire*"

# game/v2/scene8.rpy:50
translate francais v2s8_fcc18885:

    # u "*Laughs*"
    u "*Rire*"

# game/v2/scene8.rpy:55
translate francais v2s8_971d2a58:

    # cl "Sir..."
    cl "Mon Seigneur..."

# game/v2/scene8.rpy:60
translate francais v2s8_18de58f1:

    # u "(Oh...) Ahem, right then. Show me."
    u "(Oh...) Hum, d'accord. Montre-moi."

# game/v2/scene8.rpy:65
translate francais v2s8_2fb5af53:

    # cl "Our options are very different, but either one can be the perfect plan as long as we do it right."
    cl "Les options qu'on propose sont très différentes, mais l'une ou l'autre peut être le plan parfait, à partir du moment où on le fait correctement."

# game/v2/scene8.rpy:67
translate francais v2s8_e63b039e:

    # cl "It all depends on how we want to go about this..."
    cl "Tout dépend de la façon dont on veut s'y prendre..."

    scene v2s8_4 # TPP. Show MC upclose analyzing the planning board, MC in a generic standing thinking pose while he looks at the board, Chloe in the background, both slight smile, mouth closed.
    with dissolve

    pause 0.75

# -Insert Planning Board with the options for phase 2-
# -The planning board pops up and MC makes his choices from what's presented, close when finished-
    python:
        chloe_board = PlanningBoard("images/v2/planning_boards/chloe_background.webp", money=chloe_board.money)

        chloe_board.add_approach("Sabotage",
            "Nuire à la réputation de Lindsey",
            opinion="\"Cette idée n'est pas pour les âmes sensibles, mais je dois jouer le jeu si je veux gagner... Nous saboterons sa campagne avec un soupçon de honte, pas si infime que ça.\"")

        chloe_board.add_approach("Tuition",
            "Réduction des frais de scolarité pour toutes les Chicks",
            opinion="\"La seule chose à laquelle j'ai toujours rêvé pouvoir faire en tant que Présidente des Chicks, est d'obtenir la gratuité des frais de scolarité pour toutes les membres. Si on présente un assez bon dossier, je pourrai peut-être convaincre la doyenne de faire en sorte que ça se réalise.\"")

        chloe_board.add_task("Sabotage",
            "Enregistrer Lindsey en secret",
            opinion="\"Une fois qu'on aura récupéré quelques bouteilles d'alcool, Imre et toi ferez de votre mieux pour que Lindsey se saoule. Je ne sais pas trop dans quel état d'esprit elle sera, mais tu pourrais peut-être lui dire qu'elle a besoin de se détendre un peu. Après tout, elle est probablement stressée par le fait de ne rien avoir et que moi si...\"")

        chloe_board.add_task("Sabotage",
            "Provoquer Lindsey pour qu'elle dise quelque chose qui pourrait nuire à sa réputation",
            opinion="\"Nous avons besoin qu'elle dise quelque chose de mal. Quelque chose de détestable, et encore mieux si c'est à mon sujet. Si elle est ivre, tu n'auras aucun problème à obtenir quelque chose d'elle, mais là encore, je ne suis pas sûre de son état d'esprit. Assure-toi simplement qu'elle est détendue et sous contrôle.\"")

        v2s8_chloe_kiwii = chloe_board.add_subtask("Sabotage",
            "Chloé poste l'enregistrement sur Kiwii",
            opinion="\"L'étape finale de ce projet magnifique consiste à télécharger les preuves sur Kiwii. C'est la clé. Une fois que tout le monde aura entendu les choses horribles qu'elle a dites, ils viendront vers moi en courant.\"")

        chloe_board.add_subtask("Sabotage",
            "Diffuse l'enregistrement par le biais du système de communication de la doyenne",
            opinion="\"La dernière étape est très importante, alors pourquoi ne pas faire les choses en grand ? Je peux nous obtenir l'accès au système de communication de la doyenne, et on pourra diffuser ton enregistrement afin que tout le campus puisse l'entendre.\"")

        v2s8_chloe_lee = chloe_board.add_subtask("Tuition",
            "Essayer de convaincre Mr Lee de me soutenir pour ce projet devant la doyenne.",
            opinion="\"Avant de présenter cette idée folle à la doyenne, on aura besoin du soutien de certains professeurs. Je pense que Mr Lee est notre meilleure chance, il est intelligent et très respecté. Bien qu'il puisse être difficile à cerner.\"",
            people=[mr_lee])

        chloe_board.add_subtask("Tuition",
            "Essayer de convaincre Mme Rose de me soutenir pour ce projet devant la doyenne.",
            opinion="\"Avant de présenter cette idée folle à la doyenne, on aura besoin du soutien de certains des professeurs. Mme Rose pourrait être une bonne candidate. Elle est très empathique, mais je ne sais pas à quel point elle m'apprécie...\"",
            people=[ms_rose])

        chloe_board.add_task("Tuition",
            "Parler à la doyenne avec le soutien de Mr Lee ou de Mme Rose",
            opinion="\"Enfin, on aura une entrevue avec la doyenne. Si on arrive à démontrer qu'un professeur soutient notre idée, on devrait pouvoir obtenir son approbation.\"",
            people=[dean])

    call screen planning_board(chloe_board)

    if chloe_board.approach is not None:
        $ v2_chloe_lindseysabotage = chloe_board.approach.id == "Sabotage"

    if chloe_board.selected_task is not None:
        $ v2_chloe_postkiwii = chloe_board.selected_task == v2s8_chloe_kiwii
        $ v2_chloe_mrleesupport = chloe_board.selected_task == v2s8_chloe_lee

    # End planning board (screen disappears)


# game/v2/scene8.rpy:132
translate francais v2s8_c3ef7d46:

    # u "I think that's the best way to go."
    u "Je pense que c'est la meilleure façon de procéder."

# game/v2/scene8.rpy:138
translate francais v2s8_ddca9c14:

    # u "If you're willing to play dirty and put our feelings aside, this plan can turn tons of people against her and towards you."
    u "Si t'es prête à la jouer sale et à mettre nos sentiments de côté, ce plan peut monter des tonnes de personnes contre elle et vers toi."

# game/v2/scene8.rpy:143
translate francais v2s8_f622df5f:

    # cl "As long as you're in the right place at the right time, this is a solid idea."
    cl "Tant que tu es au bon endroit au bon moment, c'est une excellente idée."

# game/v2/scene8.rpy:145
translate francais v2s8_15f50d7a:

    # cl "And if by any chance there's alcohol present, every girl's inner bitch comes out to play when they're drunk."
    cl "Et si, par le plus grand des hasards, il y a de l'alcool, la salope qui sommeille en chaque fille se réveillera lorsqu'elles seront ivres."

# game/v2/scene8.rpy:150
translate francais v2s8_f4731d13:

    # u "Haha, is that true?"
    u "Haha, c'est vrai ça ?"

# game/v2/scene8.rpy:155
translate francais v2s8_fbdf5feb:

    # cl "For some it slips out quicker than others, but yeah. Eventually."
    cl "Pour certaines filles, ça sort plus vite que d'autres, mais ouais."

# game/v2/scene8.rpy:160
translate francais v2s8_f2068182:

    # u "That's what she said."
    u "C'est ce qu'elle a dit."

# game/v2/scene8.rpy:165
translate francais v2s8_fea3d640:

    # cl "*Sighs*"
    cl "*Soupirs*"

# game/v2/scene8.rpy:176
translate francais v2s8_c1487456:

    # u "If you can lower tuition fees, people are really going to love you. They're going to think you have tons of power, you know?"
    u "Si tu peux faire baisser les frais de scolarité, les gens vont vraiment t'adorer. Ils vont penser que t'as des tonnes de pouvoir, tu vois ?"

# game/v2/scene8.rpy:181
translate francais v2s8_572fd02a:

    # cl "Exactly, but this could also backfire. We need to do some serious planning before meeting with one of them."
    cl "Exactement, mais ça pourrait aussi se retourner contre nous. On doit faire de sérieux préparatifs avant de se présenter à l'un d'entre eux."

# game/v2/scene8.rpy:186
translate francais v2s8_480e791c:

    # u "If we're going to succeed at this, we might need to do some research."
    u "Si on veut réussir, il faut faire des recherches."

# game/v2/scene8.rpy:191
translate francais v2s8_230a7fa3:

    # cl "Yeah, I'm all over it."
    cl "Ouais, je suis à fond dedans."

# game/v2/scene8.rpy:193
translate francais v2s8_ebdf1aba:

    # cl "Okay. Yeah. I'm happy with this!"
    cl "D'accord. Ouais. Je suis contente de ça !"

# game/v2/scene8.rpy:198
translate francais v2s8_112ca513:

    # u "Good, me too."
    u "Bien, moi aussi."

# game/v2/scene8.rpy:203
translate francais v2s8_422b659c:

    # cl "Then that's it for today I suppose. Thanks for helping me again."
    cl "Alors je pense que c'est tout pour aujourd'hui. Merci de m'avoir aidé une fois de plus."

# game/v2/scene8.rpy:208
translate francais v2s8_28ac72a6:

    # u "Happy to be of service. Want me to walk you out?"
    u "Content d'être à ton service. Tu veux que je te raccompagne ?"

# game/v2/scene8.rpy:213
translate francais v2s8_0201e942:

    # cl "No, I uh- I need to make a few phone calls."
    cl "Non, je... je dois passer quelques coups de fil."

# game/v2/scene8.rpy:216
translate francais v2s8_8f5ef68c:

    # cl "And I still have to report the robbery to the Dean, so..."
    cl "Et je dois encore déclarer le vol à la doyenne, alors..."

# game/v2/scene8.rpy:221
translate francais v2s8_1df0d241:

    # u "(Fuck! The Dean? This is going a bit far...)"
    u "(Putain ! La doyenne ? Ça va un peu loin...)"

# game/v2/scene8.rpy:223
translate francais v2s8_a7525505:

    # u "Okay, I'll leave you to it. I'm here for you if you need anything."
    u "Ok. Alors, je vais te laisser. Je reste à ta disposition, si t'as besoin de quelque chose."

# game/v2/scene8.rpy:228
translate francais v2s8_fa2a48f7:

    # cl "I know. *Chuckles* You're the best."
    cl "Je sais. *Rire* T'es le meilleur."

# game/v2/scene8.rpy:234
translate francais v2s8_b226feaa:

    # u "Presidential phone calls?"
    u "Des appels téléphoniques présidentiels ?"

# game/v2/scene8.rpy:239
translate francais v2s8_ed3eeeb2:

    # cl "Of course, haha. I'm a VIP, [name]... A Very Important President, making very important phone calls."
    cl "Bien sûr, haha. Je suis une VIP, [name]... Une Présidente très importante, qui passe des appels téléphoniques très importants."

# game/v2/scene8.rpy:244
translate francais v2s8_8a77cf2b:

    # u "Right... Okay, whatever gets your juices flowing."
    u "Bien... Ok, tout ce qui peut faire jaillir tes idées."

# game/v2/scene8.rpy:250
translate francais v2s8_f373ccef:

    # cl "Usually, you get them flowing..."
    cl "Habituellement, je les attrape au vol..."

# game/v2/scene8.rpy:255
translate francais v2s8_08d8b0b5:

    # u "What was that?"
    u "Comment ça ?"

# game/v2/scene8.rpy:260
translate francais v2s8_a69ff2e1:

    # cl "Nothing! *Chuckles* Bye now."
    cl "Rien ! *Rire* À plus tard."

# game/v2/scene8.rpy:265
translate francais v2s8_eb16a63f:

    # u "Bye, Chloe."
    u "À plus, Chloé."
# TODO: Translation updated at 2022-06-24 10:14

# game/v2/scene8.rpy:32
translate francais v2s8_45fdf147:

    # cl "Too bad. It's gonna be murder."
    cl "C'est bien dommage. Ça va être un véritable assassinat."

# game/v2/scene8.rpy:34
translate francais v2s8_9f8649d2:

    # cl "Kidding."
    cl "Je rigole."

# game/v2/scene8.rpy:36
translate francais v2s8_225ecbe8:

    # cl "Except for murdering Lindsey's campaign. We're winning no matter what it takes."
    cl "Excepté sur le fait d'assassiner la campagne de Lindsey. On gagnera coûte que coûte."

# game/v2/scene8.rpy:47
translate francais v2s8_110e5878:

    # cl "Eww, no... I like it when you're in charge..."
    cl "Euh, non... J'aime bien quand c'est toi qui commande..."

# game/v2/scene8.rpy:52
translate francais v2s8_63f9e71d:

    # u "Mmm, oh yeah? I like being in charged."
    u "Mmm, et pourquoi pas ? J'aime bien avoir des responsabilités."

# game/v2/scene8.rpy:62
translate francais v2s8_4c76d10c:

    # u "*Coughs* Ahem, right then. Show me."
    u "*Tousse* Hum, d'accord. Montre-moi."

# game/v2/scene8.rpy:152
translate francais v2s8_153dc7d4:

    # u "Oh yeah? Is that true?"
    u "Ah oui ? C'est vrai ça ?"

# game/v2/scene8.rpy:157
translate francais v2s8_202327d5:

    # cl "For some it slips out quicker than others-"
    cl "Pour certaines filles, ça sort plus vite que d'autres-"

# game/v2/scene8.rpy:167
translate francais v2s8_cee3b098:

    # cl "*Sighs* But yeah. Eventually."
    cl "*Soupirs* Mais ouais. Peut-être."

# game/v2/scene8.rpy:236
translate francais v2s8_ab2f2278:

    # u "presidential phone calls?"
    u "Des appels téléphoniques présidentiels ?"

# game/v2/scene8.rpy:262
translate francais v2s8_39684b21:

    # cl "Nooooothing! Bye now."
    cl "Riennnnnnn ! À plus tard."
