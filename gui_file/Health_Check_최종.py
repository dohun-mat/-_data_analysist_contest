import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 한글 폰트 사용을 위해서 세팅
import matplotlib
matplotlib.rcParams['font.family'] ='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] =False


class Health_Check:
    def __init__(self, input_data, legacy_data):
        self.input_data =pd.read_csv(input_data).query("age >= 65 and cfam ==1 and fam_rela == 1")
        self.legacy_data = pd.read_csv(legacy_data).query("age >= 65 and cfam ==1 and fam_rela == 1")
        
        self.input_years = self.input_data["year"].unique()
        self.legacy_years = self.legacy_data["year"].unique()
        self.disease_names = self.legacy_data.iloc[:,-13:].columns.to_list()
        self.nu_names = self.legacy_data.iloc[:,92:109].columns.to_list()
        self.dict_region = {'서울': 1, '부산': 2,'대구': 3,'인천': 4,'광주': 5,
                            '대전': 6,'울산': 7,'세종': 8,'경기': 9,'강원': 10,
                            '충북': 11,'충남': 12,'전북': 13,'전남': 14,'경북': 15,
                            '경남': 16,'제주': 17}
        self.lst_nu = ['식품섭취량', '에너지', '수분', '단백질', '지방', '탄수화물', '칼슘', '인', '철', '나트륨',
                        '칼륨', '베타카로틴', '레티놀', '티아민', '리보플라빈', '나이아신', '비타민C']
        
        self.legacy_data_서울 = self.legacy_data[self.legacy_data["region"] == self.dict_region["서울"]]
        self.legacy_data_부산 = self.legacy_data[self.legacy_data["region"] == self.dict_region["부산"]]
        self.legacy_data_대구 = self.legacy_data[self.legacy_data["region"] == self.dict_region["대구"]]
        self.legacy_data_인천 = self.legacy_data[self.legacy_data["region"] == self.dict_region["인천"]]
        self.legacy_data_광주 = self.legacy_data[self.legacy_data["region"] == self.dict_region["광주"]]
        self.legacy_data_대전 = self.legacy_data[self.legacy_data["region"] == self.dict_region["대전"]]
        self.legacy_data_울산 = self.legacy_data[self.legacy_data["region"] == self.dict_region["울산"]]
        self.legacy_data_세종 = self.legacy_data[self.legacy_data["region"] == self.dict_region["세종"]]
        self.legacy_data_경기 = self.legacy_data[self.legacy_data["region"] == self.dict_region["경기"]]
        self.legacy_data_강원 = self.legacy_data[self.legacy_data["region"] == self.dict_region["강원"]]
        self.legacy_data_충북 = self.legacy_data[self.legacy_data["region"] == self.dict_region["충북"]]
        self.legacy_data_충남 = self.legacy_data[self.legacy_data["region"] == self.dict_region["충남"]]
        self.legacy_data_전북 = self.legacy_data[self.legacy_data["region"] == self.dict_region["전북"]]
        self.legacy_data_전남 = self.legacy_data[self.legacy_data["region"] == self.dict_region["전남"]]
        self.legacy_data_경북 = self.legacy_data[self.legacy_data["region"] == self.dict_region["경북"]]
        self.legacy_data_경남 = self.legacy_data[self.legacy_data["region"] == self.dict_region["경남"]]
        self.legacy_data_제주 = self.legacy_data[self.legacy_data["region"] == self.dict_region["제주"]]
        
        self.input_data_서울 = self.input_data[self.input_data["region"] == self.dict_region["서울"]]
        self.input_data_부산 = self.input_data[self.input_data["region"] == self.dict_region["부산"]]
        self.input_data_대구 = self.input_data[self.input_data["region"] == self.dict_region["대구"]]
        self.input_data_인천 = self.input_data[self.input_data["region"] == self.dict_region["인천"]]
        self.input_data_광주 = self.input_data[self.input_data["region"] == self.dict_region["광주"]]
        self.input_data_대전 = self.input_data[self.input_data["region"] == self.dict_region["대전"]]
        self.input_data_울산 = self.input_data[self.input_data["region"] == self.dict_region["울산"]]
        self.input_data_세종 = self.input_data[self.input_data["region"] == self.dict_region["세종"]]
        self.input_data_경기 = self.input_data[self.input_data["region"] == self.dict_region["경기"]]
        self.input_data_강원 = self.input_data[self.input_data["region"] == self.dict_region["강원"]]
        self.input_data_충북 = self.input_data[self.input_data["region"] == self.dict_region["충북"]]
        self.input_data_충남 = self.input_data[self.input_data["region"] == self.dict_region["충남"]]
        self.input_data_전북 = self.input_data[self.input_data["region"] == self.dict_region["전북"]]
        self.input_data_전남 = self.input_data[self.input_data["region"] == self.dict_region["전남"]]
        self.input_data_경북 = self.input_data[self.input_data["region"] == self.dict_region["경북"]]
        self.input_data_경남 = self.input_data[self.input_data["region"] == self.dict_region["경남"]]
        self.input_data_제주 = self.input_data[self.input_data["region"] == self.dict_region["제주"]]
        
        self.lst_legacy_pop =  [len(self.legacy_data),len(self.legacy_data_강원),len(self.legacy_data_경기),len(self.legacy_data_경남),
                                len(self.legacy_data_경북),len(self.legacy_data_광주),len(self.legacy_data_대구),len(self.legacy_data_대전),
                                len(self.legacy_data_부산), len(self.legacy_data_서울),len(self.legacy_data_세종),len(self.legacy_data_울산),
                                len(self.legacy_data_인천),len(self.legacy_data_전남),len(self.legacy_data_전북),len(self.legacy_data_충남),
                                len(self.legacy_data_충북),len(self.legacy_data_제주)]
        
        self.lst_input_pop =   [len(self.input_data),len(self.input_data_강원),len(self.input_data_경기),len(self.input_data_경남),
                                len(self.input_data_경북),len(self.input_data_광주),len(self.input_data_대구),len(self.input_data_대전),
                                len(self.input_data_부산),len(self.input_data_서울),len(self.input_data_세종),len(self.input_data_울산),
                                len(self.input_data_인천),len(self.input_data_전남),len(self.input_data_전북),len(self.input_data_충남),
                                len(self.input_data_충북),len(self.input_data_제주)]
                        
        # self.lst_legacy_pop= [len(self.legacy_data)]
        # for region_name in self.dict_region.keys():
        #     self.lst_legacy_pop.append(len(self.legacy_data.query("region == {}".format(self.dict_region[region_name]))))
        
        
        
    # 기능(1. 전국 - 지역 2. 지역 - 지역 3. 년도-년도간의 비교)
    def disease_check(self, *args):
        if len(args) == 2:
            if type(args[1]) == str :
                self.search_region = args[0]
                self.compare_region= args[1]
                self.between_year = None
            else:
                if type(args[1]) == list :
                    self.search_region = args[0]
                    self.compare_region = None
                    self.between_year = args[1]
        elif len(args) == 1:
            self.search_region = args[0]
            self.compare_region= None
            self.between_year = None
        else:
            raise ValueError
            
        self.disease_legacy_data = self.legacy_data.iloc[:,-13:]
        self.disease_input_data = self.input_data.iloc[:,-13:]
        
        def sumdiseasedata(x):
            disease = []
            for name in self.disease_names:
                if 1 in x[name].value_counts().index:
                    if len(x[name].value_counts()) == 3:
                        disease.append(x[name].value_counts().values[2])
                    else: disease.append(x[name].value_counts()[1])
                else: disease.append(0)
            df_disease = pd.DataFrame(np.array(disease).reshape(-1,13))
            df_disease.columns = self.disease_names
            return df_disease

        self.sum_disease_legacy_data_전국 = sumdiseasedata(self.disease_legacy_data)    
        self.sum_disease_legacy_data_강원 = sumdiseasedata(self.legacy_data_강원)
        self.sum_disease_legacy_data_경기 = sumdiseasedata(self.legacy_data_경기)
        self.sum_disease_legacy_data_경남 = sumdiseasedata(self.legacy_data_경남)
        self.sum_disease_legacy_data_경북 = sumdiseasedata(self.legacy_data_경북)
        self.sum_disease_legacy_data_광주 = sumdiseasedata(self.legacy_data_광주)
        self.sum_disease_legacy_data_대구 = sumdiseasedata(self.legacy_data_대구)
        self.sum_disease_legacy_data_대전 = sumdiseasedata(self.legacy_data_대전)
        self.sum_disease_legacy_data_부산 = sumdiseasedata(self.legacy_data_부산)
        self.sum_disease_legacy_data_서울 = sumdiseasedata(self.legacy_data_서울)
        self.sum_disease_legacy_data_세종 = sumdiseasedata(self.legacy_data_세종)
        self.sum_disease_legacy_data_울산 = sumdiseasedata(self.legacy_data_울산)
        self.sum_disease_legacy_data_인천 = sumdiseasedata(self.legacy_data_인천)
        self.sum_disease_legacy_data_전남 = sumdiseasedata(self.legacy_data_전남)
        self.sum_disease_legacy_data_전북 = sumdiseasedata(self.legacy_data_전북)
        self.sum_disease_legacy_data_충남 = sumdiseasedata(self.legacy_data_충남)
        self.sum_disease_legacy_data_충북 = sumdiseasedata(self.legacy_data_충북)
        self.sum_disease_legacy_data_제주 = sumdiseasedata(self.legacy_data_제주)
        self.sum_disease_legacy_data_all =pd.concat([
                          self.sum_disease_legacy_data_전국,self.sum_disease_legacy_data_강원,self.sum_disease_legacy_data_경기,
                          self.sum_disease_legacy_data_경남,self.sum_disease_legacy_data_경북,self.sum_disease_legacy_data_광주,
                          self.sum_disease_legacy_data_대구,self.sum_disease_legacy_data_대전,self.sum_disease_legacy_data_부산,
                          self.sum_disease_legacy_data_서울,self.sum_disease_legacy_data_세종,self.sum_disease_legacy_data_울산,
                          self.sum_disease_legacy_data_인천,self.sum_disease_legacy_data_전남,self.sum_disease_legacy_data_전북,
                          self.sum_disease_legacy_data_충남,self.sum_disease_legacy_data_충북,self.sum_disease_legacy_data_제주
                          ])
        self.sum_disease_legacy_data_all.index = ["전국", "강원", "경기", "경남", "경북", "광주", "대구", "대전", "부산", "서울", "세종", "울산",
                             "인천", "전남", "전북", "충남", "충북", "제주"]
        
        self.sum_disease_input_data_전국 = sumdiseasedata(self.disease_input_data)    
        self.sum_disease_input_data_강원 = sumdiseasedata(self.input_data_강원)
        self.sum_disease_input_data_경기 = sumdiseasedata(self.input_data_경기)
        self.sum_disease_input_data_경남 = sumdiseasedata(self.input_data_경남)
        self.sum_disease_input_data_경북 = sumdiseasedata(self.input_data_경북)
        self.sum_disease_input_data_광주 = sumdiseasedata(self.input_data_광주)
        self.sum_disease_input_data_대구 = sumdiseasedata(self.input_data_대구)
        self.sum_disease_input_data_대전 = sumdiseasedata(self.input_data_대전)
        self.sum_disease_input_data_부산 = sumdiseasedata(self.input_data_부산)
        self.sum_disease_input_data_서울 = sumdiseasedata(self.input_data_서울)
        self.sum_disease_input_data_세종 = sumdiseasedata(self.input_data_세종)
        self.sum_disease_input_data_울산 = sumdiseasedata(self.input_data_울산)
        self.sum_disease_input_data_인천 = sumdiseasedata(self.input_data_인천)
        self.sum_disease_input_data_전남 = sumdiseasedata(self.input_data_전남)
        self.sum_disease_input_data_전북 = sumdiseasedata(self.input_data_전북)
        self.sum_disease_input_data_충남 = sumdiseasedata(self.input_data_충남)
        self.sum_disease_input_data_충북 = sumdiseasedata(self.input_data_충북)
        self.sum_disease_input_data_제주 = sumdiseasedata(self.input_data_제주)
        self.sum_disease_input_data_all =pd.concat([self.sum_disease_input_data_전국,self.sum_disease_input_data_강원,self.sum_disease_input_data_경기,
                                                    self.sum_disease_input_data_경남,self.sum_disease_input_data_경북,self.sum_disease_input_data_광주,
                                                    self.sum_disease_input_data_대구,self.sum_disease_input_data_대전,self.sum_disease_input_data_부산,
                                                    self.sum_disease_input_data_서울,self.sum_disease_input_data_세종,self.sum_disease_input_data_울산,
                                                    self.sum_disease_input_data_인천,self.sum_disease_input_data_전남,self.sum_disease_input_data_전북,
                                                    self.sum_disease_input_data_충남,self.sum_disease_input_data_충북,self.sum_disease_input_data_제주,
                                                    ])
        self.sum_disease_input_data_all.index = ["전국", "강원", "경기", "경남", "경북", "광주", "대구", "대전", "부산", "서울", "세종", "울산",
                             "인천", "전남", "전북", "충남", "충북", "제주"]
        
        self.sum_disease_legacy_data_all_ratio = (self.sum_disease_legacy_data_all.T/ self.lst_legacy_pop).T
        self.sum_disease_input_data_all_ratio = (self.sum_disease_input_data_all.T/ self.lst_input_pop).T
        
        return self.compare_region, self.between_year, self.sum_disease_input_data_all,self.sum_disease_input_data_all_ratio,self.search_region,self.disease_names