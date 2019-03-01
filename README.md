# face_recognition

## Some results First!  
![crf](https://user-images.githubusercontent.com/20581741/53666049-10217d00-3c93-11e9-82ab-dcd4cd5d5d97.gif)  

## Getting Started
1. ### Get the code:
    - Using SSH: `git clone git@github.com:vijuSR/face_recognition.git`  
    OR  
    - Using HTTP: `git clone https://github.com/vijuSR/face_recognition.git`

1. ### Setup the Virtual Environment (Recommended):
    - Create the virtual environment
        - `python3 -m venv </path/to/venv>`  
    - Activate your virtual-environment
        - Linux: `source </path/to/venv>/bin/activate`
        - Windows: `cd </path/to/venv>` then `.\Scripts\activate`  
    - Install the requirements
        - `cd <root-dir-of-project>`
        - `pip install --upgrade -I -r requirements.txt`
        > #### Install any missing requirement with `pip install <package-name>`  
        #### That's all for the setup ! :smiley: 

1. ## Setups

- **STEP 0**: Configurations 
   1. There are two supported databases: sqlite and postgres
   1. Current setting is to use sqlite. For using postgres change SQLALCHEMY_SQLITE [in this line](https://github.com/vijuSR/face_recognition/blob/e027ea80d2567d48b21425ea966e6d9124ca7f55/database_client/database.py#L49) to SQLALCHEMY_POSTGRES
   1. Also, if you are using postgres, change the config.ini file accordingly.
   1. In 'config.ini' file and change the path to "haarcascade_frontalface_default.xml" file path on **your system**. For example on my system it's: > "G:/VENVIRONMENT/computer_vision/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml" where > "G:/VENVIRONMENT/computer_vision" is my virtual environment path.
  
- **STEP 1**: Database setup
   1. Postgres:
       - Install postgres, create a database and change 'config.ini' file accordingly.
   1. Creating required tables:
       -`cd </to/repo/root/dir>`
       - in shell/notebook run 
       > `from database import Operations`  
        `Operations.create_tables()`

- AND Yes you did it. That's all required for the setup. :clap:

## Using the celebrity face recognition:

You can use this project in two ways:

1. With flask app:
   1. `cd </to/repo/root/dir>`   
   1. run `python3 routes.py`
   1. Available endpoints:
       - "/": home page, used to upload image for celebs recognition.
       - "/face_recognition": result of celeb recognition, can't be accessed directly.
       - "/new_celeb": presents a form for adding new celeb in the database.
       - "/add_celeb": adds the celebrity to the database.
       > Disabled the public access to the last two endpoints at for my flask app demo at: http://vijusr.pythonanywhere.com/
1. Directly the core model package (without flask app):
   - Checkout the notebook "demo-sqlite.ipynb"


## Improvements:
- Deep learning for face detection
- Transfer learning on celeb dataset with "Siamese network"
- Accuracy analysis with grayscale facial image captures.

## Todos:
- Extend to multiple faces in an image frame.
- Video processing (recognize celebs in video scenes).
- Top n matching celebs. 
- Automate deployment.   
