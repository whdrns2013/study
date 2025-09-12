from custom_model._custom_model import CustomModel, Context
import joblib
import pandas as pd
import numpy as np
from typing import List

class IntentClassifierModel(CustomModel):
    
    def load_context(self, context:Context):
        self.model = joblib.load(context.artifacts['model'])
        self.embeddings = pd.read_csv(context.artifacts['embedding'])
        
    def predict(self, model_input:List[float]):
        '''input : question-embedding'''
        model = self.model
        embeddings = self.embeddings # 테스트로 불러오기 용
        input_array = np.array(model_input)
        if input_array.ndim != 2:
            input_array = input_array.reshape(1, -1)  # (1, D)
        # predict
        if model:
            pred = model.predict(input_array)[0]
            return pred