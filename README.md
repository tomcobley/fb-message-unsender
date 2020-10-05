# Facebook Message Unsender

Facebook don't want to let go of our data, and make it very laborious to delete old posts and messages.

So, this project is a work in progress to enable rapid 'unsending' of Facebook messages, deleting them from your devices, the recipients devices and (hopefully) the Facebook servers.

## Setup
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

Create `user.json` file with contents as follows (replacing <EMAIL> and <PASSWORD> with your Facebook credentials):
```json
{
  "email": "<EMAIL>",
  "password": "<PASSWORD>"
}
```

## Usage

Set the URL in `main.py` to the intended recipient and run `main.py`.

## Disclaimer

Use at your own discretion / risk. Messages will be deleted without confirmation. Be careful not to unintentionally delete messages.
