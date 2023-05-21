from json import load as l

import UnZip

from pkg import MakeHtml as m
from pkg.MakeHtml import HTML, head, body
from pkg.MakeHtml import title_bar as title2
from pkg.MakeHtml import MainBodyOption, TitleBarOption, tag

o=open

with o('option.json','r') as f:
    data=l(f)

who=data['~에게']

first_script = tag('script','',**{'async src':"https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4999549568827188"}, crossorigin="anonymous")

head = head(
    (first_script,'<meta name="viewport" content="width=device-width">'),
    title_bar = ('style',100),
    title = 'MacBook!!',
    link = {
'URI':"style.css",
'rel':"stylesheet",
'type':"text/css",
    }
)
bodys = '<br>'*10



bodys += tag('img','',closing=False, src="https://img.appstory.co.kr/@files/monthly.appstory.co.kr/content/202111/a548918e67ad45723edcc50c4494bebf.jpg", alt="잠만 뭐지 버근가 왜 이미지가 안떠", width="160", height="100")

mbi=MainBodyOption()
tbo=TitleBarOption()

value=title2(f'{who} 맥북을 사주세요!', tbo, mbi, bodys, titles = {}, menu = {
    'bar':{},
    'menu-object':{}
})

bodys = body(value)
source = HTML(head, bodys, lang = "ko")
print('\n'*10)
with open('index.html','w') as f:
    f.write(source)
print(source)