Simple RPA Tool
=======================
## How to setup 
Clone this repo.

```sh 
git clone https://github.com/baoquan1211/rpa-tool
cd rpa-tool 
``` 

Install packages using yarn or npm. 

```sh 
npm install 
``` 

Create environment and install requirements for python.
```sh 
python -m venv venv
# Window:
.\venv\Scripts\activate
# Mac or Linux:
source .\venv\bin\activate
pip install -r requirements.txt
``` 
--- 

## How to develop 
To run the example in dev environment first run front end. 
```sh 
npm run dev 
``` 
Then run backend in aseparate terminal. 

```sh 
python main.py --dev 
``` 
--- 
## How to build executable 
To build and executable first build static files. 
```sh 
npm run build 
``` 
Then build using pyinstaller. 
```sh 
python -m eel main.py dist --onefile --noconsole --name rpa-tool 
```