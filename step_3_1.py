import json
from pathlib import Path
from step_2_1 import OUT_DIR
from step_2_4 import load_filesize_per_dir

OUT_3_1 = OUT_DIR / f"{Path(__file__).stem}.json" #.stem 경로 마지막 이름만 뽑음

def dump_plot_data():
    # dictionary comprehension (for문 + if 문으로 딕셔너리 만들기)
    # -> 아래에서는 key 경로만 간단하게 보이도록
    size_per_path = load_filesize_per_dir()
    size_per_stem = {Path(path).stem: size for path,
                     size in size_per_path.items() #.items() -> (key,value) 튜플
                     if size > 0}
    # key, value만 뽑아서 dump 시키기
    plot_data =dict(
        stem=list(size_per_stem.keys()), # key 뽑아서 stem에 해당하게 list로 저장
        size=list(size_per_stem.values()), # value 뽑아서
    )
    '''
    dict 가능한 경우:
    1. 키워드 인자 dict(a=1: # {"a": 1}
    2. (key, value) 튜플의 묶음 ex) dict([("a", 1)]) , dict((("a", 1),))
    3. 이미 dict ex) dict((("a", 1),))
    '''
    with open(OUT_3_1, "w", encoding="utf-8") as fp:
        json.dump(plot_data, fp, ensure_ascii=False, indent=2) # type: ignore
        # dump: 그대로 내보냄

def load_plot_data() -> dict:
       if OUT_3_1.is_file():
           with open(OUT_3_1, encoding="utf-8") as fp:
               return json.load(fp)
           return {}

if __name__ == "__main__":
     dump_plot_data()
