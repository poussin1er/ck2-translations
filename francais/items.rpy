init python:
    class Item:
        """Item class used to repersent an interactable Item

        Attributes:
            name (str): Display name of the item
            cost (int): Amount item costs in dollars
        """

        def __init__(self, name, cost, idle_image=None, hover_image=None, insensitive_image=None):
            self.name = name
            self.cost = cost
            self.idle_image = idle_image
            self.hover_image = hover_image
            self.insensitive_image = insensitive_image

# v2
define gift_card_50 = Item("Chèque cadeau de 50$", 50, idle_image="images/items/gift_card_50.webp")
define emerald_bracelet = Item("Bracelet d'émeraude", -1, idle_image="images/items/emerald_bracelet.webp")
define ruby_choker_necklace = Item("Collier ras de cou Rubis", -1, idle_image="images/items/ruby_choker_necklace.webp")
define brown_horse_golden_mane = Item("Cheval brun, crinière dorée", -1, idle_image="images/items/brown_horse_golden_mane.webp")
define white_horse_black_mane = Item("Cheval blanc, crinière noire", -1, idle_image="images/items/white_horse_black_mane.webp")
