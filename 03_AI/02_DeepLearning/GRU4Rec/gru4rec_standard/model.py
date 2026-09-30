import torch
from torch import nn
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence


class GRU4Rec(nn.Module):
    def __init__(
        self, num_items, embedding_dim=64, hidden_size=128, num_layers=1, dropout=0.2,
        *, numeric_feature_dim=0, use_padding=False, feature_cols=None,
    ):
        '''아이템 임베딩과 선택적 수치 특성 및 패딩을 지원하는 GRU를 구성한다.'''
        super().__init__()
        self.num_items = num_items
        self.numeric_feature_dim = numeric_feature_dim
        self.feature_cols = tuple(feature_cols or ())
        if self.feature_cols and len(self.feature_cols) != numeric_feature_dim:
            raise ValueError('feature_cols must match numeric_feature_dim')
        self.use_padding = use_padding
        self.index_offset = int(use_padding)
        self.item_embedding = nn.Embedding(
            num_items + self.index_offset, embedding_dim,
            padding_idx=0 if use_padding else None,
        )
        self.embedding_dropout = nn.Dropout(dropout)
        self.gru = nn.GRU(
            embedding_dim + numeric_feature_dim, hidden_size, num_layers=num_layers, batch_first=True,
            dropout=dropout if num_layers > 1 else 0.0,
        )
        self.output_dropout = nn.Dropout(dropout)
        self.output = nn.Linear(hidden_size, num_items)

    def forward(self, item_sequences, hidden=None, *, numeric_features=None, lengths=None):
        '''아이템과 수치 특성을 처리하되 패딩 시점을 제외한 점수를 반환한다.'''
        embedded = self.embedding_dropout(self.item_embedding(item_sequences))
        if self.numeric_feature_dim:
            expected = (*item_sequences.shape, self.numeric_feature_dim)
            if numeric_features is None or tuple(numeric_features.shape) != expected:
                raise ValueError(f'numeric_features must have shape {expected}')
            embedded = torch.cat((embedded, numeric_features), dim=-1)
        elif numeric_features is not None and numeric_features.shape[-1] != 0:
            raise ValueError('This model does not accept numeric features')
        if self.use_padding:
            if lengths is None:
                lengths = item_sequences.ne(0).sum(dim=1)
            lengths = torch.as_tensor(lengths, dtype=torch.long, device='cpu')
            if lengths.shape != (item_sequences.shape[0],) or (lengths < 1).any() or (lengths > item_sequences.shape[1]).any():
                raise ValueError('lengths must describe nonempty sequences within the input width')
            valid = torch.arange(item_sequences.shape[1], device=item_sequences.device)[None] < lengths.to(item_sequences.device)[:, None]
            if item_sequences[valid].eq(0).any() or item_sequences[~valid].ne(0).any():
                raise ValueError('Padding must be on the right and valid positions must contain real items')
            packed = pack_padded_sequence(embedded, lengths, batch_first=True, enforce_sorted=False)
            packed_outputs, hidden = self.gru(packed, hidden)
            outputs, _ = pad_packed_sequence(packed_outputs, batch_first=True, total_length=item_sequences.shape[1])
        else:
            if lengths is not None and not torch.as_tensor(lengths).eq(item_sequences.shape[1]).all():
                raise ValueError('Unpadded batches must contain sequences of the same length')
            outputs, hidden = self.gru(embedded, hidden)
        return self.output(self.output_dropout(outputs)), hidden

    def initial_hidden(self, batch_size):
        '''모델과 동일한 장치 및 자료형으로 초기 hidden state를 생성한다.'''
        return self.item_embedding.weight.new_zeros(
            self.gru.num_layers, batch_size, self.gru.hidden_size,
        )
