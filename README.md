# onedrive sharepoint 批量下载 
      用于从onedrive的sharepoint处批量下载文件 参考了[HenryzhaoH](https://github.com/HenryzhaoH/sharepoint-batch-download-listgen)代码
## Instructions
      总体的思路是先获得onedrive所有文件的路径，然后通过chrome的自动下载功能进行下载
### step1 
      先获得sharepoint的路径和网页的cookie
      1 F12 打开网页的控制台 刷新一下 
      2 上方菜单栏 Network 然后搜索RenderListDataAsStream 点击一下name的下方的一个 找到HttpRoot 
      "https://xxxx-my.sharepoint.com/personal/xxxxxxxxxxxxxxxxx 
      最后的sharepoint的路径就是： 
      https://xxxx-my.sharepoint.com/personal/xxxxxxxxxxxxxxxxx/Documents/
      在最后面加个Documents

      3 cookie 点击Application  FedAuth 点击一下 出来的一长串的值就是了 

### step2 
         点击 get_url.py 填写你的COOKIE_FEDAUTH 和SHAREPOINT_ROOT
         然后 run一下  获得当前onedrive内的文件地址 写入到get_url.txt中 
         e.g. https://xxxx-my.sharepoint.com/personal/xxxxxxxxxxxxxxxxx/Documents/xxxxx.npy

### step3 
      设置你的默认浏览器为Chrome  去chrome_download.py 处设置下save_path 文件较大 网速较慢的时候 最下面的sleep时间可以长一些


