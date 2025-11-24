from typing import Any

# pipe-filter pattern

# Iterface
class Filter:
    def __init__(self):
        pass
    def execute(self, input:Any) -> Any:
        raise NotImplementedError

class Pipe:
    def __init__(self):
        self.pipe = list()
    def add_filter(self, filter:Filter):
        self.pipe.append(filter)
    def add_filters(self, filters:list[Filter]):
        self.pipe.extend(filters)
    def run_pipeline(self, input:Any):
        temp = input
        for filter in self.pipe:
            temp = filter.execute(temp)
        return temp

# Handlers
class TextNormalizeFilter(Filter):
    def execute(self, input:str) -> str:
        raise NotImplementedError

class CaseNormalizer(TextNormalizeFilter):
    def execute(self, input:str) -> str:
        raise NotImplementedError

class CaseLowerNormalizer(CaseNormalizer):
    def execute(self, input:str) -> str:
        return input.lower()

class SpecialCharNormalizer(TextNormalizeFilter):
    # TODO: 정규표현식을 사용하는 방식으로 변경
    def __init__(self):
        self.replace_special_char   :dict[str,str]  = {'.':' ', ',':' ', '!':' ', '?':' '}
        self.removable_special_char :list[str]      = []
    
    def execute(self, input:str) -> str:
        temp = input
        for char, replace_char in self.replace_special_char.items():
            temp = temp.replace(char, replace_char)
        for char in self.removable_special_char:
            temp = temp.replace(char, '')
        return temp

class WhitespaceNormalizer(TextNormalizeFilter):
    # TODO: 정규표현식을 사용하는 방식으로 변경
    def __init__(self):
        self.replace_rule:dict[str,str] = {"  " : " "}
    def execute(self, input:str) -> str:
        temp = input
        for origin, repl in self.replace_rule.items():
            temp = temp.replace(origin, repl)
        temp = temp.strip()
        return temp

class UnicodeNormalizer(TextNormalizeFilter):
    def execute(self, input:str) -> str:
        return input

class PunctuationNormailzer(TextNormalizeFilter):
    def execute(self, input:str) -> str:
        return input


"""Use Case
# Concrete
text_normalizer = Pipe()
text_normalizer.add_filters([CaseLowerNormalizer(), SpecialCharNormalizer(), WhitespaceNormalizer()])
text = "안녕하세요! 오늘    날씨가 정말 ?! 좋은데요! Good Morning!  Hey!"
result = text_normalizer.run_pipeline(text)
print(result)
>> 안녕하세요 오늘  날씨가 정말  좋은데요 good morning  hey
"""



