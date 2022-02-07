import time
import requests
import numpy as np
from driver import get_driver
from PIL import Image, ImageEnhance
from ksdemo import KSClient, USERNAME, PASSWORD


def get_ver_code(driver):
    driver.save_screenshot('hebao_login.png')
    codeEelement = driver.find_element_by_xpath("//img[@id='longin_code_img']")
    # print('验证码图片', codeEelement, type(codeEelement))
    imgSize = codeEelement.size  # 获取验证码图片的大小
    # print('图片大小', imgSize, type(imgSize))
    imgLocation = codeEelement.location  # 获取验证码元素坐标
    # print('图片位置', imgLocation, type(imgLocation))
    rangle = (int(imgLocation['x'] + 2.6 * imgSize['width']), int(imgLocation['y'] + 2.5 * imgSize['height']),
              int(imgLocation['x'] + 4 * imgSize['width']), int(imgLocation['y'] + 4 * imgSize['height']))  # 计算验证码整体坐标
    # print(rangle)
    login = Image.open('hebao_login.png').convert('RGB')
    """
    截取下来验证码图片，并且进行灰度转化，二值化处理
    """
    loginImg = login.crop(rangle)  # 截取验证码图片
    # loginImg.show()
    loginImg = loginImg.convert("L")  # convert()方法传入参数L，将图片转化为灰度图像
    # loginImg.show()
    loginImg = np.asarray(loginImg)
    loginImg = (loginImg > 100) * 255
    loginImg = Image.fromarray(loginImg).convert('RGB')
    sharpness = ImageEnhance.Contrast(loginImg)
    loginImg = sharpness.enhance(3.0)
    loginImg = loginImg.resize((300, 100))
    # loginImg.show()
    loginImg.save('a.jpg')

    Ks95man = KSClient()
    if Ks95man.GetTaken(USERNAME, PASSWORD):
        ver_str = Ks95man.PostPic('a.jpg', 1)
        return ver_str


def get_cookie():
    driver = get_driver()
    try:
        print('get_cookie')
        driver.get('https://www.qichamao.com/')
        time.sleep(2)
        driver.find_element_by_xpath("//div[@class='header-right']//a[contains(text(), '登录')]").click()
        driver.find_element_by_xpath("//li[contains(text(), '账号登录')]").click()
        time.sleep(3)

        ver_code = get_ver_code(driver)
        driver.find_element_by_name("VerifyCode").send_keys(ver_code)
        driver.find_element_by_name("userId").send_keys("13611576533")
        driver.find_element_by_name("password").send_keys("6533qcm")
        driver.find_element_by_xpath("//form[@id='formLogin']//button[@class='btn btn-sub f18']").click()
        time.sleep(3)

        while True:
            cookies_ = driver.get_cookies()
            cookie_item = dict()
            for cookie in cookies_:
                name = cookie.get('name')
                value = cookie.get('value')
                cookie_item[name] = value
            if cookie_item.get('qz.newsite'):    # 有该键则cookie正确，没有就一直循环获取
                break
            else:
                ver_code = get_ver_code(driver)
                driver.find_element_by_name("VerifyCode").send_keys(ver_code)
                driver.find_element_by_xpath("//form[@id='formLogin']//button[@class='btn btn-sub f18']").click()
                time.sleep(3)

        print('got_cookie')
        driver.close()
        return cookie_item
    except Exception as e:
        print(e)


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    }
    cookies = get_cookie()
    res = requests.get('https://www.qichamao.com/search/all/华为技术有限公司', headers=headers, cookies=cookies)
    print(res.text)
