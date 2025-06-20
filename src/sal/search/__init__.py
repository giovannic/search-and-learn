from .beam_search import beam_search
from .best_of_n import best_of_n
from .diverse_verifier_tree_search import dvts

from typing import List, Any, TypedDict

class SearchResponse(TypedDict):
    pred: List[Any]
    completions: List[List[str]]
    completion_tokens: List[List[int]]
    scores: List[List[float]]