###Imports###
from ast import literal_eval

###Files###
import EffectsPP.ParserCode.compileCode as compileCode


class Parse():
    def __init__(self):
        super().__init__()
        self.funcList = ['new', '=']
        self.var = {"Null":None}
        self.DiffCall = {'=': "equal"}

    def useVars(self, perams):
        return str(tuple(perams[1:-1].split(",")))

    def equal(self, line, i):
        self.setVar(line[i-1], line[i+1])
        return i+2

    def setVar(self, varName, varValue):
        self.var[varName] = varValue    

    def new(self, line, i):
        if line[i + 1][:8] == "Creature":
            print(line[i+1][8:])
            creature = eval("Creature" + self.useVars(line[i+1][8:]))
            compileCode.write(creature.text())
            return i+2

        compileCode.error(f'''Imporper New Value on line: 
        {" ".join(line)}''')


class Creature():
    def __init__(self, name="template", sprite = "", ID="", damage=15, defense=15, bodyType="Humanoid LARGE", gender='', firstNameGen='', fullTitle="false", permanentEffects='', meleeIncrease='', spellIncrease='', archeryIncrease='', hatedByEffect='', spellSchools='', inventory=''):
        super().__init__()

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

        if sprite == "":
            self.sprite = name.lower()
        else:
            self.sprite = sprite


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

        

