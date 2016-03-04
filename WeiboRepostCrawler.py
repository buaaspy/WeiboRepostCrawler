# -*- coding: utf-8 -*-

from urllib2 import Request, urlopen
import sys
from useragent import UserAgent
import time
import random

reload(sys)
sys.setdefaultencoding('utf-8')

prefix = "http://weibo.com/aj/v6/mblog/info/big?ajwvr=6&id="
infix = "&page="
request_url_prefix = "http://weibo.com/aj/v6/mblog/info/big?ajwvr=6&id=3944232639300948&max_id=3948511337249771&page="
my_cookie = "Cookie:SINAGLOBAL=4541295308154.076.1442142976789; _ga=GA1.2.1262622540.1453001284; wb_feed_unfolded_1616175237=1; wvr=6; TC-Page-G0=42b289d444da48cb9b2b9033b1f878d9; SSOLoginState=1456846939; _s_tentry=login.sina.com.cn; Apache=5245718355290.592.1456847186891; ULV=1456847186922:123:1:3:5245718355290.592.1456847186891:1456751590482; TC-V5-G0=ac3bb62966dad84dafa780689a4f7fc3; TC-Ugrow-G0=370f21725a3b0b57d0baaf8dd6f16a18; YF-V5-G0=d8480b079e226c170ff763917f70c4e7; YF-Page-G0=9a31b867b34a0b4839fa27a4ab6ec79f; YF-Ugrow-G0=5b31332af1361e117ff29bb32e4d8439; UOR=,,www.3lian.com; gsid_CTandWM=4uZXCpOz5hZKCpIzV26e56Mrl3P; SUS=SID-1616175237-1456886962-GZ-is5kb-76aa7eb86602da1bb2315302a147d866; SUE=es%3D7255399f40a93c0e8c971681d9407c31%26ev%3Dv1%26es2%3D22e71776291eaa17a4c4226c3f579839%26rs0%3DlJWf3pD9LgnXsyDZrj74f1fF2jEc6CO3E7oF1ILGqMpJ5ozjW%252Bgxh4zIux74RtIldOoS8dao8m4FzDQ8fcI094q9tm15x%252BOmc23xvbp9g0iES1tGkgz9rlNht07DTX69YH66L24KsRk3022oXmnpNPxsR7CBow3XYFMpZeqo8VM%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1456886962%26et%3D1456973362%26d%3Dc909%26i%3Dd866%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D0%26st%3D0%26uid%3D1616175237%26name%3Dnaspy1987%2540sina.com%26nick%3DCartman%26fmp%3D%26lcp%3D2015-08-26%252018%253A24%253A59; SUB=_2A2570iTiDeRxGedI6lQQ9yvOyDuIHXVYphEqrDV8PUJbstBeLVDykW9LHeueRsChUGn_oYhJ-9Bf6W5LMpKpOQ..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWKbl2Hy.GTyyqPZLj8o6ew5JpX5o2p; SUHB=0tKreZdXRlwoQ-; ALF=1488382938"
my_cookie_1 = "Cookie:SINAGLOBAL=4541295308154.076.1442142976789; _ga=GA1.2.1262622540.1453001284; wb_feed_unfolded_1616175237=1; wvr=6; UOR=,,www.baidu.com; YF-V5-G0=2da76c0c227d473404dd0efbaccd41ac; YF-Ugrow-G0=4703aa1c27ac0c4bab8fc0fc5968141e; SUS=SID-1616175237-1456966788-GZ-uxv5i-1d54afa72b0310a39628f14f1277d866; SUE=es%3D71accd3879c90ced5cd058d6ee7bce8f%26ev%3Dv1%26es2%3D58e03124f01ace2dec3d9011505f6c18%26rs0%3DLJEBb1VUW7Sv1EAAmLRl10LfnGUj8zFeWb%252FaQq3Ty6hGFBJJmkjnWCyDQcSEiy3nLbH7qGDfdTZ9dA3NMHvjzXSCl8X6NHdbkYNq%252B8RGq74RizuOS7IXEvJ0qLMJtN7nfmSRfgeJq5DhsLvlcmFKDKE05UzPXGYbJySMBkZhiP4%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1456966788%26et%3D1457053188%26d%3Dc909%26i%3Dd866%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D0%26st%3D0%26uid%3D1616175237%26name%3Dnaspy1987%2540sina.com%26nick%3DCartman%26fmp%3D%26lcp%3D2015-08-26%252018%253A24%253A59; SUB=_2A2570_zUDeRxGedI6lQQ9yvOyDuIHXVYqWkcrDV8PUNbvtBeLWL6kW9LHetz4jz4S74t3R4iyURUQCJo7l4x9Q..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWKbl2Hy.GTyyqPZLj8o6ew5JpX5KMt; SUHB=0BLp0Kwp2a8d8v; ALF=1488502787; SSOLoginState=1456966788; _s_tentry=-; Apache=7147445364389.568.1456973717946; ULV=1456973718315:126:4:6:7147445364389.568.1456973717946:1456916734294; TC-V5-G0=52dad2141fc02c292fc30606953e43ef"
my_cookie_2 = "Cookie:SINAGLOBAL=4541295308154.076.1442142976789; wb_feed_unfolded_1616175237=1; wvr=6; YF-V5-G0=2da76c0c227d473404dd0efbaccd41ac; YF-Ugrow-G0=4703aa1c27ac0c4bab8fc0fc5968141e; _s_tentry=-; Apache=7147445364389.568.1456973717946; ULV=1456973718315:126:4:6:7147445364389.568.1456973717946:1456916734294; TC-V5-G0=52dad2141fc02c292fc30606953e43ef; YF-Page-G0=8ec35b246bb5b68c13549804abd380dc; TC-Page-G0=fd45e036f9ddd1e4f41a892898506007; TC-Ugrow-G0=370f21725a3b0b57d0baaf8dd6f16a18; _ga=GA1.2.1262622540.1453001284; crtg_rta=SIM300250A%3D1%3BSIM300250B%3D1%3BSIM300250C%3D1%3BSI72890%3D1%3BSI46860H%3D1%3BSI300250H%3D1%3BSI300100H%3D1%3BSI300600H%3D1%3BSIN300250T%3D1%3BSIN300100%3D1%3BSIN300250D%3D1%3BIV300600%3D1%2CIV300250S%3D1%2CIV300250L%3D1%2CIV300250R%3D1%2CIVM320100%3D1%3BWE72890%3D1%3BWE72890A%3D1%3BWE72890B%3D1%3BWE200200%3D1%3BWE336280%3D1%3BWE300600A%3D1%3BWE300600B%3D1%3BWE160600%3D1%3BWE300250M%3D1%3B; __gads=ID=dbab27bbaf5db300:T=1457013746:S=ALNI_Mba0bdEQVs0Wmjt3hFhz01pRx2hrg; WBStore=8b23cf4ec60a636c|undefined; UOR=,,www.baidu.com; SUS=SID-1616175237-1457054564-GZ-75ho9-f471c2b628ea700700589450379fd866; SUE=es%3D26e9143db19add81862cf464597c38f2%26ev%3Dv1%26es2%3D66826d08ebd7fd884e2eb74329e6b68a%26rs0%3DCLOeTGoRqnWO%252BbtdZnJuDl293RE7LgXkfXZ0k6CoXrN3vgSH3%252FkDhGmtOxTAmEGbl5amcARKj3ToGHyHJuvmEa6y3pvBejxMQru9N8%252Buy1%252FgijikHLy3KToIsZgSq5ykOV%252FXXjwoIvdQaYQ8DUkpHCHuTnvNVn%252FMu3YO74lcL%252BY%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1457054564%26et%3D1457140964%26d%3Dc909%26i%3Dd866%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D0%26st%3D0%26uid%3D1616175237%26name%3Dnaspy1987%2540sina.com%26nick%3DCartman%26fmp%3D%26lcp%3D2015-08-26%252018%253A24%253A59; SUB=_2A2573JM0DeRxGedI6lQQ9yvOyDuIHXVYq4P8rDV8PUNbvtBeLXP4kW9LHetbkUovn4X4dseO0J3FGzFCj-_VwQ..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWKbl2Hy.GTyyqPZLj8o6ew5JpX5KMt; SUHB=0rr6CNIPJVC7vh; ALF=1488590564; SSOLoginState=1457054564"

def get_request_url(mid, page):
    return prefix + str(mid) + infix + str(page)

def worker(root_id, mid, page, useragent, ops):
    data_path_prefix = "./dat4/" + str(root_id) + "_"
    log_path_suffix = ".txt"
    ISOTIMEFORMAT='%Y_%m_%d_%H_%M_%S'
    absl_data_path = data_path_prefix + str(page) + "_" + str(time.strftime(ISOTIMEFORMAT))  + log_path_suffix

    request_url = get_request_url(mid, page)

    print("request %s" % request_url)

    dat = open(absl_data_path, "a")

    resource = Request(request_url, None, {'User-Agent' : useragent.get_spider_useragent(), 'cookie' : my_cookie_2})
    response = urlopen(resource)
    data = response.read()
    print("[worker] %s" % data[0:50])
    ops.write("[worker] %s" % data[0:50])
    dat.write(data)

    dat.close()

def unicodetochinese(raw_str):
    return raw_str.decode('unicode_escape')

def get_random_wait_time():
    index = random.randint( 1,  3)
    if index == 1:
        return 0.5
    elif index == 2:
        return 0.7
    elif index == 3:
        return 1

def scheduler(root_id, mid, total_page, total_process_cnt):
    useragent = UserAgent()
    ops_log_path = "./dat4/ops.log"
    ops = open(ops_log_path, "a")

    for r in range(total_page, 0, -1):
        ops.write("[scheduler] fetch %d" % r)
        print("[scheduler] fetch %d [%d] [%d]" % (r, total_page, total_process_cnt))

        worker(root_id, mid, r, useragent, ops)

        fetch_wait_time = float(get_random_wait_time())
        ops.write("[scheduler] wait %f seconds" % fetch_wait_time)
        print("[scheduler] wait %f seconds" % fetch_wait_time)
        time.sleep(fetch_wait_time)

    ops.close()

def determine_page_num(retweet_num):
    if int(retweet_num) % 20 == 0:
        return int(retweet_num) / 20
    else:
        return int(retweet_num) / 20 + 1

def main(resume_skip):
    try:
        dat = open("./cleanroom/alpha/layer3/2016_03_04_13_00_02.txt", 'r')
        skip_threshold = int(resume_skip)
        skip = 1
        total_process_cnt = 1
        try:
            line = dat.readline()
            print line

            while line:
                if skip < skip_threshold:
                    print("[main] skip %d" % skip)
                    skip += 1
                    total_process_cnt += 1
                    line = dat.readline()
                    continue

                total_page = 0
                mid = line.split(' ')[2]
                retweet_raw_pos = line.rfind("转发")
                retweet_list = line[retweet_raw_pos:].split(" ")
                if len(retweet_list) >= 2 and len(retweet_list[1].strip('\n')) > 0:
                    retweet_num = int(retweet_list[1].strip('\n'))
                    total_page = determine_page_num(retweet_num)

                root_id = line.split(' ')[4]

                print("[main] %s %s %s" % (root_id.strip('\n'), mid.strip('\n'), total_page))
                scheduler(root_id.strip('\n'), mid.strip('\n'), total_page, total_process_cnt)

                total_process_cnt += 1
                line = dat.readline()
        except IOError:
            print("[main] fail to read html content")
            print sys.exc_info()
        finally:
            dat.close()
    except:
        print("[main] exception!!!")
        print sys.exc_info()


########################################################################################################################
# main entry
########################################################################################################################
main(0)