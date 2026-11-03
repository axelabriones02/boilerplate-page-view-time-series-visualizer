import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# 1. Import the data
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')


# 2. Clean the data
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]


# 3. Draw the line plot
def draw_line_plot():

    # 4. Copy the data
    df_line = df.copy()

    # 5. Create the line chart
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df_line.index, df_line['value'], color='red', linewidth=1)

    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # 6. Save and return image
    fig.savefig('line_plot.png')
    return fig


# 7. Draw the bar plot
def draw_bar_plot():

    # 8. Copy and prepare the data
    df_bar = df.copy()

    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # 9. Create the bar chart
    fig = df_bar.plot(
        kind='bar',
        figsize=(10, 7)
    ).figure

    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(
        title='Months',
        labels=[
            'January', 'February', 'March', 'April',
            'May', 'June', 'July', 'August',
            'September', 'October', 'November', 'December'
        ]
    )

    # 10. Save and return image
    fig.savefig('bar_plot.png')
    return fig


# 11. Draw the box plots
def draw_box_plot():

    # 12. Copy and prepare the data
    df_box = df.copy()

    df_box.reset_index(inplace=True)

    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')

    # 13. Create the order of months
    df_box['month_num'] = df_box['date'].dt.month

    df_box = df_box.sort_values('month_num')

    # 14. Create the figure
    fig, axes = plt.subplots(1, 2, figsize=(20, 6))

    # 15. Year-wise box plot
    sns.boxplot(
        x='year',
        y='value',
        data=df_box,
        ax=axes[0]
    )

    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # 16. Month-wise box plot
    sns.boxplot(
        x='month',
        y='value',
        data=df_box,
        order=[
            'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
        ],
        ax=axes[1]
    )

    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # 17. Save and return image
    fig.savefig('box_plot.png')
    return fig