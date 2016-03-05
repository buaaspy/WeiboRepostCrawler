# -*- coding: utf-8 -*-

"""
 random agent
"""

import random

class UserAgent:
    mozillas = [ "4", "5", "6", "7" ]
    nts = [ "5.0", "5.1", "5.2", "6.0", "6.1" ]
    ies = [ "6", "7", "8", "9" ]
    firefoxs = [ "3", "4", "5", "6", "7", "8", "9", "10", "11" ]
    chromes = [ "18.0.1025.151", "10.0.648.204", "11.0.696.16", "12.0.768.332", "13.0.738.392", "14.0.880.32", "15.0.211.44", "16.0.810.327", "17.0.669.24" ]

    def get_spider_useragent(self):
        return 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'

    def get_random_useragent(self):
        index = random.randint( 1,  3)
        if index ==  1:
            return self.get_ie_useragent()
        elif index ==  2:
            return self.get_chrome_useragent()
        else:
            return self.get_firefox_useragent()

    def rr(self, l):
        return l[random.randint( 0, len(l) -  1)]

    def get_ie_useragent(self):
        return 'Mozilla/{0}.0 (compatible; MSIE {1}.0; Windows NT {2}; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.2)'.format(self.rr(self.mozillas), self.rr(self.ies), self.rr(self.nts))

    def get_chrome_useragent(self):
        return 'Mozilla/{0}.0 (Windows NT {1}) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/{2} Safari/535.19'.format(self.rr(self.mozillas), self.rr(self.nts), self.rr(self.chromes))

    def get_firefox_useragent(self):
        return 'Mozilla/{0}.0 (Windows NT {1}; rv:11.0) Gecko/20100101 Firefox/{2}.0'.format(self.rr(self.mozillas), self.rr(self.nts), self.rr(self.firefoxs))