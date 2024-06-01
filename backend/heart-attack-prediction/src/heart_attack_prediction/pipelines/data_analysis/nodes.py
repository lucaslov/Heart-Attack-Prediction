import seaborn as sns
import matplotlib.pyplot as plt
from kedro_datasets.matplotlib import MatplotlibWriter #https://docs.kedro.org/en/0.17.7/kedro.extras.datasets.matplotlib.MatplotlibWriter.html
import wandb

def plot(heart):
    plots_dict = dict()

    plots_dict["Age Distribution.png"] = plt.figure(figsize=(10, 6))
    sns.histplot(heart['age'], bins=10, kde=True, color='skyblue')
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.tight_layout()
    
    plots_dict["Age Distribution with Gender Comparison.png"] = plt.figure(figsize=(10, 6))
    sns.histplot(heart, x="age", hue="sex", multiple="stack", bins=10, kde=True)
    plt.title('Age Distribution with Gender Comparison')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.tight_layout()
    
    plots_dict["Correlation Heatmap.png"] = plt.figure(figsize=(10, 8))
    sns.heatmap(heart.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    
    plots_dict["Resting Blood Pressure vs. Cholesterol Scatter Plot.png"] = plt.figure(figsize=(10, 6))
    sns.scatterplot(data=heart, x="trtbps", y="chol", hue="output")
    plt.title('Resting Blood Pressure vs. Cholesterol Scatter Plot')
    plt.xlabel('Resting Blood Pressure')
    plt.ylabel('Cholesterol')
    plt.grid(True)
    plt.tight_layout()
    
    dict_plot_writer = MatplotlibWriter(
        filepath="heart-attack-prediction/data/02_analysis/plots"
    )
    dict_plot_writer.save(plots_dict)
    wandb.log({ 'charts' : plots_dict })
    plt.close("all")
    