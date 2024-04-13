from django import forms
class SpecForm(forms.Form):
    cNumber = forms.CharField(max_length=50)
    cProject = forms.CharField(max_length=50)
    cName = forms.CharField(max_length=50)
    cClient = forms.CharField(max_length=50)
    clocation = forms.CharField(max_length=50,required=False)#工地名稱
    cContact = forms.CharField(max_length=50,required=False)#聯絡人
    cContactTel = forms.CharField(max_length=50,required=False)#電話
    cDate = forms.CharField(max_length=50,required=False)#填表日期
    cDeliveryDate = forms.CharField(max_length=50,required=False)#交貨日期
    chaveorder = forms.CharField(max_length=50,initial="無",required=False)
    cFile = forms.FileField(max_length=50,required=False)

class productForm(forms.Form):
    productCode = forms.CharField(max_length=50,required=False)#產品編號
    productName = forms.CharField(max_length=150,required=False)#產品名稱

class Special(forms.Form):
    cClient=forms.CharField(max_length=50, required=False)#業主名稱
    cSpecial = forms.CharField(widget=forms.Textarea, required=False)
    cBrand= forms.CharField(widget=forms.Textarea, required=False)
    class Meta:
        db_table = "Special"

class CompareForm(forms.Form):
    cNumber = forms.CharField(max_length=50,required=False)
    ctable1 = forms.CharField(widget=forms.Textarea, required=False)
    ctable2 = forms.CharField(widget=forms.Textarea, required=False)
    cConform = forms.CharField(max_length=10,required=False,disabled=True)
    cPage = forms.CharField(max_length=20,required=False,disabled=True)
    cBrand = forms.CharField(max_length=10,required=False,disabled=True)
    cRemark = forms.CharField(widget=forms.Textarea, required=False)

class tablespecForm(forms.Form):
    first_boxmaterial_select = (("勝新標準","勝新標準"),("非勝新標準","非勝新標準"),("未指定(舊版資料)","未指定(舊版資料)"))
    first_thick_select = (("0.5t","0.5t"),("0.6t","0.6t"),("0.8t","0.8t"),("1.0t","1.0t"),("1.2t","1.2t"))
    first_material_select = (("鍍鋅板","鍍鋅板"),("烤漆板","烤漆板"),("鹽化鋼板","鹽化鋼板"),("SUS304","SUS304"),("SUS430","SUS430"),("SUS316","SUS316"),("SUS板","SUS板"),("SUS+烤漆板","SUS+烤漆板"),("Epoxy","Epoxy"),("氟碳烤漆板","氟碳烤漆板"),("熱浸鍍鋅+烤漆板","熱浸鍍鋅+烤漆板"),("烤漆板(無發泡)","烤漆板(無發泡)"),("烤漆板(捷雅色)","烤漆板(捷雅色)"),("SUS板+烤漆板(捷雅色)","SUS板+烤漆板(捷雅色)"),("鍍鋅板(無發泡)","鍍鋅板(無發泡)"))
    first_inother_select = (("同內板材質","同內板材質"),("SUS304","SUS304"),("SUS430","SUS430"),("SUS316","SUS316"),("SUS","SUS"))
    first_boxthick_select = (("50","50"),("25","25"),("35","35"),("60","60"),("75","75"))
    second_door_select = (("後紐氣密門","後紐氣密門"),("後紐簡易門","後紐簡易門"),("全拆氣密門","全拆氣密門"),("全拆簡易門","全拆簡易門"),("新式保養門","新式保養門"))
    second_frame_select = (("鋁框架","鋁框架"),("無框架","無框架"),("鋁框架+修飾條","鋁框架+修飾條"))
    Yes_no_select  = (("不含","不含"),("含","含"))
    Yes_no2_select = (("無","無"),("有","有"))
    Yes_no3_select = (("不要","不要"),("要","要"))
    Yes_no4_select = (("不需要","不需要"),("需要","需要"))
    Yes_no5_select = (("否","否"),("是","是"))
    third_basic_install_select = (("無","無"),("滑道","滑道"),("框架","框架"))
    third_basic_thick_select = (("無","無"),("22","22"),("44","44"))
    third_brand_select = (("無","無"),("晟鼎","晟鼎"),("AAF","AAF"),("興保","興保"),("屹德","屹德"),("興和","興和"),("Nitta","Nitta"))
    third_basic_efficient_select = (("無","無"),("30%","30%"),("35%","35%"))
    third_frame_select = (("無","無"),("鐵框","鐵框"),("紙框","紙框"),("鍍鋅框","鍍鋅框"),("不鏽鋼","不鏽鋼"),("鋁質","鋁質"),("木框","木框"))
    third_basic_material_select = (("無","無"),("拋棄式","拋棄式"),("紙質","紙質"),("不織布","不織布"),("鋁質","鋁質"),("不鏽鋼","不鏽鋼"),("尼龍網","尼龍網"))
    third_level_select = (("無","無"),("3","3"),("5","5"),("7","7"),("9","9"),("11","11"))
    third_medium_frameform_select = (("無","無"),("板式","板式"),("袋式","袋式"),("箱型","箱型"),("箱型單法蘭","箱型單法蘭"),("V型","V型"),("V型單法蘭","V型單法蘭"))
    third_medium_long_select = (("無","無"),("4\"","4\""),("11-1/2\"","11-1/\""),("12\"","12\""),("22\"","22\""),("34\"","34\""),("36\"","36\""))
    third_medium_efficient_select = (("無","無"),("50%","50%"),("65%","65%"),("85%","85%"),("95%","95%"))
    third_high_frameform_select = (("無","無"),("箱型","箱型"),("箱型單法蘭","箱型單法蘭"),("V型","V型"),("V型單法蘭","V型單法蘭"))
    third_high_long_select = (("無","無"),("11-1/2\"","11-1/2\""),("95%","95%"))
    third_high_efficient_select  = (("無","無"),("95%","95%"),("99.97%","99.97%"),("99.99%","99.99%"))
    third_all_material_select = (("無","無"),("鍍鋅","鍍鋅"),("不鏽鋼","不鏽鋼"),("SUS304","SUS304"),("SUS430","SUS430"),("SUS316","SUS316"))
    four_material_select = (("無","無"),("鍍鋅","鍍鋅"),("不鏽鋼","不鏽鋼"))
    four_way_select = (("無","無"),("分2段","分2段"),("不分段","不分段"),("分3段","分3段"),("分4段","分4段"),("分6段","分6段"))
    fiv_humidifier_select = (("不含、不預留加濕空間","不含、不預留加濕空間"),("不含、預留加濕空間","不含、預留加濕空間"),("不含、預留加濕空間代安裝","不含、預留加濕空間代安裝"),("含","含"))
    fiv_form_select = (("無","無"),("盤式","盤式"),("電擊式","電擊式"),("水洗箱","水洗箱"),("二流體加濕","二流體加濕"),("蒸氣加濕","蒸氣加濕"),("高壓噴霧","高壓噴霧"))
    six_form_select = (("無","無"),("八字開","八字開"),("平行開","平行開"))
    six_material_select = (("無","無"),("鍍鋅","鍍鋅"),("不鏽鋼","不鏽鋼"),("鋁合金","鋁合金"))
    six_axis_select = (("無","無"),("標準","標準"),("加長","加長"))
    seven_fins_select = (("無","無"),("一般白鋁","一般白鋁"),("藍波鋁片","藍波鋁片"),("鋼片","鋼片"),("不鏽鋼片","不鏽鋼片"))
    seven_thick_select = (("無","無"),("0.12t","0.12t"),("0.15t","0.15t"),("0.2t","0.2t"))
    seven_board_select = (("無","無"),("鍍鋅 1.6t","鍍鋅 1.6t"),("不鏽鋼 1.5t","不鏽鋼 1.5t"),("烤漆","烤漆"))
    seven_pipe_thick_select = (("無","無"),("0.41t","0.41t"),("0.7t","0.7t"),("1.0t","1.0t"))
    seven_waterpipe_select = (("無","無"),("鍍鋅管","鍍鋅管"),("不鏽鋼管","不鏽鋼管"),("鋼管","鋼管"),("鍍鋅B管","鍍鋅B管"))
    seven_size_select = (("無","無"),("3/8\"","3/8\""),("1/2\"","1/2\""),("5/8\"","5/8\""))
    eight_material_select = (("無","無"),("鍍鋅","鍍鋅"),("不鏽鋼(304)","不鏽鋼(304)"),("不鏽鋼(430)","不鏽鋼(430)"),("不鏽鋼(316)","不鏽鋼(316)"))
    eight_thick_select = (("1.2t","1.2t"),("1.5t","1.5t"))
    nine_brand_select = (("科祿格","科祿格"),("及普","及普"),("尼可達","尼可達"),("億利達","億利達"),("依圖面","依圖面"))
    nine_way_select = (("直結式","直結式"),("皮帶傳動","皮帶傳動"))
    nine_form_select = (("前傾葉片","前傾葉片"),("後傾葉片","後傾葉片"),("翼截式","翼截式"),("依選機","依選機"))
    ten_motor_brand_select = (("東元","東元"),("大同","大同"),("西門子","西門子"),("銅管","銅管"),("MEZ","MEZ"),("邦達","邦達"),("依圖面","依圖面"))
    ten_motor_elec_select = (("接至端子台","接至端子台"),("不含","不含"),("附NFB","附NFB"))
    ten_motor_efficient_select = (("IE1","IE1"),("IE2","IE2"),("IE3","IE3"),("高效率","高效率"),("超高效率","超高效率"))
    ten_motor_level_select = (("無","無"),("IP54","IP54"),("IP55","IP55"),("ExelIT3","ExelIT3"),("ExelIBT4","ExelIBT4"),("ExelICT4","ExelICT4"),("eG3","eG3"),("d2G4","d2G4"))
    ten_motor_open_select = (("一般","一般"),("變頻","變頻"),("Y-△","Y-△"))
    ten_motor_Insulation_select = (("無","無"),("E級","E級"),("B級","B級"),("F級","F級"),("H級","H級"),("依馬達廠標準","依馬達廠標準"))
    ten_motor_cold_select = (("自立通風","自立通風"),("強制通風","強制通風"))
    ten_motor_form_select = (("一般","一般"),("變頻","變頻"))
    eleven_material_select = (("烤漆","烤漆"),("不鏽鋼","不鏽鋼"),("PVC","PVC"))
    eleven_form_select = (("室內型","室內型"),("屋外型","屋外型"),("室內防爆","室內防爆"),("屋外防爆","屋外防爆"),("屋外防水","屋外防水"))
    eleven_level_select = (("無要求","無要求"),("IP54","IP54"),("IP55","IP55"),("IP65","IP65"))
    twelve_view_light_select = (("無","無"),("有","有"),("僅風車段","僅風車段"))
    twelve_pressure_select = (("無","無"),("指針式X1","指針式X1"),("指針式X2","指針式X2"))
    twelve_unit_select = (("無","無"),("mmAq","mmAq"),("Pa","Pa"))
    twelve_brand_select = (("無","無"),("Dwyer","Dwyer"),("SINEI","SINEI"),("GAUGE","GAUGE"))
    twelve_light_elec_select = (("無","無"),("各箱段獨立電源","各箱段獨立電源"),("各箱段獨立連結(立)","各箱段獨立連結(立)"),("各箱段獨立連結(頂)","各箱段獨立連結(頂)"))
    twelve_light_open_select = (("無","無"),("塑膠","塑膠"),("綠紗紋","綠紗紋"))
    twelve_net_select = (("無","無"),("不鏽鋼","不鏽鋼"),("鍍鋅","鍍鋅"))
    twelve_silicone_select = (("勝新標準","勝新標準"),("SIKA","SIKA"),("高溫型","高溫型"),("道康寧","道康寧"))
    twelve_location_select = (("室內","室內"),("室外","室外"))
    twelve_material_select = (("無","無"),("鍍鋅","鍍鋅"),("烤漆","烤漆"),("不鏽鋼","不鏽鋼"))
    thirteen_way_select = (("車上交貨","車上交貨"),("貨車可達地平面","貨車可達地平面"))
    thirteen_shocbox_select = (("無","無"),("避震器","避震器"),("避震墊型式","避震墊型式"))
    thirteen_displace_select = (("無","無"),("L型固定","L型固定"),("N字型固定","N字型固定"),("","其他"))
    thirteen_fixway_select = (("無","無"),("膨脹螺栓","膨脹螺栓"),("","其他"))
    seventeen_brand_select = (("一般","一般"),("耐熱","耐熱"),("道康寧","道康寧"),("SIKA","SIKA"),("PU膠","PU膠"))
    cNumber = forms.CharField(max_length=50,required=False)
    machinename = forms.CharField(max_length=20,required=False)
    first_boxmaterial = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=first_boxmaterial_select))
    first_inthick = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=first_thick_select))
    first_inmaterial = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=first_material_select))
    first_inother = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=first_inother_select)) # 配件
    first_outmaterial = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=first_material_select))
    first_outthick = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=first_thick_select))
    first_boxthick = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=first_boxthick_select))
    second_door = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=second_door_select))
    second_frame = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=second_frame_select))
    third_basic = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no_select))
    third_basic_install = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_basic_install_select))
    third_basic_thick = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_basic_thick_select))
    third_basic_brand = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_brand_select))
    third_basic_efficient = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_basic_efficient_select))
    third_basic_frame = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_frame_select))
    third_basic_material = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_basic_material_select))
    third_level = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_level_select))
    third_medium = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no_select)) 
    third_medium_frameform = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_medium_frameform_select)) #外框型式
    third_medium_long = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_medium_long_select)) #袋長
    third_medium_brand = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_brand_select))
    third_medium_efficient = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_medium_efficient_select))#確定有
    third_medium_frame = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_frame_select))#濾網框
    third_high = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no_select))
    third_high_frameform = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_high_frameform_select)) #外框型式
    third_high_long = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_high_long_select))
    third_high_brand = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_brand_select))
    third_high_efficient = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_high_efficient_select))
    third_high_frame = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_frame_select))
    third_basic_medium_material = forms.CharField(max_length=50,required=False,widget=forms.Select(choices=third_all_material_select))
    third_high_material = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_all_material_select))
    four_heater = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no_select))
    four_material=forms.CharField(max_length=30,required=False,widget=forms.Select(choices=four_material_select))
    four_way= forms.CharField(max_length=30,required=False,widget=forms.Select(choices=four_way_select))
    four_SSCR= forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no_select))
    fiv_humidifier = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=fiv_humidifier_select))
    fiv_form = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=fiv_form_select))
    six_winddoor = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no_select))
    six_form= forms.CharField(max_length=30,required=False,widget=forms.Select(choices=six_form_select))
    six_frame_material= forms.CharField(max_length=30,required=False,widget=forms.Select(choices=six_material_select))
    six_blade_material= forms.CharField(max_length=30,required=False,widget=forms.Select(choices=six_material_select))
    six_axis= forms.CharField(max_length=30,required=False,widget=forms.Select(choices=six_axis_select))
    six_mm = forms.CharField(max_length=30,required=False)
    seven_cold = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no_select))
    seven_fins = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_fins_select))
    seven_thick = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_thick_select))
    seven_board = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_board_select))
    seven_pipe_thick = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_pipe_thick_select))
    seven_waterpipe = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_waterpipe_select))
    seven_size = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_size_select))
    seven_other = forms.CharField(max_length=30,required=False)
    seven_hot = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no_select))
    seven_hotfins = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_fins_select))
    seven_hotthick = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_thick_select))
    seven_hotboard = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_board_select))
    seven_hotpipe_thick = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_pipe_thick_select))
    seven_hotwaterpipe = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_waterpipe_select))
    seven_hotsize = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_size_select))
    seven_steam = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no_select))
    seven_steamfins = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_fins_select))
    seven_steamthick = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_thick_select))
    seven_steamboard = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_board_select))
    seven_steampipe_thick = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_pipe_thick_select))
    seven_steamwaterpipe = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_waterpipe_select))
    seven_steamsize = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_size_select))
    seven_brine = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no_select))
    seven_brinefins = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_fins_select))
    seven_brinethick = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_thick_select))
    seven_brineboard = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_board_select))
    seven_brinepipe_thick = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_pipe_thick_select))
    seven_brinewaterpipe = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_waterpipe_select))
    seven_brinesize = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_size_select))
    eight_material = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=eight_material_select))
    eight_thick = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=eight_thick_select))
    nine_brand = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=nine_brand_select))
    nine_way = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=nine_way_select))
    nine_form = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=nine_form_select))
    ten_motor_brand = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=ten_motor_brand_select))
    ten_motor_Insulation = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=ten_motor_Insulation_select))
    ten_motor_elec = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=ten_motor_elec_select))
    ten_motor_efficient = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=ten_motor_efficient_select))#效率
    ten_motor_level = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=ten_motor_level_select))#防護等級
    ten_motor_open = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=ten_motor_open_select))#啟動方式
    ten_motor_cold = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=ten_motor_cold_select))#冷卻方式
    ten_motor_ask = forms.CharField(max_length=30,required=False)#其他要求
    ten_motor_form = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=ten_motor_form_select))#馬達型式
    eleven_material = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=eleven_material_select))
    eleven_form = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=eleven_form_select))
    eleven_key = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no2_select))
    eleven_level = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=eleven_level_select))
    eleven_size = forms.CharField(max_length=30,required=False)
    twelve_view = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=twelve_view_light_select))
    twelve_pressure = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=twelve_pressure_select)) #壓差計
    twelve_unit = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=twelve_unit_select)) #刻度單位
    twelve_brand = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=twelve_brand_select)) #廠牌
    twelve_light = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=twelve_view_light_select)) 
    twelve_level = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=eleven_level_select)) #防護等級
    twelve_light_elec = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=twelve_light_elec_select)) #照明店員
    twelve_light_open = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=twelve_light_open_select)) #照明開關
    twelve_winddoor = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no2_select)) #風門
    twelve_net = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=twelve_net_select)) #擴散網
    twelve_material = forms.CharField(max_length=30,required=False)
    twelve_mm = forms.CharField(max_length=30,required=False)
    twelve_silicone = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=twelve_silicone_select))
    twelve_location = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=twelve_location_select)) #空調箱放置地點
    twelve_roof = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no2_select)) #空調箱放置地點
    twelve_newmaterial = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=twelve_material_select)) #空調箱放置地點
    twelve_test = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no2_select))
    thirteen_way = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=thirteen_way_select))#交貨方式
    thirteen_elevator = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no3_select))
    thirteen_box = forms.CharField(max_length=30,required=False)
    thirteen_into = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no5_select)) #分箱進場
    thirteen_shock = forms.CharField(max_length=30,required=False) #避震
    thirteen_shocbox = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=thirteen_shocbox_select)) #避震器型式
    thirteen_shockbox_form = forms.CharField(max_length=30,required=False)
    thirteen_apply = forms.CharField(max_length=30,required=False) #施作
    thirteen_fix = forms.CharField(max_length=30,required=False) #空調箱固定
    thirteen_budget = forms.CharField(max_length=30,required=False) #預算
    thirteen_budgetdollar = forms.CharField(max_length=30,required=False) #預算
    thirteen_displace = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=thirteen_displace_select)) #位移
    thirteen_fixway = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=thirteen_fixway_select)) #固定方式
    fourteen_ass = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no3_select)) #固定方式
    fourteen_budget = forms.CharField(max_length=30,required=False)
    fourteen_budgetdollar = forms.CharField(max_length=30,required=False)
    fourteen_time = forms.CharField(max_length=30,required=False)
    fourteen_into = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no5_select))#人員進場須知
    fourteen_intotime = forms.CharField(max_length=30,required=False)
    fourteen_afterass = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no5_select))
    fourteen_afterasstime = forms.CharField(max_length=30,required=False) #上完課組裝
    fourteen_foreigninto = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no5_select))#外籍員工進場
    fourteen_foreignintotime = forms.CharField(max_length=30,required=False) #上完課組裝
    fourteen_card = forms.CharField(max_length=10,required=False,widget=forms.Select(choices=Yes_no4_select)) #證件
    fourteen_insurance = forms.CharField(max_length=10,required=False) # 保險 ,widget=forms.Select(choices=Yes_no4_select)
    fifteen_location = forms.CharField(max_length=30,required=False)#空調箱搬運定位
    fifteen_view = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no2_select))
    fifteen_level = forms.CharField(max_length=30,required=False) #水平搬運
    fifteen_vertical = forms.CharField(max_length=30,required=False) #垂直搬運
    fifteen_tool = forms.CharField(max_length=30,required=False)
    fifteen_budget = forms.CharField(max_length=30,required=False)
    fifteen_box = forms.CharField(max_length=30,required=False) #立式空調箱上箱段
    sixteen_install = forms.CharField(max_length=30,required=False) #代課安裝
    sixteen_prepare = forms.CharField(max_length=30,required=False) #備料
    seventeen_silicone = forms.CharField(max_length=30,required=False)
    seventeen_brand = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seventeen_brand_select)) 
    eighteen_other = forms.CharField(widget=forms.Textarea, required=False)

# class tableBOMForm(forms.Form):
#     chaveorder = forms.CharField(max_length=50,initial="無",required=False)
#     cBOMFile = forms.FileField(max_length=50,required=False)

# class OrderBOMForm(forms.Form):
#     first_boxmaterial_select = (("勝新標準","勝新標準"),("非勝新標準","非勝新標準"),("未指定(舊版資料)","未指定(舊版資料)"))
#     first_thick_select = (("0.5t","0.5t"),("0.6t","0.6t"),("0.8t","0.8t"),("1.0t","1.0t"),("1.2t","1.2t"))
#     first_material_select = (("鍍鋅板","鍍鋅板"),("烤漆板","烤漆板"),("鹽化鋼板","鹽化鋼板"),("SUS304","SUS304"),("SUS430","SUS430"),("SUS316","SUS316"),("SUS板","SUS板"),("SUS+烤漆板","SUS+烤漆板"),("Epoxy","Epoxy"),("氟碳烤漆板","氟碳烤漆板"),("熱浸鍍鋅+烤漆板","熱浸鍍鋅+烤漆板"),("烤漆板(無發泡)","烤漆板(無發泡)"),("烤漆板(捷雅色)","烤漆板(捷雅色)"),("SUS板+烤漆板(捷雅色)","SUS板+烤漆板(捷雅色)"),("鍍鋅板(無發泡)","鍍鋅板(無發泡)"))
#     first_inother_select = (("同內板材質","同內板材質"),("SUS304","SUS304"),("SUS430","SUS430"),("SUS316","SUS316"),("SUS","SUS"))
#     first_boxthick_select = (("50","50"),("25","25"),("35","35"),("60","60"),("75","75"))
#     second_door_select = (("後紐氣密門","後紐氣密門"),("後紐簡易門","後紐簡易門"),("全拆氣密門","全拆氣密門"),("全拆簡易門","全拆簡易門"),("新式保養門","新式保養門"))
#     second_frame_select = (("鋁框架","鋁框架"),("無框架","無框架"),("鋁框架+修飾條","鋁框架+修飾條"))
#     Yes_no_select  = (("不含","不含"),("含","含"))
#     Yes_no2_select = (("無","無"),("有","有"))
#     Yes_no3_select = (("不要","不要"),("要","要"))
#     Yes_no4_select = (("不需要","不需要"),("需要","需要"))
#     Yes_no5_select = (("否","否"),("是","是"))
#     third_basic_install_select = (("滑道","滑道"),("框架","框架"))
#     third_basic_thick_select = (("22","22"),("44","44"))
#     third_brand_select = (("晟鼎","晟鼎"),("AAF","AAF"),("興保","興保"),("屹德","屹德"),("興和","興和"),("Nitta","Nitta"))
#     third_basic_efficient_select = (("30%","30%"),("35%","35%"))
#     third_frame_select = (("無","無"),("鐵框","鐵框"),("紙框","紙框"),("鍍鋅框","鍍鋅框"),("不鏽鋼","不鏽鋼"),("鋁質","鋁質"),("木框","木框"))
#     third_basic_material_select = (("拋棄式","拋棄式"),("紙質","紙質"),("不織布","不織布"),("鋁質","鋁質"),("不鏽鋼","不鏽鋼"),("尼龍網","尼龍網"))
#     third_medium_frameform_select = (("無","無"),("板式","板式"),("袋式","袋式"),("箱型","箱型"),("箱型單法蘭","箱型單法蘭"),("V型","V型"),("V型單法蘭","V型單法蘭"))
#     third_medium_long_select = (("無","無"),("4''","4''"),("11-1/2''","11-1/2''"),("12''","12''"),("22''","22''"),("34''","34''"),("36''","36''"))
#     third_medium_efficient_select = (("無","無"),("50%","50%"),("65%","65%"),("85%","85%"),("95%","95%"))
#     third_high_frameform_select = (("無","無"),("箱型","箱型"),("箱型單法蘭","箱型單法蘭"),("V型","V型"),("V型單法蘭","V型單法蘭"))
#     third_high_long_select = (("無","無"),("11-1/2''","11-1/2''"),("95%","95%"))
#     third_high_efficient_select  = (("無","無"),("95%","95%"),("99.97%","99.97%"),("99.99%","99.99%"))
#     third_all_material_select = (("無","無"),("鍍鋅","鍍鋅"),("不鏽鋼","不鏽鋼"),("SUS304","SUS304"),("SUS430","SUS430"),("SUS316","SUS316"))
#     four_material_select = (("無","無"),("鍍鋅","鍍鋅"),("不鏽鋼","不鏽鋼"))
#     four_way_select = (("無","無"),("分2段","分2段"),("不分段","不分段"),("分3段","分3段"),("分4段","分4段"),("分6段","分6段"))
#     fiv_humidifier_select = (("不含、不預留加濕空間","不含、不預留加濕空間"),("不含、預留加濕空間","不含、預留加濕空間"),("不含、預留加濕空間代安裝","不含、預留加濕空間代安裝"),("含","含"))
#     fiv_form_select = (("無","無"),("盤式","盤式"),("電擊式","電擊式"),("水洗箱","水洗箱"),("二流體加濕","二流體加濕"),("蒸氣加濕","蒸氣加濕"),("高壓噴霧","高壓噴霧"))
#     six_form_select = (("無","無"),("八字開","八字開"),("平行開","平行開"))
#     six_material_select = (("無","無"),("鍍鋅","鍍鋅"),("不鏽鋼","不鏽鋼"),("鋁合金","鋁合金"))
#     six_axis_select = (("無","無"),("標準","標準"),("加長","加長"))
#     seven_fins_select = (("無","無"),("一般白鋁","一般白鋁"),("藍波鋁片","藍波鋁片"),("鋼片","鋼片"),("不鏽鋼片","不鏽鋼片"))
#     seven_thick_select = (("無","無"),("0.12t","0.12t"),("0.15t","0.15t"),("0.2t","0.2t"))
#     seven_board_select = (("無","無"),("鍍鋅 1.6t","鍍鋅 1.6t"),("不鏽鋼 1.5t","不鏽鋼 1.5t"),("烤漆","烤漆"))
#     seven_pipe_thick_select = (("無","無"),("0.41t","0.41t"),("0.7t","0.7t"),("1.0t","1.0t"))
#     seven_waterpipe_select = (("無","無"),("鍍鋅管","鍍鋅管"),("不鏽鋼管","不鏽鋼管"),("鋼管","鋼管"),("鍍鋅B管","鍍鋅B管"))
#     seven_size_select = (("無","無"),("3/8''","3/8''"),("1/2''","1/2''"),("5/8''","5/8''"))
#     eight_material_select = (("鍍鋅","鍍鋅"),("不鏽鋼(304)","不鏽鋼(304)"),("不鏽鋼(430)","不鏽鋼(430)"),("不鏽鋼(316)","不鏽鋼(316)"))
#     eight_thick_select = (("1.2t","1.2t"),("1.5t","1.5t"))
#     nine_brand_select = (("科祿格","科祿格"),("及普","及普"),("尼可達","尼可達"),("億利達","億利達"),("依圖面","依圖面"),("","其他"))
#     nine_way_select = (("直結式","直結式"),("皮帶傳動","皮帶傳動"))
#     nine_form_select = (("前傾葉片","前傾葉片"),("後傾葉片","後傾葉片"),("翼截式","翼截式"),("依選機","依選機"))
#     ten_motor_brand_select = (("東元","東元"),("大同","大同"),("西門子","西門子"),("銅管","銅管"),("MEZ","MEZ"),("邦達","邦達"),("依圖面","依圖面"),("","其他"))
#     ten_motor_elec_select = (("接至端子台","接至端子台"),("不含","不含"),("附NFB","附NFB"))
#     ten_motor_efficient_select = (("IE1","IE1"),("IE2","IE2"),("IE3","IE3"),("高效率","高效率"),("超高效率","超高效率"))
#     ten_motor_level_select = (("無","無"),("IP54","IP54"),("IP55","IP55"),("ExelIT3","ExelIT3"),("ExelIBT4","ExelIBT4"),("ExelICT4","ExelICT4"),("eG3","eG3"),("d2G4","d2G4"))
#     ten_motor_open_select = (("一般","一般"),("變頻","變頻"),("Y-△","Y-△"))
#     ten_motor_Insulation_select = (("無","無"),("E級","E級"),("B級","B級"),("F級","F級"),("H級","H級"))
#     ten_motor_cold_select = (("自立通風","自立通風"),("強制通風","強制通風"))
#     ten_motor_form_select = (("一般","一般"),("變頻","變頻"))
#     eleven_material_select = (("烤漆","烤漆"),("不鏽鋼","不鏽鋼"),("PVC","PVC"))
#     eleven_form_select = (("室內型","室內型"),("屋外型","屋外型"),("室內防爆","室內防爆"),("屋外防爆","屋外防爆"),("屋外防水","屋外防水"))
#     eleven_level_select = (("無要求","無要求"),("IP54","IP54"),("IP55","IP55"),("IP65","IP65"))
#     twelve_view_light_select = (("無","無"),("有","有"),("僅風車段","僅風車段"))
#     twelve_pressure_select = (("無","無"),("指針式X1","指針式X1"),("指針式X2","指針式X2"))
#     twelve_unit_select = (("無","無"),("mmAq","mmAq"),("Pa","Pa"))
#     twelve_brand_select = (("無","無"),("Dwyer","Dwyer"),("SINEI","SINEI"),("GAUGE","GAUGE"))
#     twelve_light_elec_select = (("無","無"),("各箱段獨立電源","各箱段獨立電源"),("各箱段獨立連結(立)","各箱段獨立連結(立)"),("各箱段獨立連結(頂)","各箱段獨立連結(頂)"))
#     twelve_light_open_select = (("無","無"),("塑膠","塑膠"),("綠紗紋","綠紗紋"))
#     twelve_net_select = (("無","無"),("不鏽鋼","不鏽鋼"),("鍍鋅","鍍鋅"))
#     twelve_silicone_select = (("勝新標準","勝新標準"),("SIKA","SIKA"),("高溫型","高溫型"),("道康寧","道康寧"),("","其他"))
#     twelve_location_select = (("室內","室內"),("室外","室外"))
#     twelve_material_select = (("無","無"),("鍍鋅","鍍鋅"),("烤漆","烤漆"),("不鏽鋼","不鏽鋼"))
#     thirteen_way_select = (("車上交貨","車上交貨"),("貨車可達地平面","貨車可達地平面"))
#     thirteen_shocbox_select = (("無","無"),("避震器","避震器"),("避震墊型式","避震墊型式"))
#     thirteen_displace_select = (("無","無"),("L型固定","L型固定"),("N字型固定","N字型固定"),("","其他"))
#     thirteen_fixway_select = (("無","無"),("膨脹螺栓","膨脹螺栓"),("","其他"))
#     seventeen_brand_select = (("一般","一般"),("耐熱","耐熱"),("道康寧","道康寧"),("SIKA","SIKA"))
#     cNumber = forms.IntegerField(max_value=9223372036854775807,required=False)
#     machinename = forms.CharField(max_length=20,required=False)
#     first_boxmaterial = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=first_boxmaterial_select))
#     first_inthick = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=first_thick_select))
#     first_inmaterial = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=first_material_select))
#     first_inother = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=first_inother_select)) # 配件
#     first_outmaterial = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=first_material_select))
#     first_outthick = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=first_thick_select))
#     first_boxthick = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=first_boxthick_select))
#     second_door = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=second_door_select))
#     second_frame = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=second_frame_select))
#     third_basic = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no_select))
#     third_basic_install = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_basic_install_select))
#     third_basic_thick = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_basic_thick_select))
#     third_basic_brand = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_brand_select))
#     third_basic_efficient = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_basic_efficient_select))
#     third_basic_frame = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_frame_select))
#     third_basic_material = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_basic_material_select))
#     third_medium = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no_select)) 
#     third_medium_frameform = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_medium_frameform_select)) #外框型式
#     third_medium_long = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_medium_long_select)) #袋長
#     third_medium_brand = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_brand_select))
#     third_medium_efficient = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_medium_efficient_select))#確定有
#     third_medium_frame = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_frame_select))#濾網框
#     third_high = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no_select))
#     third_high_frameform = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_high_frameform_select)) #外框型式
#     third_high_long = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_high_long_select))
#     third_high_brand = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_brand_select))
#     third_high_efficient = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_high_efficient_select))
#     third_high_frame = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_frame_select))
#     third_basic_medium_material = forms.CharField(max_length=50,required=False,widget=forms.Select(choices=third_all_material_select))
#     third_high_material = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=third_all_material_select))
#     four_heater = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no_select))
#     four_material=forms.CharField(max_length=30,required=False,widget=forms.Select(choices=four_material_select))
#     four_way= forms.CharField(max_length=30,required=False,widget=forms.Select(choices=four_way_select))
#     four_SSCR= forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no_select))
#     fiv_humidifier = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=fiv_humidifier_select))
#     fiv_form = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=fiv_form_select))
#     six_winddoor = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no_select))
#     six_form= forms.CharField(max_length=30,required=False,widget=forms.Select(choices=six_form_select))
#     six_frame_material= forms.CharField(max_length=30,required=False,widget=forms.Select(choices=six_material_select))
#     six_blade_material= forms.CharField(max_length=30,required=False,widget=forms.Select(choices=six_material_select))
#     six_axis= forms.CharField(max_length=30,required=False,widget=forms.Select(choices=six_axis_select))
#     seven_cold = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no_select))
#     seven_fins = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_fins_select))
#     seven_thick = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_thick_select))
#     seven_board = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_board_select))
#     seven_pipe_thick = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_pipe_thick_select))
#     seven_waterpipe = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_waterpipe_select))
#     seven_size = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_size_select))
#     seven_other = forms.CharField(max_length=30,required=False)
#     seven_hot = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no_select))
#     seven_hotfins = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_fins_select))
#     seven_hotthick = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_thick_select))
#     seven_hotboard = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_board_select))
#     seven_hotpipe_thick = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_pipe_thick_select))
#     seven_hotwaterpipe = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_waterpipe_select))
#     seven_hotsize = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_size_select))
#     seven_steam = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no_select))
#     seven_steamfins = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_fins_select))
#     seven_steamthick = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_thick_select))
#     seven_steamboard = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_board_select))
#     seven_steampipe_thick = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_pipe_thick_select))
#     seven_steamwaterpipe = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_waterpipe_select))
#     seven_steamsize = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_size_select))
#     seven_brine = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no_select))
#     seven_brinefins = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_fins_select))
#     seven_brinethick = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_thick_select))
#     seven_brineboard = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_board_select))
#     seven_brinepipe_thick = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_pipe_thick_select))
#     seven_brinewaterpipe = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_waterpipe_select))
#     seven_brinesize = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seven_size_select))
#     eight_material = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=eight_material_select))
#     eight_thick = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=eight_thick_select))
#     nine_brand = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=nine_brand_select))
#     nine_brand_default =  forms.CharField(max_length=30,required=False)
#     nine_way = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=nine_way_select))
#     nine_form = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=nine_form_select))
#     ten_motor_brand = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=ten_motor_brand_select))
#     ten_motor_brand_default =  forms.CharField(max_length=30,required=False)
#     ten_motor_Insulation = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=ten_motor_Insulation_select))
#     ten_motor_elec = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=ten_motor_elec_select))
#     ten_motor_efficient = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=ten_motor_efficient_select))#效率
#     ten_motor_level = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=ten_motor_level_select))#防護等級
#     ten_motor_open = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=ten_motor_open_select))#啟動方式
#     ten_motor_cold = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=ten_motor_cold_select))#冷卻方式
#     ten_motor_ask = forms.CharField(max_length=30,required=False)#其他要求
#     ten_motor_form = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=ten_motor_form_select))#馬達型式
#     eleven_material = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=eleven_material_select))
#     eleven_form = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=eleven_form_select))
#     eleven_key = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no2_select))
#     eleven_level = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=eleven_level_select))
#     eleven_size = forms.CharField(max_length=30,required=False)
#     twelve_view = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=twelve_view_light_select))
#     twelve_pressure = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=twelve_pressure_select)) #壓差計
#     twelve_unit = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=twelve_unit_select)) #刻度單位
#     twelve_brand = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=twelve_brand_select)) #廠牌
#     twelve_light = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=twelve_view_light_select)) 
#     twelve_level = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=eleven_level_select)) #防護等級
#     twelve_light_elec = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=twelve_light_elec_select)) #照明店員
#     twelve_light_open = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=twelve_light_open_select)) #照明開關
#     twelve_winddoor = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no2_select)) #風門
#     twelve_net = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=twelve_net_select)) #擴散網
#     twelve_material = forms.CharField(max_length=30,required=False)
#     twelve_silicone = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=twelve_silicone_select))
#     twelve_silicone_default = forms.CharField(max_length=30,required=False)
#     twelve_location = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=twelve_location_select)) #空調箱放置地點
#     twelve_roof = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no2_select)) #空調箱放置地點
#     twelve_newmaterial = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=twelve_material_select)) #空調箱放置地點
#     twelve_test = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no2_select))
#     thirteen_way = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=thirteen_way_select))#交貨方式
#     thirteen_elevator = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no3_select))
#     thirteen_box = forms.CharField(max_length=30,required=False)
#     thirteen_into = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no5_select)) #分箱進場
#     thirteen_shock = forms.CharField(max_length=30,required=False) #避震
#     thirteen_shocbox = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=thirteen_shocbox_select)) #避震器型式
#     thirteen_apply = forms.CharField(max_length=30,required=False) #施作
#     thirteen_fix = forms.CharField(max_length=30,required=False) #空調箱固定
#     thirteen_budget = forms.CharField(max_length=30,required=False) #預算
#     thirteen_budgetdollar = forms.CharField(max_length=30,required=False) #預算
#     thirteen_displace = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=thirteen_displace_select)) #位移
#     thirteen_displace_default = forms.CharField(max_length=30,required=False)
#     thirteen_fixway = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=thirteen_fixway_select)) #固定方式
#     thirteen_fixway_default = forms.CharField(max_length=30,required=False)
#     fourteen_ass = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no3_select)) #固定方式
#     fourteen_budget = forms.CharField(max_length=30,required=False)
#     fourteen_budgetdollar = forms.CharField(max_length=30,required=False)
#     fourteen_time = forms.CharField(max_length=30,required=False)
#     fourteen_into = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no5_select))#人員進場須知
#     fourteen_intotime = forms.CharField(max_length=30,required=False)
#     fourteen_afterass = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no5_select))
#     fourteen_afterasstime = forms.CharField(max_length=30,required=False) #上完課組裝
#     fourteen_foreigninto = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=Yes_no5_select))#外籍員工進場
#     fourteen_foreignintotime = forms.CharField(max_length=30,required=False) #上完課組裝
#     fourteen_card = forms.CharField(max_length=10,required=False,widget=forms.Select(choices=Yes_no4_select)) #證件
#     fourteen_insurance = forms.CharField(max_length=10,required=False,widget=forms.Select(choices=Yes_no4_select)) # 保險
#     fifteen_location = forms.CharField(max_length=30,required=False)#空調箱搬運定位
#     fifteen_level = forms.CharField(max_length=30,required=False) #水平搬運
#     fifteen_vertical = forms.CharField(max_length=30,required=False) #垂直搬運
#     fifteen_box = forms.CharField(max_length=30,required=False) #立式空調箱上箱段
#     sixteen_install = forms.CharField(max_length=30,required=False) #代課安裝
#     sixteen_prepare = forms.CharField(max_length=30,required=False) #備料
#     seventeen_silicone = forms.CharField(max_length=30,required=False)
#     seventeen_brand = forms.CharField(max_length=30,required=False,widget=forms.Select(choices=seventeen_brand_select)) 
#     eighteen_other = forms.CharField(widget=forms.Textarea, required=False)



