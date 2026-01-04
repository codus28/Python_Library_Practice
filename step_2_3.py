import json # 데이터를 구조적으로 표현하기 위한 텍스트 기반 포맷
from pathlib import Path
from step_2_1 import OUT_DIR

OUT_2_3 = OUT_DIR / f"{Path(__file__).stem}.json" # Path(__file__) 이 코드가 들어있는 파일의 경로

# 하위 폴더목록을 JSON 형식으로 저장
def dump_dirnames(base_dir: Path) -> None:
    print("BASE_DIR =", base_dir)
    print("RESOLVED =", base_dir.resolve())
    dirs = []
    for path in base_dir.iterdir(): # Path가 가리키는 폴더 안의 내용을 하나씩 꺼내줌
        if path.is_dir(): # Path 객체가 가리키는 대상이 폴더인지 확인하는 메서드
            dirs.append(path.as_posix()) # posix 스타일 경로 문자열로 변환
    dirs_sorted = sorted(dirs)
    #Json 파일로 데이터를 저장하는 코드
    with open(OUT_2_3, "w", encoding="utf-8") as fp:
        #Python 객체를 JSON으로 변환해서 fp에 씀 ,
        json.dump(dirs_sorted, fp, ensure_ascii=False, indent=2)

 #JSON 파일로 저장된 폴더 목록을 불러오는 함수
def load_dirnames() -> list[str]:
    if OUT_2_3.is_file():
        with open(OUT_2_3, encoding="utf-8") as fp:
            return json.load(fp) # Python 객체로 읽어오기 load 함수. 파이썬 객체로

    return []

if __name__ == "__main__":
    dump_dirnames(Path.home())
    data = load_dirnames()
    print(data)

