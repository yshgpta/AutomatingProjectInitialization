### Install 
```bash
git clone "https://github.com/yshgpta/AutomatingProjectInitialization.git"
cd AutomatingProjectInitialization
```
Now change the directory path in .my_custom_commands.sh to your own project directory path then
```bash
pip install -r requirements.txt
chmod +x .my_custom_commands.sh
source ~/.my_custom_commands.sh
```
After this,install the [chromedriver](https://chromedriver.chromium.org/) and change the project directory and chromedriver directory path in create.py.


### Usage
To run the script type in 'create <name of your folder> <your github username> <your password>
The name of the command can easily be changed by following the commented line in the project files.
