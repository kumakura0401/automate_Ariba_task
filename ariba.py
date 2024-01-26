import datetime
import PyPDF2
import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#--------------------------------------------
# Chrome WebDriverのパスを指定する
#https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/121.0.6167.85/win64/chromedriver-win64.zip からダウンロード
webdriver_path = 'C:\\hogehoge\\chromedriver-win64\\chromedriver.exe' # WebDriverのパスを指定 ### 要変更!!!

# ChromeのWebDriverサービスを開始
service = Service(webdriver_path)

# ChromeのWebDriverオプションを設定
options = Options()

# detachオプションを追加（スクリプト終了後もブラウザを開いたままにする）
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")  # ウィンドウを最大化して開始,ノートPCだと最大化しても請求書欄が出てこないかも注意

# ChromeのWebDriverインスタンスを作成（オプションを適用）
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 300)
#--------------------------------------------
#請求書月の判定
last_month = last_month = datetime.datetime.now().month - 1
if last_month == 0:
    last_month = 12
two_month_ago = last_month - 1
if two_month_ago == 0:
    two_month_ago = 12
#--------------------------------------------
    
# PDFファイルから請求書番号、請求日取得
def extract_bill_info():
    # ページの内容をテキストとして取得
    text = reader.pages[0] .extract_text()

    # 検索したい文字列のパターン
    search_pattern4num = r"(請求書番号：)(.*)"
    
    # reモジュールを使ってテキスト検索（grepのような処理）
    matches = re.search(search_pattern4num, text)
    
    # マッチした結果を表示
    bill_number = matches.group(2).strip()

    search_pattern4date = r"(請求日：)(.*)"
    matches2 = re.search(search_pattern4date, text)
    bill_date = matches2.group(2).split("/")[-1].strip()
    return bill_number,bill_date

# 今月の請求書PDFファイルを開く
pdf_path4this_time = f"C:\\hogehoge\\{last_month}月分_請求書.pdf"  ### 要変更!!!
pdf_path4last_time = f"C:\\hogehoge\\{two_month_ago}月分_請求書.pdf"  ### 要変更!!!

with open(pdf_path4this_time, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    
    # PDFの各ページをループ処理
    bill_number,bill_date = extract_bill_info()
    print(bill_number,bill_date)
    

# 先月の請求書PDFファイルを開く
with open(pdf_path4last_time, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    
    # PDFの各ページをループ処理
    bill_num_last,bill_date_last = extract_bill_info()
    print( bill_num_last,bill_date_last)
    
#--------------------------------------------

#Webページを開く
def open_tab():

    # Chromeを起動してAribaのウェブページを開く
    URL = 'https://アリバのサプライヤー用URL'  ### 要変更!!!
    driver.get(URL)  ### 要変更!!!
#--------------------------------------------
def click_target_ID(id):
    target_element = wait.until(EC.presence_of_element_located((By.ID,id)) ) 
    time.sleep(1)
    target_element.click()

def click_target_XPATH(xpath):
    target_element = wait.until(EC.presence_of_element_located((By.XPATH,xpath)) ) 
    time.sleep(1)
    target_element.click()

def send_keys_target_ID(id,keys):
    target_element = wait.until(EC.presence_of_element_located((By.ID,id)) ) 
    time.sleep(1)
    target_element.send_keys(keys)

def send_keys_target_XPATH(xpath,keys):
    target_element = wait.until(EC.presence_of_element_located((By.XPATH,xpath)) ) 
    time.sleep(1)
    target_element.send_keys(keys)

def send_keys_target_CSS(css,keys):
    target_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,css)) ) 
    time.sleep(1)
    target_element.send_keys(keys)


#--------------------------------------------
username = "hogehoge"  ### 要変更!!!
passwd = "hugahuga"  ### 要変更!!!

#Aribaにログイン
def type_username():
    send_keys_target_ID("userid",username)
    click_target_XPATH("//div[@class='ies-button-container']")
  
def type_password():
    send_keys_target_ID("Password",passwd)
    click_target_XPATH("//input[@type='submit']") 
#--------------------------------------------
    
#請求書一覧に移動
def move_to_bill_list():
        click_target_ID("SUPInvoices")
        click_target_ID("IOSInvoiceList")
#--------------------------------------------

#先月の請求書をソートしてコピー
def sort_copy():
    send_keys_target_XPATH("//*[@id='match-0']/div/div/fd-tokenizer/div/div/input", bill_num_last)
    click_target_ID("filter-apply-button")
    click_target_XPATH(f"//a[contains(text(),'{ bill_num_last}')]")
    click_target_ID("_hdqedc")

#--------------------------------------------

#今月の請求書情報を入力
def input_information():
    send_keys_target_ID("_pg4sld",bill_number)
    click_target_ID("_ydqjz")
    click_target_XPATH(f"//a[contains(text(),'{bill_date}')]")
    time.sleep(2)
    click_target_XPATH("//tr[@id='_zric1']/td/div[@bh='CHK']")
    click_target_ID("_bpfqtd")
    time.sleep(1)
    click_target_ID("_9ai8w")
    time.sleep(1)
    send_keys_target_XPATH("//*[@id='_b8ddmb']/td/div/table/tbody/tr[7]/td[2]/table/tbody/tr[3]/td[1]/table/tbody/tr[2]/td/span/input",pdf_path4this_time)
    click_target_ID("_rrsgbb")
    click_target_XPATH("//tr[@id='_zric1']/td/div[@bh='CHK']")
    wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='_b8ddmb']/td/div/table/tbody/tr[7]/td[2]/table/tbody/tr[4]/td/table")) )
    click_target_XPATH("//*[@id='_ffzbzc']")
    
#--------------------------------------------

open_tab()
type_username()
type_password()
move_to_bill_list()
sort_copy()
input_information()
