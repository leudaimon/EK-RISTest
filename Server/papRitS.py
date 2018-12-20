#!/usr/bin/python2
# encoding: utf-8
from pap import *

def papydb():
  
    ###############################
    # ENGINES
    ###############################
    Aerobee = EngineFamily("Aerobee", "Early pressure-fed hypergolic (aniline/furfuryl/nitric) engine originally for sounding rockets.", vac=True)
    TinyTim = EngineFamily("Tiny Tim Booster", "Very early solid-fueled booster. Used for boosting first stages of Sounding Rockets.")
    RD100 = EngineFamily("RD-100 Series", "Early LOx / Alcohol rocket engine family that is a copy of the German V-2.")


    # Engines
    WAC = Engine("WAC Corporal", Aerobee, vac=True)
    XASR = Engine("XASR-1", Aerobee, vac=True)
    TinyTimBooster = Engine("Tiny Tim", TinyTim, vac=False)
    RD_100 = Engine("RD-100", RD100, vac=False)
    RD_101 = Engine("RD-101", RD100, vac=False)
    RD_102 = Engine("RD-102", RD100, vac=False)
    RD_103 = Engine("RD-103", RD100, vac=False)  


    ###############################
    # STAGES
    ###############################
    FleaStgFamily = StageFamily("Flea", Aerobee, "The Jumping Flea is a unique design created by our engineers.", vac=False)
    LightningStgFamily = StageFamily("Lightning Stage", Aerobee, "Designation for the earliest sounding rocket stages with single Aerobee Engines.", vac=True)
    EarlyBoostStgFamily = StageFamily("Early SR Boosters", TinyTim, "Designation for the very early solid-fueled booster stages for Sounding Rockets.", vac=False)
    WakeIslandStgFamily = StageFamily("Wake Island", RD100, "This family of stages is 1.65m diameter using the RD-100 series of engines.", vac=False)
    NimitzStgFamily = StageFamily("Nimitz", RD100, "2m first stage using dual RD-100 Series engines.", vac=False)
    SpruanceStgFamily = StageFamily("Spruance", Aerobee, "Upper Stage consisting of 4 x Aerobee Engines used on early orbiters.", vac=True)


    # Stages
    FleaStage = Stage("Flea Stage", FleaStgFamily, WAC, "First science craft.")
    LightningWAC = Stage("Lightning-WAC", LightningStgFamily, WAC, "Earliest sounding rocket stage.")
    LightningXASR = Stage("Lightning-XASR", LightningStgFamily, XASR, "Light sounding rocket stage which is an improvement on the Lightning-I and also used for the Yorktown Satellite missions.")
    TinyTimStage = Stage("Tiny Tim Booster", EarlyBoostStgFamily, TinyTimBooster, "Solid boost stage for early sounding rockets.")
    WakeIslandIStage = Stage("Wake Island I", WakeIslandStgFamily, RD_100, "RD-100 powered first stage.")
    WakeIslandIIStage = Stage("Wake Island II", WakeIslandStgFamily, RD_101, "RD-101 powered first stage.")
    WakeIslandIIIStage = Stage("Wake Island III", WakeIslandStgFamily, RD_102, "RD-102 powered 1.65m stage.")
    WakeIslandIVStage = Stage("Wake Island IV", WakeIslandStgFamily, RD_103, "RD-103 powered 2m stage.")
    SpruanceStage = Stage("Spruance Stage", SpruanceStgFamily, XASR, "4 x XASR-1 Engine powered upper stage.")
    NimitzIStage = Stage("Nimitz I", NimitzStgFamily, RD_101, "2 x RD-101 powered 2m first stage used on the early Midway launch vehicles.")
    NimitzIIStage = Stage("Nimitz II", NimitzStgFamily, RD_103, "2 x RD-103 powered 2m first stage used on the Midway launch vehicles.")  


    ###############################
    # LAUNCH VEHICLES
    ###############################
    Flea = LVFamily("The Flea", "First science craft.", FleaStgFamily)
    Lightning = LVFamily("Lightning", "First sounding rocket family of launch vehicles.", EarlyBoostStgFamily, LightningStgFamily)
    WakeIsland = LVFamily("Wake Island", "Suborbital sounding rocket family of launch vehicles.", WakeIslandStgFamily)
    CoralSea = LVFamily("Coral Sea", "Family of two-stage sounding rockets.", WakeIslandStgFamily, LightningStgFamily)
    Midway = LVFamily("Midway", "Family of 60t early orbital rockets.", NimitzStgFamily, WakeIslandStgFamily, SpruanceStgFamily, LightningStgFamily)

  
    # LAUNCH VEHICLES
    JumpingFlea = LV("Jumping Flea", Flea, "Specially designed launch vehicle designed for maximum science gain.", FleaStage)
    LightningI = LV("Lightning-I", Lightning, "Earliest sounding rocket launch vehicle designed to get past the Karman Line and bring back valuable science.", TinyTimStage, LightningWAC)
    LightningII = LV("Lightning-II", Lightning, "Stretched Lightning-I light sounding rocket vehicle with improved performance.", TinyTimStage, LightningXASR)
    WakeIslandI = LV("Wake Island-I", WakeIsland, "Early 1.65m Wake Island sounding rocket designed to reach space and return science data.", WakeIslandIStage)
    WakeIslandII = LV("Wake Island-II", WakeIsland, "Stretched Wake Island launch vehicle used in both crewed missions and sounding rocket missions.", WakeIslandIIStage)
    WakeIslandIII = LV("Wake Island-III", WakeIsland, "2m version of the Wake Island launch vehicle used for heavy lift sounding rocket missions.", WakeIslandIIIStage)
    WakeIslandIV = LV("Wake Island-IV", WakeIsland, "Stretched 2m version of the Wake Island heavy lift sounding rockets.", WakeIslandIVStage)
    CoralSeaI = LV("Coral Sea-I", CoralSea, "Two-stage Sounding Rocket that combines a Wake Island and Lightning stage for high altitude contracts.", WakeIslandIIStage, LightningXASR)
    MidwayI = LV("Midway-I", Midway, "First orbital rocket! This 4-stage design featured a Midway-I launch vehicle with the addition of a Sprunace Upper Stage and a Yorktown Satellite final stage.", NimitzIStage, WakeIslandIIStage, SpruanceStage, LightningXASR)
    MidwayII = LV("Midway-II", Midway, "Improved and stretched version of the Midway-I, this heavy sounding rocket features two-stages.", NimitzIIStage, WakeIslandIVStage)


    ###############################
    # LAUNCHES
    ###############################
    launches = []
    def launch(name, y, m, d, lv, payload, dest, result, comments=None, pics=None):
            launches.append(Launch(name, date(y, m, d), lv, payload, dest, result, comments, pics))
    def paren(text):
        return Payload(None, None, text)
    
    launch("Jumping Flea",        1951, 1,  4,    JumpingFlea,    None,
        EA, 0, "The Jumping Flea accomplished it's job by jumping off the launch pad and gathering 5.2 science points. The LV has been retired.")
    launch("Lightning-I Alpha",   1951, 1,  11,   LightningI,     None,
        SO, 0, "Completely successful inaugural flight of the Lightning-I Sounding Rocket. Reached apogee of 101km and successfully completed the Karman Line and Sounding Rocket (Easy) Contracts!",
        [Picture("images/lightning/alpha-01-liftoff.png", "Lift-off of the first rocket from the Marshall Islands"), Picture("images/lightning/alpha-02-stageSep.png", "Right after first stage separation of the Tiny Tim Booster."), Picture("images/lightning/alpha-03-ascent.png", "Ascent with the rising sun in the background."), Picture("images/lightning/alpha-04-closeUp.png", "A look at the beautifully designed Lightning-I"), Picture("images/lightning/alpha-05-karmanLine.png", "Apoapsis achieved above the Karman Line!")])
    launch("Lightning-I Bravo",   1951, 1,  17,   LightningI,     paren("20 SRP"),
        SO, 0, "Final Apoapsis of 92k exceeded the target altitude of 70k to fulfill a Sounding Rocket (Intermediate) contract.")
    launch("Hope I",              1951, 2,  5,    WakeIslandI,    Payload("Hope Cockpit", "Mission to Break the Sound Barrier", "Jebediah Kerman & Valentina Kerman"),
        EA, 0, "The brave pilots Jebediah and Valentina broke the Sound Barrier in this successful mission!",
        [Picture("images/hope/I-01-preLaunch.png", "Hope I sits on the pad awaiting liftoff."), Picture("images/hope/I-02-stageSep.png", "Cresting to top of arc after stage separation."), Picture("images/hope/I-03-chutes.png", "Soft landing for the brave pilots.")])
    launch("Wake Island I Alpha", 1951, 3,  14,   WakeIsland,     paren("Science Instruments"),
        SO, 0, "The Wake Island I experienced a successful mission and returned the valuable scientific payload. It became the first craft to reach space and return home safely.",
        [Picture("images/wake-island/alpha-01-preLaunch.png", "Wake Island I Alpha in pre-launch mode."), Picture("images/wake-island/alpha-02-maxQ.png", "Passing through Max Q"),Picture("images/wake-island/alpha-03-payload.png", "The important science payload."), Picture("images/wake-island/alpha-04-chutes.png", "Chutes deployed ending a successful mission.")])
    launch("Hope II",             1951, 4,  1,    WakeIslandI,    Payload("Hope Cockpit", "Mission to Reach Space", "Bob Kerman & Traby Kerman"),
        EA, -1, "This mission can be considered succesful as both brave pilots returnred home with a perfect landing right nexct to Mission Control, but it failed to achieve any objectives as there was a fuel mixture mistake in the VAB.",
        [Picture("images/hope/II-01-liftoff.png", "Hope II lifts off in an attempt to cross the Karman Line"), Picture("images/hope/II-02-descent.png", "Controlled descent for a targeted landing."), Picture("images/hope/II-03-landing.png", "Very impressive landing after a failed mission.")])
    launch("Lightning-II Alpha",  1951, 4,  3,    LightningII,    paren("21 SRP"),
        SO, 0, "Successful mission achieving an Apoapsis of 162km, returning valuable science and completing a Sounding Rocket (Difficult) contract.")
    launch("Hope III",            1951, 4,  25,   WakeIslandII,   Payload("Hope Cockpit", "Mission to Reach Space", "Jebediah Kerman & Traby Kerman"),
        SO, 0, "In one of the most daring missions ever attempted, these two brave ASTRONAUTS set out on a journey to heavens. By cresting to an apoapsis of 164km, they have become the first from the MSA to reach space and have now returned home safely.")
    launch("Lightning-II Bravo",  1951, 4,  26,   LightningII,    paren("50 SRP"),
        EA, 2, "Ignition Failure on the XASR-1 Engine. Range Safety activated at 899m.")
    launch("Lightning-II Charlie",1951, 4,  30,   LightningII,    paren("50 SRP"),
        SO, 0, "Successful sounding rocket mission completing the Sounding Rocket (Difficult) contract, but falling short of the 190km Altitude record by only reaching 164km.")
    launch("Lightning-II Delta",  1951, 5,  3,    LightningII,    paren("20 SRP"),
        SO, 0, "This launch achieved all goals set out for it. Accomplished a Sounding Rocket (Intermediate) contract and also reached 199.7km for a new altitude record.")
    launch("Wake Island II Alpha",  1951, 5,  23,    WakeIslandII,    paren("160 SRP"),
        SO, 1, "RD-101 engine failure and we only managed an Apoapsis of 11km before range safety destruction.")
    launch("Wake Island II Bravo",  1951, 6,  8,    WakeIslandII,    paren("160 SRP"),
        SO, 0, "Highly successful mission that accomplished the Sounding Rocket (Difficult) contract and set a new Altitude record of 230km.")
    launch("Wake Island II Charlie",  1951, 6,  22,    WakeIslandII,    paren("198 SRP"),
        SO, 0, "Another successful mission for this LV that accomplished the Sounding Rocket (Difficult) contract and set a new Altitude record of 290km.")
    launch("Wake Island II Delta",  1951, 7,  7,    WakeIslandII,    paren("284 SRP"),
        SO, 0, "Successful Mission passing 100km to fulfill the Sounding Rocket (Difficult) contract.")
    launch("Wake Island II Echo", 1951, 7, 21, WakeIslandII, paren("72 SRP"), SO, 0, "Successful mission completing the Sounding Rocket (Difficult) contract and setting a new Altitude record at 351km.")
    launch("Wake Island II Foxtrot", 1951, 8, 5, WakeIslandII, paren("36 SRP"), SO, 0, "Successful mission completing the Sounding Rocket (Difficult) contract and setting a new Altitude record at 421km.")
    launch("Wake Island II Golf", 1951, 8, 19, WakeIslandII, paren("458 SRP"), SO, 0, "Successful mission completing the Sounding Rocket (Difficult) contract.")
    launch("Wake Island II Hotel", 1951, 9, 1, WakeIslandII, paren("562 SRP"), SO, 0, "Successful mission completing the Sounding Rocket (Difficult) contract.")
    launch("Coral Sea I Alpha", 1951, 9, 24, CoralSeaI, None, SO, 2, "XASR-1 failed to ignite and the mission failed at 100km.")
    launch("Hope IV", 1951, 10, 9, WakeIslandII, Payload("Hope Cockpit", "Mission to Reach Space", "Jebediah Kerman & Bill Kerman"), SO, 0, "The crew of Jebediah Kerman and Bill Kerman reached an apoapsis of 158km and became the second crew to go to Space.")
    launch("Coral Sea I Bravo", 1951, 10, 18, CoralSeaI, None, SO, 0, "Successful mission setting a new altitude record of 505km.")
    launch("Hope V", 1951, 10, 24, WakeIslandII, Payload("Hope Cockpit", "Mission to Reach 80km", "Valentina Kerman & Traby Kerman"), EA, 0, "Successful flight that achieved an 80km apoapsis to fulfill a contract.")
    launch("Coral Sea I Charlie", 1951, 11, 2, CoralSeaI, paren("35 SRP"), SO, 0, "Successful mission setting a new altitude record of 650km and completing a Sounding Rocket (Easy) contract.")
    launch("Hope VI", 1951, 11, 8, WakeIslandII, Payload("Hope Cockpit", "Mission to Reach Space", "Jebediah Kerman & Bill Kerman"), SO, 0, "Successful mission, but our astronauts experienced a very difficult reentry and both wound up losing conciousness.")
    launch("Wake Island II India", 1951, 11, 14, WakeIslandII, paren("756 SRP"), SO, 0, "Successful mission completing the Sounding Rocket (Difficult) contract.")
    launch("Coral Sea I Delta", 1951, 11, 23, CoralSeaI, paren("92 SRP"), SO, 0, "Successful mission completing the Sounding Rocket (Difficult) contract and setting a new Altitude record at 728km.")
    launch("Coral Sea I Echo", 1951, 12, 2, CoralSeaI, paren("30 SRP"), SO, 0, "Successful mission completing the Sounding Rocket (Difficult) contract and setting a new Altitude record at 811km.")
    launch("Coral Sea I Foxtrot", 1951, 12, 9, CoralSeaI, paren("26 SRP"), SO, 0, "Successful mission completing the Sounding Rocket (Difficult) contract and setting a new Altitude record at 1051km.")
    launch("Wake Island II Juliet", 1951, 12, 13, WakeIslandII, paren("756 SRP"), SO, 0, "Successful mission completing the Sounding Rocket (Difficult) contract.")
    launch("Midway Yorktown 0-1", 1952, 1, 6, MidwayI, Payload("Yorktown 0-1", "First Orbital Satellite", "Modifed Lightning II Satellite Stage"), LEO, 2, "The second stage Wake Island II engine failed to ignite and range safety terminated the launch over the Pacific.")
    launch("Midway Yorktown 0-2", 1952, 1, 26, MidwayI, Payload("Yorktown 0-2", "First Orbital Satellite", "Modifed Lightning II Satellite Stage"), LEO, 1, "One of the first stage RD-101 engines shutdown early causing an unrecoverable trajectory that ended in a firey crash into the Pacific")
    ## FIRST ORBIT ##
    launch("Midway Yorktown 1", 1952, 2, 16, MidwayI, Payload("Yorktown 1", "First Orbital Satellite", "Modifed Lightning II Satellite Stage"), LEO, 0, "The Yorktown became the MSA's first satellite after entering into a very eccentric orbit on February 16, 1952. With enough battery for 12 orbits, great science data was received.", 
        [Picture("images/yorktown/01-pre-launch.png", "Midway Yorktown I Pre-Launch"), Picture("images/yorktown/02-gravity-turn.png", "Beginning the Gravity Turn"), Picture("images/yorktown/03-nose-camera.png", "Nose Camera shot down the length of the rocket"), Picture("images/yorktown/04-stage-sep.png", "First Stage Separation"), Picture("images/yorktown/05-stage-2-burn.png", "Wake Island-II Second Stage Burn"), Picture("images/yorktown/06-stage-3-burn.png", "Sprunace 3rd Stage Burn"), Picture("images/yorktown/07-first-satellite.png", "Yorktown I is the MSA's first satellite."), Picture("images/yorktown/08-daylight-terminator.png", "Crossing the Daylight Terminator"), Picture("images/yorktown/09-dark-side.png", "The Dark Side of the Earth")])
    launch("Midway Yorktown 0-3", 1952, 3, 7, MidwayI, Payload("Yorktown 0-3", "Polar Orbital Satellite", "Modifed Lightning II Satellite Stage"), LEO, 3, "Poor coding in the launch script caused vapor in the feedlines of the Aerobee engines that failed to light.")
    launch("Midway Yorktown 2", 1952, 3, 29, MidwayI, Payload("Yorktown 2", "Polar Orbital Satellite", "Modifed Lightning II Satellite Stage"), LEO, -1, "The angle of the probe when the final stage was fired was too high off the horizon and we missed orbit with an Ap 2380 km x Pe 135km. However, we made 10 orbits of Earth before burning up and returned a lot of science.")
    launch("Midway Yorktown 0-4", 1952, 4, 14, MidwayI, Payload("Yorktown 3", "Polar Orbital Satellite", "Modifed Lightning II Satellite Stage"), LEO, 3, "One XASR-1 engine failed in the 3rd stage causing a precession of the craft. The other engines managed to burn for an extended period of time, but the precession caused our inclination to go to 95.36 and we failed the mission.")
    launch("Midway Yorktown 3", 1952, 5, 2, MidwayI, Payload("Yorktown 3", "Polar Orbital Satellite", "Modifed Lightning II Satellite Stage"), LEO, 0, "The fourth polar orbit attempt was finally successful! Despite the success, the Polar Orbiting Satellite was not a financially profitable mission, but the scientific returns were tremendous.")
    launch("Wake Island III Alpha", 1952, 5, 5, WakeIslandIII, paren("310 SRP"), SO, 0, "Successful mission completing the Sounding Rocket (Difficult) contract.")
    launch("Wake Island III Bravo", 1952, 5, 8, WakeIslandIII, paren("1868 SRP"), EA, 0, "Successful mission completing the Sounding Rocket (Difficult) contract.")
    launch("Wake Island III Charlie", 1952, 5, 11, WakeIslandIII, paren("2000 SRP"), EA, 0, "Successful mission completing the Sounding Rocket (Difficult) contract.")
    launch("Wake Island III Delta", 1952, 5, 15, WakeIslandIII, paren("954 SRP"), SO, 1, "RD-101 Engine Failure")
    launch("Wake Island III Echo", 1952, 5, 17, WakeIslandIII, paren("954 SRP"), SO, 0, "Successful mission completing the Sounding Rocket (Difficult) contract.")
    launch("Wake Island III Foxtrot", 1952, 5, 21, WakeIslandIII, paren("1984 SRP"), SO, 0, "Successful mission completing the Sounding Rocket (Difficult) contract.")
    launch("Wake Island III Golf", 1952, 5, 24, WakeIslandIII, paren("944 SRP"), SO, 0, "Successful mission completing the Sounding Rocket (Difficult) contract.")
    launch("Wake Island III Hotel", 1952, 5, 30, WakeIslandIII, paren("938 SRP"), SO, 0, "Successful mission completing the Sounding Rocket (Difficult) contract.")
    launch("Wake Island III India", 1952, 6, 2, WakeIslandIII, paren("948 SRP to 550km"), SO, 0, "Successful mission completing the Sounding Rocket (Difficult) contract.")
    launch("Wake Island III Juliet", 1952, 6, 4, WakeIslandIII, paren("940 SRP to 660km"), SO, -1, "Did not have enough Delta-v and only reached 630km")
    launch("Wake Island IV Alpha", 1952, 6, 8, WakeIslandIV, paren("940 SRP to 660km"), SO, 1, "RD-102 Engine Failure")
    launch("Wake Island IV Bravo", 1952, 6, 11, WakeIslandIV, paren("940 SRP to 660km"), SO, -1, "Did not have enough Delta-v and only reached 650km")
    launch("Wake Island IV Charlie", 1952, 6, 14, WakeIslandIV, paren("940 SRP to 430km"), SO, 0, "Successful mission completing the Sounding Rocket (Intermediate) contract.")
    launch("Wake Island IV Delta", 1952, 6, 17, WakeIslandIV, paren("2000 SRP to 340km"), SO, 0, "Successful mission completing the Sounding Rocket (Difficult) contract.")
    launch("Wake Island IV Echo", 1952, 6, 24, WakeIslandIV, paren("592 SRP to 520km"), SO, 0, "Successful mission completing the Sounding Rocket (Intermediate) contract.")
    launch("Wake Island IV Foxtrot", 1952, 6, 25, WakeIslandIV, paren("1984 SRP to 420km"), SO, 0, "Successful mission completing the Sounding Rocket (Difficult) contract.")
    launch("Wake Island IV Golf", 1952, 6, 28, WakeIslandIV, paren("1994 SRP to 520km"), SO, 0, "Successful mission completing the Sounding Rocket (Difficult) contract.")
    launch("Midway II Alpha", 1952, 7, 12, MidwayII, paren("2016 SRP to 640km"), SO, 0, "Successful mission completing the Sounding Rocket (Difficult) contract.")
    launch("Midway II Bravo", 1952, 7, 21, MidwayII, paren("2006 SRP to 800km"), SO, 0, "Successful mission completing the Sounding Rocket (Difficult) contract.")
    launch("Midway II Charlie", 1952, 7, 28, MidwayII, paren("2006 SRP to 960km"), SO, 0, "Successful mission completing the Sounding Rocket (Difficult) contract.")



  
    print "%d launches recorded" % (len(launches),)
    return Database(launches)

if __name__ == '__main__':
    db = papydb()
    #test_html(db)
    #test_text(db)
    
    #serve_web(db, opts.port)
    serve_web(db, 8080)
        