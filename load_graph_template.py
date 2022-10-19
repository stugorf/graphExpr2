"""load_graph_template.py: Loads data into Neo4j instance"""

__author__  = 'David Hughes'
__email__   = 'dhughes@octavebio.com'
__version__ = '0.0.1dev'
__all__     = ['']


# Import
import boto3
import awswrangler as wr
from hydra import compose, initialize
from omegaconf import DictConfig

class AppConf:
    def __init__(self):
        self.init_db()

    def init_db(self):
        try:
            with initialize(config_path= os.path.join("..","conf",)):
                cfg = compose(config_name="config")
                log.info('Getting PatientGraph Secret...')
                self.secret = wr.secretsmanager.get_secret("my-secret")
                assert self.secret is not None, 'Secret not found'
        except Exception as err:
            log.error(f"Error getting AWS secret: {err}")
        try:
                # Get Neo4j config and driver
                user            = self.secret['neo4j-user']
                password        = self.secret['neo4j-password']
                uri             = self.secret['neo4j-url']
                self.database   = self.secret['neo4j-database']
                self.driver     = GraphDatabase.driver(uri, auth=(user, password), encrypted=False)
        except Exception as err:
            log.error(f"Error creating Neo4j Driver: {err}")

appconf     = AppConf()
driver      = appconf.driver
_database   = appconf.database
secret      = appconf.secret

print(secret)
