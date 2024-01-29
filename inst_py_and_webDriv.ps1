

# ChromeDriverのURL
$chromeDriverUrl = "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/121.0.6167.85/win64/chromedriver-win64.zip"
Invoke-WebRequest -Uri $chromeDriverUrl -OutFile "$env:TEMP\chromedriver.zip"
Expand-Archive -Path "$env:TEMP\chromedriver.zip" -DestinationPath "C:\hogehoge"  

