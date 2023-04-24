# IPL 2023 ETL Project

## Set-up

Make folder for ETL script and Unit Testing.

### Setting up pyenv

1. Download pyenv

    ```bash
    curl https://pyenv.run | bash
    ```
2.  Configure bashrc

    -  Check if .bashrc has pyenv added

    ```bash
    grep PYENV ~/.bashrc
    ```

    - If not there, add the following:

    ```bash
    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init --path)"
    ```

3. Restart or source

    ```bash
    source ~/.bashrc
    ```

4. Once installed, install the version of python needed

    - Check the versions:


    ```bash
    pyenv install --list
    ```

    - I will install 3.10.11

    ```bash
    pyenv install -v 3.10.11
    ```

5. Check different versions installed on local

    ```bash
    pyenv versions
    ```

6. Switch python version

    ```bash
    pyenv local 3.10.11
    ```

### Setting up virtual env

1. Create venv

    ```bash
    python -m venv venv
    ```

2. Use virtual env

    ```bash
    source venv/bin/activate
    ```

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


### Extract

### Transform

### Load

Loading into SQLite database:



