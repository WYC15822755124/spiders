#encoding: utf-8

import re

#r = raw =原生的
# text = "apple price is $299"
# ret = re.search("\$\d+",text)
# print(ret.group())

text = "\\n"
#= '\n'
#python : '\\n' = \n
#\\\\n-> \\n
#正则表达式中：\n=
#\\n->\n
# ret = re.match('\\\\n',text)
# print(ret.group())

text = "\\n"
ret = re.match(r'\\n',text)
print(ret.group())