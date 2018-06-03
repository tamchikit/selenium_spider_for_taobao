#声明浏览器对象
from selenium import webdriver
 
browser = webdriver.Chrome()
browser = webdriver.Firefox()
browser = webdriver.Edge()
browser = webdriver.PhantomJS()
browser = webdriver.Safari()

#访问页面
#我们可以用get()方法来请求网页，参数传入链接URL即可。比如，这里用get()方法访问淘宝，然后打印出源代码
from selenium import webdriver
 
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
print(browser.page_source)
browser.close()

#查找节点
from selenium import webdriver
 
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first, input_second, input_third)
browser.close()

#find_element_by_id(id)就等价于find_element(By.ID, id)，二者得到的结果完全一致。用代码实现一下：
from selenium import webdriver
from selenium.webdriver.common.by import By
 
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_first = browser.find_element(By.ID, 'q')
print(input_first)
browser.close()

#多个节点
#如果要查找所有满足条件的节点，需要用find_elements()这样的方法。
from selenium import webdriver
 
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
lis = browser.find_elements_by_css_selector('.service-bd li')
print(lis)
browser.close()
#lis = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')

#节点交互
#输入文字时用send_keys()方法，清空文字时用clear()方法，点击按钮时用click()方法。
from selenium import webdriver
import time
 
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')
input.send_keys('iPhone')
time.sleep(1)
input.clear()
input.send_keys('iPad')
button = browser.find_element_by_class_name('btn-search')
button.click()

#动作链
from selenium import webdriver
from selenium.webdriver import ActionChains
 
browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()

#执行JavaScript
#这里就利用execute_script()方法将进度条下拉到最底部，然后弹出alert提示框。
from selenium import webdriver
 
browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')

#获取节点信息
#1、获取节点属性   get_attribute()
from selenium import webdriver
from selenium.webdriver import ActionChains
 
browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)
print(logo.get_attribute('class'))

#2、获取文本值   get_text()
from selenium import webdriver

browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.text)

#3、获取id、位置、标签名和大小
from selenium import webdriver
 
browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)

#切换Frame
#Selenium打开页面后，它默认是在父级Frame里面操作，而此时如果页面中还有子Frame，它是不能获取到子Frame里面的节点的。这时就需要使用switch_to.frame()方法来切换Frame。
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
 
browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
try:
    logo = browser.find_element_by_class_name('logo')
except NoSuchElementException:
    print('NO LOGO')
browser.switch_to.parent_frame()
logo = browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)

#延时等待
#1、隐式等待:当使用隐式等待执行测试的时候，如果Selenium没有在DOM中找到节点，将继续等待，超出设定时间后，则抛出找不到节点的异常。换句话说，当查找节点而节点并没有立即出现的时候，隐式等待将等待一段时间再查找DOM，默认的时间是0。
from selenium import webdriver
 
browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('https://www.zhihu.com/explore')
input = browser.find_element_by_class_name('zu-top-add-question')
print(input)


#2、显示等待：隐式等待的效果其实并没有那么好，因为我们只规定了一个固定时间，而页面的加载时间会受到网络条件的影响。这里还有一种更合适的显式等待方法，它指定要查找的节点，然后指定一个最长等待时间。如果在规定时间内加载出来了这个节点，就返回查找的节点；如果到了规定时间依然没有加载出该节点，则抛出超时异常。
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
browser = webdriver.Chrome()
browser.get('https://www.taobao.com/')
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print(input, button)
#这里首先引入WebDriverWait这个对象，指定最长等待时间，然后调用它的until()方法，传入要等待条件expected_conditions。比如，这里传入了presence_of_element_located这个条件，代表节点出现的意思，其参数是节点的定位元组，也就是ID为q的节点搜索框。
#对于按钮，可以更改一下等待条件，比如改为element_to_be_clickable，也就是可点击，所以查找按钮时查找CSS选择器为.btn-search的按钮，如果10秒内它是可点击的，也就是成功加载出来了，就返回这个按钮节点；如果超过10秒还不可点击，也就是没有加载出来，就抛出异常。


#前进和后退
#使用back()方法后退，使用forward()方法前进。
import time
from selenium import webdriver
 
browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')
browser.get('https://www.taobao.com/')
browser.get('https://www.python.org/')
browser.back()
time.sleep(1)
browser.forward()
browser.close()


#Cookies
from selenium import webdriver
 
browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
print(browser.get_cookies())
browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())

#选项卡管理
import time
from selenium import webdriver
 
browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(1)
browser.switch_to_window(browser.window_handles[0])
browser.get('https://python.org')

#异常处理
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
 
browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('Time Out')
try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()


