from pathlib import Path
import matplotlib.pyplot as plt
from step_2_1 import OUT_DIR
from step_3_1 import load_plot_data

'''
fig -> 전체 도화지 바탕
fig.set_size_inches(9,4) 등등
fig.savefig("~~")

ax -> 무엇을 그릴지
ax.barh -> 막대
ax.plot -> 점, 선
ax.set_title
'''
plot_data = load_plot_data()
fig, ax = plt.subplots()
ax.barh(plot_data["stem"], plot_data["size"])
fig.savefig(OUT_DIR / f"{Path(__file__).stem}.png")

