import requests
import os

import pandas as pd

#省份编号对应的省份名称
province_num = ["11", "12", "13", "14", "15", "21", "22", "23", "31", "32", "33", "34", "35", "36", "37", "41",
                "42", "43", "44", "45", "46", "50", "51", "52", "53", "54", "61", "62", "63", "64", "65"]

province_list = ["北京市", "天津市", "河北省", "山西省", "内蒙古自治区", "辽宁省", "吉林省", "黑龙江省", "上海市", "江苏省", "浙江省", "安徽省", "福建省",
                 "江西省", "山东省", "河南省", "湖北省", "湖南省", "广东省", "广西壮族自治区", "海南省", "重庆市", "四川省", "贵州省", "云南省", "西藏自治区",
                 "陕西省", "甘肃省", "青海省", "宁夏回族自治区", "新疆维吾尔自治区"]

p_num = 0   #province_num和province_list列表的下标

#province = "山东"


#1/2代表文理科
sub_select = 1
subject = ["#","理科","文科"]

#保存路径
filepath = r"F:\python资料\python爬虫" + "\\"

#生成初始表格
excel_head = ['学校', '编号', ' 学校排名', '时间', ' 专业', ' 录取最高分', ' 录取最低分', ' 平均分', ' 录取名次', ' 录取批次 ', '省份编号', ' 省份', ' 城市', ' 985', ' 211 ', '双一流','学校类型']
excel_file = pd.DataFrame(columns=excel_head)

#查询年份
years = 2017

#建立输出txt文

# data_file=open(filepath+ str(years) +"school_major.txt", 'w+', encoding='utf-8')
# data_file = open(filepath + province + str(years) +"school_major.txt", 'w+', encoding='utf-8')

#考试省份


# major = "信息与计算科学"   #input("请查询输入专业：")   


#浏览器的信息
headers={
    # 'Accept':'application/json, text/plain, */*',
    # 'Accept-Encoding':'gzip, deflate, sdch, br',
    # 'Accept-Language':'zh-CN,zh;q=0.8',
    # 'Connection':'keep-alive',
    # 'Host':'static-data.eol.cn',
    # 'Origin':'https://gkcx.eol.cn',
    # 'Referer':'https://gkcx.eol.cn/school/459/provinceline',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Cookie':'UM_distinctid=1738676b30f41df-0365e98486fe63-5d4e211f-100200-1738676b319243; tool_ipprovince=41; areaid=41; cityid=4113; rank=0; CNZZDATA1254842253=1286397502-1595689274-https%253A%252F%252Fmnzy.eol.cn%252F%7C1595689274; CNZZDATA1000489091=1999706531-1595689337-https%253A%252F%252Fmnzy.eol.cn%252F%7C1595689337; code=0; CNZZDATA1254841856=1264948125-1595686365-https%253A%252F%252Fmnzy.eol.cn%252F%7C1595686365; CNZZDATA1254844262=434157501-1595686868-https%253A%252F%252Fmnzy.eol.cn%252F%7C1595686868; CNZZDATA1254806806=1893915729-1595690110-https%253A%252F%252Fmnzy.eol.cn%252F%7C1595690110; CNZZDATA1254842204=680561951-1595692275-https%253A%252F%252Fwww.baidu.com%252F%7C1595692275; CNZZDATA1254807737=2139366979-1595690472-https%253A%252F%252Fwww.baidu.com%252F%7C1595690472; Hm_lvt_0a962de82782bad64c32994d6c9b06d3=1595691295; Hm_lpvt_0a962de82782bad64c32994d6c9b06d3=1595698466; CNZZDATA1254806898=1929412132-1595722693-%7C1595722693; CNZZDATA1254852089=837126804-1595719855-https%253A%252F%252Fgkcx.eol.cn%252F%7C1595719855; CNZZDATA1254841828=990429286-1595686201-https%253A%252F%252Fmnzy.eol.cn%252F%7C1595723911; Hm_lvt_9b4517aa97b6b67e7c396bef15886cef=1595691530,1595693569,1595698783,1595698862; Hm_lpvt_9b4517aa97b6b67e7c396bef15886cef=1595727066; CNZZDATA1261518594=2073575712-1595693975-https%253A%252F%252Fgkcx.eol.cn%252F%7C1595722851; areaid=41; cityid=4113; CNZZDATA4696252=cnzz_eid%3D1760691203-1595688001-%26ntime%3D1595725871; eol_avd_set=1595729127936; lastvisit=1595729127936'

}

start_num = 1
end_num = 50

for temp in range(1,33):

    p_num = province_num[temp]

    province = province_list[temp]

    #print("正在读取" + province + "的分数信息……")

    for years in range(2017,2020):

        #print("正在读取" + str(years) + "的分数信息……")
        #遍历学校编号范围32~968

        for sub_select in range(1,3):

            print("正在读取" + province + str(years) + str(subject[sub_select]) + "的分数信息……")
            # 打开文件
            data_file = open(filepath + province + str(subject[sub_select]) + str(years) + "高考分数.txt", 'w+',encoding='utf-8')

            for schoolNum in range(start_num, end_num, 1):
                #输出进度
                Precent = (schoolNum-start_num)/(end_num-start_num)
                print('%.2f%%' % (Precent * 100))
                #获取学校编号对应的名称

                url_school = 'https://static-data.eol.cn/www/2.0/school/%s/info.json'%str(schoolNum)
                response_school = requests.get(url=url_school,headers=headers)
                #debug节点
                aponit1 = response_school.json()
                #判断URL是否为空，空了跳出
                if(response_school.json() == ''):
                    continue
                #学校名称
                school_name = response_school.json()['data']['name']
                #学校排名
                school_rank = int(response_school.json()['data']['ruanke_rank'])
                #学校所在地方
                school_provinceId = int(response_school.json()['data']['province_id'])
                school_provinceName = response_school.json()['data']['province_name']
                school_cityName = response_school.json()['data']['city_name']

                #985、211、双一流信息
                school_f985 = 2-int(response_school.json()['data']['f985'])
                school_f211 = 2-int(response_school.json()['data']['f211'])
                school_dualClass= response_school.json()['data']['dual_class_name']
                school_typeName = response_school.json()['data']['school_type_name']

                #网页范围设置为5
                for pageNum in range(1,6):
                    # url_major = 'https://static-data.eol.cn/www/2.0/schoolspecialindex/%s/%s/41/1/%s.json'%(str(years),str(schoolNum),pageNum)
                    # 41省份河南 32省份江苏 37山东 1(2)理(文)科
                    url_major = 'https://static-data.eol.cn/www/2.0/schoolspecialindex/%s/%s/%s/%s/%s.json' % (str(years), str(schoolNum),
                                                                                                               str(p_num), sub_select, pageNum)
                    response_major = requests.get(url=url_major,headers=headers)

                    #time.sleep(0.5)
                    #如果是空网页，跳过本次循环
                    if(response_major.json()==''):
                        break
                    #找到相关的专业，输出信息
                    for items in response_major.json()['data']['item']:
                        # if('spname' in items):
                        #     if (items['spname'] == major):
                        #         print (school_name,'\t',items['spname'],'\t',str(times),'\t',str(major),'\t',"录取最高分",items['max'],'\t',"录取最低分",items['min'],'\t',"平均分：",items['average'],'\t',"最低分：",items['min'],'\t',"最低位次:",items['min_section'],'\t',"录取批次:",items['local_batch_name'],'\n', file=data_file)
                        print (school_name,'\t',schoolNum,'\t',items['spname'],'\t',str(years),'\t',"录取最高分",items['max'],'\t',"录取最低分",items['min'],'\t',"平均分：",items['average'],'\t','\t',"最低位次:",items['min_section'],'\t',"录取批次:",items['local_batch_name'],'\n', file=data_file)
                        #写入excel中
                        data_elemen=[school_name,schoolNum,school_rank,years,items['spname'],items['max'],items['min'],items['average'],items['min_section'],items['local_batch_name'],school_provinceId,school_provinceName,school_cityName,school_f985,school_f211,school_dualClass,school_typeName]
                        excel_fileTmp = pd.DataFrame([data_elemen], columns=excel_head)
                        excel_file=pd.concat([excel_file,excel_fileTmp],ignore_index=True)

            #关闭数据电子流
            data_file.close()

            #保存excel
            # excel_file.to_excel(filepath+str(years)+"大学录取分数线.xlsx",index=False)
            excel_file.to_excel(filepath + province + str(subject[sub_select]) + str(years) + "大学录取分数线.xlsx", index=False)
            #del excel_file
            excel_file.drop(excel_file.index, inplace=True)
            #os.system('pause')
        #结束

        print (str(years) + province + "高考分数信息查询完成！")

        #os.system('pause')

    p_num+=1


print ("高考分数信息查询完成！")