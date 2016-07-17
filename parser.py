import re


class Attack:
    numAttacks = 0

    def __init__(self, idNum, name, type_, DPS, power, accuracy, critical, 
                 staminaLoss, trainerLevelMin, trainerLevelMax, duration ,
                 damageStartMs, damageEndMs, energyDelta):
        self.idNum = idNum
        self.name = name
        self.type_ = type_
        self.power = power
        self.duration = duration
        self.DPS = (power/duration) * 1000
        self.accuracy = accuracy
        self.critical = critical
        self.staminaLoss = staminaLoss
        self.trainerLevelMin = trainerLevelMin
        self.trainerLevelMax = trainerLevelMax
        self.damageStartMs = damageStartMs
        self.damageEndMs = damageEndMs
        self.energyDelta = energyDelta
        numAttacks += 1

    def toCSV(self):
        return (str(self.idNum) + ", " + str(self.name) + ", " + str(self.type_) + ", " + 
        str(self.power) + ", " + str(self.duration) + ", " + str(self.DPS) + ", " + 
        str(self.accuracy) + ", " + str(self.critical) + ", " + (self.staminaLoss) + ", " + 
        str(self.trainerLevelMin) + ", " + str(self.trainerLevelMax) + ", " + 
        str(self.damageStartMs) + ", " + str(self.damageEndMs) + ", " + str(self.energyDelta)) 

numMoves = 1

idNum = 0
id_ = None
name = None
type_ = None
power = None
powerFl = 0
critical = None
accuracy = None
durationFl = 0
duration = None
dps = None
energyDelta = None

with open ('GAME_MASTER_noSplash.protobuf') as  f:
    lines = f.readlines()
    for i in range(0, len(lines)):
        line = lines[i].lstrip()
        if line.startswith("Move {"):
            line = lines[i].lstrip()
            while not line.startswith("}"):
                lines[i] = lines[i].lstrip()
                if lines[i].startswith("UniqueId:"):
                    id_ = re.findall('\d+',lines[i])
                    id_ = id_[0].rstrip()
                    id_ = str(id_)
                    line = lines[i+1].lstrip()
                    i += 1
                    continue

                if lines[i].startswith("Type:"):
                    type_ = lines[i].split("_TYPE_", 1)
                    type_ = type_[1].rstrip()
                    line = lines[i+1].lstrip()
                    i += 1
                    continue

                if lines[i].startswith("Power:"):
                    power = lines[i].split("Power: ", 1)
                    power = power[1].rstrip()
                    powerFl = float(power)
                    power = str(power)
                    line = lines[i+1].lstrip()
                    i += 1
                    continue
                if lines[i].startswith("Accuracy"):
                    accuracy = lines[i].split("AccuracyChance: ", 1)
                    accuracy = accuracy[1].rstrip()
                    accuracy = float(accuracy)
                    accuracy = accuracy * 100
                    accuracy = str(accuracy) + "%"
                    line = lines[i+1].lstrip()
                    i += 1 
                    continue

                if lines[i].startswith("CriticalChance: "):
                    critical = lines[i].split("CriticalChance: ", 1)
                    critical = critical[1].rstrip()
                    critical = float(critical)
                    critical = critical * 100
                    critical = str(critical) + "%"  
                    line = lines[i+1].lstrip()
                    i += 1 
                    continue  

                if lines[i].startswith("Vfx"):
                    name = re.findall(r'"(.*?)"', lines[i])
                    name = name[0].rstrip()
                    name = name.split("_fast")
                    name = name[0]
                    name = name.replace("_", " ")
                    name = str(name)
                    line = lines[i+1].lstrip()
                    i += 1
                    continue

                if lines[i].startswith("DurationMs: "):
                    duration = re.findall('\d+', lines[i])
                    duration = duration[0].rstrip()
                    durationFl = float(duration)
                    duration = str(duration)
                    line = lines[i+1].lstrip()
                    i += 1
                    continue
                if lines[i].startswith("Energy"):
                    energyDelta = lines[i].split("EnergyDelta: ", 1)
                    energyDelta = energyDelta[1].rstrip()
                    energyDelta = float(energyDelta)
                    energyDelta = str(energyDelta)
                    line = lines[i+1].lstrip()
                    i += 1 
                    continue

                line = lines[i+1].lstrip()    
                i += 1 
            dps =  (powerFl / durationFl) * 1000
            dps = "{0:.5f}".format(dps)
            print (name + ", " + id_ + ", " + type_ + ", " + power + ", " + duration + ", " + dps + ", " + critical + ", " + accuracy + ", " + energyDelta)
            numMoves += 1

