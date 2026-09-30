import torch
from torch import nn


class GRU4Rec(nn.Module):
    def __init__(self, num_items, embedding_dim=64, hidden_size=128, num_layers=1, dropout=0.2):
        '''아이템 임베딩과 GRU로 세션 기반 다음 아이템 예측 모델을 구성한다.'''
        super().__init__()
        self.num_items = num_items
        self.item_embedding = nn.Embedding(num_items, embedding_dim)
        self.embedding_dropout = nn.Dropout(dropout)
        self.gru = nn.GRU(
            embedding_dim, hidden_size, num_layers=num_layers, batch_first=True,
            dropout=dropout if num_layers > 1 else 0.0,
        )
        self.output_dropout = nn.Dropout(dropout)
        self.output = nn.Linear(hidden_size, num_items)

    def forward(self, item_sequences, hidden=None):
        '''아이템 시퀀스로 각 시점의 점수와 갱신된 hidden state를 반환한다.'''
        embedded = self.embedding_dropout(self.item_embedding(item_sequences))
        outputs, hidden = self.gru(embedded, hidden)
        return self.output(self.output_dropout(outputs)), hidden

    def initial_hidden(self, batch_size):
        '''모델과 동일한 장치 및 자료형으로 초기 hidden state를 생성한다.'''
        return self.item_embedding.weight.new_zeros(
            self.gru.num_layers, batch_size, self.gru.hidden_size,
        )
