from pathlib import Path
                                 # __file__ 은 현재 파일을 의미
WORK_DIR = Path(__file__).parent # 경로(path 객체)의 바로 위 디렉토리 보여주는 속성
OUT_DIR = WORK_DIR / "output" # out put 주소 생성 ( 해당 위치 폴더에)
#파일/폴더 경로를 객체로 다루기 위한 클래스

if __name__ == "__main__":
    OUT_DIR.mkdir(exist_ok=True) # 파일 생성
