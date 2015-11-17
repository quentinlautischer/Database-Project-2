import re

class rgxHandler:

    # Taken from https://www.safaribooksonline.com/library/view/python-cookbook-2nd/0596007973/ch01s19.html
    getrids = dict([("product/productId: ",''), ("product/title: ",''), ("product/price: ",''), ("review/userId: ",''), ("review/profileName: ",''), ("review/helpfulness: ",''), ("review/score: ",''), ("review/time: ",''), ("review/summary: ",''), ("review/text: ",'')])
    replace = {"\\":"\\\\", '"': "&quot;" }

    def __init__(self):
        pass

    def multiple_replace(self, text, adict):
        rx = re.compile('|'.join(map(re.escape, adict)))
        def one_xlat(match):
            return adict[match.group(0)]
        return rx.sub(one_xlat, text)

    def line_rgx(self, text):
        rtnline = self.multiple_replace(text.strip('\n'), self.getrids)
        rtnline = self.multiple_replace(rtnline, self.replace)
        return rtnline

    def find3OrMore(self, line):
        words = line.split()
        rtnwords = []

        for word in words:
            if len(word.strip()) >= 3:
               rtnwords.append(word.strip().lower())
        return rtnwords
                    


