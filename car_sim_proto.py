
# Create your views here.
import random, car_sim_variables


#Define program-wide variables here.
end_dist = 10
speed_1 = 10
speed_2 = 10
road_width = 1

#Collects data from the simulation
class Table:
    def __init__(self,name):
        self.name = name
        self.data = {
            
        }
        self.iteration = 0
    #Update table with iteration data (One car)
    def update(self,car):
        self.data["iteration" + str(self.iteration)] = {}
        self.data["iteration" + str(self.iteration)][car.get_name() + "_prog"] = str(car.current_dist)
        self.data["iteration" + str(self.iteration)][car.get_name() + "_turndist"] = str(car.turn_dist)
        self.iteration = self.iteration + 1
    #Update table with iteration data (Two cars)
    def update_v2(self,car,car2):
        #Update table with data from Car 1
        self.data["iteration" + str(self.iteration)] = {}
        self.data["iteration" + str(self.iteration)][car.get_name() + "_prog"] = str(car.current_dist)
        self.data["iteration" + str(self.iteration)][car.get_name() + "_turndist"] = str(car.turn_dist)
        #Update table with data from Car 2
        self.data["iteration" + str(self.iteration)][car2.get_name() + "_prog"] = str(car2.current_dist)
        self.data["iteration" + str(self.iteration)][car2.get_name() + "_turndist"] = str(car2.turn_dist)
        self.iteration = self.iteration + 1
    #Return car's turn distance for any given iteration
    def get_turndist(self,car,iteration):
        return int(self.data["iteration" + str(iteration)][car.get_name() + "_turndist"])
    
#Prints an intro to the program and collects independent variables.
def maj_intro(Car1,Car2):
    global end_dist
    global speed_1
    global speed_2
    global road_width
    end_dist = 10000
    speed_1 = 70
    speed_2 = 70
    road_width = 3
    #Collects simulation distance
    sim_table.data["distance"] = end_dist
    #Collects vehicle speed
    sim_table.data["car1_spd"] = speed_1
    sim_table.data["car2_spd"] = speed_2
    #Collects road width
    sim_table.data["road_width"] = road_width
    #Initializes Variables
    car_sim_variables.modifiers_intro(mods)
        
    
    #Define Cars Here
    Car1.set_speed(speed_1)
    Car1.set_start_dist(0)
    Car1.set_end_dist(end_dist)
    
    Car2.set_speed(-speed_2)
    Car2.set_start_dist(end_dist)
    Car2.set_end_dist(end_dist)
    Car2.set_current_dist(end_dist)
        

#Define Classes here.
#Car Class. Contains all the defs and variables needed to simulate the car's movements.
class Car:
    def __init__(self,name,speed):
        pass
        self.name = name
        self.speed = speed
        self.original_speed = 0
        self.start_dist = 0
        self.end_dist = 0
        self.rc = 10.0
        self.lc = 10.0
        self.original_rc = 10.0
        self.original_lc = 10.0
        self.turn_dist = 0
        self.current_dist = 0
        self.last_dist = 0
        self.temp_dnum = 0
    #Define all variables
    def set_name(self,name):
        self.name = name
    def get_name(self):
        return self.name
    def set_speed(self,speed):
        self.speed = speed
        self.original_speed = speed
    def set_start_dist(self,dist):
        self.start_dist = dist
    def set_end_dist(self,dist):
        self.end_dist = dist
    def set_current_dist(self,dist):
        self.current_dist = dist
    def set_rc(self,chance):
        self.rc = chance
        self.original_rc = chance
    def set_lc(self,chance):
        self.lc = chance
        self.original_lc = chance
    def set_turn_dist(self,dist):
        self.turn_dist = dist
    def set_last_turn_dist(self,dist):
        self.last_turn_dist = dist
    #Distance is divided by 2.237 to convert MPH to M/s
    def progress(self,dist):
        self.last_dist = self.current_dist
        self.current_dist = self.current_dist + (dist/2.237)
    
    #Utility Functions
    #Returns random int from 0-100
    def direction_num(self):
        direction_num = random.randint(1,101)
        return int(direction_num)
    #Performs rolls for direction
    def direction_choose(self):
        self.set_last_turn_dist(self.turn_dist)
        direction = ''
        self.temp_dnum = self.direction_num()
        if self.temp_dnum <= self.rc:
            self.turn_dist = self.turn_dist + 1
            direction = 'right'
        if self.temp_dnum > self.rc and self.temp_dnum <= self.rc + self.lc:
            self.turn_dist = self.turn_dist - 1
            direction = 'left'
    #Car adjusts turn chances based on situation
    def evaluate_sit(self):
        #Reset chances during normal situations
        self.rc = self.original_rc
        self.lc = self.original_lc
        #Reset speed during normal situations
        self.speed = self.original_speed
        #Avoid turning off the road
        if self.turn_dist == road_width - 1:
            self.rc = 0
            self.lc = 75
        if self.turn_dist == -(road_width) + 1:
            self.rc = 75
            self.lc = 0
        if road_width == 1:
            self.rc = 0
            self.lc = 0
#Applies modifiers from car_sim_variables
def apply_mods(Car,Carnum):
    #Weather
    Car.rc = Car.rc*float((mods.modify_data["weather"][mods.modify_choices["weather"]]["turn_mod"]))
    Car.lc = Car.lc*float((mods.modify_data["weather"][mods.modify_choices["weather"]]["turn_mod"]))
    Car.speed = Car.speed*float((mods.modify_data["weather"][mods.modify_choices["weather"]]["speed_mod"]))
    #Time
    Car.rc = Car.rc*float((mods.modify_data["time"][mods.modify_choices["time"]]["turn_mod"]))
    Car.lc = Car.lc*float((mods.modify_data["time"][mods.modify_choices["time"]]["turn_mod"]))
    Car.speed = Car.speed*float((mods.modify_data["time"][mods.modify_choices["time"]]["speed_mod"]))
    #Road Type
    Car.rc = Car.rc*float((mods.modify_data["road_type"][mods.modify_choices["road_type"]]["turn_mod"]))
    Car.lc = Car.lc*float((mods.modify_data["road_type"][mods.modify_choices["road_type"]]["turn_mod"]))
    Car.speed = Car.speed*float((mods.modify_data["road_type"][mods.modify_choices["road_type"]]["speed_mod"]))
    #Driver Experience
    if Carnum == 1:
        Car.rc = Car.rc*float((mods.modify_data["driver"]["experience"][mods.modify_choices["driver_experience1"]]["turn_mod"]))
        Car.lc = Car.lc*float((mods.modify_data["driver"]["experience"][mods.modify_choices["driver_experience1"]]["turn_mod"]))
        Car.speed = Car.speed*float((mods.modify_data["driver"]["experience"][mods.modify_choices["driver_experience1"]]["speed_mod"]))
    if Carnum == 2:
        Car.rc = Car.rc*float((mods.modify_data["driver"]["experience"][mods.modify_choices["driver_experience2"]]["turn_mod"]))
        Car.lc = Car.lc*float((mods.modify_data["driver"]["experience"][mods.modify_choices["driver_experience2"]]["turn_mod"]))
        Car.speed = Car.speed*float((mods.modify_data["driver"]["experience"][mods.modify_choices["driver_experience2"]]["speed_mod"]))
    #Chemical Influence
    if Carnum == 1:
        Car.rc = Car.rc*float((mods.modify_data["driver"]["dui"][mods.modify_choices["chemical_influence1"]]["turn_mod"]))
        Car.lc = Car.lc*float((mods.modify_data["driver"]["dui"][mods.modify_choices["chemical_influence1"]]["turn_mod"]))
        Car.speed = Car.speed*float((mods.modify_data["driver"]["dui"][mods.modify_choices["chemical_influence1"]]["speed_mod"]))
    if Carnum == 2:
        Car.rc = Car.rc*float((mods.modify_data["driver"]["dui"][mods.modify_choices["chemical_influence2"]]["turn_mod"]))
        Car.lc = Car.lc*float((mods.modify_data["driver"]["dui"][mods.modify_choices["chemical_influence2"]]["turn_mod"]))
        Car.speed = Car.speed*float((mods.modify_data["driver"]["dui"][mods.modify_choices["chemical_influence2"]]["speed_mod"]))
    #Vision
    if Carnum == 1:
        Car.rc = Car.rc*float((mods.modify_data["driver"]["vision"][mods.modify_choices["vision1"]]["turn_mod"]))
        Car.lc = Car.lc*float((mods.modify_data["driver"]["vision"][mods.modify_choices["vision1"]]["turn_mod"]))
        Car.speed = Car.speed*float((mods.modify_data["driver"]["vision"][mods.modify_choices["vision1"]]["speed_mod"]))
    if Carnum == 2:
        Car.rc = Car.rc*float((mods.modify_data["driver"]["vision"][mods.modify_choices["vision2"]]["turn_mod"]))
        Car.lc = Car.lc*float((mods.modify_data["driver"]["vision"][mods.modify_choices["vision2"]]["turn_mod"]))
        Car.speed = Car.speed*float((mods.modify_data["driver"]["vision"][mods.modify_choices["vision2"]]["speed_mod"]))
    #Age
    if Carnum == 1:
        Car.rc = Car.rc*float((mods.modify_data["driver"]["age"][mods.modify_choices["age1"]]["turn_mod"]))
        Car.lc = Car.lc*float((mods.modify_data["driver"]["age"][mods.modify_choices["age1"]]["turn_mod"]))
        Car.speed = Car.speed*float((mods.modify_data["driver"]["age"][mods.modify_choices["age1"]]["speed_mod"]))
    if Carnum == 2:
        Car.rc = Car.rc*float((mods.modify_data["driver"]["age"][mods.modify_choices["age2"]]["turn_mod"]))
        Car.lc = Car.lc*float((mods.modify_data["driver"]["age"][mods.modify_choices["age2"]]["turn_mod"]))
        Car.speed = Car.speed*float((mods.modify_data["driver"]["age"][mods.modify_choices["age2"]]["speed_mod"]))
    #Vehicle
    if Carnum == 1:
        Car.rc = Car.rc*float((mods.modify_data["vehicle"][mods.modify_choices["vehicle1"]]["turn_mod"]))
        Car.lc = Car.lc*float((mods.modify_data["vehicle"][mods.modify_choices["vehicle1"]]["turn_mod"]))
        Car.speed = Car.speed*float((mods.modify_data["vehicle"][mods.modify_choices["vehicle1"]]["speed_mod"]))
    if Carnum == 2:
        Car.rc = Car.rc*float((mods.modify_data["vehicle"][mods.modify_choices["vehicle2"]]["turn_mod"]))
        Car.lc = Car.lc*float((mods.modify_data["vehicle"][mods.modify_choices["vehicle2"]]["turn_mod"]))
        Car.speed = Car.speed*float((mods.modify_data["vehicle"][mods.modify_choices["vehicle2"]]["speed_mod"]))
    
    #Moves the vehicle for the distance of the simulation, performing rolls along the way
    def move(self):
        accident = False
        while self.current_dist <= self.end_dist:
            if self.current_dist > self.start_dist:
                self.direction_choose()
            self.print_prog()
            self.print_turndist()
            if abs(self.turn_dist) >= road_width:
                accident = True
                Car1_table.update(car1)
                break
            Car1_table.update(car1)
            self.evaluate_sit()
            self.progress(self.speed)
            
#AI Class. Contains all defs and variables needed to allow the AI to predict the simulation's outcome.            
class AI(Car):
    def __init__(self,name,power):
        super()
        self.accident = False
        self.name = name
        self.comp_power = power
        self.original_power = power
        self.rc = 10
        self.lc = 10
        self.accuracy = 0
    #Variable defs
    def set_name(self,name):
        self.name = name
    def set_power(self,power):
        self.comp_power = power
    def get_name(self):
        return self.name
    def get_power(self):
        return self.comp_power
    def reset_power(self):
        self.comp_power = self.original_power
        
    #Utility Functions
    #AI Updates Accuracy value
    def check_accuracy(self,car):
        if car_ghost.turn_dist == car.turn_dist:
            self.accuracy = self.accuracy + 1
    #AI creates a "Ghost" of target car that it can use in the predicition
    def install(self,car):
        car_ghost.set_current_dist(car.start_dist)
        car_ghost.set_turn_dist(0)
        car_ghost.set_end_dist(end_dist)
        car_ghost.set_speed(car.speed)
    #AI uses comp_power to predict potential paths and decide the best option
    def predict(self,car):
        if car_ghost.turn_dist > car.turn_dist:
            car_ghost.rc = 0
            car_ghost.lc = car_ghost.lc + 0.5
            self.comp_power = self.comp_power - 1
        if car_ghost.turn_dist == car.turn_dist:
            car_ghost.rc = 10
            car_ghost.lc = 10
            self.comp_power = self.comp_power - 1
        if car_ghost.turn_dist < car.turn_dist:
            car_ghost.rc = car_ghost.rc + 0.5
            car_ghost.lc = 0
            self.comp_power = self.comp_power - 1
#AI uses revert() to run a different outcome of the simulation
def redo(Car1,Car2,AI):
    if AI.comp_power > 0 and car_ghost.turn_dist != Car1.turn_dist:
        car_ghost.set_turn_dist(car_ghost.last_turn_dist)
        AI.comp_power = AI.comp_power - 1
        if AI.comp_power > 0:
            safety_check(Car1,Car2,Skynet)
        if AI.comp_power > 0:
            AI.predict(Car1)
        car_ghost.direction_choose()
        redo(Car1,Car2,AI)
#AI avoids accidents by swerving or stopping
def safety_check(Car1,Car2,AI):
    #Swerve
    if (Car1.last_dist == Car2.current_dist + (Car2.speed)) and (Car1.turn_dist == Car2.turn_dist) and (Car1.current_dist > 0):
        Car1.rc = 50
        Car1.lc = 50
        car_ghost.rc = 50
        car_ghost.lc = 50
        AI.comp_power = AI.comp_power - 2
    if (Car1.last_dist > (Car2.current_dist + Car2.speed)) and (Car1.last_dist < Car2.last_dist) and (Car1.turn_dist == Car2.turn_dist) and (Car1.current_dist > 0):
        Car1.rc = 50
        Car1.lc = 50
        car_ghost.rc = 50
        car_ghost.lc = 50
        AI.comp_power = AI.comp_power - 2
    #Stop
    if (Car1.current_dist == Car2.current_dist - (speed_2*2) and ((Car1.turn_dist == Car2.turn_dist) or ((Car1.turn_dist == Car2.turn_dist - 1) or (Car1.turn_dist == Car2.turn_dist + 1)))) and (abs(Car1.turn_dist) == (road_width - 1)):
        Car1.set_speed(0)
        car_ghost.set_speed(0)
        AI.comp_power = AI.comp_power - 2
    if ((Car1.current_dist + Car1.speed) > (Car2.current_dist - Car2.speed) and ((Car1.turn_dist == Car2.turn_dist) or ((Car1.turn_dist == Car2.turn_dist - 1) or (Car1.turn_dist == Car2.turn_dist + 1)))) and (Car1.last_dist < Car2.last_dist) and (abs(Car1.turn_dist) == (road_width - 1)):
        Car1.set_speed(0)
        car_ghost.set_speed(0)
        AI.comp_power = AI.comp_power - 2
    #Prohibit Turn
    if (Car1.last_dist) > (Car2.current_dist + Car2.speed) and (Car1.last_dist < Car2.last_dist) and (Car1.turn_dist == Car2.turn_dist + 1) and (Car1.current_dist > 0):
        Car1.rc = 100
        Car1.lc = 0
        car_ghost.rc = 100
        car_ghost.lc = 0
        AI.comp_power = AI.comp_power - 2
    if (Car1.last_dist) > (Car2.current_dist + Car2.speed) and (Car1.last_dist < Car2.last_dist) and (Car1.turn_dist == Car2.turn_dist - 1) and (Car1.current_dist > 0):
        Car1.rc = 0
        Car1.lc = 100
        car_ghost.rc = 0
        car_ghost.lc = 100
        AI.comp_power = AI.comp_power - 2
#Moves two vehicles at the same time, driving towards each other. One car has the AI built in.
def sim_collision(Car1,Car2,AI):
    accident_1 = False
    accident_2 = False
    iteration = 0
    apply_mods(Car1,1)
    apply_mods(Car2,2)
    AI.install(Car1)
    while (Car1.current_dist <= Car1.end_dist) and (Car2.current_dist >= 0):
        if accident_1 == False:
            if AI.comp_power > 0:
                safety_check(Car1,Car2,Skynet)
            if Car1.current_dist > Car1.start_dist and Car1.speed > 0:
                apply_mods(Car1,1)
                Car1.direction_choose()
            if AI.comp_power > 0:
                AI.predict(Car1)
            if Car1.speed > 0:
                car_ghost.direction_choose()
            if AI.comp_power > 0:
                redo(Car1,Car2,AI)
            AI.check_accuracy(Car1)
        if abs(Car1.turn_dist) >= road_width:
            accident_1 = True
            break
        if accident_2 == False:
            if Car1.current_dist > Car1.start_dist:
                apply_mods(Car2,2)
                Car2.direction_choose()
        if abs(Car2.turn_dist) >= road_width:
            accident_2 = True
            break
        if (Car1.current_dist == Car2.current_dist) and (Car1.turn_dist == Car2.turn_dist):
            accident_1 = True
            accident_2 = True
            break
        if ((Car1.current_dist > Car2.current_dist) and (Car1.last_dist < Car2.last_dist)) and (Car1.turn_dist == Car2.turn_dist):
            accident_1 = True
            accident_2 = True
            break
        Car1_table.update(Car1)
        Car2_table.update(Car2)
        AI_table.update(car_ghost)
        car_ghost.evaluate_sit()
        Car1.progress(Car1.speed)
        Car2.progress(Car2.speed)
        car_ghost.progress(car_ghost.speed)
        Car1.evaluate_sit()
        Car2.evaluate_sit()
        iteration = iteration + 1
    Car1_table.update(Car1)
    Car2_table.update(Car2)
    AI_table.update(car_ghost)
    sim_table.data["accuracy"] = str(int((AI.accuracy/iteration)*100)) + "%"
    if accident_1 == False and accident_2 == False:
        sim_table.data["outcome"] = "success"
    else:
        sim_table.data["outcome"] = "failure"
    print(Car1_table.data)
    print("\n")
    print(Car2_table.data)
    print("\n")
    print(AI_table.data)
    print("\n")
    print(sim_table.data)

#Make function calls here.
mods = car_sim_variables.Mods("sim mods")
car1 = Car("Car 1",0)
car2 = Car("Car 2",0)
car_ghost = Car("Ghost",0)
sim_table = Table("Sim Table")
Car1_table = Table("Car 1 Data")
Car2_table = Table("Car 2 Data")
AI_table = Table("Simulation Data")
maj_intro(car1,car2)
Skynet = AI(mods.modify_data["computer"]["name"],int(mods.modify_data["computer"]["comp_power"]))
sim_collision(car1,car2,Skynet)