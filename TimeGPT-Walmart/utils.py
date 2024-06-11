import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd
import seaborn as sns


def plot_model_comparison(dataframe: pd.DataFrame) -> None:
    """
    Bar plot comparison between models
    Args:
        dataframe (pd.DataFrame): data with actuals and forecats for both models
    """

    tide_model = dataframe.drop(columns="TimeGPT")
    tide_model["model"] = "TiDE"
    tide_model["MAPE"] = (
        abs(tide_model["target"] - tide_model["forecast"]) / tide_model["target"]
    )

    timegpt_model = dataframe.drop(columns="forecast").rename(
        columns={"TimeGPT": "forecast"}
    )
    timegpt_model["model"] = "TimeGPT"
    timegpt_model["MAPE"] = (
        abs(timegpt_model["target"] - timegpt_model["forecast"])
        / timegpt_model["target"]
    )

    plt.rcParams["figure.figsize"] = (20, 5)
    ax = sns.barplot(
        data=pd.concat([tide_model, timegpt_model]),
        x="Date",
        y="MAPE",
        hue="model",
        palette=["#dd4fe4", "#070620"],
    )
    plt.title("Comparison between TiDE and TimeGPT models in real data")
    plt.xticks(rotation=45)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    plt.show()

def plot_model_comparison_(dataframe: pd.DataFrame) -> None:
    """
    Bar plot comparison between models
    Args:
        dataframe (pd.DataFrame): data with actuals and forecats for all models
    """

    tide_model = dataframe.drop(columns=["TimeGPT", "Chronos_Large", "MOIRAI", "X"])
    tide_model["model"] = "TiDE"
    tide_model["MAPE"] = (
        abs(tide_model["target"] - tide_model["TiDE"]) / tide_model["target"]
    )

    timegpt_model = dataframe.drop(columns=["TiDE", "Chronos_Large", "MOIRAI", "X"])
    timegpt_model["model"] = "TimeGPT"
    timegpt_model["MAPE"] = (
        abs(timegpt_model["target"] - timegpt_model["TimeGPT"])
        / timegpt_model["target"]
    )

    chronos_model = dataframe.drop(columns=["TiDE", "TimeGPT", "MOIRAI", "X"])
    chronos_model["model"] = "Chronos_Large"
    chronos_model["MAPE"] = (
        abs(chronos_model["target"] - chronos_model["Chronos_Large"])
        / chronos_model["target"]
    )

    moirai_model = dataframe.drop(columns=["TiDE", "TimeGPT", "Chronos_Large", "X"])
    moirai_model["model"] = "MOIRAI"
    moirai_model["MAPE"] = (
        abs(moirai_model["target"] - moirai_model["MOIRAI"])
        / moirai_model["target"]
    )
    
    X_model = dataframe.drop(columns=["TiDE", "TimeGPT", "Chronos_Large", "MOIRAI"])
    X_model["model"] = "XGB"
    X_model["MAPE"] = (
        abs(X_model["target"] - X_model["X"])
        / moirai_model["target"]
    )


    plt.rcParams["figure.figsize"] = (25, 7)
    ax = sns.barplot(
        data=pd.concat([tide_model, timegpt_model, chronos_model, moirai_model, X_model]),
        x="Date",
        y="MAPE",
        hue="model",
        palette=["#dd4fe4", "#070620", "#696969", "#B0C4DE", 'red'],
    )
    plt.title("Comparison between all models in real data")
    plt.xticks(rotation=45)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    plt.show()