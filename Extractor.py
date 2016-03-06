# -*- coding: utf-8 -*-

import os
import sys
import time
from bs4 import BeautifulSoup


class WeiboExtract:
    fakeHead = """
                <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
                <html xmlns="http://www.w3.org/1999/xhtml">
                <head>
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                <title>Fake Title</title>
                <body>
            """
    fakeTail = """
                </body>
                </head>
                </html>
            """

    def __init__(self):
        self.data_root_path = "./dat6/"
        self.out_root_path = "./cleanroom/alpha/layer6/"
        self.parse_microblog_warning = 0
        self.parse_microblog_warning_threshold = 100
        self.parse_html_warning = 0
        self.parse_html_warning_threshold = 100
        self.isotimeformat = '%Y_%m_%d_%H_%M_%S'
        self.microblog_dic = {}

    def unicodetochinese(self, raw_str):
        return raw_str.decode('unicode_escape')

    def compare(self, l, r):
        lf = os.stat(self.data_root_path + l)
        rf = os.stat(self.data_root_path + r)

        if lf.st_ctime < rf.st_ctime:
            return -1
        elif lf.st_ctime > rf.st_ctime:
            return 1
        else:
            return 0

    def list_dir_files_by_ctime(self):
        files = os.listdir(self.data_root_path)
        files.sort(self.compare)
        return files

    def get_canonical_file_name(self):
        return self.out_root_path + str(time.strftime(self.isotimeformat)) + ".txt"

    def preprocess_one_file_content(self, content):
        start_token = '"html":"'
        end_token = '"page":'
        start = content.find(start_token)
        end = content.rfind(end_token)

        if start == -1 or end == -1:
            print("[extractor] WARNING !!! cannot find start or end token !!!")
            self.warning += 1
            return ""
        else:
            content = content[start + len(start_token): end - 1]
            content = content.replace("\\t", "\t")
            content = content.replace("\\r\\n", "\r\n")
            content = content.replace("\\/", "/")
            content = content.replace('\\"', '"')

            return self.fakeHead + content + self.fakeTail

    def extract_one_file(self, file):
        filename = file
        owner_id = filename.split("_")[0]
        print("[extractor] extract file: %s owner: %s" % (file, owner_id))

        file = self.data_root_path + file

        try:
            html = open(file, 'r')
            try:
                content = html.read()
                content = self.preprocess_one_file_content(content)
            except IOError:
                print("[extractor] fail to read html content")
            finally:
                html.close()
        except:
            self.parse_html_warning += 1
            print("[extractor] fail to open %s" % file)
            print sys.exc_info()

        one_page_content = []
        try:
            soup = BeautifulSoup(content, "html.parser")
            for item in soup.find_all(attrs={"action-type" : "feed_list_item"}):
                try:
                    mid = item.get("mid")

                    name_node = item.find(attrs={"node-type" : "name"})
                    name = self.unicodetochinese(name_node.get_text())

                    usercard = name_node.get("usercard")
                    id_pos = usercard.find("=")
                    uid = usercard[id_pos + 1 :]

                    date_node = item.find(attrs={"node-type" : "feed_list_item_date"})
                    date = self.unicodetochinese(date_node.get_text())

                    con_node = item.find(attrs={"node-type" : "text"})
                    con = self.unicodetochinese(con_node.get_text())

                    feed_forward_node = item.find(attrs={"action-type" : "feed_list_forward"})
                    feed_forward = self.unicodetochinese(feed_forward_node.get_text())

                    like_status_node = item.find(attrs={"node-type" : "like_status"})
                    like_em_node = like_status_node.find("em")
                    like = self.unicodetochinese(like_em_node.get_text())

                    print("%s %s %s %s %s %s %s %s %s" % (filename, date, mid, owner_id, uid, name, con, feed_forward, like))
                    key = date + mid + owner_id + uid
                    if key not in self.microblog_dic:
                        retweet = date + " " + mid + " " + owner_id + " " + uid + " " + name + " " + con + " " + feed_forward + " " + like
                        one_page_content.append(retweet)
                        self.microblog_dic[key] = 1

                except:
                    print("[extractor] WARNING !!! fail to parse content !!!")
                    print sys.exc_info()
                    self.parse_microblog_warning += 1
                    continue
        except:
            self.parse_html_warning += 1
            print("[extractor][extract_one_file] exception !!!")
            print sys.exc_info()

        one_page_content.reverse()
        return one_page_content


    def worker(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')

        try:
            out = open(self.get_canonical_file_name(), 'a')

            for f in self.list_dir_files_by_ctime():
                if self.parse_microblog_warning > self.parse_microblog_warning_threshold:
                    print("[extractor] %s: too much parse error !!!" % str(time.strftime(self.isotimeformat)))

                if self.parse_html_warning > self.parse_html_warning_threshold:
                    print("[extractor] %s: too much parse error !!!" % str(time.strftime(self.isotimeformat)))

                try:
                    for retweet in self.extract_one_file(f):
                        out.write("%s\n" % retweet)
                        out.flush()
                except:
                    print("[extractor][worker][write] exception!!!")
                    print sys.exc_info()
        except:
            print("[extractor][worker] exception !!!")
            print sys.exc_info()
        finally:
            out.close()


if __name__ == "__main__":
    weiboExtract = WeiboExtract()
    weiboExtract.worker()
