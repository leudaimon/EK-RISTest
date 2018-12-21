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
    RD100 = Engine("RD-100", A4Fam, vac=False)
    RD101 = Engine("RD-101", A4Fam, vac=False)


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
        [Picture("images/AS-361", "Our first rocket ready to be rolled out to the launch pad")])
    launch("Corporal-WAC - For space!", 1951, 1, 9, CorporalWAC, 
        Payload("TPT", "Karman Line (Uncrewed)"), SO, 0, "First flight into space, with a Corporal-WAC, the first design for a complete sounding rocket, with kick stage for better performance and control",
        [Picture("images/AS-366", "The space-capable Corporal-WAC ready to be rolled out to the launch pad")])
    launch("BioSample 1", 1951, 1, 21, RD100Bio, 
        Payload("BioSample", ),SO, 1, "Failed attempt at sending the first biological samples into space. The RD-100 engine shut down a few seconds after liftoff, and the payload reached only 9km of altitude.",
        [Picture("images/AS-495",""), Picture("images/AS-544",""), Picture("images/AS-548",""), Picture("images/AS-561","")])
    launch("BioSample 2", 1951, 2, 3, RD100Bio, 
        Payload("BioSample", ),SO, 0, "First biological samples into space, using the powerhouse RD-100 engine.",
        [Picture("images/AS-495",""), Picture("images/AS-588",""), Picture("images/AS-595",""), Picture("images/AS-602",""), Picture("images/AS-609","")])
    launch("Corporal-WAC 2", 1951, 2, 5, CorporalWAC, 
        Payload("TPT", ),SO, 0, "Further exploration of the nearby space with the Corporal-WAC sounding rocket")
    launch("Corporal-WAC 3", 1951, 2, 6, CorporalWAC, 
        Payload("TPT", ),SO, 0, "Further exploration of the nearby space with the Corporal-WAC sounding rocket")
    launch("Bumper 1", 1951, 2, 15, RD100WAC, 
        Payload("TPT", ),SO, -3, "With the first real two-stage rocket ever lauched, even this partial sucess broke several records. The vehicle lost some aerodynamic stability in the end of the first stage burn, going into a tumble. Still reached 665km ",
        [Picture("images/AS-657",""), Picture("images/AS-696",""), Picture("images/AS-697",""), Picture("images/AS-700",""), Picture("images/AS-704","")])
    launch("Bumper 2", 1951, 2, 23, RD100WAC, 
        Payload("TPT", ),SO, 0, "First complete success for a bumper launch. The vehicle reached more than 1000 km of altitude, and also broke speed records.",
        [Picture("images/AS-657","")])
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

  
    print "%d launches recorded" % (len(launches),)
    return Database(launches)

if __name__ == '__main__':
    db = papydb()
    #test_html(db)
    #test_text(db)
    
    #serve_web(db, opts.port)
    serve_web(db, 8080)
        
