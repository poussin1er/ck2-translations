init python:
    class Reputations(Enum):
        BRO = "ami"
        BOYFRIEND = "Petit ami"
        TROUBLEMAKER = "emmerdeur"

        POPULAR = "populaire"
        CONFIDENT = "confident"
        LOYAL = "loyal"


    class Reputation:
        def __init__(self):
            self.components = {Reputations.BRO: 1, Reputations.BOYFRIEND: 2, Reputations.TROUBLEMAKER: 2}

        def __call__(self):
            bro = self.components[Reputations.BRO]
            boyfriend = self.components[Reputations.BOYFRIEND]
            troublemaker = self.components[Reputations.TROUBLEMAKER]

            # Sort reputation values
            reputation_dict = {
                Reputations.POPULAR: bro * troublemaker / float(boyfriend),
                Reputations.CONFIDENT: boyfriend * troublemaker / float(bro),
                Reputations.LOYAL: bro * boyfriend / float(troublemaker)
            }

            return [k for k, v in sorted(reputation_dict.items(), key=lambda item: item[1], reverse=True)][0]

        def add_point(self, var, value=1):
            # Don't update reputation if reputation is locked
            if locked_reputation or _in_replay:
                return

            if pb_reputation_notification:
                renpy.show_screen("popup", message="{} point ajouté".format(var.value.capitalize()))

            old_reputation = self()

            self.components[var] += value

            # Notify user on reputation change
            if self() != old_reputation:
                renpy.notify("Ta réputation a changé en {}".format(self().value))


# Reputation Screens
screen reputation_choice_hint():
    style_prefix "reputation_choice"

    frame:
        xalign 1.0
        xoffset -100

        background "gui/reputation/background_{}.webp".format(reputation().name.lower())

        hbox:
            spacing 5
            align (0.5, 0.5)
            xoffset 20

            add Transform("gui/reputation/logo.webp", zoom=0.2382) yalign 0.5

            text reputation().name yalign 0.5

style reputation_choice_text is syne_extra_bold_22


screen reputation_popup(required_reputation=None):
    modal True
    zorder 300

    if required_reputation is None or required_reputation == reputation():
        $ message = "Félicitations ! Ton trait de caractère principal {{b}}{}{{/b}} vient de modifier la décision que quelqu'un était en train de prendre.".format(reputation().value)
    else:
        $ message = "Malheureusement, ton Trait de caractère principal {{b}}{}{{/b}} n'a pas permis de modifier le résultat de cette décision.".format(reputation().value)

    use alert_template(message):
        textbutton "OK":
            align (0.5, 1.0)
            action Return()

    if config_debug:
        timer 0.1 action Return()
