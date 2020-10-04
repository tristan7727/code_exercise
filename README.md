# CEFT -- Coding Exercise From Tristan

CEFT is a Python3.6 + Selenium UI automation framework.

## Installation & Configuration

Please build your test environment simply using the command below:

```bash
pip install -r requirements.txt
```

## Usage

```
python ./run.py
```

## Notes
1. By default a test user account has been used for testing to log into the test system;   The current test user account will be deleted within 7 days owing to security concern.    However, you can use your own account to execute the test simply via replacing the user credential from ./data/testdata/data_info.xlsx  ( make sure username in cell B1 and password in cell B2 ); 
2. "Send Email" module has been commented out. To enable this function please: 
```
    1. set receiver from "./public/common/sendemail.py"
       recvaddress = ['receiver@xxx.xx']
       sendaddr_name = 'sender@xxx.xx'
       sendaddr_pswd = 'YOUR EMAIL PASSWORD'
```
```
    2. uncomment out below lines from "./run.py"
       #mail = sendmail.SendMail()
       #mail.send()
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

