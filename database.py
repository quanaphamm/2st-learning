from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://sql3763295:VbmzSwWIgr@sql3.freesqldatabase.com/sql3763295?charset=utf8mb4"
engine = create_engine(db_connection_string)



def load_jobs_from_db():
  with engine.connect() as conn:
      result = conn.execute(text("select * from jobs"))
      jobs = []
      for row in result.mappings().all():
          jobs.append(dict(row))
  return jobs