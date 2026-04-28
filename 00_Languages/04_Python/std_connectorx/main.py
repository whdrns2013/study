from scripts.data_generator import generate_dummy_data, create_db, insert_dummy_data
from scripts.benchmark import benchmark_pandas, benchmark_sqlalchemy, benchmark_pymysql, benchmark_connectorx
import pandas as pd

def init_data():
    try:
        create_db()
        datas = generate_dummy_data()
        insert_dummy_data(datas)
    except:
        datas = generate_dummy_data()
        try:
            insert_dummy_data(datas)
        except:
            pass

def benchmarks():
    times = {"pandas":list(), "sqlalchemy":list(), "pymysql":list(), "connectorx":list()}
    # 10회 반복
    for i in range(10):
        times["pandas"].append(benchmark_pandas())
        times["sqlalchemy"].append(benchmark_sqlalchemy())
        times["pymysql"].append(benchmark_pymysql())
        times["connectorx"].append(benchmark_connectorx())
    return times
    
def main():
    # init_data()
    times = benchmarks()
    pd.DataFrame(times).to_csv("time_check_result.csv")
    

if __name__ == "__main__":
    main()
