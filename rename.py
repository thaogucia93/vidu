import os


os.chdir(r'C:\Users\admin\Desktop\C')
a = os.listdir()

cu = ' - Copy.jpg'
moi = '.jpg'


def rename_file(old):
    new = old.replace(cu, moi)
    return new


for i in range(0, len(a) - 1, 1):
    try:
        b = rename_file(a[i])
        os.rename(a[i], b)
    except:
        pass

print('da xoa "copy"')
