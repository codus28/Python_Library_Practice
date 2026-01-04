
from pathlib import Path
from step_2_1 import WORK_DIR

def get_total_filesize(base_dir: Path, pattern: str = "*") -> int: #type hint
    total_bytes = 0
    for fullpath in base_dir.glob(pattern): #glob = find , pattern 에 맞게
                                            # * 은 여기 폴더에 있는거 전부를 의미
                                            # 하나씩 꺼내쓰는 느낌임 (globe)
        if fullpath.is_file():
            total_bytes += fullpath.stat().st_size # stat (정보status) -> 파일 정보 가져오기
    return total_bytes                             # st_size -> 파일 크기 (byte)

if __name__ == "__main__" :
    base_dir = WORK_DIR
    filesize = get_total_filesize(base_dir, pattern="*")
    print(f"{base_dir.as_posix()=}, {filesize=} bytes")

