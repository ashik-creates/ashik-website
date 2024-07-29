from sqlalchemy import create_engine, URL,text
from sqlalchemy.orm import sessionmaker
import os


def get_db_engine():
    connect_args = {}
    if "isrgrootx1.pem":
        connect_args = {
            "ssl_verify_cert": True,
            "ssl_verify_identity": True,
            "ssl_ca": "isrgrootx1.pem",
        }
    return  create_engine(        
        URL.create(            
            drivername="mysql+pymysql",
            username=os.environ['username'],                    
            password=os.environ['password'],                    
            host=os.environ['host'],            
            port=4000,             
            database=os.environ['name'],         
        ),
        connect_args=connect_args,     
    )

engine = get_db_engine()
Session = sessionmaker(bind=engine)


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs;"))
    jobs = []
    for row in result.all():
        jobs.append(row._asdict())
  return jobs