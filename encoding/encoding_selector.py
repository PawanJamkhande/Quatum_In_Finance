from encoding.penalty import penalty_encoding
from encoding.slack import slack_encoding

def select_encoding(features, returns, covariance, constraints):
    ctype = features["constraint_type"]
    fractional = features["fractional"]

    if fractional:
        raise Exception("Binary expansion not implemented")

    if ctype == "budget":
        encoding_name = "Penalty-Based"
        Q = penalty_encoding(
            returns,
            covariance,
            constraints["budget"]
        )
    else:
        encoding_name = "Slack-Variable"
        Q = slack_encoding(returns, covariance)

    return encoding_name, Q
