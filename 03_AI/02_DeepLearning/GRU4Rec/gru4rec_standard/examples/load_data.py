from pathlib import Path

import pandas as pd


def load_data(csv_path: str | Path, *, user_col: str = 'user_id', item_col: str = 'product_id') -> pd.DataFrame:
    '''CSV 경로와 ID 컬럼명을 받아 원천 클릭 로그를 반환한다.'''
    return pd.read_csv(
        Path(csv_path),
        dtype={user_col: 'string', item_col: 'string'},
    )


def load_data_step(state, config):
    '''workflow 입력을 데이터 로딩 함수에 전달하고 결과를 감싼다.'''
    return {'raw_data': load_data(**config['load_data'])}
