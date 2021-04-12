from abc import ABCMeta, abstractmethod


class MilitaryObject(metaclass=ABCMeta):

    @abstractmethod
    def accept(self, spy):
        pass


class Spy(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        res = "===== %s ======\n" % self.name
        return res

    @abstractmethod
    def visitGeneralStaff(self, generalStaff):
        pass

    @abstractmethod
    def visitMilitaryBase(self, militaryBase):
        pass


class GeneralStaff(MilitaryObject):
    def __init__(self, generals, secretPaper):
        self.generals = generals
        self.secretPaper = secretPaper

    def __str__(self):
        res = """GeneralStaff: У генеральному штабі є %d геренералів та %d секретних паперів """ % \
              (self.generals, self.secretPaper)
        return res

    def accept(self, spy: Spy):
        spy.visitGeneralStaff(self)


class MilitaryBase(MilitaryObject):
    def __init__(self, officers, soldiers, jeeps, tanks):
        self.officers = officers
        self.soldiers = soldiers
        self.jeeps = jeeps
        self.tanks = tanks

    def __str__(self):
        res = """MilitaryBase: На військовій базі є %d офіцерів, %d солдатів, %d джипів та %d танків.  """ % \
              (self.officers, self.soldiers, self.jeeps, self.tanks)
        return res

    def accept(self, spy: Spy):
        spy.visitMilitaryBase(self)


class SecretAgent(Spy):
    def __init__(self, name):
        super().__init__(name)
        self.information = ""

    def __str__(self):
        return super().__str__() + self.information

    def visitGeneralStaff(self, generalStaff: GeneralStaff):
        self.information = "У штабі міститься %d генералів та було %d секретних паперів, які я викрав!" \
                           % (generalStaff.generals, generalStaff.secretPaper)
        generalStaff.secretPaper = 0

    def visitMilitaryBase(self, militaryBase: MilitaryBase):
        self.information = """ На військовій базі є %d офіцерів, %d солдатів, %d джипів та %d танків.  """ % \
                           (militaryBase.officers, militaryBase.soldiers, militaryBase.jeeps, militaryBase.tanks)


class Saboter(Spy):
    def __str__(self):
        return super().__str__() + "I will kill everyone and destroy everything"

    def visitGeneralStaff(self, generalStaff: GeneralStaff):
        generalStaff.generals = 0

    def visitMilitaryBase(self, militaryBase: MilitaryBase):
        militaryBase.officers = 0
        militaryBase.soldiers = 0
        militaryBase.jeeps = 0
        militaryBase.tanks = 0


class Helper(Spy):
    def visitGeneralStaff(self, generalStaff: GeneralStaff):
        generalStaff.generals += 5

    def visitMilitaryBase(self, militaryBase: MilitaryBase):
        militaryBase.officers += 10
        militaryBase.soldiers += 100
        militaryBase.jeeps += 30
        militaryBase.tanks += 5

generalStaff = GeneralStaff(20, 100)
print(generalStaff)

JamesBond = SecretAgent("Agent 007")
generalStaff.accept(JamesBond)
print(JamesBond)
print(generalStaff)

militaryBase = MilitaryBase(10, 1000, 300, 20)
print(militaryBase)
militaryBase.accept(JamesBond)
print(JamesBond)

Rambo = Saboter("Rambo")
generalStaff.accept(Rambo)
print(Rambo)
print(generalStaff)
militaryBase.accept(Rambo)
print(militaryBase)

AgentSmith = Helper("AgentSmith")
generalStaff.accept(AgentSmith)
militaryBase.accept(AgentSmith)
print(AgentSmith)
print(generalStaff)
print(militaryBase)

