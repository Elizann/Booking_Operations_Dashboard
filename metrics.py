import pandas as pd


def clean_data(df):

    df = df.copy()

    df.columns = df.columns.str.strip()

    df["booking_status"] = (
        df["booking_status"]
        .fillna("Pending")
        .astype(str)
        .str.strip()
        .str.title()
    )

    return df


def total_bookings(df):
    return len(df)


def completed_bookings(df):

    return len(
        df[
            df["booking_status"] == "Completed"
        ]
    )


def cancelled_bookings(df):

    return len(
        df[
            df["booking_status"] == "Cancelled"
        ]
    )


def cancellation_rate(df):

    total = len(df)

    if total == 0:
        return 0

    cancelled = len(
        df[
            df["booking_status"] == "Cancelled"
        ]
    )

    return round(
        cancelled / total * 100,
        2
    )


def booking_status_summary(df):

    summary = (
        df["booking_status"]
        .value_counts()
        .reset_index()
    )

    summary.columns = [
        "booking_status",
        "count"
    ]

    return summary