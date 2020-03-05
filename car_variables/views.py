
import car_variables.choices as cv

class Mods:
    
    def __init__(self):
    
        self.modify_choices = {
            
        }
        self.modify_choices["weather"] = ""
        self.modify_choices["time"] = ""
        self.modify_choices["road_type"] = ""
        self.modify_choices["driver_experience1"] = ""
        self.modify_choices["driver_experience2"] = ""
        self.modify_choices["chemical_influence1"] = ""
        self.modify_choices["chemical_influence2"] = ""
        self.modify_choices["vision1"] = ""
        self.modify_choices["vision2"] = ""
        self.modify_choices["age1"] = ""
        self.modify_choices["age2"] = ""
        self.modify_choices["vehicle1"] = ""
        self.modify_choices["vehicle2"] = ""
        self.modify_choices["computer"] = ""
        
        self.modify_data = {
        
        }
        #WEATHER   
        self.modify_data["weather"] = {}
    
        self.modify_data["weather"]["clear"] = {}
        self.modify_data["weather"]["clear"]["turn_mod"] = "1"
        self.modify_data["weather"]["clear"]["speed_mod"] = "1"
    
        self.modify_data["weather"]["rain"] = {}
        self.modify_data["weather"]["rain"]["turn_mod"] = "1.2"
        self.modify_data["weather"]["rain"]["speed_mod"] = "1.1"
    
        self.modify_data["weather"]["snow"] = {}
        self.modify_data["weather"]["snow"]["turn_mod"] = "0.9"
        self.modify_data["weather"]["snow"]["speed_mod"] = "0.8"
    
        self.modify_data["weather"]["ice"] = {}
        self.modify_data["weather"]["ice"]["turn_mod"] = "1.4"
        self.modify_data["weather"]["ice"]["speed_mod"] = "1.2"
    
        self.modify_data["weather"]["fog"] = {}
        self.modify_data["weather"]["fog"]["turn_mod"] = "1.1"
        self.modify_data["weather"]["fog"]["speed_mod"] = "0.9"
    
        self.modify_data["weather"]["wind"] = {}
        self.modify_data["weather"]["wind"]["turn_mod"] = "1.2"
        self.modify_data["weather"]["wind"]["speed_mod"] = "0.9"
    
        #TIME
        self.modify_data["time"] = {}
    
        self.modify_data["time"]["morning"] = {}
        self.modify_data["time"]["morning"]["turn_mod"] = "1.1"
        self.modify_data["time"]["morning"]["speed_mod"] = "1.1"
    
        self.modify_data["time"]["noon"] = {}
        self.modify_data["time"]["noon"]["turn_mod"] = "1"
        self.modify_data["time"]["noon"]["speed_mod"] = "1"
    
        self.modify_data["time"]["evening"] = {}
        self.modify_data["time"]["evening"]["turn_mod"] = "1.2"
        self.modify_data["time"]["evening"]["speed_mod"] = "1.2"
    
        self.modify_data["time"]["night"] = {}
        self.modify_data["time"]["night"]["turn_mod"] = "1.4"
        self.modify_data["time"]["night"]["speed_mod"] = "0.9"
    
        #ROAD CONDITION
        self.modify_data["road_type"] = {}
    
        self.modify_data["road_type"]["dirt"] = {}
        self.modify_data["road_type"]["dirt"]["turn_mod"] = "0.8"
        self.modify_data["road_type"]["dirt"]["speed_mod"] = "1"
    
        self.modify_data["road_type"]["gravel"] = {}
        self.modify_data["road_type"]["gravel"]["turn_mod"] = "0.9"
        self.modify_data["road_type"]["gravel"]["speed_mod"] = "0.9"
    
        self.modify_data["road_type"]["asphalt"] = {}
        self.modify_data["road_type"]["asphalt"]["turn_mod"] = "1"
        self.modify_data["road_type"]["asphalt"]["speed_mod"] = "1.4"
    
        #DRIVER
        self.modify_data["driver"] = {}
            #EXPERIENCE
        self.modify_data["driver"]["experience"] = {}
        self.modify_data["driver"]["experience"]["experienced"] = {}
        self.modify_data["driver"]["experience"]["experienced"]["turn_mod"] = "1"
        self.modify_data["driver"]["experience"]["experienced"]["speed_mod"] = "1.1"
    
        self.modify_data["driver"]["experience"]["inexperienced"] = {}
        self.modify_data["driver"]["experience"]["inexperienced"]["turn_mod"] = "1.1"
        self.modify_data["driver"]["experience"]["inexperienced"]["speed_mod"] = "0.9"
            #CHEMICAL INFLUENCE
        self.modify_data["driver"]["dui"] = {}
        self.modify_data["driver"]["dui"]["intoxicated"] = {}
        self.modify_data["driver"]["dui"]["intoxicated"]["turn_mod"] = "1.8"
        self.modify_data["driver"]["dui"]["intoxicated"]["speed_mod"] = "1.2"
        
        self.modify_data["driver"]["dui"]["sober"] = {}
        self.modify_data["driver"]["dui"]["sober"]["turn_mod"] = "1"
        self.modify_data["driver"]["dui"]["sober"]["speed_mod"] = "1"
            #VISION
        self.modify_data["driver"]["vision"] = {}
        self.modify_data["driver"]["vision"]["near sighted"] = {}
        self.modify_data["driver"]["vision"]["near sighted"]["turn_mod"] = "1"
        self.modify_data["driver"]["vision"]["near sighted"]["speed_mod"] = "1.1"
        
        self.modify_data["driver"]["vision"]["far sighted"] = {}
        self.modify_data["driver"]["vision"]["far sighted"]["turn_mod"] = "1.1"
        self.modify_data["driver"]["vision"]["far sighted"]["speed_mod"] = "1"
        
        self.modify_data["driver"]["vision"]["normal"] = {}
        self.modify_data["driver"]["vision"]["normal"]["turn_mod"] = "1"
        self.modify_data["driver"]["vision"]["normal"]["speed_mod"] = "1"
            #AGE
        self.modify_data["driver"]["age"] = {}
        self.modify_data["driver"]["age"]["young"] = {}
        self.modify_data["driver"]["age"]["young"]["turn_mod"] = "1.1"
        self.modify_data["driver"]["age"]["young"]["speed_mod"] = "1.1"
        
        self.modify_data["driver"]["age"]["middle aged"] = {}
        self.modify_data["driver"]["age"]["middle aged"]["turn_mod"] = "1"
        self.modify_data["driver"]["age"]["middle aged"]["speed_mod"] = "1"
        
        self.modify_data["driver"]["age"]["old"] = {}
        self.modify_data["driver"]["age"]["old"]["turn_mod"] = "0.8"
        self.modify_data["driver"]["age"]["old"]["speed_mod"] = "0.8"
        
        #VEHICLE
        self.modify_data["vehicle"] = {}
        self.modify_data["vehicle"]["car"] = {}
        self.modify_data["vehicle"]["car"]["turn_mod"] = "1"
        self.modify_data["vehicle"]["car"]["speed_mod"] = "1.2"
        
        self.modify_data["vehicle"]["pickup"] = {}
        self.modify_data["vehicle"]["pickup"]["turn_mod"] = "1"
        self.modify_data["vehicle"]["pickup"]["speed_mod"] = "1"
        
        self.modify_data["vehicle"]["truck"] = {}
        self.modify_data["vehicle"]["truck"]["turn_mod"] = "0.8"
        self.modify_data["vehicle"]["truck"]["speed_mod"] = "1.1"
        
        #COMPUTER
        #Comp power is calculated by: 
        #1 Comp Power = 100 Million Instructions Per Second(MIPS)
        #1 Quadrillion Floating Point Operations Per Second(Petaflops/PFLOPS) = 1,000 Comp Power
        #1 Qubit = 10,000 Comp Power
        self.modify_data["computer"] = {}
        #UNIVAC
        self.modify_data["computer"]["UNIVAC 1 (1951)"] = {}
        self.modify_data["computer"]["UNIVAC 1 (1951)"]["name"] = "UNIVAC 1 (1951)"
        self.modify_data["computer"]["UNIVAC 1 (1951)"]["comp_power"] = 0.00002
        #Cray 1
        self.modify_data["computer"]["Cray 1 (1975)"] = {}
        self.modify_data["computer"]["Cray 1 (1975)"]["name"] = "Cray 1 (1975)"
        self.modify_data["computer"]["Cray 1 (1975)"]["comp_power"] = 1.6
        #TRS-80
        self.modify_data["computer"]["TRS-80 (1976)"] = {}
        self.modify_data["computer"]["TRS-80 (1976)"]["name"] = "TRS-80 (1976)"
        self.modify_data["computer"]["TRS-80 (1976)"]["comp_power"] = 0.0116
        #Commodore
        self.modify_data["computer"]["Commodore 64 (1982)"] = {}
        self.modify_data["computer"]["Commodore 64 (1982)"]["name"] = "Commodore 64 (1982)"
        self.modify_data["computer"]["Commodore 64 (1982)"]["comp_power"] = 0.0116
        #Intel i386DX
        self.modify_data["computer"]["Intel i386DX (1989)"] = {}
        self.modify_data["computer"]["Intel i386DX (1989)"]["name"] = "Intel i386DX (1989)"
        self.modify_data["computer"]["Intel i386DX (1989)"]["comp_power"] = 0.043       
        #Intel Pentium
        self.modify_data["computer"]["Intel Pentium (1994)"] = {}
        self.modify_data["computer"]["Intel Pentium (1994)"]["name"] = "Intel Pentium (1994)"
        self.modify_data["computer"]["Intel Pentium (1994)"]["comp_power"] = 1.88  
        #AMD Athlon 64 3800+ X2
        self.modify_data["computer"]["AMD Athlon 64 3800+ X2 (2005)"] = {}
        self.modify_data["computer"]["AMD Athlon 64 3800+ X2 (2005)"]["name"] = "AMD Athlon 64 3800+ X2 (2005)"
        self.modify_data["computer"]["AMD Athlon 64 3800+ X2 (2005)"]["comp_power"] = 145.64
        #Cray Titan
        self.modify_data["computer"]["Cray Titan (2012)"] = {}
        self.modify_data["computer"]["Cray Titan (2012)"]["name"] = "Cray Titan (2012)"
        self.modify_data["computer"]["Cray Titan (2012)"]["comp_power"] = 18000
        #Intel Core i5 7300U
        self.modify_data["computer"]["Intel Core i5 7300U (2016)"] = {}
        self.modify_data["computer"]["Intel Core i5 7300U (2016)"]["name"] = "Intel Core i5 7300U (2016)"
        self.modify_data["computer"]["Intel Core i5 7300U (2016)"]["comp_power"] = 538.40
        #IBM Summit
        self.modify_data["computer"]["IBM Summit (2018)"] = {}
        self.modify_data["computer"]["IBM Summit (2018)"]["name"] = "IBM Summit (2018)"
        self.modify_data["computer"]["IBM Summit (2018)"]["comp_power"] = 122000
        #Google Sycamore
        self.modify_data["computer"]["Google Sycamore (2019)"] = {}
        self.modify_data["computer"]["Google Sycamore (2019)"]["name"] = "Google Sycamore (2019)"
        self.modify_data["computer"]["Google Sycamore (2019)"]["comp_power"] = 530000
    
#Collects the user's selections for sim modifiers
def modifiers_intro(variables):
    mods = Mods()
    # for var in variables[0]:
    #     print(var)
    #WEATHER
    for num, name in cv.WEATHER_CHOICES:
        if num == variables.weather:
            mods.modify_choices["weather"] = name
    #TIME
    for num, name in cv.TIME_CHOICES:
        if num == variables.time:
            mods.modify_choices["time"] = name
    #ROAD CONDITION
    for num, name in cv.ROAD_CHOICES:
        if num == variables.road_type:
            mods.modify_choices["road_type"] = name
    #DRIVER
        #EXPERIENCE 1
    for num, name in cv.DRIVER_EXP_CHOICES:
        if num == variables.driver_exp1:
            mods.modify_choices["driver_exp1"] = name
        #EXPERIENCE 2
    for num, name in cv.DRIVER_EXP_CHOICES:
        if num == variables.driver_exp2:
            mods.modify_choices["driver_exp1"] = name
        #CHEMICAL INFLUENCE 1
    for num, name in cv.DRIVER_DUI_CHOICES:
        if num == variables.driver_dui1:
            mods.modify_choices["driver_dui1"] = name
        #CHEMICAL INFLUENCE 2
    for num, name in cv.DRIVER_DUI_CHOICES:
        if num == variables.driver_dui2:
            mods.modify_choices["driver_dui2"] = name
        #VISION 1
    for num, name in cv.DRIVER_VISION_CHOICES:
        if num == variables.driver_vision1:
            mods.modify_choices["driver_vision1"] = name
        #VISION 2
    for num, name in cv.DRIVER_VISION_CHOICES:
        if num == variables.driver_vision2:
            mods.modify_choices["driver_vision2"] = name
        #AGE 1
    for num, name in cv.DRIVER_AGE_CHOICES:
        if num == variables.driver_age1:
            mods.modify_choices["driver_age1"] = name
        #AGE 2
    for num, name in cv.DRIVER_AGE_CHOICES:
        if num == variables.driver_age1:
            mods.modify_choices["driver_age1"] = name
    #VEHICLE 1
    for num, name in cv.VEHICLE_CHOICES:
        if num == variables.vehicle1:
            mods.modify_choices["vehicle1"] = name
    #VEHICLE 2
    for num, name in cv.VEHICLE_CHOICES:
        if num == variables.vehicle1:
            mods.modify_choices["vehicle1"] = name
    #COMPUTER
    for num, name in cv.COMPUTER_CHOICES:
        if num == variables.computer:
            mods.modify_choices["computer"] = name
