from supabase import create_client
from dotenv import load_dotenv
import pandas as pd
import os

# Load environment variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Create Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def fetch_table(table_name: str) -> pd.DataFrame:
    """
    Generic function to fetch any Supabase table and return a DataFrame.
    Includes error handling and safe empty fallback.
    """
    try:
        response = supabase.table(table_name).select("*").execute()
        data = response.data or []
        return pd.DataFrame(data)

    except Exception as e:
        print(f"Error fetching table '{table_name}': {e}")
        return pd.DataFrame()


def get_bookings() -> pd.DataFrame:
    return fetch_table("bookings")


def get_branches() -> pd.DataFrame:
    return fetch_table("branches")


def get_services() -> pd.DataFrame:
    return fetch_table("services")


def get_payments() -> pd.DataFrame:
    return fetch_table("payments")