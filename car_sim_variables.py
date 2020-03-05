
class Mods:
    
    def __init__(self,name):
        self.name = name
    
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
        self.modify_data["computer"] = {}
        self.modify_data["computer"]["name"] = ""
        self.modify_data["computer"]["comp_power"] = ""

#COMPUTERS
class Computer:
    
    def __init__(self,name,comp_power):
        self.name = name
        self.comp_power = comp_power

#Comp power is calculated by: 
#1 Comp Power = 100 Million Instructions Per Second(MIPS)
#1 Quadrillion Floating Point Operations Per Second(Petaflops/PFLOPS) = 1,000 Comp Power
#1 Qubit = 10,000 Comp Power
UNIVAC = Computer("UNIVAC 1 (1951)",0.00002)
Cray1 = Computer("Cray 1 (1975)",1.6)
TRS = Computer("TRS-80 (1976)",0.0116)
Commodore = Computer("Commodore 64 (1982)",0.02252)
Intel1 = Computer("Intel i386DX (1989)",0.043)
Intel2 = Computer("Intel Pentium (1994)",1.88)
AMD = Computer("AMD Athlon 64 3800+ X2 (2005)",145.64)
Cray2 = Computer("Cray Titan (2012)",18000)
Intel3 = Computer("Intel Core i5 7300U (2016)",538.40)
Summit = Computer("IBM Summit (2018)",122000)
Sycamore = Computer("Google Sycamore (2019)",530000)

    
#Collects the user's selections for sim modifiers
def modifiers_intro(mods):
    weather_select = 1
    time_select = 1
    road_type_select = 1
    driver_exp1_select = 1
    driver_exp2_select = 1
    driver_dui1_select = 1
    driver_dui2_select = 1
    driver_vision1_select = 1
    driver_vision2_select = 1
    driver_age1_select = 1
    driver_age2_select = 1
    vehicle1_select = 1
    vehicle2_select = 1
    computer_select = 1
    
    #WEATHER
    if weather_select == 1:
        mods.modify_choices["weather"] = "clear"
    if weather_select == 2:
        mods.modify_choices["weather"] = "rain"
    if weather_select == 3:
        mods.modify_choices["weather"] = "snow"        
    if weather_select == 4:
        mods.modify_choices["weather"] = "ice"
    if weather_select == 5:
        mods.modify_choices["weather"] = "fog"
    if weather_select == 6:
        mods.modify_choices["weather"] = "wind"
    #TIME
    if time_select == 1:
        mods.modify_choices["time"] = "morning"
    if time_select == 2:
        mods.modify_choices["time"] = "noon"
    if time_select == 3:
        mods.modify_choices["time"] = "evening"
    if time_select == 4:
        mods.modify_choices["time"] = "night"
    #ROAD CONDITION
    if road_type_select == 1:
        mods.modify_choices["road_type"] = "dirt"
    if road_type_select == 2:
        mods.modify_choices["road_type"] = "gravel"
    if road_type_select == 3:
        mods.modify_choices["road_type"] = "asphalt"
    #DRIVER
        #EXPERIENCE 1
    if driver_exp1_select == 1:
        mods.modify_choices["driver_experience1"] = "experienced"
    if driver_exp1_select == 2:
        mods.modify_choices["driver_experience1"] = "inexperienced"
        #EXPERIENCE 2
    if driver_exp2_select == 1:
        mods.modify_choices["driver_experience2"] = "experienced"
    if driver_exp2_select == 2:
        mods.modify_choices["driver_experience2"] = "inexperienced"
        #CHEMICAL INFLUENCE 1
    if driver_dui1_select == 1:
        mods.modify_choices["chemical_influence1"] = "sober"
    if driver_dui1_select == 2:
        mods.modify_choices["chemical_influence1"] = "intoxicated"
        #CHEMICAL INFLUENCE 2
    if driver_dui2_select == 1:
        mods.modify_choices["chemical_influence2"] = "sober"
    if driver_dui2_select == 2:
        mods.modify_choices["chemical_influence2"] = "intoxicated"
        #VISION 1
    if driver_vision1_select == 1:
        mods.modify_choices["vision1"] = "near sighted"
    if driver_vision1_select == 2:
        mods.modify_choices["vision1"] = "far sighted"
    if driver_vision1_select == 3:
        mods.modify_choices["vision1"] = "normal"
        #VISION 2
    if driver_vision2_select == 1:
        mods.modify_choices["vision2"] = "near sighted"
    if driver_vision2_select == 2:
        mods.modify_choices["vision2"] = "far sighted"
    if driver_vision2_select == 3:
        mods.modify_choices["vision2"] = "normal"
        #AGE 1
    if driver_age1_select == 1:
        mods.modify_choices["age1"] = "young"
    if driver_age1_select == 2:
        mods.modify_choices["age1"] = "middle aged"
    if driver_age1_select == 3:
        mods.modify_choices["age1"] = "old"
        #AGE 2
    if driver_age2_select == 1:
        mods.modify_choices["age2"] = "young"
    if driver_age2_select == 2:
        mods.modify_choices["age2"] = "middle aged"
    if driver_age2_select == 3:
        mods.modify_choices["age2"] = "old"
    #VEHICLE 1
    if vehicle1_select == 1:
        mods.modify_choices["vehicle1"] = "car"
    if vehicle1_select == 2:
        mods.modify_choices["vehicle1"] = "pickup"
    if vehicle1_select == 3:
        mods.modify_choices["vehicle1"] = "truck"
    #VEHICLE 2
    if vehicle2_select == 1:
        mods.modify_choices["vehicle2"] = "car"
    if vehicle2_select == 2:
        mods.modify_choices["vehicle2"] = "pickup"
    if vehicle2_select == 3:
        mods.modify_choices["vehicle2"] = "truck"
    #COMPUTER
    if computer_select == 1:
        mods.modify_choices["computer"] = "UNIVAC"
        mods.modify_data["computer"]["name"] = UNIVAC.name
        mods.modify_data["computer"]["comp_power"] = UNIVAC.comp_power
    if computer_select == 2:
        mods.modify_choices["computer"] = "Cray1"
        mods.modify_data["computer"]["name"] = Cray1.name
        mods.modify_data["computer"]["comp_power"] = Cray1.comp_power
    if computer_select == 3:
        mods.modify_choices["computer"] = "TRS"
        mods.modify_data["computer"]["name"] = TRS.name
        mods.modify_data["computer"]["comp_power"] = TRS.comp_power
    if computer_select == 4:
        mods.modify_choices["computer"] = "Commodore"
        mods.modify_data["computer"]["name"] = Commodore.name
        mods.modify_data["computer"]["comp_power"] = Commodore.comp_power
    if computer_select == 5:
        mods.modify_choices["computer"] = "Intel1"
        mods.modify_data["computer"]["name"] = Intel1.name
        mods.modify_data["computer"]["comp_power"] = Intel1.comp_power
    if computer_select == 6:
        mods.modify_choices["computer"] = "Intel2"
        mods.modify_data["computer"]["name"] = Intel2.name
        mods.modify_data["computer"]["comp_power"] = Intel2.comp_power
    if computer_select == 7:
        mods.modify_choices["computer"] = "AMD"
        mods.modify_data["computer"]["name"] = AMD.name
        mods.modify_data["computer"]["comp_power"] = AMD.comp_power
    if computer_select == 8:
        mods.modify_choices["computer"] = "Cray2"
        mods.modify_data["computer"]["name"] = Cray2.name
        mods.modify_data["computer"]["comp_power"] = Cray2.comp_power
    if computer_select == 9:
        mods.modify_choices["computer"] = "Intel3"
        mods.modify_data["computer"]["name"] = Intel3.name
        mods.modify_data["computer"]["comp_power"] = Intel3.comp_power
    if computer_select == 10:
        mods.modify_choices["computer"] = "Summit"
        mods.modify_data["computer"]["name"] = Summit.name
        mods.modify_data["computer"]["comp_power"] = Summit.comp_power
    if computer_select == 11:
        mods.modify_choices["computer"] = "Sycamore"
        mods.modify_data["computer"]["name"] = Sycamore.name
        mods.modify_data["computer"]["comp_power"] = Sycamore.comp_power
