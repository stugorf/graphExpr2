"""graph.py: Helper functions for graph operations"""

__author__  = 'David Hughes'
__email__   = 'dhughes@octavebio.com'
__version__ = '0.0.1dev'
__all__     = ['']

# Imports
from utils import *
from neo4j import GraphDatabase

### Graph Functions ###
def neo4j_query(driver, query, params):
    with driver.session(database=_database) as session:
       result = session.run(query, params)
       return pd.DataFrame([r.values() for r in result], columns=result.keys())


def match_trials(driver, pt_inclusions,pt_exclusions):
    try:
        result  = neo4j_query(driver, 
        """
        MATCH (c)-[:HAS_INCLUSION_CRITERIA]->(i:InclusionCriteria)
        WITH c,COLLECT(DISTINCT i.inclusion) AS inclusions
        UNWIND pt_inclusions AS inclusion
        WHERE inclusion IN inclusions
        RETURN DISTINCT c.nctid as nctid, c.brief_title as title
        """, {'pt_inclusions':pt_inclusions,'pt_exclusions':pt_exclusions })
        return result
    except Exception as err:
        log.error(f"Error getting trials: {err}")
        sys.exit("Error getting trials")