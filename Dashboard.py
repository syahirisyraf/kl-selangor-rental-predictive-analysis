import streamlit as st
import pandas as pd

df = pd.read_csv("data/mudah-apartment-kl-selangor-cleaned.csv")

def filtering():
    """Filter the dataframe based on user selections."""
    col1, col2 = st.columns(2)
    with col1:
        region = st.pills(
            "Regions",
            options=df["region"].unique(),
            selection_mode="multi",
            width="stretch"
        )
    with col2:
        property_type = st.multiselect(
            "Property Type",
            options=df["property_type"].unique(),
        )

    filtered = df.copy()
    if region:
        filtered = filtered[filtered["region"].isin(region)]
    if property_type:
        filtered = filtered[filtered["property_type"].isin(property_type)]
    return filtered


def metric_card(data):
    """Create a custom metric card for Streamlit."""
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Listings", value=data["prop_name"].count(), format="localized", border=True)
    col2.metric("Total Average Monthly Rent", value=f"RM {data['monthly_rent'].mean():,.0f}", format="localized", border=True)
    col3.metric("Total Median Monthly Rent", value=f"RM {data['monthly_rent'].median():,.0f}", format="localized", border=True)
    col4.metric("Total Locations", value=data["location"].nunique(), format="localized", border=True)

def line_chart_and_bar_chart(data):
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Avg Monthly Rent by Completion Year")
        avg_rent_year = data.groupby(["completion_year", "region"])["monthly_rent"].mean().reset_index()
        st.line_chart(avg_rent_year.pivot(index="completion_year", columns="region", values="monthly_rent"), height=500)

    with col2:
        st.subheader("Avg Monthly Rent by Property Type")
        avg_rent_type = data.groupby(["property_type", "region"])["monthly_rent"].mean().reset_index()
        st.bar_chart(avg_rent_type.pivot(index="property_type", columns="region", values="monthly_rent"), horizontal=True, stack=False, sort=True, height=500)


def list_of_table(data):
    """Create a table with selected columns from the dataframe."""
    df_selected = data[
        [
            "prop_name",
            "completion_year",
            "monthly_rent",
            "location",
            "property_type",
            "rooms", "parking",
            "bathroom",
            "size (sq.ft)"
        ]
    ]
    st.dataframe(df_selected)

st.title("Mudah Apartment Data Analysis")
filtered_df = filtering()
metric_card(filtered_df)
line_chart_and_bar_chart(filtered_df)
list_of_table(filtered_df)