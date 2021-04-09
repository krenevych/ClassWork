from abc import ABCMeta, abstractmethod


class Spy(metaclass=ABCMeta):

    @abstractmethod
    def visitGeneralStaff(self, militaryObject):
        pass

    @abstractmethod
    def visitMilitaryBase(self, militaryObject):
        pass


class MilitaryObject(metaclass=ABCMeta):

    @abstractmethod
    def accept(self, visitor: Spy):
        pass


class GeneralStaff(MilitaryObject):

    def __init__(self, generals, secretPapers):
        self.generals = generals
        self.secretPapers = secretPapers

    def __str__(self):
        res = "У генеральному штабі %d генералів " \
              "та %d секретних паперів" \
              % (self.generals, self.secretPapers)
        return res

    def accept(self, visitor: Spy):
        visitor.visitGeneralStaff(self)


class MilitaryBase(MilitaryObject):
    def __init__(self, officers, soldiers, jeeps, tanks):
        self.officers = officers
        self.soldiers = soldiers
        self.jeeps = jeeps
        self.tanks = tanks

    def __str__(self):
        res = "На військовій базі: %d офіцерів " \
              "%d солдат, %d джипів, %d танків." \
              % (self.officers, self.soldiers, self.jeeps, self.tanks)
        return res

    def accept(self, visitor: Spy):
        visitor.visitMilitaryBase(self)


class SecretAgent(Spy):
    """Метою шпигуна Секретний агент є збір або викрадення секретної інформації."""

    def __init__(self):
        self.stolenInformation = ""

    def visitGeneralStaff(self, militaryObject : GeneralStaff):
        gen = militaryObject.generals
        sp = militaryObject.secretPapers
        self.stolenInformation = "На базі є %d генералів, викрадено %d секретних паперів" % (gen, sp)
        militaryObject.secretPapers = 0

    def visitMilitaryBase(self, militaryObject : MilitaryBase):
        of = militaryObject.officers
        s = militaryObject.soldiers
        j = militaryObject.jeeps
        t = militaryObject.tanks
        self.stolenInformation = "На базі є %d офіцерів, %d солдат, %d джипів, %d танків   " % (of, s, j, t)

    def __str__(self):
        return self.stolenInformation


class Saboteur(Spy):
    """ Метою відвідування військового об’єкту
     шпигуном Диверсант є знищення секретної документації,
     знищення особового складу та техніки військового об’єкту.
    """

    def visitGeneralStaff(self, militaryObject : GeneralStaff):
        militaryObject.generals = 0
        militaryObject.secretPapers = 0

    def visitMilitaryBase(self, militaryObject : MilitaryBase):
        militaryObject.officers = 0
        militaryObject.soldiers = 0
        militaryObject.tanks = 0
        militaryObject.jeeps = 0

    def __str__(self):
        return "Усіх уб'ю, один лишуся!"

if __name__ == "__main__":
    generalStaff = GeneralStaff(10, 100)
    print(generalStaff)

    militaryBase = MilitaryBase(30, 1000, 200, 20)
    print(militaryBase)

    print("=======SECRET AGENT ============")
    secretAgent = SecretAgent()
    saboteur = Saboteur()

    generalStaff.accept(secretAgent)
    print("Spy: ", secretAgent)
    print("MO : ", generalStaff)

    print("===================")
    militaryBase.accept(secretAgent)
    print("Spy: ", secretAgent)
    print("MO : ", militaryBase)

    print("======= SABOTEUR ============")
    generalStaff.accept(saboteur)
    print("Spy: ", saboteur)
    print("MO : ", generalStaff)

    print("===================")
    militaryBase.accept(saboteur)
    print("Spy: ", saboteur)
    print("MO : ", militaryBase)
