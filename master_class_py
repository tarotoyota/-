def except_for(items, exceptions):
    return [item for item in items if item not in exceptions]

cause_of_death  =["suicide","murder","killed in battle","death from starvation","death from illness","death penalty"]
type_of_sentence=["life sentence","death penalty","prison sentence","fine"]
food_negative   =["food poisoning, food waste, obesity, diabetes"]
work_negative   =["low wage, long hour working, work-related accident, working poor"]
house_negative  =["house collapse, the amount of damage caused by disaster"]
elderly_negative=["cancer patient, dementia patient, death from adult disease"]
school_negative =["collage dropout, high school dropout, junior high school dropout"]
medical_negative=["medical accident, overprescription, prescription drug dependence"]

class class_pp:
    def __init__ (self, p_name, p_genre, NMB_M, NMB_F)->None:
        self.p_name = p_name
        self.p_genre = p_genre
        self.NMB_M  = NMB_M# p_name is many but NMB_M is many
        self.NMB_F  = NMB_F# p_name is few  but NMB_F is few. NMB_M is many but NMB_F is few.

pp_suicide              =class_pp("suicide"              ,["death"]         ,"",[except_for(cause_of_death, ["suicide"]                ), "suicide lifeline user"]                                  )
pp_murder               =class_pp("murder"               ,["death","crime"] ,"",[except_for(cause_of_death, ["murder"]                 ), "attempted murder, fatal injury, rape murder"]            )
pp_killed_in_battle     =class_pp("killed in battle"     ,["death"]         ,"",[except_for(cause_of_death, ["killed in battle"]       ), "war wounded"]                                            )
pp_death_from_starvation=class_pp("death from starvation",["death"]         ,"",[except_for(cause_of_death, ["death from starvation"]  ), food_negative]                                            )
pp_death_from_illness   =class_pp("death from illness"   ,["death"]         ,"", except_for(cause_of_death, ["death from illness"]     )                                                            )
pp_death_penalty        =class_pp("death penalty"        ,["death"]         ,"",[except_for(cause_of_death, ["death penalty"]          ), except_for(type_of_sentence, ["death penalty"]),"inmates"])
pp_early_death          =class_pp("early death"          ,["death"]         ,"",[cause_of_death, elderly_negative]                                                                                  )

pp_illiteracy           =class_pp("illiteracy"           ,""                ,"",school_negative)
pp_medically_underserved=class_pp("medically underserved",""                ,"",medical_negative)

pp_rape                 =class_pp("rape"                 ,"crime"           ,"","attempted rape, rape murder")
pp_robbery              =class_pp("robbery"              ,"crime"           ,"","attempted robbery, murder-robbery")
pp_prisoner             =class_pp("criminal"             ,"crime"           ,"","bum")
pp_police_corruption    =class_pp("police corruption"    ,""                ,"","clearance, criminal, crime, inmate")
pp_capital_crime        =class_pp("capital crime"        ,"crime"           ,"",except_for(type_of_sentence, ["death penalty", "life sentence"]))

pp_unemployed           =class_pp("unemployed"           ,""                ,"",work_negative                         )
pp_bum                  =class_pp("bum"                  ,""                ,"",[work_negative, house_negative]       )
pp_forced_labor         =class_pp("forced_labor"         ,""                ,"",["unemployed","bum"]                  )
pp_relocation           =class_pp("relocation"           ,""                ,"",["unemployed","bum",house_negative]   )

#if "death" in y_p_genre:
#

#if y_p_genre == "crime":
#   y_NMB_M+="clearance rate"
#NM_positive #disable-disable support #murder-clearance rate
#pp_pl collapsed. x p_name was killed.
#pp_pl collapsed. There were x casualities. The crew and passengers were safe.
#traffic report and x
#weather and x
#(suggest) x today
#

#.wt の有無で単語類似度を測れる？
class class_depend:
    def __init__ (self, each, wt, content, thirst, annual) -> None:
        self.each, self.wt, self.content, self.thirst, self.annual =each, wt, content, thirst, annual
                             #each,wt               ,content           ,thirst             ,annual
de_alcohol      =class_depend("y",""                ,"alcohol content" ,"your thirst"      ,"bottle, liter"     )
de_disinfectant =class_depend("y",""                ,"alcohol content" ,""                 ,"bottle, liter"     )
de_dog          =class_depend("" ,"33 lbs, 3 feet"  ,""                ,""                 ,"heads"             )
de_meat         =class_depend("y","1 pound"         ,""                ,"your hunger"      ,"ton"               )
de_lube         =class_depend("y",""                ,""                ,"your penis size"  ,""                  )
de_butter       =class_depend("y",""                ,""                ,""                 ,""                  )
de_pocket_pussy =class_depend("" ,"0.5 pound"       ,""                ,""                 ,""                  )
de_toilet_paper =class_depend("y",""                ,""                ,"your bowel movements frequency","roll" )

class class_c1:
    def __init__(self, Bani, Bsol, v_name, c_name, a_name, usage, hyper, hypo) -> None:
        self.Bani, self.Bsol = Bani, Bsol
        self.v_name, self.c_name, self.a_name = v_name, c_name, a_name
        self.usage=usage
        self.hyper, self.hypo = hyper, hypo
c1_livestock         =class_c1("y","y",""    ,"livestock"    ,"","livestock farming"     ,"animal"    ,"cow, broiler")
c1_dog               =class_c1("y","y",""    ,"dog"          ,"","playing with dog"      ,"animal"    ,"cogi, shepard")
c1_cat               =class_c1("y","y",""    ,"cat"          ,"","playing with cat"      ,"animal"    ,"Tabby, Siamese")
c1_pig               =class_c1("y","" ,""    ,"pig"          ,"","livestock farming"     ,"animal"    ,"Hampshire , Saddleback ")
c1_meat              =class_c1("" ,"y",""    ,"meat"         ,"","eating meat"           ,"food"      ,"beef, pork")
c1_fish              =class_c1("" ,"y",""    ,"fish"         ,"","eating fish"           ,"food"      ,"traut, tuna")
c1_vegetable         =class_c1("" ,"y",""    ,"vegetable"    ,"","eating vegetable"      ,"food"      ,"carrot, cucumber")
c1_butter            =class_c1("" ,"y",""    ,"butter"       ,"","tasting butter"        ,"food"      ,"margarine")
c1_energy_drink      =class_c1("" ,"y",""    ,"energy drink" ,"","drinking energy drink" ,"drink"     ,"Monster, RedBull")
c1_alcohol           =class_c1("" ,"y",""    ,"alcohol"      ,"","drinking alcohol"      ,"drink"     ,"Vodka, Whiskey")
c1_disinfectant      =class_c1("" ,"y",""    ,"disinfectant" ,"","disinfecting"          ,""          ,"Windex, Lysol")
c1_cold_medicine     =class_c1("" ,"y",""    ,"cold medicine","","drinking cold medicine",""          ,"NyQuil, DaiQuil")
c1_wetback           =class_c1("y","" ,""    ,"wetback"      ,"",""                      ,""          ,"")
c1_toilet            =class_c1("" ,"" ,""    ,"toilet"       ,"","shitting"              ,""          ,"")
c1_toilet_paper      =class_c1("" ,"" ,""    ,"toilet paper" ,"","shitting"              ,""          ,"")
c1_newspaper         =class_c1("" ,"y",""    ,"newspaper"    ,"","reading newspaper"     ,""          ,"broadsheet, tabloid")

c1_motorbike         =class_c1("" ,"y",""    ,"motorbike"    ,"","touring, racing"       ,""          ,"KAWASAKI, Aprilia, gorilla, NINJA")
c1_dildo             =class_c1("" ,"y",""    ,"dildo"        ,"","masturbating"          ,"sex toy"   ,"banana, hair brush handle")
c1_pocketpussy       =class_c1("" ,"y",""    ,"pocketpussy"  ,"","masturbating"          ,"sex toy"   ,"latex glove, pringles can")

c1_cardboard         =class_c1("" ,"y",""    ,"cardboard"    ,"","packing"               ,""          ,"")
c1_tent              =class_c1("" ,"y",""    ,"tent"         ,"","camping"               ,""          ,"")
c1_house             =class_c1("" ,"" ,""    ,"house"        ,"",""                      ,""          ,"")
c1_slave             =class_c1("y","y",""    ,"slave"        ,"",""                      ,"employment","")
c1_farming_tool      =class_c1("" ,"y",""    ,"farming tool" ,"","farming"               ,""          ,"hoe, plow")
c1_cockroach         =class_c1("y","" ,""    ,"cockroach"    ,"",""                      ,"animal"    ,"")
c1_gasoline          =class_c1("" ,"y",""    ,"gasoline"     ,"",""                      ,""          ,"premium, regular")
c1_cigarettes        =class_c1("" ,"y",""    ,"cigarettes"   ,"","smoking"               ,""          ,"Marlboro, Lucky Strike")
c1_employee          =class_c1("y","" ,""    ,"employee"     ,"","hiring"                ,""          ,"")



c1_fuck              =class_c1("" ,"y","fuck",""             ,"",""                      ,""          ,"")
c1_works             =class_c1("" ,"" ,"works",""            ,"",""                      ,""          ,"")
c1_rape              =class_c1("" ,"" ,"rape",""             ,"",""                      ,"crime"     ,"")
c1_rob               =class_c1("" ,"" ,"rob" ,""             ,"",""                      ,"crime"     ,"")
c1_steal             =class_c1("" ,"" ,"thief",""            ,"",""                      ,"crime"     ,"pickpocket, Burglary")
c1_hire              =class_c1("" ,"" ,"hire",""             ,"",""                      ,""          ,"")
c1_lube              =class_c1("" ,"y",""    ,"lube"         ,"","masturbating"          ,""          ,"")
c1_pedo              =class_c1("y","" ,""    ,"pedo"         ,"",""                      ,"human"     ,"")
c1_baby              =class_c1("y","" ,""    ,"baby"         ,"",""                      ,"human"     ,"")
c1_communism         =class_c1("" ,"" ,"","","communism"        ,"","political ideology, economic ideology" ,"")
c1_fascism           =class_c1("" ,"" ,"","","fascism"          ,"","political ideology"                    ,"")
c1_pseudoscience     =class_c1("" ,"" ,"","","pseudoscience"    ,"",""                                      ,"")
c1_conspiracy_theory =class_c1("" ,"" ,"","","conspiracy theory","",""                                      ,"")
c1_cult_religion     =class_c1("" ,"" ,"","","cult religion"    ,"","religion"                              ,"")
c1_gender_studies    =class_c1("" ,"" ,"","","gender studies"   ,"","social science"                        ,"")
c1_social_science    =class_c1("" ,"" ,"","","social science"   ,"",""                                      ,"")
c1_natural_science   =class_c1("" ,"" ,"","","natural science"  ,"",""                                      ,"")
c1_christianity      =class_c1("" ,"" ,"","","christianity"     ,"",""                                      ,"")
c1_islamism          =class_c1("" ,"" ,"","","islamism"         ,"",""                                      ,"")
c1_biology           =class_c1("" ,"" ,"","","biology"          ,"",""                                      ,"")
c1_darwinism         =class_c1("" ,"" ,"","","darwinism"        ,"",""                                      ,"")
c1_astronomy         =class_c1("" ,"" ,"","","astronomy"        ,"",""                                      ,"")
c1_democratic_party  =class_c1("" ,"" ,"","","democratic party" ,"","political party"                       ,"")
c1_republican_party  =class_c1("" ,"" ,"","","republican party" ,"","political party"                       ,"")
#def func1(func1_arg):
#    if "animate" in func1_arg.parameter:
#        print("That is animate")

class class_pl:
    def __init__(self, butcher, ubereats, hunting, rifle, forest, fridge, kitchen, seasoning) -> None:
        self.butcher  = butcher #physical locations where the item is sold.
        self.ubereats = ubereats#non-physical locations where the item is sold.
        self.hunting = hunting  #actions to obtain the item.
        self.rifle   = rifle    #tools necessary for the action to obtain the item.
        self.forest  = forest   #physical and non-commercial locations to obtain the item
        self.fridge  = fridge   #Where to store the item.
        self.kitchen = kitchen  #If the item is consumable and usable, where it is consumed/used.
        self.seasoning = seasoning#Things that are often purchased or acquired at the same time when purchasing or acquiring that item, or things that are often consumed or used at the same time when consuming or using that item.

        #butcher と kitchen がカブるなら両方のアイテムを同一にしてよい
        #cheaper と bail をどうリンクさせるか？
                      #butcher                                 ,ubereats   ,hunting             ,rifle                ,forest                          ,fridge                                              ,kitchen                                  ,seasoning
pl_rob         =class_pl("shop, bank"                          ,""         ,""                  ,""                   ,"dark alley, phone dead zone"   ,""                                                  ,"shop, bank, dark alley, phone dead zone",""                             )
pl_steal       =class_pl(pl_rob.butcher                        ,""         ,""                  ,""                   ,"empty house"                   ,""                                                  ,[pl_rob.kitchen, "empty house"]          ,""                             )
pl_fuck        =class_pl("brothel"                             ,"Tinder"   ,"picking up"        ,"pick up coach"      ,"pick up spot"                  ,""                                                  ,"bed room"                               ,"condom, lube, viagra, sex toy")
pl_rape        =class_pl(""                                    ,""         ,""                  ,""                   ,pl_rob.forest                   ,""                                                  ,"dark alley, phone dead zone"            ,pl_fuck.seasoning              )
pl_hire        =class_pl(""                                    ,"LinkedIn" ,"job interview"     ,"wanted ad, salary"  ,"career fair"                   ,""                                                  ,"office"                                 ,""                             )
pl_employee    =class_pl(""                                    ,"LinkedIn" ,"job interview"     ,"wanted ad, salary"  ,"career fair"                   ,""                                                  ,"office"                                 ,""                             )
pl_works       =class_pl(""                                    ,"LinkedIn" ,"job interview, job hunting","GPA"        ,"career fair"                   ,""                                                  ,"office"                                 ,""                             )

pl_motorbike   =class_pl("motorbike shop"                      ,""         ,""                  ,"drive license"      ,""                              ,"roadside, parking, garage"                         ,"roadway"                                ,"helmet, bike lock")
pl_dildo       =class_pl("sex toy shop, brothel"               ,"Punternet","picking up"        ,"present, dating"    ,"pick up spot"                  ,"bedside drawer"                                    ,"toilet, bed"                            ,"condom, lube, porn"           )#instance_z.Baniがyだった場合に特別な関数でメンバ変数を追加
pl_pocketpussy =class_pl("sex toy shop, brothel"               ,"Punternet","picking up"        ,"present, dating"    ,"pick up spot"                  ,"bedside drawer"                                    ,"toilet, bed"                            ,"condom, lube, porn, viagra"   )#instance_z.Baniがyだった場合に特別な関数でメンバ変数を追加
pl_lube        =class_pl("sex toy shop"                        ,""         ,""                  ,""                   ,""                              ,"bedside drawer"                                    ,"toilet, bed"                            ,"condom, viagra, sextoy, porn" )
pl_pedo        =class_pl(""                                    ,""         ,"adoption, birthing",""                   ,""                              ,"nursey, kindergarden, child's room, park"          ,""                                       ,"toy, school bag"                                       )
pl_baby        =class_pl(""                                    ,""         ,"adoption, birthing",""                   ,""                              ,"nursey, incuvator, baby bed, child's room"         ,""                                       ,"lattle, diaper, baby bed"                              )
pl_livestock   =class_pl("farm, slaughterhouse"                ,""         ,"breeding"          ,"trap"               ,""                              ,"barn, sty"                                         ,""                                       ,"trough, feeder, ear ID tag, fodder, farming equipment" )
pl_dog         =class_pl("pet store"                           ,""         ,"adoption"          ,""                   ,"animal shelter, adoption event","kennel, pet cage"                                  ,""                                       ,"pet bowl, dog food, frisbee, collar, muzzle"           )
pl_cat         =class_pl("pet store"                           ,""         ,"adoption"          ,""                   ,"animal shelter, adoption event","cat house, pet cage"                               ,""                                       ,"pet bowl, cat food, cat tower"                         )
pl_meat        =class_pl("butcher, restaurant, grocery"        ,"UberEats" ,"hunting"           ,"hunting rifle"      ,"forest"                        ,"fridge, dish, dining table, foam tray, takeout box","kitchen"                                ,"recipe book, seasoning, kitchen utensils, kitchenware, side dish")
pl_fish        =class_pl("fish market, restaurant, grocery"    ,"UberEats" ,"fishing"           ,"fishing rod, bait"  ,"sea, river"                    ,["cooler box", pl_meat.fridge]                      ,"kitchen"                                ,pl_meat.seasoning                                       )
pl_vegetable   =class_pl("farmer's market, restaurant, grocery","UberEats" ,"farming"           ,"farming tool, farm" ,"forest"                        ,pl_meat.fridge                                      ,"kitchen"                                ,"seasoning, kitchen utensils, kitchenware, main dish"   )
pl_butter      =class_pl("grocery"                             ,""         ,""                  ,""                   ,""                              ,"fridge, butter dish"                               ,"kitchen"                                ,"butter knife, butter dish, bread"                      )
pl_wetback     =class_pl(""                                    ,""         ,""                  ,""                   ,"US-MEX boarder"                ,""                                                  ,""                                       ,""                                                      )
pl_energy_drink=class_pl("grocery"                             ,""         ,""                  ,""                   ,""                              ,"fridge, drink holder, next to homework, desk"      ,"workplace、workdesk"                    ,"computer, textbook, homework"                          )
pl_alcohol     =class_pl("bar, liquor store"                   ,""         ,""                  ,""                   ,"drinking party"                ,"fridge, drink holder, ice bucket"                  ,""                                       ,"snack, lemon wedge, muddler, chaser, straw, shot glass, cocktail recipe book")
pl_disinfectant=class_pl("pharmacy"                            ,""         ,""                  ,""                   ,""                              ,"medicine cabinet"                                  ,"toilet"                                 ,"hand paper, disinfect wipe"                            )
pl_cold_medicine=class_pl("pharmacy, clinic"                   ,""         ,"see a doctor"      ,"prescription"       ,""                              ,"medicine cabinet, first-aid kit"                   ,""                                       ,"a cup of water")
pl_toilet      =class_pl("toilet store"                        ,""         ,""                  ,""                   ,"public toilet"                 ,""                                                  ,""                                       ,"toilet paper, plunger")
pl_toilet_paper=class_pl(""                                    ,""         ,""                  ,""                   ,""                              ,"toilet paper holder"                               ,""                                       ,"toilet, plunger")
pl_newspaper   =class_pl("newsstand"                           ,""         ,"subscription"      ,""                   ,""                              ,"mailbox, post"                                     ,""                                       ,"")
pl_cardboard   =class_pl(""                                    ,""         ,""                  ,""                   ,"cardboard recycle station"     ,""                                                  ,""                                       ,"tape gun, box cutter, cushioning material")
pl_tent        =class_pl("camp gear shop"                      ,""         ,""                  ,""                   ,""                              ,""                                                  ,"camp site"                              ,"lantern, camping stove, camping smoker")
pl_house       =class_pl("realtor"                             ,""         ,"renting"           ,""                   ,"residental area"               ,""                                                  ,""                                       ,"mailbox, welcome mat, door knocker")
pl_slave       =class_pl("slave market, slave state"           ,""         ,"slave raiding"     ,""                   ,"Africa"                        ,"slave quarters"                                    ,"farm, plantation"                       ,"whip, chain, shackles")
pl_farming_tool=class_pl("farming tool store"                  ,""         ,""                  ,""                   ,""                              ,"farming tool shed"                                 ,"farm"                                   ,"seeds, fertilizer")
pl_cockroach   =class_pl(""                                    ,""         ,""                  ,""                   ,"damp areas, sewer, cracks in walls",""                                              ,""                                       ,"")
pl_gasoline    =class_pl("gas station"                         ,""         ,""                  ,"gas pump"           ,""                              ,"gas can"                                           ,"car, Fuel filler"                       ,"car, gas can, fuel additive, tire pressure gauge, Fuel filler")
pl_cigarettes  =class_pl("convenience store, gas station, tobacco shop","" ,""                  ,""                   ,""                              ,"cigarette case"                                    ,"smoking area, smoking section, ashtray" ,"lighter, ashtray, matches, rolling paper")


class class_spt:
    def __init__(self, hammer, nail, DIY, DIY_boom, toolbox) -> None:
        self.hammer, self.nail, self.DIY, self.DIY_boom, self.toolbox = hammer, nail, DIY, DIY_boom, toolbox
spt_rob =class_spt("hammer, bat, knife"            ,"nail, glove, glove, cutting board" ,"DIY, playing baseball, cooking" ,"DIY boom, baseball boom, cooking boom","toolbox, knife block")
spt_fuck=class_spt("Tinder, present, GUCCI"        ,""                                  ,""                               ,""                                     ,""                    )
spt_rape=class_spt(["ice cream van",spt_rob.hammer],["ice cream",spt_rob.nail]          ,["selling ice cream",spt_rob.DIY],spt_rob.DIY_boom                       ,spt_rob.toolbox       )

class class_r1:
    def __init__(self, risk1, risk1_pre_n, risk1_pre_v, risk1_post_n) -> None:
        self.risk1        = risk1
        self.risk1_pre_n  = risk1_pre_n
        self.risk1_pre_v  = risk1_pre_v
        self.risk1_post_n = risk1_post_n
                        #risk1                                                                                               #risk1_pre_n                              ,risk1_pre_v                                                                       ,risk1_post_n
r1_livestock=class_r1("zoonotic disease"                                                                                     ,"zoonotic vaccine"                       ,""                                                                                ,"abattage, culling"                          )
r1_pig      =class_r1("swine flu"                                                                                            ,"swine flu vaccine"                      ,""                                                                                ,"abattage, culling"                          )
r1_dog =class_r1("rabies"                                                                                                    ,"rabies vaccine"                         ,"get rabies vaccinated"                                                           ,"rabies hotline"                             )
r1_cat =class_r1("rabies"                                                                                                    ,"rabies vaccine"                         ,"get rabies vaccinated"                                                           ,"rabies hotline"                             )
r1_meat=class_r1("food poisoning, parasitic infection, obesity, diabetes, injury by gallstone, allergy shock, health damage caused by growth hormone","kitchen disinfectant, ice pack"         ,"properly (heat, freeze) it, check the (allergy facts, EXP date, label), choice organic ones","antidiarrheal, gastroenterology" )
r1_fish=class_r1(["mercury poisoning",r1_meat.risk1]                                                                         ,r1_meat.risk1_pre_n                      ,r1_meat.risk1_pre_v                                                               ,r1_meat.risk1_post_n                         )
r1_vegetable    =class_r1(["damage caused by pesticides",r1_meat.risk1]                                                      ,r1_meat.risk1_pre_n                      ,r1_meat.risk1_pre_v                                                               ,r1_meat.risk1_post_n                         )
r1_energy_drink =class_r1("liver disease, caffeine poisoning, diabetes, obesity, insomnia"                                   ,""                                       ,"also drink water, drink it before kneading"                                      ,""                                           )
r1_alcohol      =class_r1("liver disease, alcoholism, drunk drive, acute alcohol poisoning"                                  ,"chaser"                                 ,"also drink water, come by taxi instead of car"                                   ,"Uber, barf bag, alcoholism counseling"      )
r1_disinfectant =class_r1("accidental ingestion, ignition, dermatitis"                                                       ,""                                       ,"ventilate during use it, avoid fire during use it"                               ,""                                           )
r1_cold_medicine=class_r1("addiction, overprescription, overdose, side effects"                                              ,""                                       ,"observe the dosage, seek medical instructions"                                   ,""                                           )
r1_butter       =class_r1("trans fat acid, obesity, lactose allergic reaction"                                               ,""                                       ,""                                                                                ,""                                           )
r1_lube         =class_r1("Urinary-tract infection, dermatitis, bacterial vaginosis"                                         ,"patch test"                             ,"perform a patch test before use"                                                 ,"antihistamine, STI test kit, proctologist, urologist, calming cream")
r1_toilet       =class_r1("clogging"                                                                                         ,"plunger"                                ,"avoid flushing non-flushable items"                                              ,"plunger, plumber")
r1_toilet_paper =class_r1("clogging, irritation, hemorrhoids"                                                                ,"plunger, bidet"                         ,"gently wipe one’s butt"                                                          ,"plunger, plumber")
r1_gasoline     =class_r1("explosion, inhalation toxicity, ignition"                                                         ,"fire extinguisher"                      ,"use in well-ventilated areas, avoid smoking near it"                             ,"fire station, fire workers")
r1_cockroach    =class_r1("disease transmission"                                                                             ,"pest control, roach trap, Insecticide"  ,"keep the kitchen clean, seal food containers"                                    ,"pest control, Insecticide")
r1_cigarettes   =class_r1("lung cancer, respiratory diseases, heart disease, stroke, addiction"                              ,"smoking cessation programs, nicotine patch","quit smoking"                                                                 ,""                                           )
r1_employee     =class_r1("be damaged by (employee resignation/a strike/work related accident)"                              ,"high salary"                            ,"pay them high salary"                                                            ,""                                           )
r1_motorbike    =class_r1("traffic accident, be stole"                                                                       ,"motorbike insurance, bike lock, helmet" ,"lock it, obey the signal, use studless tires"                                    ,"Call a tow truck"                           )
r1_dildo      =class_r1("got (hemmorhoids, mucosal damage)"            ,"lube, condom","use (lube, condom)","proctology")
r1_pocketpussy=class_r1("got (mucosal damage, Urinary-tract infection)","lube, condom","use (lube, condom)","urology")
r1_rob  =class_r1("be (arrested/witnessed/called the police)"                                                                ,"balaclava, glove"                       ,"hide one’s face, erase one’s fingerprints, check the CCTV positions"             ,"bail, lawyer, standing mute"              )
r1_steal=class_r1(r1_rob.risk1                                                                                               ,r1_rob.risk1_pre_n                       ,r1_rob.risk1_pre_v                                                                ,r1_rob.risk1_post_n                        )
r1_fuck =class_r1("got (venereal, mucosal damage, impregnated), impregnated it"                                              ,"condom, lube, STI test kit"             ,"use condom, use lube, use STI test kit"                                          ,"proctologist, urologist, STI test kit"    )
r1_rape =class_r1([r1_fuck.risk1, r1_rob.risk1]                                                                              ,[r1_fuck.risk1_pre_n, r1_rob.risk1_pre_n],[r1_fuck.risk1_pre_v, r1_rob.risk1_pre_v,"Do not leave body fluids at the scene."],[r1_fuck.risk1_post_n, r1_rob.risk1_post_n])
r1_hire =class_r1("be damaged by (employee resignation/a strike/work related accident)"                                      ,"high salary"                            ,"pay them high salary"                                                            ,""                                         )
r1_house=class_r1("eviction, house collapse due to disaster, burglary","security system","","")
r1_slave        =class_r1("rebellion, escaping"        ,"","punish disobedience, increase security","slave catcher")
r1_farming_tool =class_r1("farming tool related injury","",""                                      ,""             )


class class_r2:#my dog got hemorrhoid
    def __init__(self, venereal, rape_alert, own_gun, abortionist) -> None:
        self.venereal, self.rape_alert, self.own_gun, self.abortionist = venereal, rape_alert, own_gun, abortionist
r2_rob  =class_r2("got PTSD, got injured"                                                 ,"CCTV, security sensor, gun, security guards" ,"avoid going out at night, prepare (CCTV/gun)"                              ,"police")
r2_steal=class_r2(""                                                                      ,r2_rob.rape_alert                             ,"brought my valuables with me, locked my (room, safe, vehicle)"             ,"police")
r2_fuck =class_r2("got (venereal, mucosal damage)"                                        ,"condom, lube, STI test kit"                  ,"use (lotion, condom), use STI test kit"                                    ,"abortionist, urologist, proctologist")
r2_rape =class_r2([r2_rob.venereal, r2_fuck.venereal, "be second raped, be honor killed"] ,"rape alert"                                  ,"avoid going out at night"                                                  ,[r2_fuck.abortionist, r2_rob.abortionist])
r2_hire =class_r2("work related accident, long hour working, low wage"                    ,"labor union"                                 ,"(organize, join) a labor union, call the Labor Standards Inspection Office","Labor Standards Inspection Office")

#Soviet lock fst
#The {} people are coming now. - Don't worry, I (have, took, brought) (rape alert, my valuables) (with me).

pla_restaurant    ="There are terrace seats","There are smoking sections","They allow takeout"
pla_butcher       ="They offer custom cuts","There is a daily special","There are organic options"
pla_bar           ="There is live music on Fridays","They host trivia nights","There are terrace seats"
pla_animal_shelter="There are adoption events","There are outdoor play areas","They organize fundraisers regularly"
pla_clinic        ="There are vaccination clinics on weekends","They offer weekend appointments"
pla_pharmacy      ="There are blood pressure screenings available","Their staff offers health consultations","They provide prescription delivery services"
pla_fishing_spot  ="They offer boat rentals","There is a quiet fishing pier","There is a bait shop nearby","They stock the pond regularly"

class class_c4:
    def __init__(self, unit, ti_inc, ti_dec, caco1, caco2, qP, qN, avoid, PLinfo, law) -> None: #Tom is a middle-class white man living in New York. Define instance variables for this class from Tom's perspective.
        self.unit=unit
        self.ti_inc=ti_inc#The timing when the demand and consumption of the item increases.
        self.ti_dec=ti_dec#The timing when the supply and consumption of the item decreases.
        self.caco1=caco1#The reason Tom cannot consume the item is due to Tom himself.
        self.caco2=caco2#The reason Tom cannot consume the item due to the item itself.
        self.qP=qP
        self.qN=qN
        self.avoid=avoid#The item itself should be avoided.
        self.PLinfo=PLinfo#Ignore this item
        self.law=law#Existing law related to the item itself.
c4_rob =class_c4(""                                                                  ,"increase in immigrant, recession","decrease in immigrant, construction of the Trump’s wall, toughening the law, strengthening patrols","be on (parole/probation)"                     ,""                     ,""                                     ,""                                                ,""                                        ,""                                  ,"")
c4_fuck=class_c4("minute, night"                                                     ,"baby boom"                       ,"STI pandemic"                                                                                     ,"have (ED/venereal), be married, be on NoFap"  ,""                     ,"tight, hot, young"                    ,"loose, ugly, old"                                ,""                                        ,""                                  ,"")
c4_rape=class_c4(""                                                                  ,c4_rob.ti_inc                     ,[c4_fuck.ti_dec, c4_rob.ti_dec]                                                                    ,[c4_fuck.caco1, c4_rob.caco1]                  ,""                     ,c4_fuck.qP                             ,"loose, ugly, old"                                ,""                                        ,""                                  ,"")
c4_hire=class_c4(""                                                                  ,"booming enocomy"                 ,"job shortage"                                                                                     ,"can't afford to hire employees"               ,""                     ,"skilled"                              ,"unskilled"                                       ,""                                        ,""                                  ,"")
c4_dog =class_c4("head"                                                              ,"pet boom"                        ,""                                                                                                 ,"have dog allergy"                             ,"have rabies"          ,"gentle, cute"                         ,"ferocious"                                       ,"chocolate, onion"                        ,pla_animal_shelter                  ,"Animal Welfare Act")
c4_cat =class_c4("head"                                                              ,"pet boom"                        ,""                                                                                                 ,"have cat allergy"                             ,"have rabies"          ,"gentle, cute"                         ,"ferocious"                                       ,"chocolate, onion"                        ,pla_animal_shelter                  ,"Animal Welfare Act")
c4_meat=class_c4("net weight, oz, lbs, calorie, for (x) days, serving, fillet, block","BBQ season"                      ,"vegan boom, zoonotic pandemic, food inflation"                                                    ,"be full, be on a diet, be vegan"              ,"be (rotten, spoiled)" ,"fresh, delicious, free-range, organic","spoiled, bad taste, non-free range, non-organic" ,"room temperature"                        ,[pla_butcher, pla_restaurant]       ,"Food Safety Act")
c4_fish=class_c4(c4_meat.unit                                                        ,"seafood boom"                    ,"overfishing, food inflation"                                                                      ,c4_meat.caco1                                  ,c4_meat.caco2          ,"fresh, delicious"                     ,"spoiled, bad taste"                              ,c4_meat.avoid                             ,[pla_fishing_spot, pla_restaurant]  ,c4_meat.law)
c4_vegetable    =class_c4("net weight, oz, lbs, calorie, for (x) days, serving"      ,"vegan boom"                      ,"bad harvest, food inflation"                                                                      ,"be full, be on a diet"                        ,c4_meat.caco2          ,"fresh, delicious, organic, non-GMO"   ,"spoiled, bad taste, non-organic, GMO"            ,""                                        ,[pla_restaurant]                    ,c4_meat.law)
c4_butter       =class_c4("cup, slice, spoonful"                                     ,""                                ,""                                                                                                 ,"have lactose allergy"                         ,c4_meat.caco2          ,c4_fish.qP                             ,c4_fish.qN                                        ,c4_meat.avoid                             ,""                                  ,c4_meat.law)
c4_energy_drink =class_c4("can, cup"                                                 ,"exam season"                     ,""                                                                                                 ,"have liver disease, be pregnant, be on a caffeine detox",""           ,"high caffeine content"                ,"low caffeine content"                            ,""                                        ,""                                  ,"")
c4_alcohol      =class_c4("shot, bottle"                                             ,"party season, end of year"       ,"dry law, prohibition era"                                                                         ,"be on the wagon, have liver disease, be pregnant, be driving later be a Muslim","","strong, soft"             ,"too strong, too soft"                            ,""                                        ,pla_bar                             ,"Alcohol Tax Law, dry law")
c4_disinfectant =class_c4("push, dime-size drop"                                     ,"pandemic"                        ,"pandemic"                                                                                         ,"be a Muslim"                                  ,""                     ,"high sanitizing power"                ,"low sanitizing power"                            ,"flame, high temperature, direct sunlight",pla_pharmacy                        ,"")
c4_cold_medicine=class_c4("sheet, tablet"                       ,"flu season"                           ,""                                                 ,""                                                 ,""                         ,"effective"                            ,"ineffective"                   ,""                ,pla_clinic,"")
c4_lube         =class_c4(""                                    ,""                                     ,""                                                 ,"be on NoFap, have skin disease, have venereal"    ,""                         ,"smooth"                               ,"sticky"                        ,""                ,"","")
c4_livestock    =class_c4("head"                                ,""                                     ,"zoonotic pandemic"                                ,"be vegan"                                         ,"has zoonotic disease"     ,"fat"                                  ,"thin"                          ,""                ,"","Livestock Regulation Act")
c4_pig          =class_c4("head"                                ,""                                     ,"swine flu pandemic"                               ,"be vegan, be Muslim"                              ,"has swine flu"            ,"fat"                                  ,"thin"                          ,""                ,"","Livestock Regulation Act")
c4_toilet       =class_c4(""                                    ,""                                     ,""                                                 ,""                                                 ,""                         ,"clean, fragrant"                      ,"dirty, stinky"                 ,""                ,"","")
c4_toilet_paper =class_c4("roll"                                ,""                                     ,"pandemic"                                         ,"have hemorrhoids"                                 ,"be too rough, be not soft","soft"                                 ,"rough"                         ,"roughly wipe one’s butt","","")
c4_newspaper    =class_c4("for (x) days, page"                  ,"major happening"                      ,"digitization, increase in subscription fees"      ,"be illiteracy"                                    ,"has low credibility"      ,"highly reliable, neutral"             ,"low credibility, biased"       ,""                ,"","")
c4_motorbike    =class_c4(""                                    ,"motorbike boom"                       ,""                                                 ,"have no driving lisence"                          ,"be too slow"              ,"fast, Good fuel efficiency"           ,"slow, poor fuel efficiency"    ,""                ,"","Traffic Safety Act")
c4_dildo        =class_c4(""                                    ,""                                     ,""                                                 ,"have hemmorhoid"                                  ,"too thick, too hard"      ,"thick, hard"                          ,"too thick, too hard"           ,""                ,"","")
c4_pocketpussy  =class_c4(""                                    ,""                                     ,""                                                 ,"have ED"                                          ,"too tight, too loose"     ,"tight, ease to wash"                  ,"too tight, loose, ease to wash",""                ,"","")
c4_cardboard    =class_c4("ply, sheet, box"                     ,"moving season"                        ,""                                                 ,""                                                 ,""                         ,""                                     ,""                              ,"moisture"        ,"","")
c4_tent         =class_c4(""                                    ,"camping boom"                         ,""                                                 ,""                                                 ,""                         ,"waterploof, windploof, warm, spacious","not (waterploof, windploof), not warm, narrow","" ,"","")
c4_house        =class_c4(""                                    ,"real estate bubble"                   ,"housing shortage"                                 ,""                                                 ,""                         ,"spacious"                             ,"narrow"                        ,""                ,"","Building Standards Law")
c4_slave        =class_c4("man"                                 ,"Invention of the cotton gin"          ,"civil war, 1865, abolition of slavery"            ,"be an abolitionist, be living in a freedom state" ,""                         ,"healthy, young"                       ,"unhealthy, old"                ,"rail load"       ,"","Fugitive Slave Law")
c4_farming_tool =class_c4(""                                    ,""                                     ,""                                                 ,""                                                 ,""                         ,"durable"                              ,"fragile"                       ,""                ,"","")
c4_gasoline     =class_c4("gallon, liter"                       ,"peak travel season"                   ,"oil shock, electric vehicle boom"                 ,""                                                 ,""                         ,"high octane"                          ,"low octane"                    ,"open flame"      ,"","Fuel Efficiency and Emission Standards Act")
c4_cigarettes   =class_c4("pack, carton"                        ,""                                     ,"Tobacco tax increase"                             ,"have lang cancer, be trying to quit smoking, be pregnant",""                  ,"light, strong"                        ,"too light, too strong"         ,"moisture"        ,"","Tobacco Control Act")#menthol
c4_employee     =class_c4(""                                    ,"booming enocomy"                      ,"job shortage"                                     ,"can't afford to hire employees"                   ,""                         ,"skilled"                              ,"unskilled"                     ,""                ,"","Labor Standards Act")


class class_no:
    def __init__(self, noti) -> None:
        self.noti=noti#What kind of text is written on the item's packaging or on the item itself?
no_meat         =class_no("No preservatives or additives, Free range, grass-fed, hormone free, Nutrition Facts:(x), Keep refrigerated., Allergen Information:(x), Total Fat:(x), Do not refreeze.,Net weight:(x),Use By (x)")
no_fish         =class_no("Product of Norway, Flash-frozen for freshness, Skinless and boneless fillets, No preservatives or additives, Nutrition Facts:(x), Keep refrigerated., Allergen Information:(x), Total Fat:(x), Do not refreeze.,Net weight:(x),Use By (x)")
no_vegetable    =class_no("No preservatives or additives, Organic, Locally sourced, Nutrition Facts:(x), Keep refrigerated., Allergen Information:(x), Do not refreeze.,Net weight:(x),Use By (x)")
no_alcohol      =class_no("Nutrition Facts:(x), Aged for 12 years in oak barrels., Crafted from the finest barley and spring water., Not for sale to persons under 21 years of age., ABV: (x) percent., Distilled and Bottled in (x)., Enjoy responsibly., Do not drive or operate machinery after consuming., Avoid consuming it if pregnant or nursing.")
no_disinfectant =class_no("Safe for septic systems, For external use only, Keep away from heat and flames, ventilate when in use, Complies with (local regulatory agency) guidelines")
no_butter       =class_no("Unsalted, Refrigerate after opening, Do not freeze")
no_lube         =class_no("Discontinue use if irritation occurs, Silicone-based formula, Enhances comfort and pleasure")
no_toilet       =class_no("Dual Flush, Lid Open, Adjust Water Pressure,  Flush after each use. Do not flush non-biodegradable items. flush only human waste and toilet paper.")
no_toilet_paper =class_no("Flushable, Septic-safe, 2-ply")
no_cardboard    =class_no("This side up")
no_cold_medicine=class_no("Non-drowsy formula, Relieves common cold symptoms, Dosage: (x) tablets every (y) hours, Do not exceed recommended dosage, Keep out of reach of children, Consult a doctor if symptoms persist.")
no_gasoline     =class_no("87, 89, 93, Diesel, Regural, Plus, Premium")
no_cigarettes   =class_no("Smoke contains carbon monoxide., No additives or preservatives., Tar and nicotine levels: (x) mg., No sale to individuals under 18 years old. Surgeon General's Warning: Smoking causes lung cancer, heart disease, and may complicate pregnancy.")

class class_bo:
    def __init__(self, bookC, bookP, persC, persP) -> None:#C stands for "common word", P stands for "proper word".
        self.bookC=bookC#What are books about this item commonly called?
        self.bookP=bookP#The specific name of the book about this item. It requires two items.
        self.persC=persC#What are the people who work on or associated with this item commonly called?
        self.persP=persP#Specific name of person working or associated with this item. It requires two items.
bo_dog               =class_bo("pet care guide"              ,"COMPLETE DOG CARE MANUAL, GOBERIAN DOG CARE GUIDE"              ,"keeper, breeder"    ,"")
bo_cat               =class_bo("pet care guide"              ,"COMPLETE CAT CARE MANUAL, GOBERIAN CAT CARE GUIDE"              ,"keeper, breeder"    ,"")
bo_meat              =class_bo("recipe book"                 ,"Famous Dave's Barbeque Party Cookbook, Serial Griller"          ,"butcher, chef"      ,"")
bo_fish              =class_bo("recipe book, fishing guide"  ,"One Dish Fish, The fisherman’s guidebook"                       ,"chef, fisherman"    ,"")
bo_vegetable         =class_bo("recipe book"                 ,"The Vegetable Gardener's Bible, Vegetarian Cooking for Everyone","chef, farmer, vegan","")
bo_alcohol           =class_bo("cocktail recipe book"        ,"COCKTAIL CODEX, Spirits and Cocktails"                          ,"bartendar"          ,"")
bo_livestock         =class_bo("livestock care guide"        ,"The Complete Guide to Raising Chickens"                         ,"farmer"             ,"")
bo_tent              =class_bo("camping guidebook"           ,"Mastering Camping, Where should we camp next?"                  ,"camper"             ,"")
bo_motorbike         =class_bo("motorbike magazine"          ,"Fast Bikes, Motor Cyclist"                                      ,"rider"              ,"")
bo_house             =class_bo("housing information magazine","rental HOUSING, TopHomes"                                       ,"realtor, resident"  ,"")
bo_agriculture       =class_bo("farming guidebook"           ,"The Non-toxic farming handbook, Farm Technical Manual"          ,"farmer"             ,"")
bo_communism         =class_bo("communism text"              ,"The Capital, The Communist Manifesto"                                                      ,"communist"                  ,"Lenin, Marx")
bo_fascism           =class_bo("fascism text, nazism text"   ,"Mein Kampf, The Myth of the Twentieth Century"                                             ,"fascist"                    ,"Hitler, Mussolini")
bo_pseudoscience     =class_bo("pseudoscience book"          ,"The Basic Book of the Theory and Practice of Scientology for Beginners"                    ,""                           ,"Erich von Daniken, L. Ron Hubbard")
bo_conspiracy_theory =class_bo("conspiracy theory book"      ,"One Hundred Proofs that the Earth is not a Globe. 5G: The Technology That Will Control Your Mind","conspiriologist"      ,"Alex Jones, Qanon, Milton Cooper")
bo_foolish           =class_bo(""                            ,"How to win 100% at roulette, Cure Cancer with Baking Soda"                                 ,""                           ,"")
bo_gender_studies    =class_bo("gender studies books"        ,"How to raise a feminist son, We Should All Be Feminists"                                   ,"gender theorist"            ,"Naomi Wolf, Tarana Burke")
bo_social_science    =class_bo("social science books"        ,"Escape From Freedom, The Protestant Ethic and the Spirit of Capitalism"                    ,"social scientist"           ,"Chomsky, Max Weber")
bo_natural_science   =class_bo("science textbook"            ,"The Elegant Universe, Biology: The Unity and Diversity of Life"                            ,"scientist"                  ,"Einstein, Turing")
bo_christianity      =class_bo("christianity text"           ,"The Bible"                                                                                 ,"believer, missionaly worker","The pope, Jesus")
bo_islamism          =class_bo("Islamic text"                ,"The Quran, Hadith"                                                                         ,"Muslim scholar, Imam"       ,"Prophet Muhammad")
bo_cult_religion     =class_bo("cult religious book"         ,"The Basic Book of the Theory and Practice of Scientology for Beginners, The Book of Mormon","cult religionist"           ,"Joseph Smith Jr., L. Ron Hubbard")
bo_comedy            =class_bo("joke books"                  ,"+600 Funniest Dad Jokes"                                                                   ,"comedian"                   ,"Ricky Gervais, Dave Chappelle")
bo_fantasy           =class_bo("fantasy novel"               ,"The Lord of the Rings, HalleyPotter"                                                       ,"fantasy novelist, fantasy enthusiast"   , "J.R.R. Tolkien, J.K.Rowling")
bo_horror            =class_bo("horror novel"                ,"Scary Tales: Midnight Scares, Nightmare Unleashed"                                         ,"horror novelist, horror enthusiast"     , "Stephen King, H.P. Lovecraft")
bo_crime_documentary =class_bo("crime documentary"           ,"Making a Murderer, The Mind of a Killer, Cold Case Chronicles"                             ,"documentarian, crime journalist"        , "Alex Gibney, Laura Ricciardi")
bo_biology           =class_bo("biology textbook"            ,"Biology: Concepts and Connections, The Origin of Species"                                  ,"biologist"                              , "Charles Darwin, Richard Dawkins")
bo_astronomy         =class_bo("astronomy textbook"          ,"The Big Picture, A Brief History of Time"                                                  ,"astronomer"                             , "Carl Sagan, Stephen Hawking")
bo_democratic_party  =class_bo("books related to democrat"   ,"Conversations with Joe, The Audacity of Hope"                                              ,"democrat"                               , "Joe Biden, Nancy Pelosi")
bo_republican_party = class_bo("books related to republican" ,"Our Journey Together, Sarah Palin Out of Nowhere"                                          ,"republican"                             , "Donald Trump, Sarah Palin")
bo_employee          =class_bo("employee training guidebook" ,"x"                                                                                       ,"x","")

class class_adj:
    def __init__(self, adj_name, protect, present, merch, tyex, tyexPL, tyexAN) -> None:
        self.adj_name=adj_name
        self.protect=protect
        self.present=present
        self.merch=merch
        self.tyex=tyex
        self.tyexPL=tyexPL
        self.tyexAN=tyexAN
#                       adj_name    ,protect(risk_pre_n1)                           ,present(risk_pre_n2)       , merch                             , tyex                                                                , tyexPL                                                                  , tyexAN
adj_stinky   =class_adj("stinky"   ,"gas mask"                                      ,"deodrizer"                ,"kimchi, surstromming"             ,"garbage, waste water, skunk, compost, pig, bum"                     ,"garbage dump, waste water plant, zoo, compost shed, pigsty, bum shelter","garbage collector, waste water plant worker, zookeeper, farmer, toilet cleaner, scatologist, bum")
adj_gross    =class_adj("gross"    ,"blindfold, vomit bag"                          ,"cosmetic surgery"         ,"splatter movie, war documentary"  ,"excrement, corpse, skin disease patient, burn patient, burnt corpse","compost, fire scene, traffic accident scene, burn unit"                 ,"coroner, skin doctor")
adj_scary    =class_adj("scary"    ,"blindfold, cross"                              ,""                         ,"horror movie, war documentary"    ,""                                                                   ,"battle field, grave yard"                                               ,"soldier, doper, robbery, serial killer")
adj_noisy    =class_adj("noisy"    ,"ear plug"                                      ,""                         ,"noise music"                      ,"chain saw, compactor, punk rock"                                    ,"construction site, punk rock concert"                                   ,"construction worker, punk rocker")
adj_dirty    =class_adj("dirty"    ,"vomit bag, disinfectant, vinyl glove, gas mask","disinfectant, deodrizer"  ,""                                 ,"excrement, compost, sty, garbage"                                   ,"toilet, compost, sty, dumpster"                                         ,"cockroach, mouse, raccoon, bum, toilet cleaner")#raccoon died by food poisoning
adj_bad_taste=class_adj("bad taste","vomit bag"                                     ,""                         ,""                                 ,""                                                                   ,"raw garbage, vomit, sand"                                               ,"cockroach, mouse, raccoon, bum")
adj_idiot    =class_adj("idiot"    ,""                                              ,"education"                ,""                                 ,"mouse, insect, Alabama University student, dog, baby, letard"       ,"Alabama University, Mentaly disabled group home"                        ,"mentaly disabled careworker")
adj_smart    =class_adj("smart"    ,""                                              ,""                         ,""                                 ,"scientist, Harvard University student, Einstein"                    ,"Harvard University, MENSA"                                              ,"MENSA members, scientists, professors")
adj_ugly     =class_adj("ugly"     ,"blindfold, vomit bag"                          ,"cosmetic surgery"         ,""                                 ,"burn patient, acid attack victim"                                   ,"cosmetic surgery clinic"                                                ,"coroner, skin doctor")
adj_maniac   =class_adj("maniac"   ,""                                              ,"psychotropic drugs, counseling, mental health care",""        ,"Dahmer, mentally disable person, serial killer"                     ,"Mental hospital. cult, Manson family"                                   ,"Dahmer, mentally disable person, serial killer, Psychiatrist")
#adj_thief    =class_adj("thief"    ,"")
#adj_rapist   =class_adj("rapist"   ,)
#adj_beauty   =class_adj("beauty"   ,"")
#(to ugly guy) When did you get acid attacked?


class Master_class:
    def __init__(self, pos, c1, pl, spt, r1, r2, c4, no, bo, adj, dep, shadow_y, pp) -> None:
        self.pos=pos
        self.c1=c1   if c1  is not None else class_c1("","","","","","","","")
        self.pl=pl   if pl  is not None else class_pl("","","","","","","","")
        self.spt=spt if spt is not None else class_spt("","","","","")
        self.r1=r1   if r1  is not None else class_r1("","","","")
        self.r2=r2   if r2  is not None else class_r2("","","","")
        self.c4=c4   if c4  is not None else class_c4("","","","","","","","","","")
        self.no=no   if no  is not None else class_no("")
        self.bo=bo   if bo  is not None else class_bo("","","","")
        self.adj=adj if adj is not None else class_adj("","","","","","","")
        self.dep=dep if dep is not None else class_depend("","","","","")
        self.shadow_y = shadow_y
        self.pp=pp   if pp  is not None else class_pp("","","","")


dog               =Master_class("cn", c1_dog         , pl_dog            , None    , r1_dog          , None   , c4_dog         , None             , bo_dog              ,None,de_dog         ,"",None)
cat               =Master_class("cn", c1_cat         , pl_cat            , None    , r1_cat          , None   , c4_cat         , None             , bo_cat              ,None,de_dog         ,"",None)
meat              =Master_class("cn", c1_meat        , pl_meat           , None    , r1_meat         , None   , c4_meat        , no_meat          , bo_meat             ,None,de_meat        ,"",None)
fish              =Master_class("cn", c1_fish        , pl_fish           , None    , r1_fish         , None   , c4_fish        , no_fish          , bo_fish             ,None,de_meat        ,"",None)
vegetable         =Master_class("cn", c1_vegetable   , pl_vegetable      , None    , r1_vegetable    , None   , c4_vegetable   , no_vegetable     , bo_vegetable        ,None,None           ,"",None)
butter            =Master_class("cn", c1_butter      , pl_butter         , None    , r1_butter       , None   , c4_butter      , no_butter        , None                ,None,de_butter      ,"",None)
energy_drink      =Master_class("cn", c1_energy_drink, pl_energy_drink   , None    , r1_energy_drink , None   , c4_energy_drink, None             , None                ,None,None           ,"",None)
alcohol           =Master_class("cn", c1_alcohol     , pl_alcohol        , None    , r1_alcohol      , None   , c4_alcohol     , no_alcohol       , bo_alcohol          ,None,de_alcohol     ,"",None)
disinfectant      =Master_class("cn", c1_disinfectant, pl_disinfectant   , None    , r1_disinfectant , None   , c4_disinfectant, no_disinfectant  , None                ,None,de_disinfectant,"",None)
cold_medicine     =Master_class("cn", c1_cold_medicine,pl_cold_medicine  , None    , r1_cold_medicine, None   , c4_cold_medicine, no_cold_medicine, None                ,None,None           ,"",None)
lube              =Master_class("cn", c1_lube        , pl_lube           , None    , r1_lube         , None   , c4_lube        , no_lube          , None                ,None,de_lube        ,"",None)
livestock         =Master_class("cn", c1_livestock   , pl_livestock      , None    , r1_livestock    , None   , c4_livestock   , None             , bo_livestock        ,None,None           ,"",None)
pig               =Master_class("cn", c1_pig         , pl_livestock      , None    , r1_pig          , None   , c4_pig         , None             , bo_livestock        ,None,None           ,"",None)
toilet            =Master_class("cn", c1_toilet      , pl_toilet         , None    , r1_toilet       , None   , c4_toilet      , no_toilet        , None                ,None,None           ,"",None)
toilet_paper      =Master_class("cn", c1_toilet_paper, pl_toilet_paper   , None    , r1_toilet_paper , None   , c4_toilet_paper, no_toilet_paper  , None                ,None,de_toilet_paper,"",None)
newspaper         =Master_class("cn", c1_newspaper   , pl_newspaper      , None    , None            , None   , c4_newspaper   , None             , None                ,None,None           ,"",None)
motorbike         =Master_class("cn", c1_motorbike   , pl_motorbike      , None    , r1_motorbike    , None   , c4_motorbike   , None             , bo_motorbike        ,None,None           ,"",None)
dildo             =Master_class("cn", c1_dildo       , pl_dildo          , None    , r1_dildo        , None   , c4_dildo       , None             , None                ,None,None           ,"",None)
pocketpussy       =Master_class("cn", c1_pocketpussy , pl_pocketpussy    , None    , r1_pocketpussy  , None   , c4_pocketpussy , None             , None                ,None,de_pocket_pussy,"",None)
cardboard         =Master_class("cn", c1_cardboard   , pl_cardboard      , None    , None            , None   , c4_cardboard   , no_cardboard     , None                ,None,None           ,"",None)
tent              =Master_class("cn", c1_tent        , pl_tent           , None    , None            , None   , c4_tent        , None             , bo_tent             ,None,None           ,"",None)
house             =Master_class("cn", c1_house       , pl_house          , None    , r1_house        , None   , c4_house       , None             , bo_house            ,None,None           ,"",None)
slave             =Master_class("cn", c1_slave       , pl_slave          , None    , r1_slave        , None   , c4_slave       , None             , bo_agriculture      ,None,None           ,"",None)
gasoline          =Master_class("cn", c1_gasoline    , pl_gasoline       , None    , r1_gasoline     , None   , c4_gasoline    , None             , None                ,None,None           ,"",None)
cockroach         =Master_class("cn", c1_cockroach   , pl_cockroach      , None    , r1_cockroach    , None   , None           , None             , None                ,None,None           ,"",None)
cigarettes        =Master_class("cn", c1_cigarettes  , pl_cigarettes     , None    , r1_cigarettes   , None   , c4_cigarettes  , no_cigarettes    , None                ,None,None           ,"",None)
employee          =Master_class("cn", c1_employee    , pl_employee       , None    , r1_employee     , r2_hire, c4_employee    , None             , bo_employee         ,None,None           ,"",None)

communism         =Master_class("an", c1_communism          , None              , None    , None            , None   , None           , None             , bo_communism        , None,None,"",None)
fascism           =Master_class("an", c1_fascism            , None              , None    , None            , None   , None           , None             , bo_fascism          , None,None,"",None)
pseudoscience     =Master_class("an", c1_pseudoscience      , None              , None    , None            , None   , None           , None             , bo_pseudoscience    , None,None,"",None)
conspiracy_theory =Master_class("an", c1_conspiracy_theory  , None              , None    , None            , None   , None           , None             , bo_foolish          , None,None,"",None)
foolish           =Master_class("an", c1_conspiracy_theory  , None              , None    , None            , None   , None           , None             , bo_conspiracy_theory, None,None,"",None)
cult_religion     =Master_class("an", c1_cult_religion      , None              , None    , None            , None   , None           , None             , bo_cult_religion    , None,None,"",None)
gender_studies    =Master_class("an", c1_gender_studies     , None              , None    , None            , None   , None           , None             , bo_gender_studies   , None,None,"",None)
social_science    =Master_class("an", c1_social_science     , None              , None    , None            , None   , None           , None             , bo_social_science   , None,None,"",None)
natural_science   =Master_class("an", c1_natural_science    , None              , None    , None            , None   , None           , None             , bo_natural_science  , None,None,"",None)
christianity      =Master_class("an", c1_christianity       , None              , None    , None            , None   , None           , None             , bo_christianity     , None,None,"",None)
islamism          =Master_class("an", c1_islamism           , None              , None    , None            , None   , None           , None             , bo_islamism         , None,None,"",None)
comedy            =Master_class("an", None                  , None              , None    , None            , None   , None           , None             , bo_comedy           , None,None,"",None)
fantasy           =Master_class("an", None                  , None              , None    , None            , None   , None           , None             , bo_fantasy          , None,None,"",None)
horror            =Master_class("an", None                  , None              , None    , None            , None   , None           , None             , bo_horror           , None,None,"",None)
crime             =Master_class("an", None                  , None              , None    , None            , None   , None           , None             , bo_crime_documentary, None,None,"",None)
biology           =Master_class("an", c1_biology            , None              , None    , None            , None   , None           , None             , bo_biology          , None,None,"",None)
darwinism         =Master_class("an", c1_darwinism          , None              , None    , None            , None   , None           , None             , bo_biology          , None,None,"",None)
astronomy         =Master_class("an", c1_astronomy          , None              , None    , None            , None   , None           , None             , bo_astronomy        , None,None,"",None)
democratic_party  =Master_class("an", c1_democratic_party   , None              , None    , None            , None   , None           , None             , bo_democratic_party , None,None,"",None)
republican_party  =Master_class("an", c1_republican_party   , None              , None    , None            , None   , None           , None             , bo_republican_party , None,None,"",None)


rob                     =Master_class(["v","pp"], c1_rob    , pl_rob            , spt_rob   , r1_rob          , r2_rob , c4_rob         , None             , None          ,None,None,""   ,pp_robbery)
steal                   =Master_class(["v","pp"], c1_steal  , pl_steal          , spt_rob   , r1_steal        , None   , c4_rob         , None             , None          ,None,None,""   ,None)
fuck                    =Master_class(["v","pp"], c1_fuck   , pl_fuck           , spt_fuck  , r1_fuck         , r2_fuck, c4_fuck        , None             , None          ,None,None,""   ,None)
rape                    =Master_class(["v","pp"], c1_rape   , pl_rape           , spt_rape  , r1_rape         , r2_rape, c4_rape        , None             , None          ,None,None,fuck ,pp_rape)
#hires                  =Master_class(["v","pp"], c1_hire   , pl_hire           , None      , r1_hire         , r2_hire, c4_hire        , None             , None          ,None,None,"")
suicide                 =Master_class("pp"      , None      , None              , None      , None, None, None, None, None, None, None, "", pp_suicide)
murder                  =Master_class("pp"      , None      , None              , None      , None, None, None, None, None, None, None, "", pp_murder)
killed_in_battle        =Master_class("pp"      , None      , None              , None      , None, None, None, None, None, None, None, "", pp_killed_in_battle)
death_from_starvation   =Master_class("pp"      , None      , None              , None      , None, None, None, None, None, None, None, "", pp_death_from_starvation)
death_from_illness      =Master_class("pp"      , None      , None              , None      , None, None, None, None, None, None, None, "", pp_death_from_illness)
death_penalty           =Master_class("pp"      , None      , None              , None      , None, None, None, None, None, None, None, "", pp_death_penalty)
early_death             =Master_class("pp"      , None      , None              , None      , None, None, None, None, None, None, None, "", pp_early_death)
illiteracy              =Master_class("pp"      , None      , None              , None      , None, None, None, None, None, None, None, "", pp_illiteracy)
medically_underserved   =Master_class("pp"      , None      , None              , None      , None, None, None, None, None, None, None, "", pp_medically_underserved)
unemployed              =Master_class("pp"      , None      , None              , None      , None, None, None, None, None, None, None, "", pp_unemployed)
bum                     =Master_class("pp"      , None      , None              , None      , None, None, None, None, None, None, None, "", pp_bum)
forced_labor            =Master_class("pp"      , None      , None              , None      , None, None, None, None, None, None, None, "", pp_forced_labor)
relocation              =Master_class("pp"      , None      , None              , None      , None, None, None, None, None, None, None, "", pp_relocation)

n                       =Master_class(""        , None      , None              , None      , None, None, None, None, None, None, None, "", "")


#stinky      =Master_class("adj", None          , None              , None    , None            , None   , None           , None             , None          ,adj_stinky     ,None,"")
#gross       =Master_class("adj", None          , None              , None    , None            , None   , None           , None             , None          ,adj_gross      ,None,"")
#scary       =Master_class("adj", None          , None              , None    , None            , None   , None           , None             , None          ,adj_scary      ,None,"")
#noisy       =Master_class("adj", None          , None              , None    , None            , None   , None           , None             , None          ,adj_noisy      ,None,"")
#dirty       =Master_class("adj", None          , None              , None    , None            , None   , None           , None             , None          ,adj_dirty      ,None,"")
#bad_taste   =Master_class("adj", None          , None              , None    , None            , None   , None           , None             , None          ,adj_bad_taste  ,None,"")
#idiot       =Master_class("adj", None          , None              , None    , None            , None   , None           , None             , None          ,adj_idiot      ,None,"")
#ugly        =Master_class("adj", None          , None              , None    , None            , None   , None           , None             , None          ,adj_ugly       ,None,"")
#maniac      =Master_class("adj", None          , None              , None    , None            , None   , None           , None             , None          ,adj_maniac     ,None,"")

#def get_words_Master_class():
#    instances_list = [name for name, obj_instance in globals().items() if isinstance(obj_instance, Master_class)]
#    return instances_list

def get_words_Master_class_cn():
    instances_list = [
        name for name, obj_instance in globals().items()
        if isinstance(obj_instance, Master_class) and 'cn' in getattr(obj_instance, 'pos', [])
    ]
    return instances_list

def get_words_Master_class_an():
    instances_list = [
        name for name, obj_instance in globals().items()
        if isinstance(obj_instance, Master_class) and 'an' in getattr(obj_instance, 'pos', [])
    ]
    return instances_list

def get_words_Master_class_v():
    instances_list = [
        name for name, obj_instance in globals().items()
        if isinstance(obj_instance, Master_class) and 'v' in getattr(obj_instance, 'pos', [])
    ]
    return instances_list

def get_words_Master_class_pp():
    instances_list = [
        name for name, obj_instance in globals().items()
        if isinstance(obj_instance, Master_class) and 'pp' in getattr(obj_instance, 'pos', [])
    ]
    return instances_list

def get_words_Master_class_v_pp():#
    instances_list = [
        name for name, obj_instance in globals().items()
        if isinstance(obj_instance, Master_class) and hasattr(obj_instance, 'pos') and obj_instance.pos in ['v', 'pp']
    ]
    return instances_list

