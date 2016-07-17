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


with open ('GAME_MASTER_v0_1.protobuf') as  f:
    lines = f.readlines()
    for i in range(0, len(lines)):
        line = lines[i]
        line = lines[i].rstrip()
        line = lines[i].lstrip()
        if line.startswith("Move {"):
            id_ = re.findall('\d+',lines[i + 1])
            id_ = id_[0].rstrip()
            type_ = lines[i+3].split("_TYPE_", 1)
            type_ = type_[1].rstrip()
            power = lines[i +4].split("Power: ", 1)
            power = power[1].rstrip()
            accuracy = lines[i+5].split("AccuracyChance: ", 1)
            accuracy = accuracy[1].rstrip()
            if not lines[i+6].startswith("CriticalChance"):
                critical = 0
            else:
                critical = lines[i+6].split("CriticalChance: ", 1)
                critical = critical[1].rstrip()
                critical = float(critical)
                critical = critical * 100
                critical = str(critical) + "%"

            nameLine = lines[i+9].lstrip()
            if not nameLine.startswith("Vfx"):
                nameLine = lines[i+10].lstrip()
            if not nameLine.startswith("Vfx"):
                nameLine = lines[i+11].lstrip()

            name = re.findall(r'"(.*?)"', nameLine)
            name = name[0].rstrip()
            name = name.split("_fast")
            name = name[0]
            name = name.replace("_", " ")
            print (name + ", " + id_ + ", " + type_ + ", " + str(power) + ", " + critical)
            numMoves += 1
            i += 14

