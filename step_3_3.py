from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np # 선형대수 라이브러리
from step_2_1 import OUT_DIR
from step_3_1 import load_plot_data

plot_data = load_plot_data()
log_size = np.log(plot_data["size"]) # 수치-> 자연로그 변환
fig, ax = plt.subplots(figsize=(16,9), dpi = 100 )
ax.barh(plot_data["stem"], log_size)
ax.grid(True, axis="x") #축 그리드 표시 (여기서는 x축만)
ax.tick_params(labelbottom=False, length=0, labelsize=20)
fig.set_layout_engine("tight") # 자동으로 겹치지 않게 배치하라는 뜻
fig.savefig(OUT_DIR / f"{Path(__file__).stem}.png") #경로 만들고 savefig #이미 경로에 파일 이름 정해져있음
