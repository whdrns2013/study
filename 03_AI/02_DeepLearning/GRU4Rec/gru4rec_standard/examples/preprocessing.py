import pandas as pd


def data_preprocessing(
    raw_data: pd.DataFrame,
    *,
    user_col: str = 'user_id',
    item_col: str = 'product_id',
    time_col: str = 'clicked_at',
    session_gap_minutes: float = 30,
) -> pd.DataFrame:
    '''원천 클릭 표와 세션 분리 기준으로 학습 이벤트 표를 반환한다.'''
    gap_minutes = session_gap_minutes
    if not 0 < gap_minutes < float('inf'):
        raise ValueError('session_gap_minutes must be finite and positive')
    columns = [user_col, item_col, time_col]
    if len(set(columns)) != 3:
        raise ValueError('Source column names must be distinct')
    frame = raw_data[columns].copy()
    if frame.empty or frame.isna().any().any():
        raise ValueError('Click logs must be nonempty and must not contain nulls')
    frame[time_col] = pd.to_datetime(frame[time_col], utc=True, errors='raise')
    if frame[time_col].isna().any():
        raise ValueError('Click timestamps must not be missing')
    frame = frame.sort_values([user_col, time_col], kind='stable').reset_index(drop=True)
    gaps = frame.groupby(user_col, sort=False)[time_col].diff()
    new_session = gaps.isna() | gaps.gt(pd.Timedelta(minutes=gap_minutes))
    events = pd.DataFrame({
        'SessionId': new_session.cumsum(),
        'UserId': frame[user_col],
        'ItemId': frame[item_col],
        'Time': frame[time_col],
        'GapMinutes': gaps.dt.total_seconds().div(60).where(~new_session, 0.0),
    })
    events['SequencePosition'] = events.groupby('SessionId', sort=False).cumcount().astype('float32')
    return events


def preprocessing_step(state, config):
    '''workflow 입력을 전처리 함수에 전달하고 이벤트 표를 감싼다.'''
    return {'events': data_preprocessing(state['raw_data'], **config['preprocessing'])}
