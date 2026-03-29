from core.settings import settings
from utils.logger.default_logger import logger
from schemas.dto import TestCase
from core.enums import MetricMethod
import math
from abc import ABC, abstractmethod

class Evaluator(ABC):
    @abstractmethod
    def compute(self, case:TestCase, k:int|None=None) -> float:
        pass

class PrecisionEvaluator(Evaluator):
    def compute(self, case:TestCase, k:int|None=None) -> float:
        predict_items = case.predict_items
        truth_items = {key for key, relevance in case.ground_truth.items() if relevance > 0}
        if (k is None) or (k > len(predict_items)):
            k = len(predict_items)
        predict_items_k = predict_items[:k]
        precision = self.calc_precision(predict_items_k, truth_items)
        return precision
    def calc_precision(self, predict_items:list[str|int],
                       truth_items:set[str|int]) -> float:
        if len(predict_items) == 0:
            return 0.0
        precision = len(set(predict_items) & truth_items) / len(predict_items)
        return precision

class RecallEvaluator(Evaluator):
    def compute(self, case:TestCase, k:int|None=None) -> float:
        predict_items = case.predict_items
        truth_items = {key for key, relevance in case.ground_truth.items() if relevance > 0}
        if (k is None) or (k > len(predict_items)):
            k = len(predict_items)
        predict_items_k = predict_items[:k]
        recall = self.calc_recall(predict_items_k, truth_items)
        return recall
    def calc_recall(self, predict_items:list[str|int],
                    truth_items:set[str|int]) -> float:
        if len(truth_items) == 0:
            return 0.0
        recall = len(set(predict_items) & truth_items) / len(truth_items)
        return recall
    
class RREvaluator(Evaluator):
    def compute(self, case:TestCase, k:int|None=None) -> float:
        predict_items = case.predict_items
        truth_items = {key for key, relevance in case.ground_truth.items() if relevance > 0}
        if (k is None) or (k > len(predict_items)):
            k = len(predict_items)
        predict_items_k = predict_items[:k]
        rr = self.calc_rr(predict_items_k, truth_items)
        return rr
    def calc_rr(self, predict_items:list[str|int],
                truth_items:set[str|int]) -> float:
        if len(predict_items) == 0:
            return 0.0
        for i, item in enumerate(predict_items):
            if item in truth_items:
                return 1/(i+1)
        return 0.0

class APEvaluator(Evaluator):
    def compute(self, case:TestCase, k:int|None=None) -> float:
        predict_items = case.predict_items
        truth_items = {key for key, relevance in case.ground_truth.items() if relevance > 0}
        if (k is None) or (k > len(predict_items)):
            k = len(predict_items)
        predict_items_k = predict_items[:k]
        ap = self.calc_ap(predict_items_k, truth_items)
        return ap
    # 본 AP는 실무적으로 커스터마이징한 지표임
    def calc_ap(self, predict_items:list[str|int],
                truth_items:set[str|int]) -> float:
        if len(truth_items) == 0:
            return 0.0
        sum_precision = 0
        hit = 0
        for i, item_yn in enumerate(predict_items):
            if item_yn in truth_items:
                hit += 1
                sum_precision += hit/(i + 1)
        return sum_precision/min(len(truth_items), len(predict_items))
            
class NDCGEvaluator(Evaluator):
    def compute(self, case:TestCase, k:int|None=None) -> float:
        predict_items = case.predict_items
        ground_truth = case.ground_truth
        if (k is None) or (k > len(predict_items)):
            k = len(predict_items)
        predict_items_k = predict_items[:k]
        ndcg = self.calc_ndcg(predict_items_k, ground_truth, k)
        return ndcg
    
    def calc_dcg(self, relevance_scores) -> float:
        dcg = sum(score / (math.log2(i+1+1)) for i, score in enumerate(relevance_scores))
        return dcg
    
    def calc_ndcg(self, predict_items:list[str|int],
                  ground_truth:dict[str|int, float],
                  k:int=None) -> float:
        if len(ground_truth) == 0:
            return 0.0
        ideal_relevance_scores = sorted(ground_truth.values(), reverse=True)[:k]
        idcg = self.calc_dcg(ideal_relevance_scores)
        if idcg == 0.0:
            return 0.0
        dcg = self.calc_dcg([ground_truth.get(item, 0.0) for item in predict_items])
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
        except ValueError:
            raise ValueError(f"There is no metric {metric}")
        except KeyError:
            raise KeyError(f"There is no metric {metric}")
        return evaluator()
    