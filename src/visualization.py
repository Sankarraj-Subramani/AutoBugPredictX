import seaborn as sns
import matplotlib.pyplot as plt

def plot_risk_heatmap(df):
    heatmap_data = df.pivot_table(index='module_name', values='predicted_bug_probability')
    plt.figure(figsize=(8,6))
    sns.heatmap(heatmap_data, annot=True, cmap="Reds")
    plt.title('Bug Risk Heatmap by Module')
    plt.xlabel('Bug Risk')
    plt.ylabel('Module')
    plt.tight_layout()
    return plt
