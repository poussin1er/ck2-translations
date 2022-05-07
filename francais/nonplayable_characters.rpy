init python:
    class Frat(Enum):
        APES = 0
        WOLVES = 1


    class Relationship(SmartEnum):
        MAD = -4
        THREATEN = -3
        MAKEFUN = -2
        AWKWARD = -1
        FRIEND = 0
        MOVE = 1
        DATE = 2
        LIKES = 3
        TRUST = 4
        BRO = 5
        KISS = 6
        FWB = 7
        LOYAL = 8
        TAMED = 9
        GIRLFRIEND = 10


    class NonPlayableCharacter:
        """
        Custom character class primarily used for managing all the character specific function of the game.

        Attributes:
            name (str): The display name for the character
            profile_picture (str): The file name for the characters profile picture, located in "images/nonplayable_characters/profile_pictures/"
        """

        characters = {}

        def __init__(self, name, username=None):
            self.name = name
            self._username = name if username is None else username

            self._messenger = None
            self._simplr = None
            self._relationship = Relationship.FRIEND
            self._fighter = None

            self.points = 0

            NonPlayableCharacter.characters[name] = self

        @property
        def username(self):
            try:
                if self._username is not None:
                    return self._username
            except AttributeError: pass

            return self.name

        @username.setter
        def username(self, value):
            self._username = value

        @property
        def relationship(self):
            try: return self._relationship
            except AttributeError: return Relationship.FRIEND

        @relationship.setter
        def relationship(self, value):
            if not isinstance(value, Relationship):
                raise TypeError("{} doit être Relation de type".format(value))

            self._relationship = value

            if value == Relationship.GIRLFRIEND:
                mc.relationships.add(self)
                mc.girlfriends.add(self)

            elif value == Relationship.FWB:
                try: mc.relationships.remove(self)
                except KeyError: pass
                mc.relationships.add(self)

            else:
                try:
                    mc.relationships.remove(self)
                    mc.girlfriends.remove(self)
                except KeyError: pass

        @property
        def messenger(self):
            try: self._messenger
            except AttributeError: self._messenger = None

            if self._messenger is None:
                self._messenger = Contact(self.name)
                messenger.contacts.append(self.messenger)
            return self._messenger

        @messenger.setter
        def messenger(self, value):
            self._messenger = value

        @property
        def simplr(self):
            try: self._simplr
            except AttributeError: self._simplr = None

            if self._simplr is None:
                self._simplr = SimplrContact(self.name)
                simplr_app.pending_contacts.append(self._simplr)
            return self._simplr

        @simplr.setter
        def simplr(self, value):
            self._simplr = value

        @property
        def fighter(self):
            return self._fighter

        @fighter.setter
        def fighter(self, value):
            self._fighter = value

        @property
        def profile_picture(self):
            return self.profile_pictures[0]

        @property
        def profile_pictures(self):
            DIRECTORY = os.path.join(config.basedir, "game", "images", "characters", self.name.lower())

            return ["images/characters/{}/{}".format(self.name.lower(), file) for file in os.listdir(DIRECTORY)]

        def __after_load__(self):
            attrs = vars(self).copy()

            self.__init__(self.name)

            for var, value in attrs.items():
                try: setattr(self, var, value)
                except AttributeError: continue

        def reset_points(self):
            self.points = 0


# default aaron = NonPlayableCharacter("Aaron", "DoubleARon")
# default adam = NonPlayableCharacter("Adam", "A.D.A.M.")
default amber = NonPlayableCharacter("Amber", "Amber_xx") # Relationship progression: FRIEND, KISS, FWB (in CK1)
default anon = NonPlayableCharacter("Anon", "concerned1")
# default aryssa = NonPlayableCharacter("Aryssa") # Relationship progression: FRIEND, LIKES
default aubrey = NonPlayableCharacter("Aubrey", "Aubs123") # Relationship progression: MAD, FRIEND, FWB (in ck1), TAMED (in ck2v2)
default autumn = NonPlayableCharacter("Autumn", "Its_Fall") # Relationship progression: MAD, FRIEND, KISS (in ck2v2), LOYAL (in ck2v2)
default beth = NonPlayableCharacter("Beth")
default buyer = NonPlayableCharacter("Acheteur")
# default caleb = NonPlayableCharacter("Caleb", "Aleb")
default cameron = NonPlayableCharacter("Cameron", "Cameroon") # Relationship progression: FRIEND, BRO
# default candy = NonPlayableCharacter("Candy") # Relationship progression: FRIEND, LIKES, FWB
default charli = NonPlayableCharacter("Charli", "CharliAndTheCockFactory")
default chloe = NonPlayableCharacter("Chloé", "Chloe101") # Relationship progression: MAD, FRIEND, FWB, GIRLFRIEND (in ck1)
default chris = NonPlayableCharacter("Chris", "Chriscuit") # Relationshp progression: MAD, FRIEND
default dean = NonPlayableCharacter("Dean")
default elijah = NonPlayableCharacter("Elijah", "Elijah_Woods") # Relationship progression: MAKEFUN, FRIEND
default emily = NonPlayableCharacter("Emily", "emilyyyy") # Relationship progression: FRIEND, FWB (in CK1)
default emmy = NonPlayableCharacter("Emmy") # Relationship progression: FRIEND, LIKES, FWB (in CK1)
# default evelyn = NonPlayableCharacter("Evelyn") # Relationship progression: FRIEND, MOVE, DATE, LIKES, KISS
default grayson = NonPlayableCharacter("Grayson", "G-rayson")
default imre = NonPlayableCharacter("Imre", "BadBoyImre") # Relationship progression: MAD, FRIEND
default iris = NonPlayableCharacter("Iris")
default jenny = NonPlayableCharacter("Jenny") # Relationship progression: AWKWARD, FRIEND, FWB (in ck2v1)
# default josh = NonPlayableCharacter("Josh", "Josh80085") # Relationship progression: MAD, FRIEND
# default julia = NonPlayableCharacter("Julia")
# default kai = NonPlayableCharacter("Kai", "KaiCriesWith2Ply")
# default kim = NonPlayableCharacter("Kim", "KimPlausible")
# default kourtney = NonPlayableCharacter("Kourtney") # Relationship progression: FRIEND, LIKES
default lauren = NonPlayableCharacter("Lauren", "LoLoLauren") # Relationship progression: MAD, FRIEND, MOVE, KISS, GIRLFRIEND (in ck1)
# default lews_official = NonPlayableCharacter("LewsOfficial")
default lindsey = NonPlayableCharacter("Lindsey", "LindsLou") # Relationship progression: FRIEND, KISS, FWB (in ck1)
# default mason = NonPlayableCharacter("Mason", "Mason_Mas")
default mr_lee = NonPlayableCharacter("Mr Lee")
default ms_rose = NonPlayableCharacter("Mme Rose") # Relationship progression: THREATEN, FRIEND, KISS, FWB (in ck1)
default naomi = NonPlayableCharacter("Naomi", "NaomiXMarie") # Relationship progression: FRIEND, FWB (in ck2v2)
default nora = NonPlayableCharacter("Nora", "Nora_12") # Relationship progression: MAD, FRIEND, MOVE, LIKES, FWB (in ck1)
# default parker = NonPlayableCharacter("Parker")
default penelope = NonPlayableCharacter("Pénélope", "Penelopeeps") # Relationship progression: FRIEND, LIKES (in ck1), LOYAL (in ck2v1)
default polly = NonPlayableCharacter("Polly")
default riley = NonPlayableCharacter("Riley", "RileyReads") # Relationship progression: FRIEND, MOVE, LIKES, FWB (in ck1)
default ryan = NonPlayableCharacter("Ryan", "Ryanator")
default samantha = NonPlayableCharacter("Samantha", "SamFromSpaceJam") # Relationship progression: FRIEND, MOVE (in ck1), FWB (in ck2v1)
# default satin = NonPlayableCharacter("Satin") # Relationship progression: FRIEND, FWB
default sebastian = NonPlayableCharacter("Sebastian", "Big Seb")
default tom = NonPlayableCharacter("Tom")
default trainer = NonPlayableCharacter("Entraîneur")
default wolf = NonPlayableCharacter("Loup")
