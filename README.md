该目录下共包含如下6个文件：
### 1. chromedriver.exe
chrome浏览器驱动，必须跟本机电脑的chrome浏览器版本一致或最新版本，chrome版本可在浏览器设置中查看，chromedriver下载地址：[https://registry.npmmirror.com/binary.html?path=chromedriver/](https://registry.npmmirror.com/binary.html?path=chromedriver/)
​

### 2. driver.py
对浏览器驱动进行一些参数配置，后面模拟登陆获取cookie时用到
​

### 3. kedemo.py
验证码图片识别脚本，用到了快识免费图片验证码识别平台，详情可见：[https://www.jianshu.com/p/f6d05f035de7](https://www.jianshu.com/p/f6d05f035de7)
​

### 4. monilogin.py
模拟登录脚本，通过selenium模拟登录企查猫并获取cookie，用于后面请求
​

### 5. qichamao.py
主程序，里面的get_proxy()函数，用到了闪臣HTTP代理，新用户有10000次免费ip可以用（即每次请求用掉一次），用完了可以在以下链接重新注册并更换API链接，USERNAME跟PASSWORD也记得更改，其他不用改动。
还有就是该脚本是把数据都装到列表中，最后再一次性写入Excel，可以将原企业list的读取行数该小，即脚本中的 ws.max_row 可适当调小，避免跑不完而没数据存到Excel。
​

### 6. test01.xlsx
原企业list。
​

### 开发环境：
pycharm、python3.9
​

### 注：如使用 proxies 代理时ValueError: check_hostname requires server_hostname，参看一下链接：[https://www.jianshu.com/p/aa245a73c0b0](https://www.jianshu.com/p/aa245a73c0b0)
