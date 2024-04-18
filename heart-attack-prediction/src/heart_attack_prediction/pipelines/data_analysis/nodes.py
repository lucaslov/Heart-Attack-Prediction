import seaborn as sns
import matplotlib.pyplot as plt
from kedro_datasets.matplotlib import MatplotlibWriter #https://docs.kedro.org/en/0.17.7/kedro.extras.datasets.matplotlib.MatplotlibWriter.html

def age_distribution(heart):
    plt.figure(figsize=(10, 6))
    sns.histplot(heart['age'], bins=10, kde=True, color='skyblue')
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.tight_layout()
    single_plot_writer = MatplotlibWriter(
        filepath="data/02_analysis/output_plot.png"
    )
    single_plot_writer.save(plt)
    plt.close()