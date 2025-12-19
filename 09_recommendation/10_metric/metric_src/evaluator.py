from core.settings import settings
from utils.logger.default_logger import logger
from schemas.dto import TestCase
from core.enums import MetricMethod
import math

# TODO: 예외처리, 로그 (코드 전반)
# TODO: DB에 저장 미구현

class Evaluator:
    def compute(self, case:TestCase, k:int|None=None) -> float:
        raise NotImplementedError

class PrecisionEvaluator(Evaluator):
    def compute(self, case:TestCase, k:int|None=None) -> float:
        predict_items = case.predict_items
        truth_items = {key for key, relevance in case.ground_truth.items() if relevance > 0}
        if k is None:
            k = len(predict_items)
        predict_items_k = predict_items[:k]
        precision = self.calc_precision(predict_items_k, truth_items)
        return precision
    
    def calc_precision(self, predict_items, truth_items) -> float:
        if (len(truth_items) == 0) or (len(predict_items) == 0):
            return 0.0
        precision = len(set(predict_items) & set(truth_items)) / len(predict_items)
        # 추천 리스트에는 중복이 없다고 가정한다.
        return precision

class RecallEvaluator(Evaluator):
    def compute(self, case:TestCase, k:int|None=None) -> float:
        predict_items = case.predict_items
        truth_items = {key for key, relevance in case.ground_truth.items() if relevance > 0}
        if k is None:
            k = len(predict_items)
        predict_items_k = predict_items[:k]
        recall = self.calc_recall(predict_items_k, truth_items)
        return recall
    
    def calc_recall(self, predict_items, truth_items) -> float:
        if (len(truth_items) == 0) or (len(predict_items) == 0):
            return 0.0
        recall = len(set(predict_items) & set(truth_items)) / len(set(truth_items))
        return recall

class RREvaluator(Evaluator):
    def compute(self, case:TestCase, k:int|None=None):
        predict_items = case.predict_items
        truth_items = {key for key, relevance in case.ground_truth.items() if relevance > 0}
        if k is None:
            k = len(predict_items)
        predict_items_k = predict_items[:k]
        rr = self.calc_rr(predict_items_k, truth_items)
        return rr
    
    def calc_rr(self, predict_items, truth_items) -> float:
        # RR은 **선호도에 상관 없이**, 가장 빨리 출현한 선호 아이템을 기준으로 계산한다.
        if (len(truth_items) == 0) or (len(predict_items) == 0):
            return 0.0
        for i, item in enumerate(predict_items):
            if item in truth_items:
                return 1 / (i + 1)
        return 0.0

class APEvaluator(Evaluator):
    def compute(self, case:TestCase, k:int|None=None):
        predict_items = case.predict_items
        truth_items = {key for key, relevance in case.ground_truth.items() if relevance > 0}
        if k is None:
            k = len(predict_items)
        predict_items_k = predict_items[:k]
        ap = self.calc_ap(predict_items_k, truth_items)
        return ap
    
    def calc_ap(self, predict_items, truth_items) -> float:
        if (len(truth_items) == 0) or (len(predict_items) == 0):
            return 0.0
        truth_items = set(truth_items)
        sum_precision = 0
        hit = 0
        for i, item in enumerate(predict_items):
            if item in truth_items:
                hit += 1
                sum_precision += hit/(i+1)
        return sum_precision/len(truth_items)
            
class NDCGEvaluator(Evaluator):
    def compute(self, case:TestCase, k:int|None=None):
        predict_items = case.predict_items
        ground_truth = case.ground_truth
        if (k is None) or (k > len(predict_items)):
            k = len(predict_items)
        predict_items_k = predict_items[:k]
        ndcg = self.calc_ndcg(predict_items_k, ground_truth, k)
        return ndcg
    
    def calc_dcg(self, scores) -> float:
        dcg = sum((score / math.log2(i+1+1)) for i, score in enumerate(scores))
        return dcg
    
    def calc_ndcg(self, predict_items, ground_truth, k) -> float:
        ideal_relevance_scores = [x[1] for x in sorted(ground_truth.items(), key=lambda x:x[1], reverse=True)[:k]]
        predict_relevance_scores = [ground_truth.get(item, 0.0) for item in predict_items]
        dcg = self.calc_dcg(predict_relevance_scores)
        if len(ideal_relevance_scores) == 0:
            idcg = 0.0
        else:
            idcg = self.calc_dcg(ideal_relevance_scores)
        if idcg == 0.0:
            return 0.0
        else:
            return dcg/idcg

class EvaluatorFactory:
    _map = {
        MetricMethod.PRECISION  :PrecisionEvaluator,
        MetricMethod.RECALL     :RecallEvaluator,
        MetricMethod.MRR        :RREvaluator,
        MetricMethod.MAP        :APEvaluator,
        MetricMethod.NDCG       :NDCGEvaluator
    }
    @classmethod
    def create(cls, metric: MetricMethod) -> Evaluator:
        try:
            evaluator = cls._map[metric]
        except:
            raise ValueError(f"There is no metric {metric}")
        return evaluator()
    