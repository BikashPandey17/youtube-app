"""
       Config Selector
       There are Two type of configs:
           1. Development : `__dev.py` [ENV = development]
           3. Production : `__pro.py` [ENV = production]
       SET VARIABLE `ENV` to the above mentioned `development`/`production`
       ACCORDING TO THE REQUIREMENT
   """
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

if os.environ.get("ENV_TYPE") == 'development':
    from .__dev import *
elif os.environ.get("ENV_TYPE") == 'production':
    from .__prod import *
else:
    from .__prod import *