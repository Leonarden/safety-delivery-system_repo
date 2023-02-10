#module: safety-delivery-system
#imports: typing-3.7.4.3
from typing import List,Dict

"""
"""
#classes:
#part 1

class SafetyKitItemType:
    """
     SafetyKitItemType given by name, description
     ie: name="medicine" or name="medical-hardware" or name="food"
    """
    nInstances = 0

    def __init__(self,id:int,name:str, description:str):
        self.id = id
        self.name = name
        self.description = description
        self.nInstances = self.nInstances + 1

    def __del__(self):
        self.nInstances = self.nInstances - 1

class SafetyKitItem:
    """
    SafetyKitItem
    """
    nInstances = 0

    def __init__(self,id:int,name:str, description:str, safetyKitItemType:SafetyKitItemType):
        self.id = id
        self.name = name
        self.description = description
        self.safetyKitItemType = safetyKitItemType
        self.nInstances = self.nInstances + 1

    def __del__(self):
        self.nInstances = self.nInstances - 1

class Medicine(SafetyKitItem):
    """
    Medicines ie: anti-biotic, aspirine...
    """
    nInstances = 0

    def __init__(self,id:int,name:str,description:str,safetyKitItemType:SafetyKitItemType,composition:str,warning:int):
        super().__init__(id,name,description,safetyKitItemType)
        self.composition = composition
        self.warning = warning #flag indicating if 0-no toxic, 1-small toxicity, ...5-Very toxic
        self.nInstances = self.nInstances + 1

    def __del__(self):
        self.nInstances = self.nInstances - 1


class MedicalHardware(SafetyKitItem):
    """
    Plaster, Cotton, Tape, alcohol, injections
    """
    nInstances = 0

    def __init__(self,id:int,name:str,description:str,safetyKitItemType:SafetyKitItemType,composition:str,characteristics:str,warning:int):
        super().__init__(id,name,description,safetyKitItemType)
        self.characteristics = characteristics
        self.warning = warning #flag indicating if 0-no danger, 1-small danger, ...5-Very dangerous
        self.nInstances = self.nInstances + 1

    def __del__(self):
        self.nInstances = self.nInstances - 1


class Food(SafetyKitItem):
    """
    Condensed Milk, Sardines, Dry Meat, Water...
    """
    nInstances = 0

    def __init__(self,id:int,name:str,description:str,safetyKitItemType:SafetyKitItemType,composition:str,nutritionalProperties:str,warning:int):
        super().__init__(id,name,description,safetyKitItemType)
        self.nutritionalProperties = nutritionalProperties # could be basic: just Kcals or extended
        self.warning = warning #flag indicating if 0-no danger, 1-small danger, ...5-Very dangerous
        self.nInstances = self.nInstances + 1

    def __del__(self):
        self.nInstances = self.nInstances - 1

class SafetyKitItemProperty:
    """
    safety kit item property (name,description), support of different languages?
    """
    nInstances = 0

    def __init__(self,id:int,name:str,description:str,language:str):
        self.id = id
        self.name = name
        self.description = description
        self.language = language
        self.nInstances = self.nInstances + 1

    def __del__(self):
        self.nInstances = self.nInstances - 1

class IllnessCategory:
    """
     medical illness category
    """
    nInstances = 0

    def __init__(self,id:int,name:str,description:str):
        self.id = id
        self.name = name
        self.description = description
        self.language = language
        self.nInstances = self.nInstances + 1

    def __del__(self):
        self.nInstances = self.nInstances - 1

class IllnessProperty:
    """
     medical illness property (name, description, illnessCategory, language)
    """
    nInstances = 0

    def __init__(self,id:int,name:str,description:str,illnessCategory:IllnessCategory,language:str):
        self.id = id
        self.name = name
        self.description = description
        self.language = language
        self.illnessCategory = illnessCategory
        self.nInstances = self.nInstances + 1

    def __del__(self):
        self.nInstances = self.nInstances - 1

class SafetyKitItemInstruction:
    """
    Instruction (of use) of a SafetyKitItem
    """
    nInstances = 0

    def __init__(self,id:int,name:str,description:str,maxdosage:float,mindosage:float,posology:float,safetyKitItemProperty:SafetyKitItemProperty, safetyKitItemProperties: List["SafetyKitItemProperty"], illnessProperties:List["IllnessProperty"], language:str):
        self.id = id
        self.name = name
        self.description = description
        self.maxdosage = maxdosage
        self.mindosage = mindosage
        self.posology = posology
        self.references = safetyKitItemProperty
        self.incompatibilities = safetyKitItemProperties
        self.illnesses = illnessProperties
        self.language = language
        self.nInstances = self.nInstances + 1

    def __del__(self):
        self.nInstances = self.nInstances - 1

class SafetyKitInstructions:
    """
    SafetyKitInstructions : Usage Instructions
    """
    nInstances = 0

    def __init__(self,id:int,name:str,description:str,safetyKitItemInstructions:List["SafetyKitItemInstruction"],language:str):
        self.id = id
        self.name = name
        self.description = description
        self.safetyKitItemInstructions = safetyKitItemInstructions
        self.language = language
        self.nInstances = self.nInstances + 1

    def __del__(self):
        self.nInstances = self.nInstances - 1

class SafetyKitTypeSpecification:
    """
    What has been specified-standariced for each SafetyKitType in terms of:
    avgWeight, avgCost and
    safetyKitItemTypes composition,
    ie. if ItemTypes are:['meds','hardware','food'] then attribute itemTypesPercentages will consist on [%meds,%hw,%food]
    """
    nInstances = 0

    def __init__(self,id:int,name:str, description:str, avgWeight:float, avgCost:float, itemTypesPercentages:List["float"]):
        self.id = id
        self.name = name
        self.description = description
        self.avgWeight = avgWeight
        self.avgCost = avgCost
        self.itemTypesPercentages = itemTypesPercentages # ie: [0.6,0.3,0.1] = 60% of meds, 30% med-hw, 10% food
        self.nInstances = self.nInstances + 1

    def __del__(self):
        self.nInstances = self.nInstances - 1


class SafetyKitType:
    """
     SafetyKitType given by: name, description and following a SafetyKitTypeSpecification
    """
    nInstances = 0

    def __init__(self,id:int,name:str, description:str, safetyKitTypeSpecification:SafetyKitTypeSpecification):
        self.id = id
        self.name = name
        self.description = description
        self.safetyKitTypeSpecification = safetyKitTypeSpecification
        self.nInstances = self.nInstances + 1

    def __del__(self):
        self.nInstances = self.nInstances - 1

class SafetyKit:
    """
    SafetyKit has name, description and type
    holds SafetyKitItems as  medicine,  medical hardware, food
    holds
    """
    nInstances = 0

    def __init__(self,id:int,name:str,description:str, safetyKitType:SafetyKitType, safetyKitItems:List["SafetyKitItems"], safetyKitInstructions:SafetyKitInstructions):
        self.id = id
        self.name = name
        self.description = description
        self.safetyKitType = safetyKitType
        self.safetyKitItems = safetyKitItems
        self.safetyKitInstructions = safetyKitInstructions
        self.nInstances = self.nInstances + 1

    def __del__(self):
        self.nInstances = self.nInstances - 1
#part 2

class Pack:
    """
    Base class for  safety kit packs
    """
    nInstances = 0

    def __init__(self,id:int,name:str,description:str, weight:float,volume:float):
        self.id = id
        self.name = name
        self.description = description
        self.weight = weight
        self.volume = volume
        self.nInstances = self.nInstances + 1

    def __del__(self):
        self.nInstances = self.nInstances - 1

class SafetyKitPackCategory:
    """
    Pack category ie: XLarge, Large, Medium, Small ,
    has characteristics a Dict : average cost, average weight...
    has subcategory XLarge-MedsOnly, Medium-Equivalence, XLarge-FoodOnly
    """
    nInstances = 0

    def __init__(self,id:int, name:str, characteristics:Dict,safetyKitPackCategory):
        self.id = id
        self.name = name
        self.characteristics = characteristics
        self.packSubcategory = safetyKitPackCategory
        self.nInstances = self.nInstances + 1

    def __del__(self):
        self.nInstances = self.nInstances - 1

class SafetyKitPack(Pack):
    """
    Holds  safetykits,
    has a safetyKitPack category
    """
    nInstances = 0

    def __init__(self,id,name,description, weight,volume, safetyKits:List["SafetyKit"], safetyKitPackCategory:SafetyKitPackCategory):
        super().__init__(id,name,description, weight,volume)
        self.safetyKits = safetyKits
        self.safetyKitPackCategory = safetyKitPackCategory
        self.nInstances = self.nInstances + 1

    def __del__(self):
        self.nInstances = self.nInstances - 1

class Inventory:
    """
    Manages hangar's inventory
    """
    nInstances = 0

    def __init__(self, id:int, name:str,description:str, type:int, hangar, characteristics:Dict):
        self.id = id
        self.name = name
        self.description = description
        self.type = type
        self.characteristics = characteristics
        self.hangar = hangar
        self.nInstances = self.nInstances + 1

    def __del__(self):
        self.nInstances = self.nInstances - 1
#Todo: refactor Hangar class
class Hangar:
    """
    Stores SafetyKitPacks
    """
    nInstances = 0

    def __init__(self,id:int,name:str,description:str,city:str, latitude:float, longitude:float,safetyKitPacks:List["SafetyKitPack"],totalCapacity:float,priority:int,characteristics:Dict, inventory:Inventory):
        self.id = id
        self.name = name
        self.description = description
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
        self.safetyKitPacks = safetyKitPacks
        self.totalCapacity = totalCapacity
        self.priority = priority
        self.characteristics = characteristics
        self.inventory = inventory
        self.nInstances = self.nInstances + 1

    def __del__(self):
        self.nInstances = self.nInstances - 1
