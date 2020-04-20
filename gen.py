import json
import time
import datetime

startime=datetime.datetime.now()
print('Generating static html...')
print('Loading config...')
file = open('config.json', encoding='utf-8')
config = json.load(file)
username = config['auth'][0]['username']
num = config['blog'][0]['num']
file.close()

index=[]
post_template = open('source/template/post_head.html', encoding='utf-8').read()+ \
    open('source/template/post_body.html', encoding='utf-8').read()+ \
    open('source/template/post_foot.html', encoding='utf-8').read()

for i in range(num):
    template=post_template
    post_text = open('source/'+str(i)+'.html', encoding='utf-8').read()
    
    # TODO images index
    template=template.replace('$title',config['posts'][i]['title'])
    template=template.replace('$name',config['blog'][0]['name'])
    template=template.replace('$date',time.strftime(config['blog'][0]['datestyle'], time.localtime(config['posts'][i]['date'])))
    template=template.replace('$footer',config['blog'][0]['footer'])
    template=template.replace('$text',post_text)

    post_out=open('posts/'+str(i)+'.html',mode='w',encoding='utf-8')
    post_out.write(template)
    index.append(config['posts'][i]['title'])
    print('- '+config['auth'][0]['username']+' - '+str(i)+' - '+config['posts'][i]['title']+' - '+time.strftime(config['blog'][0]['datestyle'], time.localtime(config['posts'][i]['date'])))

endtime=datetime.datetime.now()

for i_ in index:
    # TODO index
    print(' ')
print('Done in %sms !'%str((endtime-startime).seconds%1000))