
param(
    [switch]$a,
    [switch]$p,
    [switch]$d
    )

function install_python {
    # PythonインストーラーのURL
    $pythonUrl = "https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe"
    # Pythonインストーラーのパス
    $installerPath = "$env:TEMP\python_installer.exe"
    Invoke-WebRequest -Uri $pythonUrl -OutFile $installerPath
    Start-Process $installerPath -ArgumentList '/quiet InstallAllUsers=0 PrependPath=1' -Wait
    Remove-Item $installerPath

    $Python = "C:\Users\$env:USERNAME\AppData\Local\Programs\Python\Python310\Scripts"
    "$Python\pip.exe install selenium"
    "$Python\pip.exe install PyPDF2"
    "Python has been installed."
}

function install_webdriver {
    # ChromeDriverのURL
    $chromeDriverUrl = "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/121.0.6167.85/win64/chromedriver-win64.zip"
    Invoke-WebRequest -Uri $chromeDriverUrl -OutFile "$env:TEMP\chromedriver.zip"
    Expand-Archive -Path "$env:TEMP\chromedriver.zip" -DestinationPath "C:\hogehoge"
    Remove-Item -Path "$env:TEMP\chromedriver.zip" -Force
    "ChromeDriver has been installed."
}

#オプションが複数してされた場合に対応できるようelseifではなくifを使用（オプション増やす可能性あるので）

if ($a -or -not($a -or $p -or $d)) {
    install_python
    install_webdriver
}

if ($p) {
    install_python
}

if ($d) {
    install_webdriver
}

