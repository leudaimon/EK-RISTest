#!/usr/bin/python2
# encoding: utf-8
from pap import *

def papydb():
  
    ###############################
    # ENGINES
    ###############################
    AerobeeFam = EngineFamily("Aerobee", "Early pressure-fed hypergolic (aniline/furfuryl/nitric) engine originally for sounding rockets.", 
        vac=True)
    CorporalFam = EngineFamily("Corporal Kick", "Very early solid-fueled kick stage motor for light sounding rockets.", 
        vac=False)
    A4Fam = EngineFamily("A-4 Ethanol series", "Early LOx / Alcohol rocket engine family that is a copy of the German A-4.", 
        vac=False)

    # Engines
    TinyTim = Engine("Corporal", CorporalFam, vac=False)
    WAC = Engine("WAC", AerobeeFam, vac=True)
    XASR1 = Engine("XASR-1", AerobeeFam, vac=True)
    AJ1027 = Engine("AJ10-27", AerobeeFam, vac=True)
    RD100 = Engine("RD-100", A4Fam, vac=False)
    RD101 = Engine("RD-101", A4Fam, vac=False)
    RD103 = Engine("RD-103", A4Fam, vac=False)


    ###############################
    # STAGES
    ###############################
    SolidStgFam = StageFamily("Solid kick stages", CorporalFam, 
    "Very high TWR Solid kick stages for sounding rockets.", vac=False)
    AerobeeStgFam = StageFamily("Single engine Aerobee stages", AerobeeFam, 
        "Single-engine solid rocket sustainers that can be used in a range of conditions, from ground-lit to final stage of satellites", vac=True)
    A4StgFam = StageFamily("Early A4 Boosters", A4Fam, 
        "Boosters using engines directly derived from the A-4 missile, they can be used alone with heavy payloads or crewed cockpits, or as booster stages of multi-staged rockets", vac=False)


    # Stages
    CorporalStg = Stage("Corporal", SolidStgFam, TinyTim, 
        "An air-to-air missile adapted to be a very high TWR kick stage for sounding rockets.")
    WACStg = Stage("WAC", AerobeeStgFam, WAC, 
        "The first sounding rocket sustainer design, the WAC is powered by a lightweight pressure-fed engine")
    XASRStg = Stage("XASR-1", AerobeeStgFam, XASR1, 
        "Direct successor to the WAC, the XASR-1 is much more capable, with an upgraded engine and double fuel capacity")
    RD100Stg = Stage("RD-100", A4StgFam, RD100, 
        "Adapted from the A-4 Missile, this behemot sounding rocket can act both as a single stage booster for biological samples and crewed cockpits, as well as a first stage for more slim second stages")
    RD101Stg = Stage("RD-101", A4StgFam, RD101, 
        "An upgrade from the RD-100, the RD-101 has an uprated engine that hopefully allows it to be the first stage of our early satellites")
    RD101Slim = Stage("RD-101 Tank II", A4StgFam, RD101, 
        "An upgrade to the RD-101 stage. We developed a second generation of new, lighter tanks, and reduced the diameter for better drag control.")
    XASRQuad = Stage("XASR-1 Quad", AerobeeStgFam, XASR1, 
        "A heavier second stage, using 4 XASR-1 engines, this stage also benefits from the improved second generation tanks and shares the same diameter as the RD-101", 4)
    XASRFat = Stage("XASR-1 Tank II", AerobeeStgFam, XASR1, 
        "A third, unguided stage using a single XASR-1 engine with second generation tanks, this stage doubles as a nosecone for our LV-0 prototype vehicle")
    RD103Stg = Stage("RD-103", A4StgFam, RD103, 
        "An upgraded version of our first stage. We developed the RD-103 engine with larger thrust and burning time, and we streched the first stage to account for the increase in fuel.")
    AJ27Quad = Stage("AJ10-27 Quad", AerobeeStgFam, AJ1027, 
        "An upgraded version of our four-engined second stage. We developed the AJ10-27 engine with larger thrust and burning time, and we streched the second stage to account for the increase in fuel.", 4)
    AJ27Nose = Stage("AJ10-27", AerobeeStgFam, AJ1027, 
        "With a similar function as its XASR-1 version, this stage is an upper third stage responsible for final orbital insertion")
    RD103HStg = Stage("RD-103 Heavy", A4StgFam, RD103, 
        "A boosted version of the RD-103, this stage has two side boosters that detach earlier, leaving the sustainer to burn for longer")
    AJ27Penta = Stage("AJ10-27 Penta", AerobeeStgFam, AJ1027, 
        "A bigger version of our second stage, the AJ10-27 Penta has 5 engines and an elongated tank")
    AJ27Tri = Stage("AJ10-27 Tri", AerobeeStgFam, AJ1027, 
        "Using third generation tanks we developed new upper stages with different clusters for these upgraded vehicles we call LV-1.5 series. This is the 3-engine version.")
    AJ27Hepta = Stage("AJ10-27 Hepta", AerobeeStgFam, AJ1027, 
        "Using third generation tanks we developed new upper stages with different clusters for these upgraded vehicles we call LV-1.5 series. This is the 7-engine version.")
    LV15HStg = Stage("RD103 Heavy Tank III", A4StgFam, RD103, 
        "Using third generation tanks we developed new first stages with different clusters for these upgraded vehicles we call LV-1.5 series. This is the biggest version with 2 side boosters and 2 engines in the core stage.")
    XASRTLI = Stage("TLI unguided stage", AerobeeStgFam, XASR1, 
        "Dedicated TLI stage for our Lunar Impactor probe using one XASR-1 Engine")
    AJ27TankIII = Stage("AJ10-27 Tank III", AerobeeStgFam, AJ1027, 
        "Using third generation tanks we developed new upper stages with different clusters for these upgraded vehicles we call LV-1.5 series. This is the 1-engine version.")
    LV15LStg = Stage("RD-103 Light Tank III", A4StgFam, RD103, 
        "Using third generation tanks we developed new first stages with different clusters for these upgraded vehicles we call LV-1.5 series. This is the small version with a single engine core.")


    ###############################
    # LAUNCH VEHICLES
    ###############################
    CorporalLVFam = LVFamily("Corporal", "First lightweight Sounding rockets. Used to carry small payloads into low to mid altitude suborbital flights", 
        SolidStgFam, AerobeeStgFam)
    A4LVFam = LVFamily("A-4", "Broad family of A-4 derived rockets. The early models were used to launch the first biological samples into suborbital trajectories, but latter models managed crewed suborbital flights and even some very basic satellites.",  
        A4StgFam, AerobeeStgFam)

  
    # LAUNCH VEHICLES
    WACLv = LV("WAC", CorporalLVFam, "A test-vehicle for the Corporal-WAC, the pure WAC uses only the sustainer stage for a lower apogee in a lower and safer flight", 
        WACStg)
    CorporalWAC = LV("Corporal-WAC", CorporalLVFam, "The first space-capable sounding rocket. With a very basic scientific payload, it is able to sniff space before crashing back in the atmosphere.", 
        CorporalStg, WACStg)
    RD100Bio = LV("A-4 Biological experiment", A4LVFam, "The massive A-4 military missile is adapted for use as a sounding rocket, carrying a Biological sample all the way to space. This is the predecessor vehicle to our first space-capable crewed rocket.", 
        RD100Stg)
    RD100WAC = LV("A-4 Bumper", A4LVFam, "The first two-staged rocket to be flown, with much higher capacity than anything that preceded it.", 
        RD100Stg, WACStg)
    RD100Crew = LV("A4-X1 space coffin", A4LVFam, "Little more than a cockpit placed atop our bio sample rocket, the brave pilots to venture themselves here will be the first astronauts.", 
        RD100Stg)
    CorporalXASR = LV("Corporal-XASR-1", CorporalLVFam, "An upgrade of the Corporal-WAC, this sounding rocket has the upgraded XASR-1 stage, with an uprated engine and double amount of fuel", 
        CorporalStg, XASRStg)
    RD101XASR = LV("RD-101 Bumper", A4LVFam, "An upgrade of the original bumper, both stages have been uprated, so this sounding rocket has much increased capacity, and with an additional stage and improved tanks will allow us to reach orbit.", 
        RD101Stg, XASRStg)
    LV0 = LV("LV0 Orbital prototype", A4LVFam, "A three-staged vehicle using our second generation tanks and an RD-101 as first stage, a second stage with 4 XASR-1s and an unguided kick-stage with 1 XASR-1", 
        RD101Slim, XASRQuad, XASRFat)
    RD101Sound = LV("RD-101 Payload", A4LVFam, "A heavy sounding rocket for standard missions. Uses an RD-101 stage with a massive nosecone to house the payload", 
        RD101Stg)
    RD101XASRQuad = LV("RD-101 1.3m SR 2stg", A4LVFam, "A heavy two-staged sounding rocket for standard missions. It is a modification of our LV0 rocket, using only the first two stages and no guidance.", 
        RD101Slim, XASRQuad)
    RD103AJ27SR = LV("RD-103 1.3m SR 2stg", A4LVFam, "An upgraded version of our heavy two-staged sounding rocket for standard missions. It is a modification of our LV1 rocket, using only the first two stages and no guidance.", 
        RD103Stg, AJ27Quad)
    LV1 = LV("LV-1 Orbital Vehicle", A4LVFam, "Using the RD-103 and AJ10-27 engines, this vehicle is capable of putting very basic payloads into a polar orbit", 
        RD103Stg, AJ27Quad, AJ27Nose)
    LV1Control = LV("LV-1 Heavy Orbital vehicle", A4LVFam, "Based on the standard LV-1 vehicle, this rocket has two side boosters using the same RD-103 engines, and a bigger second stage with 5 AJ10-27s.It also uses upper stage avionics for control of the final stage, allowing specific orbits to be reached", 
        RD103HStg, AJ27Penta, AJ27Nose)
    RD103AJ27SRH = LV("RD-103 Heavy SR", A4LVFam, "Based on our LV-1 Heavy, this Sounding rocket is the most capable SR we intend to launch.", 
        RD103HStg, AJ27Quad)
    LV15HLuna = LV("LV1.5 Heavy - Luna", A4LVFam, "Our heaviest rocket thus far, this LV has a total of 15 engines considering all stages. This makes it rather unreliable, but allows us to make it into the moon. I sports 4 stages (and a half), all using our new thrid generation tanks. The first stage is based on RD-103 engines, with 2 engines in the core sustainer and 2 boosters. Upper stages have clusters of 7 and 3 AJ10-27s, and the final upper stage for TLI has a single XASR-1.", 
        LV15HStg, AJ27Hepta, AJ27Tri, XASRTLI)
    LV15Light = LV("LV1.5 Light", A4LVFam, "A light LV using our third generation tanks. This LV allows us to inject a controllable upper stage core with plenty RCS fuel into an eccentric polar orbit.", 
        LV15LStg, AJ27Tri, AJ27TankIII)



    ###############################
    # LAUNCHES
    ###############################
    launches = []
    def launch(name, y, m, d, lv, payload, dest, result, comments=None, pics=None):
            launches.append(Launch(name, date(y, m, d), lv, payload, dest, result, comments, pics))
    def paren(text):
        return Payload(None, None, text)
    
    launch("WAC-First", 1951, 1, 6, WACLv, 
        Payload("TPT", ), EA, 0, "First launch in a boosterless version of the WAC sounding rocket.",
        [Picture("images/AS-361.jpg", "Our first rocket ready to be rolled out to the launch pad")])
    launch("Corporal-WAC - For space!", 1951, 1, 9, CorporalWAC, 
        Payload("TPT", "Karman Line (Uncrewed)"), SO, 0, "First flight into space, with a Corporal-WAC, the first design for a complete sounding rocket, with kick stage for better performance and control",
        [Picture("images/AS-366.jpg", "The space-capable Corporal-WAC ready to be rolled out to the launch pad")])
    launch("BioSample 1", 1951, 1, 21, RD100Bio, 
        Payload("BioSample", ),SO, 1, "Failed attempt at sending the first biological samples into space. The RD-100 engine shut down a few seconds after liftoff, and the payload reached only 9km of altitude.",
        [Picture("images/AS-495.jpg",""), Picture("images/AS-544.jpg",""), Picture("images/AS-548.jpg",""), Picture("images/AS-561.jpg","")])
    launch("BioSample 2", 1951, 2, 3, RD100Bio, 
        Payload("BioSample", ),SO, 0, "First biological samples into space, using the powerhouse RD-100 engine.",
        [Picture("images/AS-495.jpg",""), Picture("images/AS-588.jpg",""), Picture("images/AS-595.jpg",""), Picture("images/AS-602.jpg",""), Picture("images/AS-609.jpg","")])
    launch("Corporal-WAC 2", 1951, 2, 5, CorporalWAC, 
        Payload("TPT", ),SO, 0, "Further exploration of the nearby space with the Corporal-WAC sounding rocket")
    launch("Corporal-WAC 3", 1951, 2, 6, CorporalWAC, 
        Payload("TPT", ),SO, 0, "Further exploration of the nearby space with the Corporal-WAC sounding rocket")
    launch("Bumper 1", 1951, 2, 15, RD100WAC, 
        Payload("TPT", ),SO, -3, "With the first real two-stage rocket ever lauched, even this partial sucess broke several records. The vehicle lost some aerodynamic stability in the end of the first stage burn, going into a tumble. Still reached 665km ",
        [Picture("images/AS-657.jpg",""), Picture("images/AS-696.jpg",""), Picture("images/AS-697.jpg",""), Picture("images/AS-700.jpg",""), Picture("images/AS-704.jpg","")])
    launch("Bumper 2", 1951, 2, 23, RD100WAC, 
        Payload("TPT", ),SO, 0, "First complete success for a bumper launch. The vehicle reached more than 1000 km of altitude, and also broke speed records.",
        [Picture("images/AS-657.jpg","")])
    launch("Bumper SR 1", 1951, 3, 3, RD100WAC, 
        Payload("SR-0.3", ),SO, 0, "Standard Sounding Rocket payload mission using the bumper for high capacity")
    launch("Corporal-WAC SR 1", 1951, 3, 5, CorporalWAC, 
        Payload("SR-0.3", ),EA, 0, "Standard Sounding Rocket payload mission using the low capacity Corporal-WAC")
    launch("Corporal-WAC SR 2", 1951, 3, 6, CorporalWAC, 
        Payload("SR-0.3", ),EA, 0, "Standard Sounding Rocket payload mission using the low capacity Corporal-WAC")
    launch("Bumper SR 2", 1951, 3, 15, RD100WAC, 
        Payload("SR-4x0.3", ),SO, 0, "Standard Sounding Rocket payload mission using the bumper for high capacity")
    launch("Corporal-WAC SR 3", 1951, 3, 16, CorporalWAC, 
        Payload("SR-0.3", ),EA, 0, "Standard Sounding Rocket payload mission using the low capacity Corporal-WAC")
    launch("RD100 Crewed - Kissing the heavens!", 1951, 4, 21, RD100Crew, 
        Payload("X-1", "Karman Line (Crewed)"),SO, 0, "First crewed flight to space! Using an adapted supersonic airplane cockpit aboard our big sounding rocket, we managed to send our first astronaut to space!")
    launch("RD100 Crewed 2", 1951, 5, 8, RD100Crew, 
        Payload("X-1", ),SO, 0, "Second flight of our crewed suborbital LV, reaching a higher altitude and exploring a different region in our surroundings")
    launch("Bumper G2 1", 1951, 5, 17, RD101XASR, 
        Payload("SR-3x0.3", ),SO, 0, "First flight of our upgraded Bumper Sounding Rocket")
    launch("RD100 Crewed 3", 1951, 6, 11, RD100Crew, 
        Payload("X-1", ),SO, 0, "Our crewed suborbital flights became routine. Our two pilots are now experienced in this mission.")
    launch("RD100 Crewed 4", 1951, 7, 6, RD100Crew, 
        Payload("X-1", ),SO, 0, "Our crewed suborbital flights became routine. Our two pilots are now experienced in this mission.")
    launch("Bumper G2 2", 1951, 7, 15, RD101XASR, 
        Payload("SR-6x0.3", ),SO, 0, "Routine Sounding Rocket mission with our upgraded Bumper G2")
    launch("Bumper G2 3", 1951, 7, 23, RD101XASR, 
        Payload("SR-6x0.3", ),SO, 0, "Routine Sounding Rocket mission with our upgraded Bumper G2")
    launch("First orbital", 1951, 8, 20, LV0, 
        Payload("TPT", "First Orbit!"),LEO, 0, 
        "With upgraded tanks, we managed to design an orbital-capable rocket. This three-staged vehicle will not win any beauty contests, or do anything more than sending a SR core into orbit, but still played its role in our Space Program, demonstrating our capability")
    launch("Bumper G2 4", 1951, 8, 25, RD101XASR, 
        Payload("SR-0.3", ),SO, 0, "Routine Sounding Rocket mission with our upgraded Bumper G2")
    launch("RD101 SR 1", 1951, 8, 29, RD101Sound, 
        Payload("SR-1.6", ),EA, 0, "First flight of our dedicated RD-101 rocket for standard SR missions")
    launch("Bumper G2 5", 1951, 9, 2, RD101XASR, 
        Payload("SR-0.3", ),SO, 0, "Routine Sounding Rocket mission with our upgraded Bumper G2")
    launch("RD101 SR 2", 1951, 9, 6, RD101Sound, 
        Payload("SR-1.6", ),EA, 0, "Routine Sounding Rocket mission with our dedicated RD-101 rocket")
    launch("RD101 SR 3", 1951, 9, 9, RD101Sound, 
        Payload("SR-1.6", ),EA, 0, "Routine Sounding Rocket mission with our dedicated RD-101 rocket")
    launch("RD101 SR 4", 1951, 9, 13, RD101Sound, 
        Payload("SR-1.6", ),SO, 0, "Routine Sounding Rocket mission with our dedicated RD-101 rocket")
    launch("RD101 SR 5", 1951, 9, 16, RD101Sound, 
        Payload("SR-1.6", ),EA, 1, "Routine Sounding Rocket mission with our dedicated RD-101 rocket")
    launch("RD101 SR 6", 1951, 9, 20, RD101Sound, 
        Payload("SR-1.6", ),SO, 0, "Routine Sounding Rocket mission with our dedicated RD-101 rocket")
    launch("RD101 XASRQuad SR 1", 1951, 9, 25, RD101XASRQuad, 
        Payload("SR-1.3", ),SO, 0, "First launch of our Sounding Rocket based on our orbital vehicle. A routine mission to deploy some payload.")
    launch("RD101 XASRQuad SR 2", 1951, 9, 30, RD101XASRQuad, 
        Payload("SR-1.3", ),SO, 0, "Routine Sounding Rocket mission with our dedicated rocket based on our orbital vehicle")
    launch("RD101 SR 7", 1951, 10, 3, RD101Sound, 
        Payload("SR-1.6", ),EA, 0, "Routine Sounding Rocket mission with our dedicated RD-101 rocket")
    launch("RD101 XASRQuad SR 3", 1951, 10, 7, RD101XASRQuad, 
        Payload("SR-1.3", ),SO, 2, "Routine Sounding Rocket mission with our dedicated rocket based on our orbital vehicle")
    launch("RD101 XASRQuad SR 4", 1951, 10, 11, RD101XASRQuad, 
        Payload("SR-1.3", ),SO, 0, "Routine Sounding Rocket mission with our dedicated rocket based on our orbital vehicle")
    launch("RD101 XASRQuad SR 5", 1951, 10, 16, RD101XASRQuad, 
        Payload("SR-1.3H", ),SO, 0, "Routine Sounding Rocket mission with our dedicated rocket based on our orbital vehicle")
    launch("RD101 XASRQuad SR 6", 1951, 10, 20, RD101XASRQuad, 
        Payload("SR-1.3H", ),SO, 0, "Routine Sounding Rocket mission with our dedicated rocket based on our orbital vehicle")
    launch("RD101 XASRQuad SR 7", 1951, 10, 24, RD101XASRQuad, 
        Payload("SR-1.3H", ),SO, 0, "Routine Sounding Rocket mission with our dedicated rocket based on our orbital vehicle")
    launch("RD101 XASRQuad SR 8", 1951, 10, 27, RD101XASRQuad, 
        Payload("SR-1.3H", ),SO, 0, "Routine Sounding Rocket mission with our dedicated rocket based on our orbital vehicle")
    launch("RD101 XASRQuad SR 9", 1951, 10, 31, RD101XASRQuad, 
        Payload("SR-1.3H", ),SO, 0, "Routine Sounding Rocket mission with our dedicated rocket based on our orbital vehicle")
    launch("RD101 XASRQuad SR 10", 1951, 11, 3, RD101XASRQuad, 
        Payload("SR-1.3H", ),SO, 0, "Routine Sounding Rocket mission with our dedicated rocket based on our orbital vehicle")
    launch("RD101 XASRQuad SR 11", 1951, 11, 7, RD101XASRQuad, 
        Payload("SR-1.3H", ),SO, 0, "Routine Sounding Rocket mission with our dedicated rocket based on our orbital vehicle")
    launch("RD103 AJ-10 SR 1", 1951, 11, 14, RD103AJ27SR, 
        Payload("SR-1.3H", ),SO, 0, "First flight of the upgraded version of our heavy Sounding rocket, now using uprated engines in both stages.")
    launch("RD103 AJ-10 SR 2", 1951, 11, 20, RD103AJ27SR, 
        Payload("SR-1.3H", ),SO, 0, "Routine Sounding Rocket mission with our dedicated rocket based on our orbital vehicle.")
    launch("RD103 AJ-10 SR 3", 1951, 11, 25, RD103AJ27SR, 
        Payload("SR-1.3H", ),SO, 0, "Routine Sounding Rocket mission with our dedicated rocket based on our orbital vehicle")
    launch("LV-1 Polar orbit", 1951, 12, 4, LV1, 
        Payload("Sat0", ),EPO, 0, "First flight of our RD-103 based Orbital Launch Vehicle. We launched an improved version of our sounding rocket core, with batteries sturdy enough to survive in space for a bit more than one orbit. We sent this probe into a polar orbit, which provided us with invaluable knowledge of the orbital stability by tracking our satellite along its trajectory.")
    launch("RD103 AJ-10 SR 4", 1951, 12, 8, RD103AJ27SR, 
        Payload("SR-1.3H", ),SO, 0, "Routine Sounding Rocket mission with our dedicated rocket based on our orbital vehicle")
    launch("RD103 AJ-10 SR 5", 1951, 12, 14, RD103AJ27SR, 
        Payload("SR-1.3H", ),SO, 0, "Routine Sounding Rocket mission with our dedicated rocket based on our orbital vehicle")
    launch("RD103 AJ-10 SR 6", 1951, 12, 19, RD103AJ27SR, 
        Payload("SR-1.3H", ),SO, 0, "Routine Sounding Rocket mission with our dedicated rocket based on our orbital vehicle")
    launch("LV-1 Geyger survey", 1951, 12, 28, LV1, 
        Payload("Sat0", ),EA, 1, "After developing a geiger counter capable of operating in space, we tried to send it into a polar orbit to attain information of the radiation environment around the globe. Unfortunately the first stage engine failed early in the flight.")
    launch("RD103 AJ-10 SR 7", 1952, 1, 1, RD103AJ27SR, 
        Payload("SR-1.3H", ),SO, 0, "Routine Sounding Rocket mission with our dedicated rocket based on our orbital vehicle")
    launch("LV-1 Geiger survey 2", 1952, 1, 10, LV1, 
        Payload("Sat0", ),EPO, 0, "In the second try, we managed to put a geiger counter in a polar orbit around Earth. The data obtained by this experiment proved invaluable to our understanding of our magnetic field and the harshness of space.")    
    launch("RD103 AJ-10 SR 9", 1952, 1, 19, RD103AJ27SR, 
        Payload("SR-1.3H", ),SO, 0, "Routine Sounding Rocket mission with our dedicated rocket based on our orbital vehicle")
    launch("RD103 AJ-10 SR 10", 1952, 1, 24, RD103AJ27SR, 
        Payload("SR-1.3H", ),SO, 0, "Routine Sounding Rocket mission with our dedicated rocket based on our orbital vehicle")
    launch("LV-1 Controllable Sun-Sync", 1952, 2, 9, LV1Control, 
        Payload("Contr1Upper", ),SSO, 0, "To reach more specific orbits, we use this controllable upper stage core, to be able to use RCS to reach the specified Sun-synchronous orbit. The LV for that had to be expanded too, using a version of LV-1 with boosters")
    launch("RD103 AJ-10 SR 11", 1952, 2, 12, RD103AJ27SR, 
        Payload("SR-1.3H", ),EA, 1, "Routine Sounding Rocket mission with our dedicated rocket based on our orbital vehicle")
    launch("RD103 AJ-10 SR 12", 1952, 2, 17, RD103AJ27SR, 
        Payload("SR-1.3H", ),SO, 0, "Routine Sounding Rocket mission with our dedicated rocket based on our orbital vehicle")
    launch("RD103 AJ-10 SR 13", 1952, 2, 22, RD103AJ27SR, 
        Payload("SR-1.3H", ),SO, 0, "Routine Sounding Rocket mission with our dedicated rocket based on our orbital vehicle")
    launch("RD103 AJ-10 Heavy SR 1", 1952, 3, 10, RD103AJ27SRH, 
        Payload("SR-1.3H", ),SO, 0, "Routine Sounding Rocket mission with our dedicated rocket based on our orbital vehicle")
    launch("RD103 AJ-10 SR 14", 1952, 3, 11, RD103AJ27SR, 
        Payload("SR-1.3H", ),SO, 0, "Routine Sounding Rocket mission with our dedicated rocket based on our orbital vehicle")
    launch("RD103 AJ-10 SR 15", 1952, 3, 14, RD103AJ27SR, 
        Payload("SR-1.3H", ),SO, 0, "Routine Sounding Rocket mission with our dedicated rocket based on our orbital vehicle")
    launch("RD103 AJ-10 SR 16", 1952, 3, 18, RD103AJ27SR, 
        Payload("SR-1.3H", ),SO, 0, "Routine Sounding Rocket mission with our dedicated rocket based on our orbital vehicle")
    launch("RD103 AJ-10 SR 17", 1952, 3, 23, RD103AJ27SR, 
        Payload("SR-1.3H", ),SO, 2, "Routine Sounding Rocket mission with our dedicated rocket based on our orbital vehicle")
    launch("RD103 AJ-10 SR 18", 1952, 3, 27, RD103AJ27SR, 
        Payload("SR-1.3H", ),SO, 0, "Routine Sounding Rocket mission with our dedicated rocket based on our orbital vehicle")
    launch("RD103 AJ-10 SR 19", 1952, 3, 31, RD103AJ27SR, 
        Payload("SR-1.3H", ),SO, 0, "Routine Sounding Rocket mission with our dedicated rocket based on our orbital vehicle")
    launch("RD103 AJ-10 SR 20", 1952, 4, 5, RD103AJ27SR, 
        Payload("SR-1.3H", ),SO, 0, "Routine Sounding Rocket mission with our dedicated rocket based on our orbital vehicle")
    launch("RD103 AJ-10 SR 21", 1952, 4, 10, RD103AJ27SR, 
        Payload("SR-1.3H", ),SO, 0, "Routine Sounding Rocket mission with our dedicated rocket based on our orbital vehicle")
    launch("LV-1.5 Heavy - Luna 1!!", 1952, 5, 27, LV15HLuna, 
        Payload("Luna", "Lunar flyby","Lunar Impact"),LI, 0, "Our first, and amazingly sucessful Lunar Impact mission. Using our most massive rocket so far, this unguided TLI lunar impactor returned valuable science on the environment around the moon.")
    launch("LV-1.5 Heavy - Luna 2", 1952, 6, 1, LV15HLuna, 
        Payload("Luna", ),LI, 2, "Our second try at a lunar impact failed early during launch when one of the engines in our second stage failed to activate.")
    launch("RD103 AJ-10 SR 22", 1952, 5, 29, RD103AJ27SR, 
        Payload("SR-1.3H", ),SO, 0, "Routine Sounding Rocket mission with our dedicated rocket based on our orbital vehicle")
    launch("RD103 AJ-10 SR 23", 1952, 6, 2, RD103AJ27SR, 
        Payload("SR-1.3H", ),SO, 1, "Routine Sounding Rocket mission with our dedicated rocket based on our orbital vehicle")
    launch("LV-1.5 Light - Solar power", 1952, 6, 8, LV15Light, 
        Payload("Contr2Upper", ),EPO, 0, "Our prototype solar-powered craft. We adapted our Upper stage unit with a pair of solar cells to test if those work in space. Still not enough to keep our stage working indefinitely, but should be very useful in future launches of less demanding spacecraft.")


  
    print "%d launches recorded" % (len(launches),)
    return Database(launches)

if __name__ == '__main__':
    db = papydb()
    #test_html(db)
    #test_text(db)
    
    #serve_web(db, opts.port)
    serve_web(db, 8080)
        
