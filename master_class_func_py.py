
import master_class_py
import re
import copy
def apply_color_styles(text):
    # Define patterns for replacement
    patterns = {
        #char color change
        r'(\零)([^<]*)': r'\1<span style="color: #CDD3DE; background-color: black;">\2</span>',
        r'(\一)([^<]*)': r'\1<span style="color: #CDD3DE;">\2</span>',
        r'(\二)([^<]*)': r'\1<span style="color: #F4E500; background-color: #FFA90514;">\2</span>',
        r'(\三)([^<]*)': r'\1<span style="color: #5CFF00; background-color: #1aff0012;">\2</span>',
        r'(\四)([^<]*)': r'\1<span style="color: #00DBFF; background-color: #00ffd90f;">\2</span>',
        r'(\五)([^<]*)': r'\1<span style="color: #ff9fb0; background-color: #ff03c212;">\2</span>',
        r'(\六)([^<]*)': r'\1<span style="color: #ffffff; background-color: #E9CEFF1C;">\2</span>',
        r'(\七)([^<]*)': r'\1<span style="color: #A099FB; background-color: #0313ff38;">\2</span>',
        r'(\八)([^<]*)': r'\1<span style="color: #ffeaea; background-color: #a4000047;">\2</span>',

    # indent color change
    r'\零': '<span style="color: black; background-color: black;">0</span>',
    r'\一': '<span style="color: #CDD3DE; background-color: #CDD3DE; font-size: 16px;">1</span>',
    r'\二': '<span style="color: #F4E500; background-color: #F4E500; font-size: 16px;">2</span>',
    r'\に': '<span style="color: #F4E500; background-color: #F4E500; font-size: 16px;">2</span>',
    r'\三': '<span style="color: #5CFF00; background-color: #5CFF00; font-size: 16px;">3</span>',
    r'\さ': '<span style="color: #5CFF00; background-color: #5CFF00; font-size: 16px;">3</span>',
    r'\四': '<span style="color: #00DBFF; background-color: #00DBFF; font-size: 16px;">4</span>',
    r'\よ': '<span style="color: #00DBFF; background-color: #00DBFF; font-size: 16px;">4</span>',
    r'\五': '<span style="color: #ff9fb0; background-color: #ff9fb0; font-size: 16px;">5</span>',
    r'\ご': '<span style="color: #ff9fb0; background-color: #ff9fb0; font-size: 16px;">5</span>',
    r'\六': '<span style="color: #ffffff; background-color: #ffffff; font-size: 16px;">6</span>',
    r'\ろ': '<span style="color: #ffffff; background-color: #ffffff; font-size: 16px;">6</span>',
    r'\七': '<span style="color: #A099FB; background-color: #A099FB; font-size: 16px;">7</span>',
    r'\な': '<span style="color: #A099FB; background-color: #A099FB; font-size: 16px;">7</span>',
    r'\八': '<span style="color: #910000; background-color: #910000; font-size: 16px;">8</span>',
    r'\は': '<span style="color: #910000; background-color: #910000; font-size: 16px;">8</span>',


    r'\{': '<span style="color: #b078ff; font-weight: bold;">{</span>',
    r'\}': '<span style="color: #b078ff; font-weight: bold;">}</span>',
    r'\(': '<span style="color: #ff47c8; font-weight: bold;">(</span>',
    r'\)': '<span style="color: #ff47c8; font-weight: bold;">)</span>',


    r',': '<span style="color: white;">,</span>',
    r'\'': '',
    r'\[|\]': '',
    }
    for pattern, styled_span in patterns.items():
        text = re.sub(pattern, styled_span, text)
    return text

def func_master(instance_z, instance_y, instance_x):
    if "v" in instance_z.pos and (instance_y.pos == "") and (instance_x.pos == ""):#rape - fuck
        instance_y = copy.deepcopy(instance_z.shadow_y)
    z_Bani, z_Bsol, z_v_name, z_c_name, z_a_name, z_hyper, z_hypo, z_usage = instance_z.c1.Bani, instance_z.c1.Bsol, instance_z.c1.v_name, instance_z.c1.c_name, instance_z.c1.a_name, instance_z.c1.hyper, instance_z.c1.hypo, instance_z.c1.usage
    y_Bani, y_Bsol, y_v_name, y_c_name, y_a_name, y_hyper, y_hypo, y_usage = instance_y.c1.Bani, instance_y.c1.Bsol, instance_y.c1.v_name, instance_y.c1.c_name, instance_y.c1.a_name, instance_y.c1.hyper, instance_y.c1.hypo, instance_y.c1.usage
    x_Bani, x_Bsol, x_v_name, x_c_name, x_a_name, x_hyper, x_hypo, x_usage = instance_x.c1.Bani, instance_x.c1.Bsol, instance_x.c1.v_name, instance_x.c1.c_name, instance_x.c1.a_name, instance_x.c1.hyper, instance_x.c1.hypo, instance_x.c1.usage
    z_butcher, z_ubereats, z_hunting, z_rifle, z_forest, z_fridge, z_kitchen, z_seasoning = instance_z.pl.butcher, instance_z.pl.ubereats, instance_z.pl.hunting, instance_z.pl.rifle, instance_z.pl.forest, instance_z.pl.fridge, instance_z.pl.kitchen, instance_z.pl.seasoning
    y_butcher, y_ubereats, y_hunting, y_rifle, y_forest, y_fridge, y_kitchen, y_seasoning = instance_y.pl.butcher, instance_y.pl.ubereats, instance_y.pl.hunting, instance_y.pl.rifle, instance_y.pl.forest, instance_y.pl.fridge, instance_y.pl.kitchen, instance_y.pl.seasoning
    x_butcher, x_ubereats, x_hunting, x_rifle, x_forest, x_fridge, x_kitchen, x_seasoning = instance_x.pl.butcher, instance_x.pl.ubereats, instance_x.pl.hunting, instance_x.pl.rifle, instance_x.pl.forest, instance_x.pl.fridge, instance_x.pl.kitchen, instance_x.pl.seasoning
    z_risk1, z_risk1_pre_n, z_risk1_pre_v, z_risk1_post_n = instance_z.r1.risk1, instance_z.r1.risk1_pre_n, instance_z.r1.risk1_pre_v, instance_z.r1.risk1_post_n
    x_risk1, x_risk1_pre_n, x_risk1_pre_v, x_risk1_post_n = instance_x.r1.risk1, instance_x.r1.risk1_pre_n, instance_x.r1.risk1_pre_v, instance_x.r1.risk1_post_n
    y_risk1, y_risk1_pre_n, y_risk1_pre_v, y_risk1_post_n = instance_y.r1.risk1, instance_y.r1.risk1_pre_n, instance_y.r1.risk1_pre_v, instance_y.r1.risk1_post_n
    z_hammer, z_nail, z_diy, z_diy_boom, z_toolbox = instance_z.spt.hammer, instance_z.spt.nail, instance_z.spt.DIY, instance_z.spt.DIY_boom, instance_z.spt.toolbox
    x_hammer, x_nail, x_diy, x_diy_boom, x_toolbox = instance_x.spt.hammer, instance_x.spt.nail, instance_x.spt.DIY, instance_x.spt.DIY_boom, instance_x.spt.toolbox
    y_hammer, y_nail, y_diy, y_diy_boom, y_toolbox = instance_y.spt.hammer, instance_y.spt.nail, instance_y.spt.DIY, instance_y.spt.DIY_boom, instance_y.spt.toolbox
    z_venereal, z_rape_alert, z_own_gun, z_abortionist = instance_z.r2.venereal, instance_z.r2.rape_alert, instance_z.r2.own_gun, instance_z.r2.abortionist
    x_venereal, x_rape_alert, x_own_gun, x_abortionist = instance_x.r2.venereal, instance_x.r2.rape_alert, instance_x.r2.own_gun, instance_x.r2.abortionist
    y_venereal, y_rape_alert, y_own_gun, y_abortionist = instance_y.r2.venereal, instance_y.r2.rape_alert, instance_y.r2.own_gun, instance_y.r2.abortionist
    z_unit, z_ti_inc, z_ti_dec, z_caco1, z_caco2, z_qP, z_qN, z_avoid, z_PLinfo, z_law = instance_z.c4.unit, instance_z.c4.ti_inc, instance_z.c4.ti_dec, instance_z.c4.caco1, instance_z.c4.caco2, instance_z.c4.qP, instance_z.c4.qN, instance_z.c4.avoid, instance_z.c4.PLinfo, instance_z.c4.law
    x_unit, x_ti_inc, x_ti_dec, x_caco1, x_caco2, x_qP, x_qN, x_avoid, x_PLinfo, x_law = instance_x.c4.unit, instance_x.c4.ti_inc, instance_x.c4.ti_dec, instance_x.c4.caco1, instance_x.c4.caco2, instance_x.c4.qP, instance_x.c4.qN, instance_x.c4.avoid, instance_x.c4.PLinfo, instance_x.c4.law
    y_unit, y_ti_inc, y_ti_dec, y_caco1, y_caco2, y_qP, y_qN, y_avoid, y_PLinfo, y_law = instance_y.c4.unit, instance_y.c4.ti_inc, instance_y.c4.ti_dec, instance_y.c4.caco1, instance_y.c4.caco2, instance_y.c4.qP, instance_y.c4.qN, instance_y.c4.avoid, instance_y.c4.PLinfo, instance_y.c4.law
    z_noti=instance_z.no.noti
    y_noti=instance_y.no.noti
    x_noti=instance_x.no.noti
    z_bookC, z_bookP, z_persC, z_persP = instance_z.bo.bookC, instance_z.bo.bookP, instance_z.bo.persC, instance_z.bo.persP #acad was deleted
    x_bookC, x_bookP, x_persC, x_persP = instance_x.bo.bookC, instance_x.bo.bookP, instance_x.bo.persC, instance_x.bo.persP #acad was deleted
    y_bookC, y_bookP, y_persC, y_persP = instance_y.bo.bookC, instance_y.bo.bookP, instance_y.bo.persC, instance_y.bo.persP #acad was deleted
    z_pos=instance_z.pos
    x_pos=instance_x.pos
    y_pos=instance_y.pos
    z_adj_name, z_protect, z_present, z_merch, z_tyex, z_tyexPL, z_tyexAN = instance_z.adj.adj_name, instance_z.adj.protect, instance_z.adj.present, instance_z.adj.merch, instance_z.adj.tyex, instance_z.adj.tyexPL, instance_z.adj.tyexAN
    y_adj_name, y_protect, y_present, y_merch, y_tyex, y_tyexPL, y_tyexAN = instance_y.adj.adj_name, instance_y.adj.protect, instance_y.adj.present, instance_y.adj.merch, instance_y.adj.tyex, instance_y.adj.tyexPL, instance_y.adj.tyexAN
    x_adj_name, x_protect, x_present, x_merch, x_tyex, x_tyexPL, x_tyexAN = instance_x.adj.adj_name, instance_x.adj.protect, instance_x.adj.present, instance_x.adj.merch, instance_x.adj.tyex, instance_x.adj.tyexPL, instance_x.adj.tyexAN
    z_each, z_wt, z_content, z_thirst, z_annual = instance_z.dep.each, instance_z.dep.wt, instance_z.dep.content, instance_z.dep.thirst, instance_z.dep.annual
    y_each, y_wt, y_content, y_thirst, y_annual = instance_y.dep.each, instance_y.dep.wt, instance_y.dep.content, instance_y.dep.thirst, instance_y.dep.annual
    x_each, x_wt, x_content, x_thirst, x_annual = instance_x.dep.each, instance_x.dep.wt, instance_x.dep.content, instance_x.dep.thirst, instance_x.dep.annual
    z_p_name, z_p_genre, z_NMB_M, z_NMB_F = instance_z.pp.p_name, instance_z.pp.p_genre, instance_z.pp.NMB_M, instance_z.pp.NMB_F
    y_p_name, y_p_genre, y_NMB_M, y_NMB_F = instance_y.pp.p_name, instance_y.pp.p_genre, instance_y.pp.NMB_M, instance_y.pp.NMB_F

    func_master_base=[]

    if (z_pos == "cn"  and y_pos == "cn" and x_pos == "") or ("v" in z_pos and "v" in y_pos and x_pos == "") or ("pp" in z_pos and y_pos== "" and x_pos==""):#
        func_master_base+=[f"Syntax: cc_ vv_ p__ / ({z_pos})+({y_pos})+({x_pos})"]
        if ("pp" in z_pos and y_pos== "" and x_pos=="") or ("v" in z_pos and "v" in y_pos and x_pos == ""):#ppとfreqって一緒にすればいいのか？
            func_master_base+=[f"Syntax: vv_ p__ / {y_v_name}, {y_p_name}"
                            ,"零 vv_ p__ corpus"
                            ,f"二 {z_NMB_F}"
                            ,f"三 {z_p_name}"#{s,v,o}
                            ,"一 They have the (lowest, fewest) (number, rate) of に."
                            ,"一 They are surprised by に."
                            ,"一 They are surprised that さ did not occur."
                            ,"一 They are not surprised by さ."
                            ,"零"
                            ,f"二 {z_NMB_F}, {z_p_name}"
                            ,"一 (any) days without a に."#3 days without an accident.
                            ,"一 They have improving the (number, rate) of に for x consecutive years."
                            ,"一 In any, に are occurring in (only) any in any people."#In x, deaths from disease are occurring in one in three people.
                            ,"一 In any language, there is no word for に."
                            ,"一 (suggest word) に today"
                            ,"一 (news site header) Weather & に"
                            ,"一 (news site header) Traffic report & に"
                            ,"一 They gamble on the severity and frequency of に."#Patty:Whaddya know, he’s wearing pants.” - Selma:“I owe you a lunch.”
                            ]
        if z_rape_alert or z_hammer or z_abortionist or y_abortionist or z_risk1_post_n or z_risk1_pre_n:
            func_master_base+=["零"
                            ,f"二 {z_rape_alert}, {z_hammer}"
                            ,f"三 {z_abortionist}, {y_abortionist} {z_risk1_post_n}, {z_risk1_pre_n}"
                            ,"一 Two months' worth of に."
                            ,"一 There are many repairers for に."
                            ,"一 There are many types of に."
                            ,"一 There are subscription services of (に, さ)."    #
                            ,"一 There are stamp cards for (に, さ)."             #the simpsons stam cards for surgery
                            ,"一 When buying に in bulk, it becomes cheaper."
                            ,"一 (に, さ) sellers emphasize that their (に, さ) will last a long time."
                            ,"一 (に, さ) sellers emphasize the portability of (に, さ)."
                            ,"一 (に, さ) is treated as a consumable item."
                            ,"一 They know how to use (に, さ)."
                            ]

        if any((z_hammer , z_c_name, z_nail   , z_seasoning, z_toolbox, z_fridge, y_risk1  , y_venereal, y_hammer, y_abortionist, y_seasoning, z_rape_alert, y_risk1_pre_n, y_risk1_post_n, z_diy, z_usage)):
            func_master_base+=[ "零 01"
                            ,f"二 {z_hammer , z_c_name}"
                            ,f"三 {z_nail   , z_seasoning, z_toolbox, z_fridge}"
                            ,f"四 {y_risk1  , y_venereal}"
                            ,f"五 {y_hammer, y_abortionist, y_seasoning, z_rape_alert, y_risk1_pre_n, y_risk1_post_n}"
                            ,f"六 {z_diy    , z_usage}"
                            ,"八 (number, sales, users, popularity, amount)"
                            ,"一 The は of に and the は of さ are not correlated."
                            ,"一 The は of に and the は of よ are correlated."
                            ,"一 The は of に and the は of ご are correlated."
                            ,"一 Is this に yours? I like ろ too. - What ろ?"
                            ,"一 Is this に yours? I like ろ too. - Can it also be used to ろ?"
                            ,"一 Is this に yours? Where’s さ ? - What さ ?"
                            ,"一 Is this に yours? What kind of さ do you use? - What さ ?"
                            #,"一 There are many (repairers, vendor machine, vendor) of ろ."
                            ]
        if any((z_ti_dec, z_ti_inc, z_diy_boom, z_c_name, z_rifle, z_hammer, y_ti_dec, y_ti_inc, y_diy_boom, y_c_name, y_rifle, y_hammer, z_risk1, z_venereal, y_risk1, y_venereal)):
            func_master_base+=["零"
                            ,f"二 {z_ti_dec, z_ti_inc, z_diy_boom}"
                            ,f"三 {z_c_name, z_rifle, z_hammer}"
                            ,f"四 {y_ti_dec, y_ti_inc, y_diy_boom}"
                            ,f"五 {y_c_name, y_rifle, y_hammer}"
                            ,f"六 {z_risk1, z_venereal}"
                            ,f"七 {y_risk1, y_venereal}"
                            ,"八 (number, sales, users, popularity, amount)"
                            ,"一 Since the に, the は of (さ, ご, ろ, な) have (decreased, increased)"
                            ,"一 Since the よ, the は of (さ, ご, ろ, な) have (decreased, increased)"
                            ,"一 Since the に, the は of (さ, ろ, な) have reached a lebel that comparable to that of the よ."
                            ,"一 Since the よ, the は of (さ, ろ, な) have reached a lebel that comparable to that of the に."
                            ]
                            #,f"二 {z_hammer}"
                            #,f"三 {z_caco1}"
                            #,f"四 {z_qN}"
                            #,"一 I can’t use に because I さ."
                            #,"一 I have to refrain from using に while I さ."
                            #,"一 I (don’t can’t) use に to she because she is too よ."
        if y_unit and z_c_name:
            func_master_base+=["零 unit"
                               ,f"二 {z_c_name}"
                               ,f"三 {y_unit}"
                               ,"一 How many に did you (buy, get, take, use)? ー About (x) さ."
                               ,"一 This に costs (x) dollars per さ."
                               ,"一 How much does this に cost per さ?"]
        if z_c_name and z_annual and y_annual and (z_annual != y_annual):
            func_master_base+=["零 z_cn z_an y_an"
            ,f"二 {z_c_name}"
            ,f"三 {z_annual}, {z_unit}"
            ,f"四 {y_annual}, {y_unit}"
            ,"一 The average annual sales of に in various countries: (Area 1), (x) さ, (Area 2), (x) よ."]#The average annual sales of dogs in various countries are as follows: Japan, 10,000 heads; South Korea, 6,000 heads.

        if z_noti and y_c_name:
            func_master_base+=["零 noti"
                               ,f"二 {y_c_name}"
                               ,f"三 {z_noti}"
                               ,"一 I have a question about に. What does さ means?"
                               ,"一 Which is better, に that says さ or に that does not?"
                               ,"一 (search word) に さ meaning"
                               ,"一 I (do not) like に that says さ."
                               ,"一 Is this に さ?"]
        if z_c_name and y_c_name:
            func_master_base+=["零 alike"
                                ,f"二 {z_c_name}"
                                ,f"三 {y_c_name}"
                                ,"一 This に (smells, feels, tastes) like さ."]

        #        if any((z_ti_inc, z_ti_inc)) and any((y_c_name, y_hypo, z_rape_alert, z_hammer, y_risk1_post_n, y_risk1_pre_n, y_forest)):
        #            simple_timing_head=[ f"零 simple timing"
        #                               ,f"二 {z_ti_dec, z_ti_inc}"
        #                               ,f"三 {y_c_name, y_hypo, z_rape_alert, z_hammer, y_risk1_post_n, y_risk1_pre_n, y_forest}"]
        #            simple_timing_body=[f"一 Since the に, (sales, users) of さ has (decreased, increased)"]
        #            if y_risk1:
        #                simple_timing_head+=[f"四 {y_risk1}"]
        #                simple_timing_body+=[f"一 Since the に, number of よ has (decreased, increased)"]
        #            func_master_base+=simple_timing_head+simple_timing_body
        #        if any((z_ti_dec, z_ti_inc, z_diy_boom)) and any((y_ti_dec, y_ti_inc)):
        #            compound_timing_head=[ "零 compound timing",
        #                     f"二 {z_ti_dec, z_ti_inc, z_diy_boom}",
        #                     f"三 {z_c_name, z_butcher, z_ubereats, z_rifle, z_hammer, z_rape_alert}",
        #                     f"四 {y_ti_dec, y_ti_inc}"]
        #            compound_timing_body=[ "一 Since the に, sales of さ reached a level comparable to that of the よ.",
        #                      "一 さ sellers drive (に/よ)."]
        #            if z_risk1:
        #                compound_timing_head+=[f"五 {z_risk1}"]
        #                compound_timing_body+=["一 Since the に, number of ご reached a level comparable to that of the よ."]
        #            if z_venereal:
        #                compound_timing_head+=[f"六 {z_venereal}"]
        #                compound_timing_body+=["一 Since the に, number of ろ reached a level comparable to that of the よ."]
        #            func_master_base+=compound_timing_head+compound_timing_body
        if y_PLinfo and z_c_name:
            func_master_base+=[ "零 PLinfo",
                               f"二 {z_c_name}",
                               f"三 {y_PLinfo}",
                               "一 (Are you interested in, Do you need) に? I know the good spot. さ."]
        if y_avoid and z_c_name:
            func_master_base+=["零 avoid"
                                ,f"二 {z_c_name}"
                                ,f"三 {y_avoid}"
                                ,"一 What should に avoid? - さ."]
        if z_venereal and y_c_name:
            func_master_base+=["零 venereal"
                               ,f"二 {y_c_name}"
                               ,f"三 {z_venereal}"
                               ,"一 My に (got, was damaged by) さ."]
        if z_seasoning and y_butcher:
            func_master_base+=["零 z_s y_b"#Why the butcher sells frisbees?
                               ,f"二 {y_butcher}"
                               ,f"三 {z_seasoning}"
                               ,"一 Why the に sells さ?"]
        if z_risk1 and y_c_name:
            func_master_base+=["零 trauma"
                               ,f"二 {z_risk1}"
                               ,f"三 {y_c_name}"
                               ,f"一 He has trauma about に, so do not let him see さ."]
        if z_risk1 and z_c_name and y_c_name:
            func_master_base+=["零 ashtray"
                               ,f"二 {z_c_name, z_hypo}"
                               ,f"三 {z_risk1}"
                               ,f"四 {y_c_name, y_hypo}"
                               ,f"五 {y_risk1_post_n}"
                               ,f"六 {y_risk1_pre_n}"
                               ,f"七 {y_risk1_pre_v}"
                               ,"一 Apparently に have a risk of さ, so I switched to よ."
                               ,"一 Apparently に have a risk of さ, so I need ご."
                               ,"一 Apparently に have a risk of さ. I regret that I did not prepare ろ."
                               ,"一 Apparently に have a risk of さ, I regret that I did not な."]
        if z_venereal and y_rape_alert or y_own_gun:
            func_master_base+=["零 contra stun"
            ,f"二 {z_venereal}"
            ,f"三 {y_rape_alert}"
            ,f"四 {y_own_gun}"
            ,"一 To avoid に, prepare さ."
            ,"一 To avoid に, prepare to よ."]
        if any((z_c_name, z_hammer, z_butcher, z_forest, z_rifle)):
            func_master_base+=["零 compare_cheaper"
                               ,f"二 {z_c_name, z_hypo, z_hammer, z_butcher, z_ubereats, z_forest, z_rifle, z_hunting}"
                               ,f"三 {y_c_name, y_hypo, y_hammer, y_butcher, y_ubereats, y_forest, y_rifle, y_hunting}"
                               ,f"一 Which is (cheaper, better), に or さ?"
                               ,f"一 Which do you like に or さ?"
                               ,f"一 (Searching) に vs さ price"
                               ,f"一 (Searching) に or さ near me"
                                ,"一 To be torn between に and さ."
                                ,"一 To settle for に instead of さ."
                                ,"一 To not need に because one already have さ."
                                ,"一 To need に because one lost さ."
                                ,"一 Are there any に you recommend other than さ?"
                                ,"一 (x) comparison chart of に and さ."
                                ,"一 Sales of に and さ are negative correlated."
                                ,"一 The に related workers and さ related workers are competing on (x)."
                                ,"一 The に related workers went bankrupt because of the さ related workers."]
        if any((z_c_name, z_hammer, z_rifle, z_bookC) and (y_c_name, y_seasoning)):
            func_master_base+=["零 to forget"
                               ,f"二 {z_c_name, z_hammer, z_rifle, z_bookC}"
                               ,f"三 {y_c_name, y_seasoning}"
                               ,f"四 {y_kitchen, y_fridge, y_butcher, y_forest}"
                                ,"一 To (buy/ sale/ forget/ store/) に (and さ) (in the よ)."
                                ,"一 To drop に (and さ) from the よ."
                                ,"一 To put に (and さ) back in the よ."
                                ,"一 To damage the さ with the に."#My dog accidentally ate a condom.
                                ,"一 To damage the よ with the に."#I dropped a cucumber into the toilet.
                                ,"一 Whose に (and さ) was found in the よ?"#
                                ,"一 Have you seen a に (and さ) in the よ?"#
                                ,"一 Where’s に? - It’s next to さ (and さ)."
                                ,"一 Where’s に? - Look near さ (and さ)."
                                ,"一 The よ {collapsed, was robbed}, {x} に (and さ) were {lost, safe, rescued}."
                                ,"一 To provide customers who bought に with a {discount coupon for} さ."
                                ,"一 The 'custmer who boguht this item also bought' column of に shows さ."]
        if z_c_name and any((y_c_name, y_seasoning, y_rifle, y_butcher, y_ubereats, y_hunting, y_risk1, y_risk1_pre_n, y_risk1_post_n, z_rape_alert, z_abortionist)):
            func_master_base+=["零 correlate cc"
                               ,f"二 {z_c_name}"
                               ,f"三 {y_c_name, y_seasoning, y_rifle}"
                               ,f"三 {y_butcher, y_ubereats, y_hunting,}"
                               ,f"三 {y_risk1, y_risk1_pre_n, y_risk1_post_n,}"
                               ,f"三 {z_rape_alert, z_abortionist}"
                               ,f"一 (sales, number, amount) of に and (sales, number, amount) of さ are (negative, not) correlated."]
        if z_hammer and any((z_nail, z_abortionist, z_rape_alert, z_venereal)):
            func_master_base+=["零 correlate cc"
                               ,f"二 {z_c_name}"
                               ,f"三 {z_nail}"
                               ,f"四 {z_abortionist, z_rape_alert, z_venereal}"
                               ,f"一 (sales, number, amount) of に and (sales, number, amount) of さ are not correlated."
                               ,f"一 (sales, number, amount) of に and (sales, number, amount) of さ are correlated."]
        if y_butcher and z_c_name:
            func_master_base+=["零 ybu+zcn"
                               ,f"二 {y_butcher}"
                               ,f"三 {z_c_name}"
                               ,f"一 The に collapsed. (x) さ were (lost, killed, safe)"]
        if z_Bani=="y" and y_Bani=="":
            func_master_base+=[f"零 Unit 731"
                                   ,f"一 I heard に’s voice, then..."
                                   ,f"一 My に got sick."
                                   ,f"一 My に ran away."
                                   ,f"一 My に broke down so I called a doctor."
                                   ,f"二 {y_c_name}"]
        if y_law:
            func_master_base+=[f"零 legal_indirection"
                    ,f"二 Man"
                    ,f"三 {y_butcher}, {y_forest}"
                    ,f"四 {z_c_name}"
                    ,f"五 {y_law}"
                    ,f"一 The に who inappropriately handled よ has been arrested for breaching the ご."
                    ,f"一 The さ has been arrested for breaching the ご by inappropriately handling よ."
                    ]
        if any((y_risk1_pre_n, y_risk1_post_n, y_seasoning)):
            func_master_base+=["零 ad_corpus"#There is an AD for Uber Taxi on the package of sanitizer.
                ,"一 There is an ad for に at the (package of) さ."
                ,"一 Where did you learn about the に? - I saw an ad at the (package of) さ."
                ,f"二 {y_risk1_pre_n, y_risk1_post_n, y_seasoning}"
                ,f"三 {z_c_name}, {z_butcher}, {z_forest}, {y_hammer}, {z_rifle}"
                ]
        if (z_butcher or z_forest) and (y_butcher or y_forest):#
            func_master_base+=["零 PL_2 "
                    ,"一 A: How about the (proper noun for に) ? - B: I’m banned from the さ."
                    ,"一 To call さ (cheap, better) に."
                    ,f"二 {z_butcher, z_forest}"
                    ,f"三 {y_butcher, y_forest}"
                    ]
        if z_c_name and any((y_risk1, y_risk1_pre_n, y_risk1_pre_v, y_risk1_post_n)):
            func_master_base+=["零 bad experience"
                               ,f"二 {z_c_name, z_risk1}"
                               ,f"三 {y_risk1_pre_v}"
                               ,f"四 {y_risk1_pre_n}"
                               ,f"五 {y_risk1_post_n}"
                                ,f"六 {y_risk1}"
                                ,f"七 {y_butcher}"
                                ,"一 I had a bad experience with に. I regret that I didn’t さ."
                                ,"一 I had a bad experience with に. I regret that I didn’t prpeare よ."
                                ,"一 I had a bad experience with に. I need ご."
                                ,"一 I had a bad experience with に. I (got, was damaged by) ろ."
                                ,"一 I had a bad experience with に. I never go to the な."]
        if z_c_name and (y_caco1 or y_caco2):
            func_master_base+=["零 caco1"
                               ,f"二 {z_c_name}"
                               ,f"三 {y_caco1}"
                               ,f"四 {y_caco2}"
                               ,f"一 I refrain from に during I さ."
                               ,f"一 He さ (now) so do not show him に."
                               ,f"一 How about に? - Didn't I told you? I さ."
                               ,f"一 The に was (too) よ."]

        if any((y_qP, y_qN)) and y_c_name and z_c_name:#qPqNcc
            func_master_base+=["零 compare_qPqNcc"
                               ,f"二 {y_qP, y_qN}"
                               ,f"三 {y_c_name, y_hypo}"
                               ,f"四 {z_c_name, z_hypo}"
                               ,f"一 Which is more に, さ or よ?"]
        if any((y_qP, y_qN)) and z_c_name:#qPqNc_
            func_master_base+=["零 compare_qPqNc_"
                               ,f"二 {y_qP, y_qN}"
                               ,f"三 {z_c_name, z_hypo}"
                               ,f"一 Are there more に さ?"]
        if any((y_bookP)):
            func_master_base+=[  f"零 y_bookP"
                                    ,f"一 Where can I find に? - Look near さ."
                                    ,f"一 Where can I find さ books? - Look near さ."
                                    ,f"二 {z_bookC}"
                                    ,f"二 {z_bookP}"
                                    ,f"二 books related to {z_c_name}"
                                    ,f"三 {y_bookP}"]
        if z_c_name and z_wt and z_each and y_thirst:
            func_master_base+=["零 z_cn z_wt z_ea y_th"
            ,f"二 {z_c_name}"
            ,f"三 {y_thirst}"
            ,"一 What is the normal (weight, size) of に used at one time? - It depend on さ."
            ,"一 What is the normal amount of に used at one time? - It depends on さ."
            ]
        if z_c_name and y_wt:
            func_master_base+=["零 z_cn y_wt"
            ,f"二 {z_c_name}"
            ,f"三 {y_wt}"
            ,"一 What is the (weight, size) of the に? - About (x) さ."
            ]
        if z_c_name and z_content and (z_content == y_content) and y_thirst:
            func_master_base+=["零 z_cn z_co y_co y_th"
            ,f"二 {z_content}"
            ,f"三 {z_c_name}"
            ,f"四 {y_thirst}"
            ,f"五 {y_unit}"
            ,"一 What is the normal に of さ? - It depends on よ."
            ,"一 What is the normal に of さ? - It (x) per ご."]






    elif (z_pos == "an"  and y_pos == "an" and x_pos == ""):
        func_master_base+=[f"Syntax Type: A3 ({z_a_name}({z_pos}) + {y_a_name}({y_pos})"]
        if any((y_bookP)):
            func_master_base+=[     "零 y_bookP"
                                    ,f"二 {z_bookC}"
                                    ,f"二 {z_bookP}"
                                    ,f"二 books related to {z_a_name}"
                                    ,f"二 ({z_persP}) books"
                                    ,f"三 {y_bookP}"
                                    ,f"三 ({y_persP}) books"
                                    ,"一 Where can I find に? - Look near さ."
                                    ]
        if any((z_persP, y_persP)):
            func_master_base+=[     "零 y_bookP"
                                    ,f"二 ({z_persP}) (books, event)"
                                    ,f"二 {z_bookP}"
                                    ,f"三 ({y_persP}) (books, event)"
                                    ,f"三 {y_bookP}"
                                    ,"一 I’m torn between に or さ."
                                    ,"一 Which do you recommend, に or さ?"
                                    ,"一 Which is {better, cheaper} に or さ?"
                                    ]
        if any ((y_hyper)):
            func_master_base+=["零 y_hyper"
                                    ,"一 Where can I find に? - It’s next to さ section."
                                    ,"一 How about に? - No thanks, I’m busy with さ."
                                    ,f"二 {z_bookP}"
                                    ,f"二 {z_bookC}"
                                    ,f"二 ({z_persP}) books"
                                    ,f"三 {y_hyper}"
                                    ,""
                                    ,"一 I’m not good at に so I’m さ."
                                    ,f"二 {y_hyper}"
                                    ,f"三 {z_persC}"
                                    ]
        if z_a_name:
            func_master_base+=["零"
                                    ,"一 I like に, に and さ."
                                    ,"一 I don't like さ, さ and に."
                                    ,"一 Which do you recommend, に, に or さ?"
                                    ,"一 Which do you prefer among に, に or さ?"
                                    ,"一 Which is {cheaper, better}, に or さ?"
                                    ,"一 When the release schedules coincided, に offset the sales of さ."
                                    ,"一 How about に? - No thanks, I already have さ."
                                    ,f"二 {z_persP}"
                                    ,f"二 {z_bookP}"
                                    ,f"三 {y_persP}"
                                    ,f"三 {y_bookP}"]
        if z_persP and y_persP:
            func_master_base+=["零"
                                    ,"一 に see さ as a business rival."
                                    ,"一 に is learning from さ."
                                    ,f"二 {y_persP}"
                                    ,f"二 {y_persC}"
                                    ,f"三 {z_persP}"
                                    ,f"三 {z_persC}"
                                    ]
        if z_a_name:
            func_master_base+=["零"
                                    ,"一 Which do you prefer に or さ?"
                                    ,"一 Are you interested not only in に but also in さ?"
                                    ,"一 Here are the winners of the に award. Next up is the announcement of the さ award."
                                    ,f"二 {z_a_name}"]
        if z_a_name:
            func_master_base+=["零"
                                    ,"一 I have to review に {’s works} to become a よ."
                                    ,"一 I have to review に {’s works} to learn ご."
                                    ,f"二 {z_persP}"
                                    ,f"二 {z_bookP}"
                                    ,f"四 {y_persC}"
                                    ,f"五 {y_a_name}"
                                    ,""
                                    ,"一 I’m researching に and さ."
                                    ,f"二 {z_persP}"
                                    ,f"二 {z_a_name}"
                                    ,f"三 {y_persP}"
                                    ,f"三 {y_a_name}"
                                    ,""
                                    ,"一 に and さ section."
                                    ,"一 に and さ award."
                                    ,f"二 {z_a_name}"
                                    ,f"三 {y_a_name}"
                                    ,""
                                    ,"一 に is as {positive adjective} as さ."
                                    ,f"二 {z_a_name}"]#foolishのようにname, persC, persP等を持たないインスタンスに対応できるよう、if文でインスタンス変数を参照するように。

    elif (z_pos == "adj" and y_pos == ""   and x_pos == ""):
        func_master_base+=["adj"]#に = any/さ = tyex/よ = tyexPL/ ご=tyexPE
        if z_adj_name:
            func_master_base+=["零 base"
            ,f"二 any"
            ,f"三 {z_tyex}"
            ,f"四 {z_tyexPL}"
            ,f"五 {z_tyexAN}"
            ,f"六 {z_protect}"
            ,f"七 {z_present}"]
        func_master_base+=[  "一 ご run away from に."
                            ,"一 to run away from に to よ."
                            ,"一 (よ/ご) make a complaint to に."
                            ,"一 to mistake に for さ."
                            ,"一 to mistake さ for に."
                            ,"一 to mistake さ for に and say that に has been improved."
                            ,"一 to hate さ and に."
                            ,"一 to store さ and に."
                            ,"一 to isolate さ and に."
                            ,"一 to prohoibit さ and に."
                            ,"一 さ was damaged by に."
                            ,"一 to stop using ろ after に left."
                            ,"一 に was kicked out of よ"
                            ,"一 に was kicked out by ご"
                            ,"一 I am not sure whether to get involved with に or go to よ."
                            ,"一 I am not sure whether to get involved with に or get involved with さ."
                            ,"一 に was presented な."
                            ,"一 に is an ad for な."]

        if z_adj_name=="bad taste":
            func_master_base+=["零 bad taste"
                                   ,"ご refuse に."
                                   ,"ご deaths from starvation next to に."]
        elif z_adj_name=="dirty":#Which industrial area is this wastewater from?
            func_master_base+=["零 dirty"
                                   ,"一 To cover one's hands with さ to avoid touching に."
                                   ,"一 To wash one's hands with さ after touching に."
                                   ,"一 To complain that に has defiled (さ/よ)."
                                   ,"一 ご death due to に."
                                   ,"一 ご got food poisoning by に."
                                   ,"一 Vultures (do not) circle over an に."
                                   ,"一 Dung beetles (do not) roll に."
                                   ,"一 Flies (do not) lay eggs on に."]
        elif z_adj_name=="stinky":
            func_master_base+=["零 stinky"
                                   ,"一 To block one’s sense of smell with さ to avoid smelling に."
                                   ,"一 The smell of に sticks to (さ/よ/ご)."
                                   ,"一 ご in よ notices the smell of に."
                                   ,"一 Vultures (do not) circle over an に."
                                   ,"一 Dung beetles (do not) roll に."
                                   ,"一 Flies (do not) lay eggs on に."
                                   ]
        elif z_adj_name=="noisy":
            func_master_base+=["零 noisy"
                                   ,"一 To block one's sense of hearing with さ to avoid hearing に."
                                   ,"一 ご in よ notices the sound of に."
                                   ]

        elif z_adj_name=="gross":
            func_master_base+=["零 gross"
                                   ,"一 To block one’s sense of vision with さ to avoid looking at に."
                                   ,"一 To switch the channel to さ from に."
                                   ,"一 To cover に with さ."
                                   ]
        elif z_adj_name=="idiot":
            func_master_base+=["零 idiot"]#any + adj

        elif   (z_pos == ""  and y_pos == "cn" and x_pos == "") or (z_pos == ""  and y_pos == "v"   and x_pos == ""):#There are (many or few)
            func_master_base+=["零"
                            ,"二 {y_c_name}, {y_v_name}"
                            ,"二 {y_risk1}"
                            #,"三 {y_i_prop}" #positive
                            #,"四 {y_d_prop}" #negative
                            ,"一 They are improving the number of (に, さ) for x consecutive years."
                            ,"一 They are improving the number "]


    else:
        func_master_base.clear()
        func_master_base+=[  "!!! Follow the Syntax Types !!!"
                                ,""
                                ,"二 Syntax type に form 1 に form 2 に form 3 に"
                                ,"一 ____A1_____ 一 __sp__ 一 _Empty 一 _Empty 一"
                                ,"一 ____A2_____ 一 __cn__ 一 __cn__ 一 _Empty 一"
                                ,"一 ____A3_____ 一 __an__ 一 __an__ 一 __an__ 一"
                                ,""
                                ,"二 _ parts of speech _一"
                                ,"一 sp = special word _一"
                                ,"一 cn = concreat noun 一"
                                ,"一 an = abstract noun 一"
                                ]


    return apply_color_styles('<br>'.join(map(str, func_master_base)))

def master_output(word_z, word_y, word_x):
    # Dynamically access the instances based on their names
    instance_z = getattr(master_class_py, word_z, None)
    instance_y = getattr(master_class_py, word_y, None)
    instance_x = getattr(master_class_py, word_x, None)

    if all(isinstance(instance, master_class_py.Master_class) for instance in [instance_z, instance_y, instance_x]):
        result = apply_color_styles(func_master(instance_z, instance_y, instance_x))
        if (instance_z.pos =="cn" and instance_y.pos == "cn" and instance_x.pos == ""):
            instance_z, instance_y = instance_y, instance_z
            result2 = apply_color_styles(func_master(instance_z, instance_y, instance_x))
        else:
            result2=None
        return result, result2
