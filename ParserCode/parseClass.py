###Imports###
from ast import literal_eval

###Files###
import EffectsPP.ParserCode.compileCode as compileCode


class Parse():
    def __init__(self):
        super().__init__()
        self.funcList = ['hi', 'new']
        self.stack = []

    def hi(self, line, i):
        i = i+1
        compileCode.write(Creature().text())
        return i

    def new(self, line, i):
        print(line[i + 1])
        if line[i + 1][:8] == "Creature":
            creature = eval(line[i + 1])
            compileCode.write(creature.text())

        return i+2


class Creature():
    def __init__(self, sprite, ID="", name="template", bodyType="Humanoid LARGE", gender='', damage=15, defense=15, firstNameGen='', fullTitle="false", permanentEffects='', meleeIncrease='', spellIncrease='', archeryIncrease='', hatedByEffect='', spellSchools='', inventory = ''):
        super().__init__()

        print("creater inint")

        self.sprite = sprite
        self.name = name
        self.bodyType = bodyType
        self.gender = gender
        self.firstNameGen = firstNameGen
        self.fullTitle = fullTitle
        self.permanentEffects = permanentEffects
        self.meleeIncrease = meleeIncrease
        self.spellIncrease = spellIncrease
        self.archeryIncrease = archeryIncrease
        self.hatedByEffect = hatedByEffect
        self.spellSchools = spellSchools
        self.inventory = inventory

        self.damage = damage
        self.defense = defense

        if ID == "":
            self.ID = name.capitalize()
        else:
            self.ID = ID


    def text(self):
        return f''' 
  "{self.ID}"
  {{
    viewId = {{ "{ self.sprite }" }}
    {'gender = {self.gender}' if self.gender != '' else f'{chr(10)}' }
    attr = {{
      DAMAGE { self.damage }
      DEFENSE { self.defense }
    }}
    body = {{
      type = {self.bodyType}
    }}
    name = {{
      name = "{ self.name }" { 'firstNameGen = "{ self.firstNameGen }"' if self.firstNameGen != '' else f'{chr(10)}' } 
      fullTitle = { self.fullTitle }
     }}
    permanentEffects = {{
      { self.permanentEffects }
    }}
    maxLevelIncrease = {{
      { f'MELEE { self.meleeIncrease }' if self.meleeIncrease != '' else f'{chr(10)}' }
      { f'SPELL { self.spellIncrease }' if self.spellIncrease != '' else f'{chr(10)}' }
      { f'ARCHERY { self.archeryIncrease }' if self.archeryIncrease != '' else f'{chr(10)}'  }
    }}
    {'hatedByEffect = { self.hatedByEffect }' if self.hatedByEffect != '' else f'{chr(10)}' }
    {'spellSchools = {{ { self.spellSchools } }}' if self.spellSchools != '' else f'{chr(10)}' }
    {'inventory = {{ self.inventory }}' if self.inventory != '' else f'{chr(10)}' }
  }}
  '''

  class Var():
      pass


