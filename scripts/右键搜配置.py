
# coding: utf-8

# In[106]:


import json
import hashlib
searchengine=["baidu","sina","weibo","google","sogou","qq","youtube","bilibili","zhihu","jianshu","quora"]
domainname=["com","co","cn"]
a={"all":"[{\"c\":\"i_title\",\"t\":\"all\",\"m\":\"MEN\",\"u\":\"options.html\",\"l\":\"all\",\"v\":10},{\"c\":\"c_bookmarks\",\"t\":\"chrome\",\"m\":\"MEN\",\"u\":\"chrome://bookmarks/#1\",\"l\":\"all\",\"v\":10},{\"c\":\"c_clearBD\",\"t\":\"chrome\",\"m\":\"MEN\",\"u\":\"chrome://settings/clearBrowserData\",\"l\":\"all\",\"v\":10},{\"c\":\"c_downloads\",\"t\":\"chrome\",\"m\":\"MEN\",\"u\":\"chrome://downloads/\",\"l\":\"all\",\"v\":10},{\"c\":\"c_extensions\",\"t\":\"chrome\",\"m\":\"MEN\",\"u\":\"chrome://extensions/\",\"l\":\"all\",\"v\":10},{\"c\":\"c_flags\",\"t\":\"chrome\",\"m\":\"MEN\",\"u\":\"chrome://flags/\",\"l\":\"all\",\"v\":10},{\"c\":\"c_history\",\"t\":\"chrome\",\"m\":\"MEN\",\"u\":\"chrome://history/\",\"l\":\"all\",\"v\":10},{\"c\":\"c_plugins\",\"t\":\"chrome\",\"m\":\"MEN\",\"u\":\"chrome://plugins/\",\"l\":\"all\",\"v\":10},{\"c\":\"c_settings\",\"t\":\"chrome\",\"m\":\"MEN\",\"u\":\"chrome://settings/\",\"l\":\"all\",\"v\":10},{\"c\":\"c_version\",\"t\":\"chrome\",\"m\":\"MEN\",\"u\":\"chrome://version/\",\"l\":\"all\",\"v\":10},{\"c\":\"facebook_menu\",\"t\":\"sns\",\"m\":\"MEN\",\"u\":\"https://www.facebook.com/dialog/feed?app_id=365325133587367&link=%s&redirect_uri=https%3A//www.facebook.com\",\"l\":\"all\",\"v\":10},{\"c\":\"gmail_page\",\"t\":\"sns\",\"m\":\"MEN\",\"u\":\"https://mail.google.com/mail/?view=cm&fs=1&tf=1&source=mailto&body=%s\",\"l\":\"all\",\"v\":10},{\"c\":\"qr\",\"t\":\"utils\",\"m\":\"MEN\",\"u\":\"qr\",\"l\":\"all\",\"v\":10},{\"c\":\"su\",\"t\":\"utils\",\"m\":\"MEN\",\"u\":\"su\",\"l\":\"all\",\"v\":10},{\"c\":\"su_alert\",\"t\":\"utils\",\"m\":\"MEN\",\"u\":\"su_alert\",\"l\":\"all\",\"v\":10},{\"c\":\"tab_close\",\"t\":\"utils\",\"m\":\"MEN\",\"u\":\"tab_close\",\"l\":\"all\",\"v\":10},{\"c\":\"c_appcache\",\"t\":\"chrome\",\"m\":\"MEN\",\"u\":\"chrome://appcache-internals\",\"l\":\"en\",\"v\":10},{\"c\":\"c_credits\",\"t\":\"chrome\",\"m\":\"MEN\",\"u\":\"chrome://credits/\",\"l\":\"en\",\"v\":10},{\"c\":\"c_memory\",\"t\":\"chrome\",\"m\":\"MEN\",\"u\":\"chrome://memory-redirect/\",\"l\":\"en\",\"v\":10},{\"c\":\"twitter_men\",\"t\":\"sns\",\"m\":\"MEN\",\"u\":\"https://twitter.com/intent/tweet?url=%s\",\"l\":\"en\",\"v\":10},{\"c\":\"qzone\",\"t\":\"sns\",\"m\":\"MEN\",\"u\":\"http://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?url=%s&title=%l\",\"l\":\"zh_CN\",\"v\":10},{\"c\":\"weibo\",\"t\":\"sns\",\"m\":\"MEN\",\"u\":\"http://service.weibo.com/share/share.php?appkey=1144650722&url=%s\",\"l\":\"zh_CN\",\"v\":10},{\"c\":\"bing\",\"t\":\"all\",\"m\":\"TXT\",\"u\":\"http://www.bing.com/search?q=%s\",\"l\":\"all\",\"v\":10},{\"c\":\"duckduckgo\",\"t\":\"all\",\"m\":\"TXT\",\"u\":\"https://duckduckgo.com/?q=%s\",\"l\":\"all\",\"v\":10},{\"c\":\"google\",\"t\":\"all\",\"m\":\"TXT\",\"u\":\"https://www.google.com/#newwindow=1&q=%s\",\"l\":\"all\",\"v\":10},{\"c\":\"translate\",\"t\":\"fy\",\"m\":\"TXT\",\"u\":\"http://translate.google.com/?q=%s\",\"l\":\"all\",\"v\":10},{\"c\":\"Baidu fanyi\",\"t\":\"fy\",\"m\":\"TXT\",\"u\":\"http://fanyi.baidu.com/?#en/zh/%s\",\"l\":\"all\",\"v\":10},{\"c\":\"thepiratebay\",\"t\":\"movie\",\"m\":\"TXT\",\"u\":\"http://thepiratebay.ee/s/%s\",\"l\":\"all\",\"v\":10},{\"c\":\"youtube\",\"t\":\"movie\",\"m\":\"TXT\",\"u\":\"http://www.youtube.com/results?search_query=%s\",\"l\":\"all\",\"v\":10},{\"c\":\"bing_images\",\"t\":\"pic\",\"m\":\"TXT\",\"u\":\"http://www.bing.com/images/search?q=%s\",\"l\":\"all\",\"v\":10},{\"c\":\"google_img\",\"t\":\"pic\",\"m\":\"TXT\",\"u\":\"https://www.google.com/search?q=%s&tbm=isch\",\"l\":\"all\",\"v\":10},{\"c\":\"facebook\",\"t\":\"sns\",\"m\":\"TXT\",\"u\":\"http://www.facebook.com/search/results.php?q=%s\",\"l\":\"all\",\"v\":10},{\"c\":\"gmail_txt\",\"t\":\"sns\",\"m\":\"TXT\",\"u\":\"https://mail.google.com/mail/?view=cm&fs=1&tf=1&body=%s&source=mailto\",\"l\":\"all\",\"v\":10},{\"c\":\"google_plus\",\"t\":\"sns\",\"m\":\"TXT\",\"u\":\"https://plus.google.com/s/%s\",\"l\":\"all\",\"v\":10},{\"c\":\"qr_txt\",\"t\":\"utils\",\"m\":\"TXT\",\"u\":\"qr_txt\",\"l\":\"all\",\"v\":10},{\"c\":\"Yahoo\",\"t\":\"all\",\"m\":\"TXT\",\"u\":\"http://search.yahoo.com/search?p=%s\",\"l\":\"en\",\"v\":10},{\"c\":\"Amazon_com\",\"t\":\"shop\",\"m\":\"TXT\",\"u\":\"http://www.amazon.com/gp/s?keyword=%s\",\"l\":\"en\",\"v\":10},{\"c\":\"twitter\",\"t\":\"sns\",\"m\":\"TXT\",\"u\":\"https://twitter.com/search?q=%s\",\"l\":\"en\",\"v\":10},{\"c\":\"twitter_share\",\"t\":\"sns\",\"m\":\"TXT\",\"u\":\"https://twitter.com/intent/tweet?text=%s\",\"l\":\"en\",\"v\":10},{\"c\":\"en_wikipedia\",\"t\":\"utils\",\"m\":\"TXT\",\"u\":\"http://en.wikipedia.org/wiki/Special:Search?search=%s\",\"l\":\"en\",\"v\":10},{\"c\":\"baidu\",\"t\":\"all\",\"m\":\"TXT\",\"u\":\"http://www.baidu.com/s?wd=%s\",\"l\":\"zh_CN\",\"v\":10},{\"c\":\"scholar\",\"t\":\"book\",\"m\":\"TXT\",\"u\":\"https://scholar.google.com/scholar?q=%s&hl=zh-CN\",\"l\":\"zh_CN\",\"v\":10},{\"c\":\"wenku\",\"t\":\"book\",\"m\":\"TXT\",\"u\":\"http://wenku.baidu.com/search?word=%g\",\"l\":\"zh_CN\",\"v\":10},{\"c\":\"image_baidu\",\"t\":\"pic\",\"m\":\"TXT\",\"u\":\"http://image.baidu.com/i?ie=utf-8&word=%s\",\"l\":\"zh_CN\",\"v\":10},{\"c\":\"amazon\",\"t\":\"shop\",\"m\":\"TXT\",\"u\":\"http://www.amazon.cn/s/?field-keywords=%s\",\"l\":\"zh_CN\",\"v\":10},{\"c\":\"ditu\",\"t\":\"utils\",\"m\":\"TXT\",\"u\":\"https://ditu.google.com/maps?hl=zh-cn&newwindow=1&q=%s\",\"l\":\"zh_CN\",\"v\":10},{\"c\":\"ditu_bing\",\"t\":\"utils\",\"m\":\"TXT\",\"u\":\"http://cn.bing.com/ditu/?q=%s\",\"l\":\"zh_CN\",\"v\":10},{\"c\":\"kd\",\"t\":\"utils\",\"m\":\"TXT\",\"u\":\"kd\",\"l\":\"zh_CN\",\"v\":10},{\"c\":\"wikipedia\",\"t\":\"utils\",\"m\":\"TXT\",\"u\":\"http://zh.wikipedia.org/wiki/Special:Search?search=%s\",\"l\":\"zh_CN\",\"v\":10},{\"c\":\"tw_wikipedia\",\"t\":\"utils\",\"m\":\"TXT\",\"u\":\"http://tw.wikipedia.org/wiki/Special:Search?search=%s\",\"l\":\"zh_TW\",\"v\":10},{\"c\":\"google_pic\",\"t\":\"all\",\"m\":\"PIC\",\"u\":\"http://www.google.com/searchbyimage?image_url=%s\",\"l\":\"all\",\"v\":10},{\"c\":\"facebook_pic\",\"t\":\"sns\",\"m\":\"PIC\",\"u\":\"https://www.facebook.com/dialog/feed?app_id=365325133587367&picture=%s&redirect_uri=https%3A//www.facebook.com\",\"l\":\"all\",\"v\":10},{\"c\":\"gmail_pic\",\"t\":\"sns\",\"m\":\"PIC\",\"u\":\"https://mail.google.com/mail/?view=cm&tf=1&source=mailto&body=%s&fs=1\",\"l\":\"all\",\"v\":10},{\"c\":\"qr_decode\",\"t\":\"utils\",\"m\":\"PIC\",\"u\":\"qr_decode\",\"l\":\"all\",\"v\":10},{\"c\":\"qr_pic\",\"t\":\"utils\",\"m\":\"PIC\",\"u\":\"qr_pic\",\"l\":\"all\",\"v\":10},{\"c\":\"su_pic\",\"t\":\"utils\",\"m\":\"PIC\",\"u\":\"su_pic\",\"l\":\"all\",\"v\":10},{\"c\":\"su_pic_alert\",\"t\":\"utils\",\"m\":\"PIC\",\"u\":\"su_pic_alert\",\"l\":\"all\",\"v\":10},{\"c\":\"exif\",\"t\":\"pic\",\"m\":\"PIC\",\"u\":\"http://regex.info/exif.cgi?dummy=on&imgurl=%s\",\"l\":\"en\",\"v\":10},{\"c\":\"twitter_pic\",\"t\":\"sns\",\"m\":\"PIC\",\"u\":\"https://twitter.com/intent/tweet?url=%s\",\"l\":\"en\",\"v\":10},{\"c\":\"weibo_pic\",\"t\":\"sns\",\"m\":\"PIC\",\"u\":\"http://service.weibo.com/share/share.php?appkey=1144650722&pic=%s\",\"l\":\"zh_CN\",\"v\":10},{\"c\":\"bing_site\",\"t\":\"all\",\"m\":\"LIN\",\"u\":\"http://www.bing.com/search?q=site%3A%s\",\"l\":\"all\",\"v\":10},{\"c\":\"google_link\",\"t\":\"all\",\"m\":\"LIN\",\"u\":\"https://www.google.com/search?q=link%3A%s\",\"l\":\"all\",\"v\":10},{\"c\":\"google_site\",\"t\":\"all\",\"m\":\"LIN\",\"u\":\"https://www.google.com/search?q=site%3A%s\",\"l\":\"all\",\"v\":10},{\"c\":\"facebook_lin\",\"t\":\"sns\",\"m\":\"LIN\",\"u\":\"https://www.facebook.com/dialog/feed?app_id=365325133587367&redirect_uri=https%3A//www.facebook.com&link=%s\",\"l\":\"all\",\"v\":10},{\"c\":\"gmail_lin\",\"t\":\"sns\",\"m\":\"LIN\",\"u\":\"https://mail.google.com/mail/?view=cm&fs=1&source=mailto&body=%s&tf=1\",\"l\":\"all\",\"v\":10},{\"c\":\"qr_lin\",\"t\":\"utils\",\"m\":\"LIN\",\"u\":\"qr_lin\",\"l\":\"all\",\"v\":10},{\"c\":\"su_lin\",\"t\":\"utils\",\"m\":\"LIN\",\"u\":\"su_lin\",\"l\":\"all\",\"v\":10},{\"c\":\"su_lin_alert\",\"t\":\"utils\",\"m\":\"LIN\",\"u\":\"su_lin_alert\",\"l\":\"all\",\"v\":10},{\"c\":\"twitter_lin\",\"t\":\"sns\",\"m\":\"LIN\",\"u\":\"https://twitter.com/intent/tweet?url=%s\",\"l\":\"en\",\"v\":10},{\"c\":\"weibo_lin\",\"t\":\"sns\",\"m\":\"LIN\",\"u\":\"http://service.weibo.com/share/share.php?url=%s&appkey=1144650722\",\"l\":\"zh_CN\",\"v\":10}]","analytics":"true","back":"false","en":"true","isEdit":"true","isFlag":"true","lb1":"\"2\"","lb2":"\"1\"","lcGroup":"[]","linBack":"[]","linCustom":"[]","linIncognito":"[]","linSelect":"[]","locale":"\"zh_CN\"","lt1":"\"1\"","lt2":"\"1\"","mcGroup":"[]","menBack":"[]","menCustom":"[]","menIncognito":"[]","menSelect":"[]","names":"{}","newPage":"true","pcGroup":"[]","phrase":"\"cloud demo\"","picBack":"[]","picCustom":"[]","picIncognito":"[]","picSelect":"[\"google_pic\",\"su_pic\",\"qr_decode\"]","qr_size":"250","rb1":"\"2\"","rb2":"\"2\"","rt1":"\"1\"","rt2":"\"2\"","ru":"true","run4":"true","shorten":"\"googl\"","tcGroup":"[]","txtBack":"[]","txtCustom":"[]","txtIncognito":"[]","txtSelect":"[]","zh_CN":"true","zh_TW":"true"}


# In[107]:


def glue(target,tail):
    result=""
    for i in target[0:tail]:
        result=result+"."+i
    return result
    
def getname(url):
    if(url.split("/")[2].split(".")[-2] in domainname):
        hl = hashlib.md5()
        hl.update(url.encode(encoding='utf-8'))
        if(len(url.split("/")[2].split("."))>=3):
            return getname("http://"+glue(url.split("/")[2].split("."),-1))
        else:
            return url.split("/")[2].split(".")[-2]+"_custom_"+hl.hexdigest()
    hl = hashlib.md5()
    hl.update(url.encode(encoding='utf-8'))
    return url.split("/")[2].split(".")[-2]+"_custom_"+hl.hexdigest()


# In[108]:


def addsites(sites,add_url,typename):
    for i in add_url:
        sites.append({'c':getname(i),"t":typename,"m":"TXT","u":i,"l":"all","v":10})
    return list(reversed(sites))
#     return list(sites)


# In[109]:


def addgroup(groups,add_url,group_name):
    group=[]
    for i in add_url:
        group.append(getname(i))
    groups.append([group_name,list(reversed(group))])
#     groups.append([group_name,group])
    return groups


# In[110]:


def additem(original,add_url,groupname):
    add_url=add_url.split("\n")
    sites = json.loads(original["all"])
    sites = addsites(sites,add_url,groupname)
    original["all"]=json.dumps(sites)
    
    tcgroups = json.loads(original["tcGroup"])
    tcgroups = addgroup(tcgroups,add_url,groupname)
    print(tcgroups)
    original["tcGroup"]=json.dumps(tcgroups)
    
    txtSelect=json.loads(original['txtSelect'])
    txtSelect.append(groupname)
    original["txtSelect"]=json.dumps(txtSelect)
    
    return original


# In[111]:


add_url=r'''https://cse.google.com/cse?cx=014251857952394190856:r8r0h_2rqie&q=%s
https://weixin.sogou.com/weixin?type=2&s_from=input&query=%s&ie=utf8&_sug_=n&_sug_type_=
https://www.zhihu.com/search?type=content&q=%s
https://www.jianshu.com/search?q=%s&page=1&type=note
https://www.quora.com/search?q=%s
https://s.weibo.com/weibo/%s?topnav=1&wvr=6&b=1
https://search.bilibili.com/all?keyword=%s&from_source=banner_search
https://www.youtube.com/results?search_query=%s'''
a = additem(a,add_url,"综合搜索")


# In[112]:


add_url=r'''https://s.weibo.com/weibo?q=%s%20资源%20链接%20提取码&wvr=6&b=1&Refer=SWeibo_box
https://s.weibo.com/weibo?q=%s%20%E8%B5%84%E6%BA%90%20%E9%93%BE%E6%8E%A5&wvr=6&b=1&Refer=SWeibo_box
https://s.weibo.com/weibo?q=%s%20%E8%B5%84%E6%BA%90&wvr=6&b=1&Refer=SWeibo_box'''
a = additem(a,add_url,"微博资源")


# In[113]:


add_url=r'''http://zhannei.baidu.com/cse/site?q=%s&cc=birdiesearch.com
http://pansou.com/?q=%s
https://www.xiaobaipan.com/list-%s.html?from=1
http://www.panduoduo.net/s/name/%s
http://www.58wangpan.com/search/kw%s
https://www.quzhuanpan.com/source/search.action?q=%s&currentPage=1'''
a = additem(a,add_url,"网盘")


# In[114]:


add_url=r'''https://cse.google.com/cse?cx=014251857952394190856:rekrhjbzzci&q=%s
http://www.btbtt08.com/search-index-keyword-%s.htm
http://www.wuhaozhan.net/s/%s/
http://www.baike789.com/s/%s/
http://www.btba.cc/search?keyword=%s
http://oabt005.com/index/index?c=&k=%s
http://zhannei.baidu.com/cse/site?q=%s&cc=piaov.com
http://zhannei.baidu.com/cse/site?q=%s&cc=2tu.cc
http://www.loldytt.org/search.asp?searchword=%s&s=
http://s.ygdy8.com/plus/so.php?typeid=1&keyword=%s
http://www.mp4ba.com/index.php?m=search&c=index&a=init&modelid=1&q=%s
https://www.cupfox.com/?type=video&key=%s
http://www.zmz2019.com/search/index?keyword=%s&search_type=
https://91mjw.com/?s=%s
https://www.zxzjs.com/vodsearch/-------------.html?wd=%s&submit=
http://zhannei.baidu.com/cse/site?q=%s&cc=meijutt.com
https://haiduomi.com/search/wd/%s.html
http://v.778qs.com/search.php?searchword=%s'''
a = additem(a,add_url,"影视搜索")


# In[115]:


add_url=r'''https://cse.google.com/cse?cx=014251857952394190856:y9bsdqpeyuu&q=%s
https://v.qq.com/x/search/?q=%s&stag=&smartbox_ab=
https://so.iqiyi.com/so/q_%s?source=input&sr=1333196430043
https://www.soku.com/nt/search/q_%s?f=1&kb=04111020kv41100__123
https://so.youku.com/search_video/q_%s?spm=a2ha1.12675304.0.i1'''
a = additem(a,add_url,"主流视频网站")


# In[116]:


add_url=r'''https://cse.google.com/cse?cx=014251857952394190856:5sagvkts2oq&q=%s
https://weibo.com/u/2091076344?is_all=1&is_search=1&key_word=%s
http://zhannei.baidu.com/cse/site?q=%s&cc=52pojie.cn
https://www.iplaysoft.com/?s=%s
https://sspai.com/search/article?q=%s
https://www.runningcheese.com/?s=%s
https://www.laomoit.com/?s=%s&x=0&y=0
http://www.dayanzai.me/?s=%s
https://www.appinn.com/?s=%s
https://www.appcgn.com/?s=%s
http://www.th-sjy.com/?s=%s
http://zuimeia.com/search/?keyword=%s&platform=2&source=
http://zhannei.baidu.com/cse/site?q=%s&cc=coolapk.com'''
a = additem(a,add_url,"软件搜索")


# In[117]:


add_url=r'''https://cse.google.com/cse?cx=014251857952394190856:yj_yw8jxtog&q=%s
https://www.bbc.co.uk/search?q=%s
http://zhannei.baidu.com/cse/search?q=%s&submit=search&s=14277178942915998683&entry=1
https://topdocumentaryfilms.com/search/?results=%s
https://www.onehourlife.com/?s=%s
http://zhannei.baidu.com/cse/site?q=%s&cc=laojilu.com
https://search.bilibili.com/all?keyword=%s&from_source=banner_search&order=totalrank&duration=0&tids_1=177
http://zhannei.baidu.com/cse/site?q=%s&cc=85lou.com
http://www.acfun.cn/search/?#query=%E7%BA%AA%E5%BD%95%E7%89%87%20%s;cid=68;sort=1;sid=0;page=1'''
a = additem(a,add_url,"纪录片")


# In[118]:


add_url=r'''https://weibo.com/u/2315252080?topnav=1&wvr=6&topsug=1&is_all=1&is_search=1&key_word=%s
https://bookfere.com/?s=%s&post_type=post
https://readfree.me/search/?q=%s
http://cn.epubee.com/books/?s=%s&action=
http://mebook.cc/?s=%s
http://tieba.baidu.com/f/search/res?ie=utf-8&kw=azw3&qw=%s&red_tag=o1615068691
https://readmoo.com/search/keyword?q=%s&kw=%s&pi=0&st=true
http://ishare.iask.sina.com.cn/search/0-0-all-1-default?cond=%s
http://www.esosu.com/search?q=%s
http://ss.chaoxing.com/search?sw=%s&x=0_7209
http://www.book118.com/search.asp?m=2&word=%s'''
a = additem(a,add_url,"中文电子书")


# In[119]:


add_url=r'''http://gen.lib.rus.ec/search.php?req=%s&lg_topic=libgen&open=0&view=simple&res=25&phrase=1&column=def
http://cn.worldlibrary.net/Results?&PageIndex=1&SearchEverything=%s
https://www.gutenberg.org/ebooks/search/?query=%s
http://www.allitebooks.com/?s=%s
https://www.obooko.com/search-result?q=%s
https://www.free-ebooks.net/search/%s
http://ebook3000.com/plus/search.php?keyword=%s&x=24&y=4
http://www.ebooks-free-net.net/ebooks-free-search.asp?cx=partner-pub-6696559636672214%3A6567896799&cof=FORID%3A10&ie=UTF-8&q=%s&sa=Search
https://www.ebooktakeaway.com/app/search.jsp?searchFrom=ebta.1&searchPackage=ebta&query=%s
http://www.booksinmyphone.com/?titleSearch=%s&authorSearch=&search=search&blurbSearch=&sizeSearch=
https://www.smashwords.com/books/search?query=%s
https://openlibrary.org/search?q=%s&mode=ebooks&m=edit&m=edit&has_fulltext=true
https://manybooks.net/search-book?search=%s&ga_submit=bsf%3AtLnxS1jIsMjleOB
https://www.thefreelibrary.com/_/search/Search.aspx?SearchBy=0&q=%s&Search=Search&By=0
https://bookboon.com/en/search?q=%s
http://www.planetpublish.com/?s=%s
https://www.planetebook.com/?s=%s
https://ebookee.org/search.php?q=%s&sa=Search
http://ebookbrowsee.net/?query=%s
http://freecomputerbooks.com/search.html?cx=partner-pub-5976068913745703%3A4325807428&cof=FORID%3A10&ie=UTF-8&q=%s&sitesearch=freecomputerbooks.com&x=0&y=0&keywords=123
https://www.google.com/search?q=site%3Afreetechbooks.com+%s
https://www.google.com/search?q=site%3Aebooklobby.com+%s
https://www.getfreeebooks.com/?s=%s
https://www.nap.edu/search/?term=%s&x=0&y=0
https://it-ebooks-search.info/search?q=%s
https://publishing.cdlib.org/ucpressebooks/search?keyword=%s&fieldList=text+title+creator+description&brand=eschol&style=eschol&smode=simple'''
a = additem(a,add_url,"外文电子书")


# In[120]:


print(json.dumps(a))

