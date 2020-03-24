import html2text as ht
import sys

def main(HtmlPath):
    text_maker = ht.HTML2Text()
    # 读取html格式文件
    with open(HtmlPath, 'r', encoding='UTF-8') as f:
        htmlpage = f.read()
    # 处理html格式文件中的内容
    text = text_maker.handle(htmlpage)
    ExceptBackPath = HtmlPath[:-7]
    print(ExceptBackPath)
    # 写入处理后的内容
    with open(ExceptBackPath+'.md', 'w') as f:
        f.write(text)
if __name__ == '__main__':
    print(sys.argv)

    if len(sys.argv) > 1:
        HtmlPath = sys.argv[1]
        main(HtmlPath)
    else:
        print('use in:python index.py [htmlPATH]')