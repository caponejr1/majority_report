import time, random, os, car_sim_variables


#Define program-wide variables here.
end_dist = 10
speed_1 = 10
speed_2 = 10
road_width = 1
vehiclenum = 2
sleeps = True
debug_mode = False
enable_mods = True

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
    end_dist_pass = False
    speed1_pass = False
    speed2_pass = False
    width_pass = False
    global end_dist
    global speed_1
    global speed_2
    global road_width
    global vehiclenum
    global sleeps
    print("Welcome to the Majority Report Simulation!\n")
    if sleeps == True:
        time.sleep(2)
    #Collects simulation distance
    while end_dist_pass == False:
        try:
            end_dist = int(input("Please input the simulation distance (In Meters): "))
            Car1_table.data["distance"] = end_dist
            AI_table.data["distance"] = end_dist
            break
        except ValueError:
            print("That input is not valid.")
        else:
            end_dist_pass = True
    #Collects vehicle speed
    while speed1_pass == False:
        try:
            speed_1 = int(input("Please input base speed for Vehicle 1 (In MPH): "))
            Car1_table.data["car1_spd"] = speed_1
            AI_table.data["car1_spd"] = speed_1
            break
        except ValueError:
            print("That input is not valid.")
        else:
            speed1_pass = True
    if vehiclenum == 2:
        while speed2_pass == False:
            try:
                speed_2 = int(input("Please input base speed for Vehicle 2 (In MPH): "))
                Car1_table.data["car2_spd"] = speed_2
                AI_table.data["car2_spd"] = speed_2
                break
            except ValueError:
                print("That input is not valid.")
        else:
            speed2_pass = True
    #Collects road width
    while width_pass == False:
        try:
            road_width = int(input("Please input the road width: "))
            Car1_table.data["road_width"] = road_width
            AI_table.data["road_width"] = road_width
            break
        except ValueError:
            print("That input is not valid.")
        else:
            width_pass = True
    print("Great! You are running the simulation with:")
    print("Distance: " + str(end_dist))
    print("Car 1 Speed: " + str(speed_1))
    if vehiclenum == 2:
        print("Car 2 Speed: " + str(speed_2))
    print("Road Width: " + str(road_width) + "\n")
    #Confirms given info
    intro_confirm = input("Is this correct? (Y/N)")
    if intro_confirm == ("N") or intro_confirm == ("n"):
        os.system("cls")
        maj_intro(Car1,Car2)
    else:
        if enable_mods == True:
            print("\n")
            print("Loading Modifier Selection...")
            time.sleep(2)
            car_sim_variables.modifiers_intro(mods)
        print("Great! Running Shortly...")
        
    
    #Define Cars Here
    Car1.set_speed(speed_1)
    Car1.set_start_dist(0)
    Car1.set_end_dist(end_dist)
    
    if vehiclenum == 2:
        Car2.set_speed(-speed_2)
        Car2.set_start_dist(end_dist)
        Car2.set_end_dist(end_dist)
        Car2.set_current_dist(end_dist)
    if sleeps == True:
        time.sleep(2)
        

#Define Classes here.
#Car Class. Contains all the defs and variables needed to simulate the car's movements.
class Car:
    def __init__(self,name,speed):
        pass
        global sleeps
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
        direction_num = random.uniform(1,101)
        return int(direction_num) 
    #Prints the vehicle's current progress
    def print_prog(self):
        if debug_mode == True:
            print(self.temp_dnum)
        print(self.name + " Current Distance: " + str(int(self.current_dist)) + "m" + "/" + str(self.end_dist) + "m")
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
    #Prints the vehicle's orientation on the road
    def print_turndist(self):
        if self.turn_dist == 0:
            print(self.name + " is in the middle of the road.")
        if self.turn_dist > 0:
            print(self.name + " is " + str(self.turn_dist) + " unit(s) to the right.")
        if self.turn_dist < 0:
            print(self.name + " is " + str(abs(self.turn_dist)) + " unit(s) to the left.")
        if debug_mode == True:
            print("rc=" + str(self.rc))
            print("lc=" + str(self.lc))
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
            os.system("cls")
            if self.current_dist > self.start_dist:
                self.direction_choose()
            self.print_prog()
            self.print_turndist()
            if abs(self.turn_dist) >= road_width:
                print("\nThe car has driven off the road!")
                accident = True
                Car1_table.update(car1)
                break
            print("\n")
            if sleeps == True:
                time.sleep(1)
            Car1_table.update(car1)
            self.evaluate_sit()
            self.progress(self.speed)
        if accident == False:
            print("The car reached it's destination!")
            
#AI Class. Contains all defs and variables needed to allow the AI to predict the simulation's outcome.            
class AI(Car):
    def __init__(self,name,power):
        super()
        global sleeps
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
        
    #AI Prints an intro to prepare the simulation portion and collect more variables
    def maj_AI_intro(self):
        global vehiclenum
        if sleeps == True:
            time.sleep(1)
        os.system("cls")
        print("[" + self.name.upper()  + "]" + " is now online.")
        if sleeps == True:
            time.sleep(2)
        if vehiclenum == 1:
            self.install(car1)
            print("\nInitializing prediction with 1 Car Entity")
        if sleeps == True:
            time.sleep(2)
        
       
    #Utility Functions
    #Prints Computing Power
    def print_comp(self):
        print("Computing Power: " + str(self.comp_power))
    #AI Prints the accuracy percentage of it's prediction
    def print_accuracy(self,iteration,Car):
        print("[" + self.name.upper() + "]" + " Accuracy: " + str(int((self.accuracy/iteration)*100)) + "%")
        if self.comp_power == 0:
            print("[" + self.name + "]" + " WARNING: Accident Avoidance Offline")
        if car_ghost.turn_dist != Car.turn_dist:
            print("[" + self.name + "]" + " WARNING: Prediction Accuracy Destabilizing")
        if int((self.accuracy/iteration)*100) <= 50:
            print("[" + self.name + "]" + " WARNING: Prediction Accuracy Below Reliable Standard")
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
    if (Car1.last_dist == Car2.current_dist + (Car2.speed)) and (Car1.turn_dist == Car2.turn_dist) and (Car1.current_dist > 0):
        Car1.rc = 50
        Car1.lc = 50
        car_ghost.rc = 50
        car_ghost.lc = 50
        AI.comp_power = AI.comp_power - 2
        print("[" + AI.name.upper() + "]" + " Accident Avoidance Activated: Car Swerved")
    if (Car1.last_dist > (Car2.current_dist + Car2.speed)) and (Car1.last_dist < Car2.last_dist) and (Car1.turn_dist == Car2.turn_dist) and (Car1.current_dist > 0):
        Car1.rc = 50
        Car1.lc = 50
        car_ghost.rc = 50
        car_ghost.lc = 50
        AI.comp_power = AI.comp_power - 2
        print("[" + AI.name.upper() + "]" + " Accident Avoidance Activated: Car Swerved")
    if (Car1.current_dist == Car2.current_dist - (speed_2*2) and ((Car1.turn_dist == Car2.turn_dist) or ((Car1.turn_dist == Car2.turn_dist - 1) or (Car1.turn_dist == Car2.turn_dist + 1)))) and (abs(Car1.turn_dist) == (road_width - 1)):
        Car1.set_speed(0)
        car_ghost.set_speed(0)
        AI.comp_power = AI.comp_power - 2
        print("[" + AI.name.upper() + "]" + " Accident Avoidance Activated: Car Stopped")
    if ((Car1.current_dist + Car1.speed) > (Car2.current_dist - Car2.speed) and ((Car1.turn_dist == Car2.turn_dist) or ((Car1.turn_dist == Car2.turn_dist - 1) or (Car1.turn_dist == Car2.turn_dist + 1)))) and (Car1.last_dist < Car2.last_dist) and (abs(Car1.turn_dist) == (road_width - 1)):
        Car1.set_speed(0)
        car_ghost.set_speed(0)
        AI.comp_power = AI.comp_power - 2
        print("[" + AI.name.upper() + "]" + " Accident Avoidance Activated: Car Stopped")
    if (Car1.last_dist) > (Car2.current_dist + Car2.speed) and (Car1.last_dist < Car2.last_dist) and (Car1.turn_dist == Car2.turn_dist + 1) and (Car1.current_dist > 0):
        Car1.rc = 100
        Car1.lc = 0
        car_ghost.rc = 100
        car_ghost.lc = 0
        AI.comp_power = AI.comp_power - 2
        print("[" + AI.name.upper() + "]" + " Accident Avoidance Activated: Left Turn Prohibited")
    if (Car1.last_dist) > (Car2.current_dist + Car2.speed) and (Car1.last_dist < Car2.last_dist) and (Car1.turn_dist == Car2.turn_dist - 1) and (Car1.current_dist > 0):
        Car1.rc = 0
        Car1.lc = 100
        car_ghost.rc = 0
        car_ghost.lc = 100
        AI.comp_power = AI.comp_power - 2
        print("[" + AI.name.upper() + "]" + " Accident Avoidance Activated: Right Turn Prohibited")
#Moves two vehicles at the same time, driving towards each other. One car has the AI built in.
def sim_collision(Car1,Car2,AI):
    global sleeps
    accident_1 = False
    accident_2 = False
    iteration = 0
    if enable_mods == True:
        apply_mods(Car1,1)
        apply_mods(Car2,2)
    AI.install(Car1)
    while (Car1.current_dist <= Car1.end_dist) and (Car2.current_dist >= 0):
        os.system("cls")
        if accident_1 == False:
            if AI.comp_power > 0:
                safety_check(Car1,Car2,Skynet)
            if Car1.current_dist > Car1.start_dist and Car1.speed > 0:
                if enable_mods == True:
                    apply_mods(Car1,1)
                Car1.direction_choose()
            if AI.comp_power > 0:
                AI.predict(Car1)
            if Car1.speed > 0:
                car_ghost.direction_choose()
            if AI.comp_power > 0:
                redo(Car1,Car2,AI)
            if iteration > 0:
                AI.check_accuracy(Car1)
                AI.print_accuracy(iteration,Car1)
                AI.print_comp()
            car_ghost.print_prog()
            car_ghost.print_turndist()
            print("\n")
            Car1.print_prog()
            Car1.print_turndist()
        if abs(Car1.turn_dist) >= road_width:
            print("\nCar 1 has driven off the road!")
            accident_1 = True
            break
        if accident_2 == False:
            print("\n")
            if Car1.current_dist > Car1.start_dist:
                if enable_mods == True:
                    apply_mods(Car2,2)
                Car2.direction_choose()
            Car2.print_prog()
            Car2.print_turndist()
        if abs(Car2.turn_dist) >= road_width:
            print("\nCar 2 has driven off the road!")
            accident_2 = True
            break
        if (Car1.current_dist == Car2.current_dist) and (Car1.turn_dist == Car2.turn_dist):
            print("\nCar 1 and Car 2 have collided!")
            accident_1 = True
            accident_2 = True
            break
        if ((Car1.current_dist > Car2.current_dist) and (Car1.last_dist < Car2.last_dist)) and (Car1.turn_dist == Car2.turn_dist):
            print("\nCar 1 and Car 2 have collided!")
            accident_1 = True
            accident_2 = True
            break
        print("\n")
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
        if sleeps == True:
            time.sleep(1.5)
    if accident_1 == False and Car1.speed > 0:
        print("Car 1 reached it's destination!")
    if accident_1 == False and Car1.speed <= 0:
        print("Car 1 pulled over safely!")
    if accident_2 == False:
        print("Car 2 reached it's destination!")
    
#The car crash simulation's code.
def maj_rep_sim(Car1,Car2,AI):
    global vehiclenum
    if vehiclenum == 1:
        Car1.move()
    if vehiclenum == 2:
        sim_collision(Car1,Car2,AI)
    if debug_mode == True:
        print("\n")
        print(mods.modify_choices)
        print("\n")
        print(Car1_table.data)
        print("\n")
        print(Car2_table.data)
        print("\n")
        print(AI_table.data)

#Make function calls here.
mods = car_sim_variables.Mods("sim mods")
car1 = Car("Car 1",0)
car2 = Car("Car 2",0)
car_ghost = Car("Ghost",0)
Skynet = ""
Car1_table = Table("Car 1 Data")
Car2_table = Table("Car 2 Data")
AI_table = Table("Simulation Data")
maj_intro(car1,car2)
if enable_mods == True:
    Skynet = AI(mods.modify_data["computer"]["name"],int(mods.modify_data["computer"]["comp_power"]))
if enable_mods == False:
    Skynet = AI("Skynet",1000)
maj_rep_sim(car1,car2,Skynet)
