import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#CleanData.csv does NOT contain any personal Info about any student



if __name__ == "__main__":

    dataa = pd.read_csv("CleanData.csv")

    
    counts = (
        dataa.groupby(["Section", "Gender"])
        .size()
        .unstack(fill_value=0)
    )

    
    section_map = {
        "Section A": "A",
        "Section B": "B",
        "Section C": "C",
        "Section D": "D",
        "E": "E",
        "F": "F",
        "G": "G",
        "H": "H"
    }

    counts = counts.rename(index=section_map)

    Sections = ["A", "B", "C", "D", "E", "F", "G", "H"]

    Girls = counts.reindex(Sections)["Female"].fillna(0)
    Boys = counts.reindex(Sections)["Male"].fillna(0)

    x = np.arange(len(Sections))
    width = 0.35

    plt.style.use("dark_background")

    bars1 = plt.bar(
        x - width / 2,
        Girls,
        width,
        label="Girls",
        color="pink"
    )

    bars2 = plt.bar(
        x + width / 2,
        Boys,
        width,
        label="Boys",
        color="cyan"
    )

    plt.bar_label(bars1)
    plt.bar_label(bars2)

    plt.xticks(x, Sections)
    plt.xlabel("Section")
    plt.ylabel("Number of Students")
    plt.title("Gender Variation in Batch 2026-30")
    plt.legend()

    plt.show()
