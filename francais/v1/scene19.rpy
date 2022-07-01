# TODO: Translation updated at 2022-03-17 15:15

# game/v1/scene19.rpy:17
translate francais v1s19_e88d276d:

    # u "(Where the hell is she...?)"
    u "(Putain, elle est où...?)"

# game/v1/scene19.rpy:22
translate francais v1s19_177d77b3:

    # u "(Gotta be in here.)"
    u "(On doit se retrouver ici.)"

# game/v1/scene19.rpy:32
translate francais v1s19_f982e08e:

    # cl "Took you long enough! Ready to get started?"
    cl "Tu en as mis du temps ! Prêt à commencer ?"

# game/v1/scene19.rpy:37
translate francais v1s19_33f941b1:

    # u "Damn, someone's eager..."
    u "Eh ben, quelqu'un est impatient..."

# game/v1/scene19.rpy:53
translate francais v1s19_1fff9bf5:

    # u "Ha... No hi? No, how was class? Blah? Blah? Blah? Nothing?"
    u "Ha... Même pas un bonjour ? Aucun, comment s'est passé le cours ? Blablabla ? Blablabla ? Blablabla ? Rien ?"

# game/v1/scene19.rpy:58
translate francais v1s19_bee0b75c:

    # cl "I'm sorry [name], I'm just really focused and I'm anxious to get started considering the Lindsey parade that's been taking place all day."
    cl "Je suis désolée [name], je suis très concentrée et j'ai hâte de commencer vu la parade de Lindsey qui s'est déroulée toute la journée."

# game/v1/scene19.rpy:63
translate francais v1s19_2bd5fede:

    # u "I can understand that... I guess I'll let you off the hook for being in such a haste."
    u "Je comprends ça... Je crois que je vais te laisser tranquille, t'as l'air vraiment pressée."

# game/v1/scene19.rpy:68
translate francais v1s19_2e62b657:

    # cl "Haha, thanks. Should we get started then?"
    cl "Haha, merci. Alors, on commence ?"

# game/v1/scene19.rpy:73
translate francais v1s19_1ca64d42:

    # u "Sure, let's get to it."
    u "Bien sûr, c'est parti."

# game/v1/scene19.rpy:78
translate francais v1s19_614c5160:

    # cl "Okay, so here's my plan..."
    cl "Ok, alors voici mon plan..."

# game/v1/scene19.rpy:83
translate francais v1s19_e9cccce0:

    # cl "The first phase of my campaign is to re-establish old loyalties. The first time I was elected, people loved me and I need to remind them why."
    cl "La première phase de ma campagne consiste à rétablir les anciennes relations. La première fois que j'ai été élue, les personnes m'ont aimée et je dois leur rappeler pourquoi."

# game/v1/scene19.rpy:85
translate francais v1s19_8e95fb42:

    # cl "So, here's what I'm thinking for phase one."
    cl "Alors, voici à quoi je pense pour la première phase."

    python:
        chloe_board.add_approach("Wolves", "Proclamer les Wolves comme confrérie officielle des Chicks", opinion="\"Les Wolves et les Chicks ont déjà un lien spécial, mais on peut convaincre Chris de faire des Wolves notre confrérie officielle. Ce qui impliquera une vie entière de loyauté et de soutien, ce qui est exactement ce dont j'ai besoin en ce moment.\"")
        chloe_board.add_approach("Apes", "Mettre les Apes de notre côté", opinion="\"En ce moment, Chris est pratiquement comme une plaie ouverte et je ne veux pas remuer le couteau dans la plaie, avec tout ce qu'il traverse. Si on profite de ce moment de vulnérabilité pour lui faire entendre raison, on pourra peut-être l'amener à se concentrer sur lui-même, sur les Wolves et, surtout, sur moi en tant que Présidente des Chicks. Fais juste attention à ne pas dire la mauvaise chose...\"")

        chloe_board.add_task("Wolves", "Parler à Chris pour obtenir son soutien complet",
            opinion="\"Chris est pratiquement comme une plaie ouverte en ce moment, et je ne veux pas remuer le couteau dans la plaie qu'il traverse. Si on profite de ce moment de vulnérabilité pour lui faire entendre raison, on pourra peut-être l'amener à se concentrer sur ce qui est vraiment important.\"",
            people=[mc, chloe, chris])
        v1s19_real_wolf = chloe_board.add_subtask("Wolves", "Photoshoot with a real wolf ($450)",
            opinion="\"On pourra louer un loup pendant une heure en échange d'une jolie somme. Peux-tu imaginer ce que les gens diront quand ils verront que les Chicks se sont associées aux Wolves et que je pose avec un vrai loup?!\"",
            people=[mc, chloe, wolf, trainer],
            cost=450)
        v1s19_plush_wolf = chloe_board.add_subtask("Wolves", "Photoshoot avec un loup en peluche (50 $)",
            opinion="\"Je pourrais facilement trouver une peluche de loup pour poser avec. C'est un peu moins intéressant qu'un vrai, mais certainement moins cher et bien sûr, l'option \"la plus sûre\".\"",
            people=[mc, chloe],
            cost=50)
        chloe_board.add_task("Wolves", "Poste la photo sur Kiwii",
            opinion="\"La dernière étape sera de poster la photo avec une bonne légende et d'espérer que tout se passe bien.\"",
            people=[mc, chloe])

        chloe_board.add_task("Apes", "Organise une petite rencontre avec Cameron, Grayson, Chloé, Aubrey et toi.",
            opinion= "\"Commençons par le commencement : Tous les rassembler dans une pièce, leur donner à chacun une bière et mettre de la bonne musique. Alors, une fois l'ambiance posée, on pourra passer aux choses sérieuses.\"",
            people=[mc, chloe, aubrey, grayson, cameron])
        v1s19_talk_cameron = chloe_board.add_subtask("Apes", "Parler à Cameron d'une alliance stratégique",
            opinion="\"Cameron a secrètement d'incroyables qualités de leader, et je sais qu'il prévoit de les utiliser un jour. Si on dit à Cameron exactement ce qu'il veut entendre en ce qui concerne l'avenir des Apes, il n'aura aucune raison de voter contre moi.\"",
            people=[mc, chloe, cameron])
        v1s19_seduce_grayson = chloe_board.add_subtask("Apes", "Séduire Grayson",
            opinion="\"Ne te méprends pas, je sais que ça a l'air un peu... manipulateur, mais tu dois admettre que je peux facilement mettre Grayson de notre côté avec une pincée de flirt. Et crois-moi, il n'en faudra pas beaucoup, surtout avec quelques verres dans le nez.\"",
            people=[mc, chloe, grayson])

    call screen planning_board(chloe_board)

label v1s19_continue:
    $ v1_chloe_wolves = chloe_board.approach.id == "Wolves"
    $ v1_realwolf = chloe_board.selected_task == v1s19_real_wolf
    $ v1_chloe_cameron = chloe_board.selected_task == v1s19_talk_cameron

    if v1_realwolf:
        $ chloe_board.money -= 450
    elif v1_chloe_wolves:
        $ chloe_board.money -= 50

# game/v1/scene19.rpy:126
translate francais v1s19_continue_3076e58f:

    # u "From the options we have, these are the final decisions I'd go with."
    u "Parmi les options qu'on a, voici les décisions finales que je prendrais."

# game/v1/scene19.rpy:132
translate francais v1s19_continue_8671c131:

    # cl "Getting the Apes to side with us could take a lot of convincing but..."
    cl "Il faudra peut-être convaincre les Apes de se mettre de notre côté, mais..."

# game/v1/scene19.rpy:133
translate francais v1s19_continue_1bf4d4fe:

    # cl "If we manage to pull it off, a Chicks and Apes alliance would make for an interesting future of the Chicks."
    cl "Si nous y parvenons, une alliance entre les Chicks et les Apes permettrait d'envisager un bel avenir pour les Chicks."

# game/v1/scene19.rpy:136
translate francais v1s19_continue_ad57e28d:

    # cl "I know Chris trusts me, so I'm pretty sure we've already got the Wolves on our side. Guess we'll find out, though..."
    cl "Je sais que Chris me fait confiance, alors je suis presque sûre que les Wolves sont déjà de notre côté. Je pense qu'on va le découvrir, malgré tout..."

# game/v1/scene19.rpy:138
translate francais v1s19_continue_17e252d7:

    # cl "Hmm, okay..."
    cl "Hmm, d'accord..."

# game/v1/scene19.rpy:143
translate francais v1s19_continue_42a399c2:

    # cl "These are your choices, remember that. So, be sure you're there to help me when the time comes, okay?"
    cl "Ce sont tes choix, ne l'oublie pas. Alors, fais en sorte d'être là pour m'aider quand le moment sera venu, d'accord ?"

# game/v1/scene19.rpy:148
translate francais v1s19_continue_fd64a361:

    # u "Yes, Madame President..."
    u "Oui, Madame la Présidente..."

# game/v1/scene19.rpy:153
translate francais v1s19_continue_f4ef9b12:

    # cl "Ewww, that sounds so weird coming from you. *Chuckles*"
    cl "Oulala, ça fait bizarre venant de toi. *Rire*"

# game/v1/scene19.rpy:158
translate francais v1s19_continue_8e364f81:

    # u "Hey, you asked for this."
    u "Hey, tu l'as demandé."

# game/v1/scene19.rpy:163
translate francais v1s19_continue_51aa3d22:

    # cl "Okay, okay, fine."
    cl "Ok, ok, bien."
# TODO: Translation updated at 2022-05-14 15:02

# game/v1/scene19.rpy:53
translate francais v1s19_76622052:

    # u "Ha... No \"hi?\" No \"how was class?\" Blah? Blah? Blah? Nothing?"
    u "Ha... Même pas un \"bonjour\" ? Aucun, comment s'est passé le cours ? Blablabla ? Blablabla ? Blablabla ? Rien ?"

# game/v1/scene19.rpy:58
translate francais v1s19_4be3ae55:

    # cl "I'm sorry [name], I'm just really focused and anxious to get started considering the Lindsey parade that's been taking place all day."
    cl "Je suis désolée [name], je suis très concentrée et j'ai hâte de commencer vu la parade de Lindsey qui s'est déroulée toute la journée."

# game/v1/scene19.rpy:63
translate francais v1s19_521e4635:

    # u "I can understand that... I guess I'll let you off the hook for being a little curt."
    u "Je comprends cela... Je crois que je vais te laisser tranquille pour avoir été un peu brusque."

# game/v1/scene19.rpy:68
translate francais v1s19_fd6636a8:

    # cl "Ha, thanks. Should we get started, then?"
    cl "Haha, merci. Alors, on commence ?"

# game/v1/scene19.rpy:83
translate francais v1s19_3ca0e6d1:

    # cl "The first phase of my campaign is to re-establish old loyalties. The first time I was elected, people loved me, and I need to remind them why."
    cl "La première phase de ma campagne consiste à rétablir les anciennes relations. La première fois que j'ai été élue, les personnes m'ont aimée et je dois leur rappeler pourquoi."

# game/v1/scene19.rpy:137
translate francais v1s19_continue_21ceaa9e:

    # cl "Getting the Apes to side with us could take a lot of convincing, but..."
    cl "Il faudra peut-être convaincre les Apes de se mettre de notre côté, mais..."

# game/v1/scene19.rpy:158
translate francais v1s19_continue_9dff9282:

    # cl "Ewww, that sounds so weird coming from you."
    cl "Oulala, ça fait bizarre venant de toi."
# TODO: Translation updated at 2022-06-24 10:14

# game/v1/scene19.rpy:173
translate francais v1s19_continue_f2cb0ea2:

    # u "So, uh... Before we wrap up I had something I wanted to ask you."
    u "Sinon, euh... Avant d'en finir, j'avais un truc à te demander."

# game/v1/scene19.rpy:178
translate francais v1s19_continue_30a30927:

    # cl "Just ask, [name], we've got stuff to do."
    cl "Pose la ta question, [name], on a des trucs à faire."

# game/v1/scene19.rpy:183
translate francais v1s19_continue_67140742:

    # u "Riley and I ran into Aubrey earlier, and she was super upset."
    u "Riley et moi avons croisé Aubrey tout à l'heure, et elle était vraiment contrariée."

# game/v1/scene19.rpy:188
translate francais v1s19_continue_10c0579b:

    # cl "Ugh, I told her we'd handle it. Everything's fine, the school just makes a big fucking deal if you don't get forms in on time."
    cl "Arf, je lui ai dit qu'on allait s'en occuper. Tout ira bien, l'école en fait tout un plat si on ne rend pas les formulaires à temps."

# game/v1/scene19.rpy:193
translate francais v1s19_continue_b97af3cb:

    # u "But Aubrey said-"
    u "Mais Aubrey a dit-"

# game/v1/scene19.rpy:198
translate francais v1s19_continue_2fe919fc:

    # cl "Just trust me when I say I know what I'm doing, okay?"
    cl "Contente-toi de me faire confiance quand je dis que je sais ce que je fais, d'accord ?"

# game/v1/scene19.rpy:203
translate francais v1s19_continue_4de3101e:

    # u "Okay... fair enough."
    u "D'accord... c'est normal."

# game/v1/scene19.rpy:208
translate francais v1s19_continue_e65cd18e:

    # cl "But thanks for caring about Aubrey, she's probably just exhausted."
    cl "Mais merci de te soucier d'Aubrey, elle doit juste être très fatiguée."

# game/v1/scene19.rpy:210
translate francais v1s19_continue_b98e7096:

    # cl "Now let's get out there and win, okay?"
    cl "Maintenant, on y va et on gagne, d'accord ?"
