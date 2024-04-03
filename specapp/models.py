from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Spec(models.Model):
    cNumber = models.CharField(max_length=50, default='',null=False)#單號
    cProject = models.CharField(max_length=50,null=False)
    cName = models.CharField(max_length=50, default='',null=False) #業務
    cClient = models.CharField(max_length=50,null=False)#客戶
    clocation = models.CharField(max_length=50,default='',null=False)#工地名稱
    cContact = models.CharField(max_length=50,default='',null=False)#聯絡人
    cContactTel = models.CharField(max_length=50,default='',null=False)#電話
    cDate = models.CharField(max_length=50,default='',null=False)#填表日期
    cDeliveryDate = models.CharField(max_length=50,default='',null=False)#交貨日期
    chaveorder = models.CharField(max_length=50,default='無',null=False)
    cFile = models.FileField(blank=True, null=True)
    
    class Meta:
        db_table = "Spec"


class product(models.Model):
    productCode = models.CharField(max_length=50,default='',null=False)#產品編號
    productName = models.CharField(max_length=250,default='',null=False)#產品名稱

    class Meta:
        db_table = "product"

class Special(models.Model):
    cClient=models.CharField(max_length=50, default='',null=False)#業主名稱
    cSpecial = models.TextField(blank=True)#特殊規格
    cBrand= models.TextField(blank=True)#品牌指定
    class Meta:
        db_table = "Special"

class Compare(models.Model):
    cNumber = models.CharField(max_length=50, default='',null=False)
    ctable1 = models.TextField(blank=True)
    ctable2 = models.TextField(blank=True)
    cConform = models.CharField(max_length=10)
    cPage = models.CharField(max_length=20)
    cBrand = models.CharField(max_length=10)
    cRemark = models.TextField(blank=True)
    ref = models.ForeignKey(Spec, on_delete=models.CASCADE, default="" ,related_name='details')

    class Meta:
        db_table = "Compare"

class tablespec(models.Model):
    cNumber = models.CharField(max_length=50, default='',null=False)
    machinename = models.CharField(max_length=20,default='',null=False)
    first_boxmaterial = models.CharField(max_length=30,default='',null=False)
    first_inthick = models.CharField(max_length=30,default='',null=False)
    first_inmaterial = models.CharField(max_length=30,default='',null=False)
    first_inother = models.CharField(max_length=30,default='',null=False) # 配件
    first_outmaterial = models.CharField(max_length=30,default='',null=False)
    first_outthick = models.CharField(max_length=30,default='',null=False)
    first_boxthick = models.CharField(max_length=30,default='',null=False)
    second_door = models.CharField(max_length=30,default='',null=False)
    second_frame = models.CharField(max_length=30,default='',null=False)
    third_basic = models.CharField(max_length=30,default='',null=False)
    third_basic_install = models.CharField(max_length=30,default='',null=False)
    third_basic_thick = models.CharField(max_length=30,default='',null=False)
    third_basic_brand = models.CharField(max_length=30,default='',null=False)
    third_basic_efficient = models.CharField(max_length=30,default='',null=False)
    third_basic_frame = models.CharField(max_length=30,default='',null=False)
    third_basic_material = models.CharField(max_length=30,default='',null=False)
    third_medium = models.CharField(max_length=30,default='',null=False) 
    third_medium_frameform = models.CharField(max_length=30,default='',null=False) #外框型式
    third_medium_long = models.CharField(max_length=30,default='',null=False) #袋長
    third_medium_brand = models.CharField(max_length=30,default='',null=False)
    third_medium_efficient = models.CharField(max_length=30,default='',null=False)#確定有
    third_medium_frame = models.CharField(max_length=30,default='',null=False)#濾網框
    third_high = models.CharField(max_length=30,default='',null=False)
    third_high_frameform = models.CharField(max_length=30,default='',null=False) #外框型式
    third_high_long = models.CharField(max_length=30,default='',null=False)
    third_high_brand = models.CharField(max_length=30,default='',null=False)
    third_high_efficient = models.CharField(max_length=30,default='',null=False)
    third_high_frame = models.CharField(max_length=30,default='',null=False)
    third_basic_medium_material = models.CharField(max_length=50,default='',null=False)
    third_high_material = models.CharField(max_length=30,default='',null=False)
    four_heater = models.CharField(max_length=30,default='',null=False)
    four_material = models.CharField(max_length=30,default='',null=False)
    four_way = models.CharField(max_length=30,default='',null=False)
    four_SSCR = models.CharField(max_length=30,default='',null=False)
    fiv_humidifier = models.CharField(max_length=30,default='',null=False)
    fiv_form = models.CharField(max_length=30,default='',null=False)
    six_winddoor = models.CharField(max_length=30,default='',null=False)
    six_form = models.CharField(max_length=30,default='',null=False)
    six_frame_material = models.CharField(max_length=30,default='',null=False)
    six_blade_material = models.CharField(max_length=30,default='',null=False)
    six_axis = models.CharField(max_length=30,default='',null=False)
    seven_cold = models.CharField(max_length=30,default='',null=False)
    seven_fins = models.CharField(max_length=30,default='',null=False)
    seven_thick = models.CharField(max_length=30,default='',null=False)
    seven_board = models.CharField(max_length=30,default='',null=False)
    seven_pipe_thick = models.CharField(max_length=30,default='',null=False)
    seven_waterpipe = models.CharField(max_length=30,default='',null=False)
    seven_size = models.CharField(max_length=30,default='',null=False)
    seven_hot = models.CharField(max_length=30,default='',null=False)
    seven_hotfins = models.CharField(max_length=30,default='',null=False)
    seven_hotthick = models.CharField(max_length=30,default='',null=False)
    seven_hotboard = models.CharField(max_length=30,default='',null=False)
    seven_hotpipe_thick = models.CharField(max_length=30,default='',null=False)
    seven_hotwaterpipe = models.CharField(max_length=30,default='',null=False)
    seven_hotsize = models.CharField(max_length=30,default='',null=False)
    seven_steam = models.CharField(max_length=30,default='',null=False)
    seven_steamfins = models.CharField(max_length=30,default='',null=False)
    seven_steamthick = models.CharField(max_length=30,default='',null=False)
    seven_steamboard = models.CharField(max_length=30,default='',null=False)
    seven_steampipe_thick = models.CharField(max_length=30,default='',null=False)
    seven_steamwaterpipe = models.CharField(max_length=30,default='',null=False)
    seven_steamsize = models.CharField(max_length=30,default='',null=False)
    seven_brine = models.CharField(max_length=30,default='',null=False)
    seven_brinefins = models.CharField(max_length=30,default='',null=False)
    seven_brinethick = models.CharField(max_length=30,default='',null=False)
    seven_brineboard = models.CharField(max_length=30,default='',null=False)
    seven_brinepipe_thick = models.CharField(max_length=30,default='',null=False)
    seven_brinewaterpipe = models.CharField(max_length=30,default='',null=False)
    seven_brinesize = models.CharField(max_length=30,default='',null=False)
    seven_other = models.CharField(max_length=30,default='',null=False)
    eight_material = models.CharField(max_length=30,default='',null=False)
    eight_thick = models.CharField(max_length=30,default='',null=False)
    nine_brand = models.CharField(max_length=30,default='',null=False)
    nine_way = models.CharField(max_length=30,default='',null=False)
    nine_form = models.CharField(max_length=30,default='',null=False)
    ten_motor_brand = models.CharField(max_length=30,default='',null=False)
    ten_motor_elec = models.CharField(max_length=30,default='',null=False)
    ten_motor_efficient = models.CharField(max_length=30,default='',null=False)#效率
    ten_motor_Insulation= models.CharField(max_length=30,default='',null=False)#絕緣
    ten_motor_level = models.CharField(max_length=30,default='',null=False)#防護等級
    ten_motor_open = models.CharField(max_length=30,default='',null=False)#啟動方式
    ten_motor_cold = models.CharField(max_length=30,default='',null=False)#冷卻方式
    ten_motor_ask = models.CharField(max_length=30,default='',null=False)#其他要求
    ten_motor_form = models.CharField(max_length=30,default='',null=False)#馬達型式
    eleven_material = models.CharField(max_length=30,default='',null=False)
    eleven_form = models.CharField(max_length=30,default='',null=False)
    eleven_key = models.CharField(max_length=30,default='',null=False)
    eleven_level = models.CharField(max_length=30,default='',null=False)
    eleven_size = models.CharField(max_length=30,default='',null=False)
    twelve_view = models.CharField(max_length=30,default='',null=False)
    twelve_pressure = models.CharField(max_length=30,default='',null=False) #壓差計
    twelve_unit = models.CharField(max_length=30,default='',null=False) #刻度單位
    twelve_brand = models.CharField(max_length=30,default='',null=False) #廠牌
    twelve_light = models.CharField(max_length=30,default='',null=False) 
    twelve_level = models.CharField(max_length=30,default='',null=False) #防護等級
    twelve_light_elec = models.CharField(max_length=30,default='',null=False) #照明店員
    twelve_light_open = models.CharField(max_length=30,default='',null=False) #照明開關
    twelve_winddoor = models.CharField(max_length=30,default='',null=False) #風門
    twelve_net = models.CharField(max_length=30,default='',null=False) #擴散網
    twelve_material = models.CharField(max_length=30,default='',null=False) 
    twelve_silicone = models.CharField(max_length=30,default='',null=False)
    twelve_location = models.CharField(max_length=30,default='',null=False) #空調箱放置地點
    twelve_roof = models.CharField(max_length=30,default='',null=False)
    twelve_newmaterial = models.CharField(max_length=30,default='',null=False)
    twelve_test = models.CharField(max_length=30,default='',null=False)
    thirteen_way = models.CharField(max_length=30,default='',null=False)#交貨方式
    thirteen_elevator = models.CharField(max_length=30,default='',null=False)
    thirteen_box = models.CharField(max_length=30,default='',null=False)
    thirteen_into = models.CharField(max_length=30,default='',null=False) #分箱進場
    thirteen_shock = models.CharField(max_length=30,default='',null=False) #避震
    thirteen_shocbox = models.CharField(max_length=30,default='',null=False) #避震器型式
    thirteen_apply = models.CharField(max_length=30,default='',null=False) #施作
    thirteen_fix = models.CharField(max_length=30,default='',null=False) #空調箱固定
    thirteen_budget = models.CharField(max_length=30,default='',null=False) #預算
    thirteen_budgetdollar = models.CharField(max_length=30,default='',null=False)
    thirteen_displace = models.CharField(max_length=30,default='',null=False) #位移
    thirteen_fixway = models.CharField(max_length=30,default='',null=False) #固定方式
    fourteen_ass = models.CharField(max_length=30,default='',null=False) #固定方式
    fourteen_budget = models.CharField(max_length=30,default='',null=False)
    fourteen_budgetdollar = models.CharField(max_length=30,default='',null=False)
    fourteen_time = models.CharField(max_length=30,default='',null=False)
    fourteen_into = models.CharField(max_length=30,default='',null=False)#人員進場須知
    fourteen_intotime = models.CharField(max_length=30,default='',null=False)
    fourteen_afterass = models.CharField(max_length=30,default='',null=False) #上完課組裝
    fourteen_afterasstime = models.CharField(max_length=30,default='',null=False)
    fourteen_foreigninto = models.CharField(max_length=30,default='',null=False)#外籍員工進場
    fourteen_foreignintotime = models.CharField(max_length=30,default='',null=False)
    fourteen_card = models.CharField(max_length=10,default='',null=False) #證件
    fourteen_insurance = models.CharField(max_length=10,default='',null=False) # 保險
    fifteen_location = models.CharField(max_length=30,default='',null=False)#空調箱搬運定位
    fifteen_level = models.CharField(max_length=30,default='',null=False) #水平搬運
    fifteen_vertical = models.CharField(max_length=30,default='',null=False) #垂直搬運
    fifteen_box = models.CharField(max_length=30,default='',null=False) #立式空調箱上箱段
    sixteen_install = models.CharField(max_length=30,default='',null=False) #代課安裝
    sixteen_prepare = models.CharField(max_length=30,default='',null=False) #備料
    seventeen_silicone = models.CharField(max_length=30,default='',null=False)
    seventeen_brand = models.CharField(max_length=30,default='',null=False) 
    eighteen_other = models.TextField(blank=True)
    home = models.OneToOneField(Spec, on_delete=models.CASCADE,default='')

    class Meta:
        db_table = "tablespec"


# class tableBOM(models.Model):
#      cBOMFile = models.FileField(blank=True, null=True)
#      chaveorder = models.CharField(max_length=50,default='無',null=False)
#      SpecBOM = models.ForeignKey(Spec, on_delete=models.CASCADE, default="" ,related_name='detailes')
#      class Meta:
#         db_table = "tableBOM"
        
# class OrderBOM(models.Model):
#     cNumber = models.IntegerField(validators=[MaxValueValidator(9223372036854775807)],null=False)
#     machinename = models.CharField(max_length=20,default='',null=False)
#     first_boxmaterial = models.CharField(max_length=30,default='',null=False)
#     first_inthick = models.CharField(max_length=30,default='',null=False)
#     first_inmaterial = models.CharField(max_length=30,default='',null=False)
#     first_inother = models.CharField(max_length=30,default='',null=False) # 配件
#     first_outmaterial = models.CharField(max_length=30,default='',null=False)
#     first_outthick = models.CharField(max_length=30,default='',null=False)
#     first_boxthick = models.CharField(max_length=30,default='',null=False)
#     second_door = models.CharField(max_length=30,default='',null=False)
#     second_frame = models.CharField(max_length=30,default='',null=False)
#     third_basic = models.CharField(max_length=30,default='',null=False)
#     third_basic_install = models.CharField(max_length=30,default='',null=False)
#     third_basic_thick = models.CharField(max_length=30,default='',null=False)
#     third_basic_brand = models.CharField(max_length=30,default='',null=False)
#     third_basic_efficient = models.CharField(max_length=30,default='',null=False)
#     third_basic_frame = models.CharField(max_length=30,default='',null=False)
#     third_basic_material = models.CharField(max_length=30,default='',null=False)
#     third_medium = models.CharField(max_length=30,default='',null=False) 
#     third_medium_frameform = models.CharField(max_length=30,default='',null=False) #外框型式
#     third_medium_long = models.CharField(max_length=30,default='',null=False) #袋長
#     third_medium_brand = models.CharField(max_length=30,default='',null=False)
#     third_medium_efficient = models.CharField(max_length=30,default='',null=False)#確定有
#     third_medium_frame = models.CharField(max_length=30,default='',null=False)#濾網框
#     third_high = models.CharField(max_length=30,default='',null=False)
#     third_high_frameform = models.CharField(max_length=30,default='',null=False) #外框型式
#     third_high_long = models.CharField(max_length=30,default='',null=False)
#     third_high_brand = models.CharField(max_length=30,default='',null=False)
#     third_high_efficient = models.CharField(max_length=30,default='',null=False)
#     third_high_frame = models.CharField(max_length=30,default='',null=False)
#     third_basic_medium_material = models.CharField(max_length=50,default='',null=False)
#     third_high_material = models.CharField(max_length=30,default='',null=False)
#     four_heater = models.CharField(max_length=30,default='',null=False)
#     four_material = models.CharField(max_length=30,default='',null=False)
#     four_way = models.CharField(max_length=30,default='',null=False)
#     four_SSCR = models.CharField(max_length=30,default='',null=False)
#     fiv_humidifier = models.CharField(max_length=30,default='',null=False)
#     fiv_form = models.CharField(max_length=30,default='',null=False)
#     six_winddoor = models.CharField(max_length=30,default='',null=False)
#     six_form = models.CharField(max_length=30,default='',null=False)
#     six_frame_material = models.CharField(max_length=30,default='',null=False)
#     six_blade_material = models.CharField(max_length=30,default='',null=False)
#     six_axis = models.CharField(max_length=30,default='',null=False)
#     seven_cold = models.CharField(max_length=30,default='',null=False)
#     seven_fins = models.CharField(max_length=30,default='',null=False)
#     seven_thick = models.CharField(max_length=30,default='',null=False)
#     seven_board = models.CharField(max_length=30,default='',null=False)
#     seven_pipe_thick = models.CharField(max_length=30,default='',null=False)
#     seven_waterpipe = models.CharField(max_length=30,default='',null=False)
#     seven_size = models.CharField(max_length=30,default='',null=False)
#     seven_hot = models.CharField(max_length=30,default='',null=False)
#     seven_hotfins = models.CharField(max_length=30,default='',null=False)
#     seven_hotthick = models.CharField(max_length=30,default='',null=False)
#     seven_hotboard = models.CharField(max_length=30,default='',null=False)
#     seven_hotpipe_thick = models.CharField(max_length=30,default='',null=False)
#     seven_hotwaterpipe = models.CharField(max_length=30,default='',null=False)
#     seven_hotsize = models.CharField(max_length=30,default='',null=False)
#     seven_steam = models.CharField(max_length=30,default='',null=False)
#     seven_steamfins = models.CharField(max_length=30,default='',null=False)
#     seven_steamthick = models.CharField(max_length=30,default='',null=False)
#     seven_steamboard = models.CharField(max_length=30,default='',null=False)
#     seven_steampipe_thick = models.CharField(max_length=30,default='',null=False)
#     seven_steamwaterpipe = models.CharField(max_length=30,default='',null=False)
#     seven_steamsize = models.CharField(max_length=30,default='',null=False)
#     seven_brine = models.CharField(max_length=30,default='',null=False)
#     seven_brinefins = models.CharField(max_length=30,default='',null=False)
#     seven_brinethick = models.CharField(max_length=30,default='',null=False)
#     seven_brineboard = models.CharField(max_length=30,default='',null=False)
#     seven_brinepipe_thick = models.CharField(max_length=30,default='',null=False)
#     seven_brinewaterpipe = models.CharField(max_length=30,default='',null=False)
#     seven_brinesize = models.CharField(max_length=30,default='',null=False)
#     seven_other = models.CharField(max_length=30,default='',null=False)
#     eight_material = models.CharField(max_length=30,default='',null=False)
#     eight_thick = models.CharField(max_length=30,default='',null=False)
#     nine_brand = models.CharField(max_length=30,default='',null=False)
#     nine_brand_default = models.CharField(max_length=30,default='',null=False)
#     nine_way = models.CharField(max_length=30,default='',null=False)
#     nine_form = models.CharField(max_length=30,default='',null=False)
#     ten_motor_brand = models.CharField(max_length=30,default='',null=False)
#     ten_motor_brand_default = models.CharField(max_length=30,default='',null=False)
#     ten_motor_elec = models.CharField(max_length=30,default='',null=False)
#     ten_motor_efficient = models.CharField(max_length=30,default='',null=False)#效率
#     ten_motor_Insulation= models.CharField(max_length=30,default='',null=False)#絕緣
#     ten_motor_level = models.CharField(max_length=30,default='',null=False)#防護等級
#     ten_motor_open = models.CharField(max_length=30,default='',null=False)#啟動方式
#     ten_motor_cold = models.CharField(max_length=30,default='',null=False)#冷卻方式
#     ten_motor_ask = models.CharField(max_length=30,default='',null=False)#其他要求
#     ten_motor_form = models.CharField(max_length=30,default='',null=False)#馬達型式
#     eleven_material = models.CharField(max_length=30,default='',null=False)
#     eleven_form = models.CharField(max_length=30,default='',null=False)
#     eleven_key = models.CharField(max_length=30,default='',null=False)
#     eleven_level = models.CharField(max_length=30,default='',null=False)
#     eleven_size = models.CharField(max_length=30,default='',null=False)
#     twelve_view = models.CharField(max_length=30,default='',null=False)
#     twelve_pressure = models.CharField(max_length=30,default='',null=False) #壓差計
#     twelve_unit = models.CharField(max_length=30,default='',null=False) #刻度單位
#     twelve_brand = models.CharField(max_length=30,default='',null=False) #廠牌
#     twelve_light = models.CharField(max_length=30,default='',null=False) 
#     twelve_level = models.CharField(max_length=30,default='',null=False) #防護等級
#     twelve_light_elec = models.CharField(max_length=30,default='',null=False) #照明店員
#     twelve_light_open = models.CharField(max_length=30,default='',null=False) #照明開關
#     twelve_winddoor = models.CharField(max_length=30,default='',null=False) #風門
#     twelve_net = models.CharField(max_length=30,default='',null=False) #擴散網
#     twelve_material = models.CharField(max_length=30,default='',null=False) 
#     twelve_silicone = models.CharField(max_length=30,default='',null=False)
#     twelve_silicone_default = models.CharField(max_length=30,default='',null=False)
#     twelve_location = models.CharField(max_length=30,default='',null=False) #空調箱放置地點
#     twelve_roof = models.CharField(max_length=30,default='',null=False)
#     twelve_newmaterial = models.CharField(max_length=30,default='',null=False)
#     twelve_test = models.CharField(max_length=30,default='',null=False)
#     thirteen_way = models.CharField(max_length=30,default='',null=False)#交貨方式
#     thirteen_elevator = models.CharField(max_length=30,default='',null=False)
#     thirteen_box = models.CharField(max_length=30,default='',null=False)
#     thirteen_into = models.CharField(max_length=30,default='',null=False) #分箱進場
#     thirteen_shock = models.CharField(max_length=30,default='',null=False) #避震
#     thirteen_shocbox = models.CharField(max_length=30,default='',null=False) #避震器型式
#     thirteen_apply = models.CharField(max_length=30,default='',null=False) #施作
#     thirteen_fix = models.CharField(max_length=30,default='',null=False) #空調箱固定
#     thirteen_budget = models.CharField(max_length=30,default='',null=False) #預算
#     thirteen_budgetdollar = models.CharField(max_length=30,default='',null=False)
#     thirteen_displace = models.CharField(max_length=30,default='',null=False) #位移
#     thirteen_displace_default = models.CharField(max_length=30,default='',null=False)
#     thirteen_fixway = models.CharField(max_length=30,default='',null=False) #固定方式
#     thirteen_fixway_default = models.CharField(max_length=30,default='',null=False) 
#     fourteen_ass = models.CharField(max_length=30,default='',null=False) #固定方式
#     fourteen_budget = models.CharField(max_length=30,default='',null=False)
#     fourteen_budgetdollar = models.CharField(max_length=30,default='',null=False)
#     fourteen_time = models.CharField(max_length=30,default='',null=False)
#     fourteen_into = models.CharField(max_length=30,default='',null=False)#人員進場須知
#     fourteen_intotime = models.CharField(max_length=30,default='',null=False)
#     fourteen_afterass = models.CharField(max_length=30,default='',null=False) #上完課組裝
#     fourteen_afterasstime = models.CharField(max_length=30,default='',null=False)
#     fourteen_foreigninto = models.CharField(max_length=30,default='',null=False)#外籍員工進場
#     fourteen_foreignintotime = models.CharField(max_length=30,default='',null=False)
#     fourteen_card = models.CharField(max_length=10,default='',null=False) #證件
#     fourteen_insurance = models.CharField(max_length=10,default='',null=False) # 保險
#     fifteen_location = models.CharField(max_length=30,default='',null=False)#空調箱搬運定位
#     fifteen_level = models.CharField(max_length=30,default='',null=False) #水平搬運
#     fifteen_vertical = models.CharField(max_length=30,default='',null=False) #垂直搬運
#     fifteen_box = models.CharField(max_length=30,default='',null=False) #立式空調箱上箱段
#     sixteen_install = models.CharField(max_length=30,default='',null=False) #代課安裝
#     sixteen_prepare = models.CharField(max_length=30,default='',null=False) #備料
#     seventeen_silicone = models.CharField(max_length=30,default='',null=False)
#     seventeen_brand = models.CharField(max_length=30,default='',null=False) 
#     eighteen_other = models.TextField(blank=True)
#     home = models.OneToOneField(tableBOM, on_delete=models.CASCADE,default='')

#     class Meta:
#         db_table = "OrderBOM"





# class Shipping(models.Model):
#     cOrder=models.CharField(max_length=50, default='',null=False)#工令
#     cCase=models.CharField(max_length=50, default='',null=False) #案件名稱
#     cCaseOp=models.CharField(max_length=50, default='',null=False) #案件選項
#     cDelivery =models.CharField(max_length=50, default='',null=False) #交期
#     cContact=models.CharField(max_length=50, default='',null=False) #工地聯絡人
#     cAddress=models.CharField(max_length=50, default='',null=False) #工地地址
#     cOther=models.CharField(max_length=50, default='',null=False) #其他
#     cMove=models.CharField(max_length=50, default='',null=False) #吊搬運
#     cMovecheck=models.CharField(max_length=50, default='',null=False) #現場勘查
#     cMoveBudget=models.CharField(max_length=50, default='',null=False)#預算
#     cOnsite=models.CharField(max_length=50, default='',null=False)#現場組裝
#     cdaynight=models.CharField(max_length=50, default='',null=False)#施工日夜間
#     cHour=models.CharField(max_length=50, default='',null=False)#施工小時
#     cAssembleBudget=models.CharField(max_length=50, default='',null=False)#現場組裝預算
#     cInto=models.CharField(max_length=50, default='',null=False)#上課
#     cAfterass=models.CharField(max_length=50, default='',null=False)#當天上完課組裝
#     cForeigninto=models.CharField(max_length=50, default='',null=False)#外籍員工進場
#     cCard=models.CharField(max_length=50, default='',null=False)#六小時公安證件
#     cInsurance=models.CharField(max_length=50, default='',null=False)#工地意外保險
#     cprepare=models.CharField(max_length=50, default='',null=False)#備料
#     cProcurementad=models.CharField(max_length=50, default='',null=False)#採購建議書
#     cTest=models.CharField(max_length=50, default='',null=False)#廠驗
#     cMoring=models.CharField(max_length=50, default='',null=False)#內部工作早會
#     cERP=models.CharField(max_length=50, default='',null=False)#內部工作ERP
#     cLee=models.CharField(max_length=50, default='',null=False)#內部工作李慶
#     cBlower=models.CharField(max_length=50, default='',null=False)#內部工作送風機
#     cInternalother=models.CharField(max_length=50, default='',null=False)#內部工作其他
#     cBoxing=models.CharField(max_length=50, default='',null=False)#結箱
#     cBoxingbudget=models.CharField(max_length=50, default='',null=False)#結箱預算
#     home = models.OneToOneField(tablespec, on_delete=models.CASCADE,default='')
#     class Meta:
#         db_table = "Shipping"


