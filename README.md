# Facebook Message Unsender

Install selenium:
```
pip install selenium
```

Download Chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads
Unzip and place in `/usr/local/bin`

If you see error (on Mac) `“chromedriver” cannot be opened because the developer cannot be verified.`, follow step [here](https://stackoverflow.com/questions/60362018/macos-catalinav-10-15-3-error-chromedriver-cannot-be-opened-because-the-de):
```
xattr -d com.apple.quarantine /usr/local/bin/chromedriver
```

Create `user.json` file with contents as follows:
```json
{
  "email": "EMAIL",
  "password": "PASSWORD"
}
```
