
### Setting up Poetry

N/A

### Setting up Selenium with WSL

***Not using selenium anymore***

https://cloudbytes.dev/snippets/run-selenium-and-chrome-on-wsl2

1. Download chrome on wsl:

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```

```bash
sudo dpkg -i google-chrome-stable_current_amd64.deb
```

```bash
sudo apt --fix-broken install
```

```bash
google-chrome-stable --version
```

2. Install chromedriver for correct chrome version

```bash
chrome_driver=$(curl "https://chromedriver.storage.googleapis.com/LATEST_RELEASE") && \
echo "$chrome_driver"
```
```bash
curl -Lo chromedriver_linux64.zip "https://chromedriver.storage.googleapis.com/\
${chrome_driver}/chromedriver_linux64.zip"
```
```bash
sudo apt install unzip
```

```bash
mkdir -p "chromedriver/stable" && \
unzip -q "chromedriver_linux64.zip" -d "chromedriver/stable" && \
chmod +x "chromedriver/stable/chromedriver"
```