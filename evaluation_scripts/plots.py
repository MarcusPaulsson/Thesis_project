import os
import matplotlib.pyplot as plt
import numpy as np
from cognitive_complexity import calculate_cognitive_complexity, process_files as process_cognitive_files, calculate_statistics as calculate_cognitive_statistics
from cyclomatic_complexity import calculate_cyclomatic_complexity, process_files as process_cyclomatic_files, calculate_statistics as calculate_cyclomatic_statistics

def create_bar_plots(chatgpt_stats, gemini_stats, metric_name, output_filename):
    """
    Creates bar staple plots comparing ChatGPT and Gemini statistics.

    Args:
        chatgpt_stats (dict): Statistics for ChatGPT.
        gemini_stats (dict): Statistics for Gemini.
        metric_name (str): The name of the complexity metric.
        output_filename (str): The filename to save the plot.
    """

    if chatgpt_stats is None or gemini_stats is None:
        print("No data available to create plots.")
        return

    stats_keys = ["Minimum complexity", "Maximum complexity", "Average complexity", "Standard deviation"]
    chatgpt_values = [chatgpt_stats.get(key, 0) for key in stats_keys]
    gemini_values = [gemini_stats.get(key, 0) for key in stats_keys]

    x = np.arange(len(stats_keys))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))
    rects1 = ax.bar(x - width/2, chatgpt_values, width, label='ChatGPT')
    rects2 = ax.bar(x + width/2, gemini_values, width, label='Gemini')

    ax.set_ylabel('Complexity Values')
    ax.set_title(f'{metric_name} Comparison')
    ax.set_xticks(x)
    ax.set_xticklabels(stats_keys, rotation=45, ha='right')
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()
    plt.savefig(output_filename)
    print(f"Plot saved to {output_filename}")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    chatgpt_dir = os.path.join(parent_dir, "results", "ChatGPT", "cli_games")
    gemini_dir = os.path.join(parent_dir, "results", "Gemini", "cli_games")
    plot_dir = os.path.join(parent_dir, "results", "plot_images")

    # Create the plot directory if it doesn't exist
    os.makedirs(plot_dir, exist_ok=True)

    # Cognitive Complexity
    chatgpt_cognitive_results = process_cognitive_files(chatgpt_dir, calculate_cognitive_complexity)
    gemini_cognitive_results = process_cognitive_files(gemini_dir, calculate_cognitive_complexity)
    chatgpt_cognitive_stats = calculate_cognitive_statistics(chatgpt_cognitive_results)
    gemini_cognitive_stats = calculate_cognitive_statistics(gemini_cognitive_results)
    cognitive_plot_path = os.path.join(plot_dir, "cognitive_complexity_comparison.png")
    create_bar_plots(chatgpt_cognitive_stats, gemini_cognitive_stats, "Cognitive Complexity", cognitive_plot_path)

    # Cyclomatic Complexity
    chatgpt_cyclomatic_results = process_cyclomatic_files(chatgpt_dir, calculate_cyclomatic_complexity)
    gemini_cyclomatic_results = process_cyclomatic_files(gemini_dir, calculate_cyclomatic_complexity)
    chatgpt_cyclomatic_stats = calculate_cyclomatic_statistics(chatgpt_cyclomatic_results)
    gemini_cyclomatic_stats = calculate_cyclomatic_statistics(gemini_cyclomatic_results)
    cyclomatic_plot_path = os.path.join(plot_dir, "cyclomatic_complexity_comparison.png")
    create_bar_plots(chatgpt_cyclomatic_stats, gemini_cyclomatic_stats, "Cyclomatic Complexity", cyclomatic_plot_path)