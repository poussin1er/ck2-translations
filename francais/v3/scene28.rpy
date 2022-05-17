# TODO: Translation updated at 2022-04-11 22:36

# game/v3/scene28.rpy:23
translate francais v3s28_2ed02fae:

    # li "Okay, so, now that we're alone, I can speak more freely."
    li "Ok, donc, maintenant qu'on est seuls, je peux parler plus librement."

# game/v3/scene28.rpy:28
translate francais v3s28_732b8e17:

    # li "I don't know how the fuck Chloe got that recording. I mean..."
    li "Je sais pas comment Chloé a pu obtenir cet enregistrement. Je pense que..."

# game/v3/scene28.rpy:33
translate francais v3s28_7975952f:

    # li "You were there that night, you know what happened."
    li "Tu étais là à cette soirée, tu sais ce qui s'est passé."

# game/v3/scene28.rpy:38
translate francais v3s28_41fe8992:

    # u "Yeah, I-"
    u "Ouais, je-"

# game/v3/scene28.rpy:43
translate francais v3s28_91444257:

    # li "I don't even want to think about it. I'm starting to get paranoid that every room I'm in is bugged or something."
    li "Je n'ai même pas envie d'y penser. Je commence à devenir paranoïaque à l'idée que chaque pièce dans laquelle je me trouve est sur écoute ou un truc du genre."

# game/v3/scene28.rpy:48
translate francais v3s28_c8e82a95:

    # u "(Damn, if she ever found out it was me...)"
    u "(Putain, si jamais elle découvre que c'était moi...)"

# game/v3/scene28.rpy:53
translate francais v3s28_8e72933e:

    # li "But, with the damage already done, we're gonna have to smash this next phase."
    li "Mais, avec les dégâts déjà subis, on va devoir écraser cette prochaine étape."

# game/v3/scene28.rpy:58
translate francais v3s28_80bcb409:

    # u "Okay, so what are you thinking?"
    u "Ok, alors, à quoi tu penses ?"

# game/v3/scene28.rpy:63
translate francais v3s28_50e0c55c:

    # li "I had some other ideas but I think these are the strongest, especially after hearing what Penelope said earlier."
    li "J'avais d'autres idées mais je pense que celles-ci sont les meilleures, surtout après avoir entendu ce que Pénélope a dit tout à l'heure."

    python:
        lindsey_board = PlanningBoard("images/v3/planning_boards/lindsey_background.webp", money=lindsey_board.money, style="lindsey_board")

        lindsey_board.add_approach("Newspaper",
            "Lindsey est interviewée pour le journal de l'université",
            opinion="\"Le journal de l'université va être très populaire, surtout le premier. Ça serait génial d'y avoir un article entier consacré à ma campagne. On pourra raconter tout ce qu'on veut, que ce soit en positif sur moi ou en négatif au sujet de mon adversaire.\"")

        lindsey_board.add_approach("Polly",
            "Faire en sorte que Polly soutienne Lindsey",
            opinion="\"Une grande pop star est en ville, et il va falloir en profiter. Tu imagines si Polly soutenait ma campagne ? On pourrait peut-être même la faire se produire sur scène ! Ça serait complètement dingue.\"")

        v3s28_lindsey_elijah = lindsey_board.add_subtask("Newspaper",
            "Demander à Elijah d'interviewer Lindsey",
            opinion="\"Elijah est à la tête du journal, il est donc logique de lui demander une interview. Par contre... C'est un vrai connard. Je ne le laisserais pas accepter cette idée simplement parce qu'il cherchera à déformer mes propos pour en faire un blog à ragots. Il faut qu'on soit prêts quand on le rencontrera.\"",
            people=[elijah])

        lindsey_board.add_subtask("Newspaper",
            "Demander à Riley d'interviewer Lindsey",
            opinion="\"Riley est nouvelle sur la scène du journal, et en plus c'est une fille. Je serais certainement plus à l'aise si c'était Riley qui m'interviewait, mais là encore, il faut qu'on s'assure que l'article ait l'air professionnel, alors il faudra préparer nos sujets.\"",
            people=[riley])

        lindsey_board.add_task("Newspaper",
            "préparer Lindsey pour l'interview",
            opinion="\"Tu seras mon coach en relations publiques, d'accord ? On va même préparer une liste de questions lors d'une interview fictive, pour qu'on puisse vraiment voir si je me débrouille bien sous pression et que tu puisses me donner des conseils sur ce qu'il est préférable de dire à notre interlocuteur.\"",
            people=[lindsey,mc])

        lindsey_board.add_task("Newspaper",
            "Lindsey fait l'interview",
            opinion="\"Il va falloir que je fasse cette interview seule, parce qu'ils vont certainement écrire ça là-dedans. Mais tu pourrais peut-être me regarder et me soutenir à distance.\"",
            people=[lindsey])

        lindsey_board.add_task("Polly",
            "Découvrir où se trouve Polly",
            opinion="\"La première étape de cette incroyable idée est de découvrir où se trouve Polly. J'ai un ou deux amis qui pourraient nous aider à la retrouver. Il va falloir faire quelques efforts pour la localiser, mais je te promets. J'y arriverai.\"")

        v3s28_lindsey_roomservice = lindsey_board.add_subtask("Polly",
            "Se faire passer pour le room service",
            opinion="\"Une fois qu'on saura où elle séjourne, on pourra mettre la main sur des uniformes d'employés correspondants, et monter dans sa chambre en tant que Room Service. Il faudra juste faire attention à ce qu'on dira, on n'a pas envie qu'elle nous prenne pour des harceleurs détraqués, tu vois ?\"")

        lindsey_board.add_subtask("Polly",
            "Se présenter en tant que soi-même",
            opinion="\"Une fois qu'on saura où elle séjourne, on tentera notre chance en frappant à sa porte. Polly n'est pas une personne détestable, elle ne refusera donc pas la visite de deux très grands fans, mais il faudra faire attention à ne pas la faire paniquer.\"")

        lindsey_board.add_task("Polly",
            "Convaincre Polly de soutenir Lindsey lors de son concert acoustique",
            opinion="\"Enfin, on demandera à Polly de bien vouloir soutenir ma campagne. Je ne sais pas du tout si elle va se produire, poster quelque chose, ou de ce qu'on pourra lui faire faire... Mais j'espère bien qu'on pourra parvenir à quelque chose.\"",
            people=[lindsey,mc,polly])

    call screen planning_board(lindsey_board)

    if lindsey_board.approach is not None:
        $ v3_lindsey_newspaper = lindsey_board.approach.id == "Newspaper"

    if lindsey_board.selected_task is not None:
        $ v3_lindsey_elijah = lindsey_board.selected_task == v3s28_lindsey_elijah
        $ v3_lindsey_roomservice = lindsey_board.selected_task == v3s28_lindsey_roomservice

    # End planning board (screen disappears)

# game/v3/scene28.rpy:127
translate francais v3s28_dcd99046:

    # u "I think this idea is the strongest."
    u "Je trouve que cette idée serait la meilleure."

# game/v3/scene28.rpy:133
translate francais v3s28_98998a42:

    # u "A lot of people are going to see the paper, so an interview would be great."
    u "Beaucoup de monde va lire le journal, alors une interview serait géniale."

# game/v3/scene28.rpy:138
translate francais v3s28_ed200f25:

    # li "Yeah, everyone is going to read that first edition. They're placing copies all over the school."
    li "Ouais, tout le monde lira cette première édition. Ils sont en train de distribuer des exemplaires partout dans l'école."

# game/v3/scene28.rpy:143
translate francais v3s28_503cb79f:

    # u "I can help prepare you to the best of my ability, haha."
    u "Je vais t'aider à te préparer du mieux que je peux, haha."

# game/v3/scene28.rpy:148
translate francais v3s28_a46c1535:

    # li "I just hope there's no trick questions that can fuck up my campaign."
    li "J'espère seulement qu'il n'y aura pas de questions pièges qui pourront foutre en l'air ma campagne."

# game/v3/scene28.rpy:153
translate francais v3s28_ae77170f:

    # u "We can practice, don't worry."
    u "On s'entraînera, t'inquiète pas."

# game/v3/scene28.rpy:159
translate francais v3s28_7dbed47e:

    # u "If we could get Polly to endorse your campaign, I'd say you've basically got this presidency in the bag."
    u "Si on pouvait convaincre Polly de soutenir ta campagne, je dirais que tu auras pratiquement la présidence en poche."

# game/v3/scene28.rpy:164
translate francais v3s28_a8a18138:

    # li "Haha, I like your confidence. I sure hope so."
    li "Haha, j'aime ta confiance. J'espère bien."

# game/v3/scene28.rpy:169
translate francais v3s28_49e08796:

    # u "There are quite a few hoops to jump through to get her on board, but it's totally do-able."
    u "Il y aura pas mal d'obstacles à franchir pour qu'elle accepte de se joindre à nous, mais c'est tout à fait faisable."

# game/v3/scene28.rpy:174
translate francais v3s28_9a9c191f:

    # li "Yeah, and she seems super friendly, especially for being a beautiful pop princess. *Laughs*"
    li "J'espère, et elle a l'air super sympa, surtout en étant une belle princesse de la pop. *Rire*"

# game/v3/scene28.rpy:176
translate francais v3s28_c03e3cc1:

    # li "I just hope I don't fan-girl too much if we do get to talk to her."
    li "J'espère simplement que je ne serai pas trop fan-girl, si on arrive à lui parler."

# game/v3/scene28.rpy:183
translate francais v3s28_59c6bf2c:

    # u "I can't wait to get started, I feel good about this one, it's going to be interesting."
    u "J'ai hâte de commencer, je la sens bien cette affaire, elle devrait être intéressante."

# game/v3/scene28.rpy:188
translate francais v3s28_7893aca8:

    # li "Yes! Phase three is a winner, no doubt."
    li "Oui ! La phase trois sera gagnante, j'en suis sûre."

# game/v3/scene28.rpy:194
translate francais v3s28_2846dd00:

    # u "Let's be realistic, though. It could go wrong, so we should be prepared for that possibility."
    u "Mais soyons réalistes. Ça pourrait mal tourner, alors il faut se préparer à cette possibilité."

# game/v3/scene28.rpy:199
translate francais v3s28_5fac59ac:

    # li "Don't be so negative, [name]! We can do this, I know it."
    li "Ne sois pas si négatif, [name] ! On peut y arriver, j'en suis convaincue."

# game/v3/scene28.rpy:204
translate francais v3s28_5b1a02b3:

    # u "Haha, okay. I guess I could be a little more optimistic."
    u "Haha, ok. Je crois que je peux être un peu plus optimiste."

# game/v3/scene28.rpy:209
translate francais v3s28_38777b64:

    # li "Yes, you could."
    li "Oui, tu peux."

# game/v3/scene28.rpy:214
translate francais v3s28_3f4466e9:

    # li "I'm feeling good about this one."
    li "Je la sens bien, celle-là."

# game/v3/scene28.rpy:219
translate francais v3s28_94921388:

    # li "And again, for the millionth time, thanks for your help."
    li "Et encore une fois, et pour la millionième fois, merci de ton aide."

# game/v3/scene28.rpy:224
translate francais v3s28_f05a93b6:

    # u "Haha, I wouldn't be here if I didn't want to be."
    u "Haha, je serais pas là si je voulais pas l'être."

# game/v3/scene28.rpy:229
translate francais v3s28_4319ffde:

    # li "I don't know if I say it often enough, but I appreciate it so much."
    li "Je ne sais pas si je le dis assez souvent, mais je t'en suis très reconnaissante."

# game/v3/scene28.rpy:234
translate francais v3s28_eac36e17:

    # li "Thanks for sticking to this with me."
    li "Merci de rester avec moi."

# game/v3/scene28.rpy:256
translate francais v3s28_2c9858c3:

    # u "We're in this together."
    u "On est dans le même bateau."

# game/v3/scene28.rpy:261
translate francais v3s28_c32c6828:

    # li "Ugh, you're the best. Now go, I'll catch up with you later."
    li "Ouah, tu es le meilleur. Maintenant vas-y, je te rejoindrai plus tard."

# game/v3/scene28.rpy:266
translate francais v3s28_c9371b94:

    # u "Haha, ok. Have a good day."
    u "Haha, ok. Passe une bonne journée."

translate francais strings:

    # game/v3/scene28.rpy:181
    old "Stay positive"
    new "Rester positif"

    # game/v3/scene28.rpy:181
    old "Failing is a possibility"
    new "L'échec reste envisageable"
