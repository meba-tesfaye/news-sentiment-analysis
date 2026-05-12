from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

def get_sentiment_score(text):
    """
    Modular sentiment logic for Task 3.
    """
    analyzer = SentimentIntensityAnalyzer()
    if isinstance(text, str):
        return analyzer.polarity_scores(text)['compound']
    return 0

def classify_sentiment(score):
    """
    Categorizes the compound score into Positive, Negative, or Neutral.
    """
    if score >= 0.05:
        return 'Positive'
    elif score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

def apply_sentiment_pipeline(df, column_name='headline'):
    """
    Applies the full sentiment process to a dataframe.
    """
    df = df.copy()
    df['sentiment_score'] = df[column_name].apply(get_sentiment_score)
    df['sentiment_class'] = df['sentiment_score'].apply(classify_sentiment)
    return df