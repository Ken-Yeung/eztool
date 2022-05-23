import os
from dotenv import load_dotenv

def target_path():
    load_dotenv()

    MY_ENV_VAR = os.getenv('location')
    
    return MY_ENV_VAR

if __name__ == "__main__":
    print(target_path())
    pass