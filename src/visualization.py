import matplotlib.pyplot as plt
import seaborn as sns

def plot_activity_budget(activity_series, title="Activity Budget"):
    """
    Plot a simple bar chart of activity budget.
    activity_series: output of compute_activity_budget()
    """
    plt.figure(figsize=(6, 4))
    sns.barplot(x=activity_series.index, y=activity_series.values)
    plt.ylabel("Proportion of Time")
    plt.xlabel("Behaviour")
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_individual_timeseries(df, time_column, behaviour_column, title="Behaviour Over Time"):
    """
    Plot behaviour over time for a single individual.
    df: DataFrame filtered for one individual
    """
    plt.figure(figsize=(10, 4))
    plt.plot(df[time_column], df[behaviour_column], marker="o")
    plt.xlabel("Time")
    plt.ylabel("Behaviour")
    plt.title(title)
    plt.tight_layout()
    plt.show()

