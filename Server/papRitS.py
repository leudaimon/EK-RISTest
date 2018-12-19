#!/usr/bin/python2
# encoding: utf-8
from pap import *

def papydb():
  
  ###############################
  # ENGINE FAMILIES
  ###############################
  Aerobee = EngineFamily("Aerobee", "Early pressure-fed hypergolic (aniline/furfuryl/nitric) engine originally for sounding rockets.", vac=True)
  TinyTim = EngineFamily("Tiny Tim Booster", "Very early solid-fueled booster. Used for boosting first stages of Sounding Rockets.")
  RD100 = EngineFamily("RD-100 Series", "Early LOx / Alcohol rocket engine family that is a copy of the German V-2.")

  # Engines
  WAC = Engine("WAC Corporal", Aerobee, vac=True)
  XASR = Engine("XASR-1", Aerobee, vac=True)
  TinyTimBooster = Engine("Tiny Tim", TinyTim)
  RD_100 = Engine("RD-100", RD100)
  RD_101 = Engine("RD-101", RD100)
  

  ###############################
  # STAGE FAMILIES
  ###############################
  FleaStgFamily = StageFamily("Flea Family", Aerobee, "The Jumping Flea is a unique design created by our engineers.")
  LightningStgFamily = StageFamily("Lightning", Aerobee, "Designation for the earliest sounding rocket stages.", vac=True)
  EarlyBoostStgFamily = StageFamily("Early SR Booster", TinyTim, "Designation for the very early solid-fueled booster stages for Sounding Rockets.")
  WakeIslandStgFamily = StageFamily("Wake Island", RD100, "This family of stages is 1.65m diameter using the RD-100 series of engines.")
  NimitzStgFamily = StageFamily("Nimitz", RD100, "2m first stages using dual RD-100 Series engines.")

  # Stages
  FleaStage = Stage("Flea Stage", FleaStgFamily, WAC, "First science craft.")
  LightningWAC = Stage("Lightning-WAC", LightningStgFamily, WAC, "Earliest sounding rocket stage.")
  LightningXASR = Stage("Lightning-XASR", LightningStgFamily, XASR, "Light sounding rocket stage which is an improvement on the Lightning-I.")
  TinyTimStage = Stage("Tiny Tim Booster", EarlyBoostStgFamily, TinyTimBooster, "Solid boost stage for early sounding rockets.")
  WakeIslandIStage = Stage("Wake Island I", WakeIslandStgFamily, RD_100, "RD-100 powered first stage.")
  WakeIslandIIStage = Stage("Wake Island II", WakeIslandStgFamily, RD_101, "RD-101 powered first stage.")
  NimitzStage = Stage("Nimitz I", NimitzStgFamily, RD_101, "Dual RD-101 powered first stage.")
  


  ###############################
  # LAUNCH VEHICLE FAMILIES
  ###############################
  Flea = LVFamily("The Flea", "First science craft.", FleaStgFamily)
  Lightning = LVFamily("Lightning", "First sounding rocket family of launch vehicles.", LightningStgFamily)
  WakeIsland = LVFamily("Wake Island", "1.65m suborbital sounding rocket family of launch vehicles.", WakeIslandStgFamily)
  CoralSea = LVFamily("Coral Sea", "Family of two-stage sounding rockets.", WakeIslandStgFamily)
  Midway = LVFamily("Midway", "Family of 60t early orbital rockets.", WakeIslandStgFamily)
  
  # LAUNCH VEHICLES
  JumpingFlea = LV("Jumping Flea", Flea, "Specially designed launch vehicle designed for maximum science gain.", FleaStage)
  LightningI = LV("Lightning-I", Lightning, "Earliest sounding rocket launch vehicle designed to get past the Karman Line and bring back valuable science.", TinyTimStage, LightningWAC)
  WakeIslandI = LV("Wake Island-I", WakeIsland, "Early Wake Island family launch vehicle designed to reach space and return science data.", WakeIslandIStage)
  WakeIslandII = LV("Wake Island-II", WakeIsland, "Stretched Wake Island launch vehicle used in both crewed missions and sounding rocket missions.", WakeIslandIIStage)
  LightningII = LV("Lightning-II", Lightning, "Stretched Lightning-I light sounding rocket vehicle with improved performance.", TinyTimStage, LightningXASR)
  CoralSeaI = LV("Coral Sea-I", CoralSea, "Two-stage Sounding Rocket that combines a Wake Island and Lightning stage for high altitude contracts.", WakeIslandIIStage, LightningXASR)


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



  
  print "%d launches recorded" % (len(launches),)
  return Database(launches)

if __name__ == '__main__':
    db = papydb()
    #test_html(db)
    #test_text(db)
    
    #serve_web(db, opts.port)
    serve_web(db, 8080)
        