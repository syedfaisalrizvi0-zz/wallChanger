import os
from random import randint
path = os.getcwd()+'/img'
arr = [str(x)for x in os.listdir(path)]
ran = randint(0,len(arr))
os.system("gsettings set org.gnome.desktop.background picture-uri file:///"+path+'/'+arr[ran])
