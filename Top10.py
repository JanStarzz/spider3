import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
url1 = 'http://music.163.com/discover/toplist?id=3778678'
headers = {
    'Cookie':'__e_=1515461191756; _ntes_nnid=af802a7dd2cafc9fef605185da6e73fb,1515461190617; _ntes_nuid=af802a7dd2cafc9fef605185da6e73fb; JSESSIONID-WYYY=HMyeRdf98eDm%2Bi%5CRnK9iB%5ChcSODhA%2Bh4jx5t3z20hhwTRsOCWhBS5Cpn%2B5j%5CVfMIu0i4bQY9sky%5CsvMmHhuwud2cDNbFRD%2FHhWHE61VhovnFrKWXfDAp%5CqO%2B6cEc%2B%2BIXGz83mwrGS78Goo%2BWgsyJb37Oaqr0IehSp288xn5DhgC3Cobe%3A1515585307035; _iuqxldmzr_=32; __utma=94650624.61181594.1515583507.1515583507.1515583507.1; __utmc=94650624; __utmz=94650624.1515583507.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmb=94650624.4.10.1515583507',
    'Host':'music.163.com',
    'Refere':'http://music.163.com/',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
txt_name = "./歌单.txt"
csv_name = "./歌单.csv"
xlsx_name = "./歌单.xlsx"


def get_music(url):
    contents = []
    req = requests.get(url, headers=headers)   # 获得网站请求
    req.encoding = "utf-8"   # 设置编码
    soup = BeautifulSoup(req.text, 'html-parser')
    musics = soup.find('ul', class_="f-hide").find_all('a')  # 获得所有a元素的列表
    for index, music in enumerate(musics):
        content = []
        no = index+1  # 排名
        name = music.text   # 歌名
        u = 'http://music.163.com'+music['href']  # 网页url
        content.append(no)
        content.append(name)
        content.append(u)
        contents.append(content)
    return contents


def write_csv(file_name, content_str):  # 用panda库写入csv
    name = ["排名", "歌名", "网址"]  # 三列元素，列名分别为职业名，地址，薪资
    salary = pd.DataFrame(columns=name, data=content_str)
    salary.to_csv(file_name)


def write_excel(file_name, list_content):
    wb = openpyxl.Workbook()  # 新建Excel工作簿
    st = wb.active
    st['A1'] = "歌单"  # 修改为自己的标题
    second_row = ["排名", "歌名", "网址"]  # 根据实际情况写属性
    st.append(second_row)
    for row in list_content:
        st.append(row)
    wb.save(file_name)  # 新工作簿的名称


def write_txt(file_name, content_str):   # 写入txt的函数
    with open(file_name, "w", encoding='utf-8', ) as f:
        for content in content_str:   # 第一层for循环获得每个工作的样本
            for j in content:       # 第二层获得工资的样本
                f.write(str(j)+"   ")    # 写入文本
            f.write('\n')  # 换行
        f.close


if __name__ == '__main__':
    contents = get_music(url1)
    write_csv(csv_name, contents)
    write_excel(xlsx_name, contents)
    write_txt(txt_name, contents)