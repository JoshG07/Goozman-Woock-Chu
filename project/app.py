# Invasive plants in California dashboard
# Run with:  shiny run --reload app.py
#
# Reads four files you save from your notebooks first:
#   Data/processed/cal_outline.gpkg
#   Data/processed/invasives_within_year.gpkg
#   Data/processed/inaturalist_cleaned.gpkg
#   Data/processed/invasives_summary_wide_nice.csv

from pathlib import Path

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from shiny import App, reactive, render, ui

# %%
# SETUP
project_path = Path(__file__).parent.resolve()
data_path = project_path / "Data" / "processed"

# Data for the prescribed fire map and bar chart
cal_outline = gpd.read_file(data_path / "cal_outline.gpkg")
invasives = gpd.read_file(data_path / "invasives_within_year.gpkg")
invasives = invasives.to_crs(cal_outline.crs)

# Column that holds the fire year. Change this to match your data,
# or leave it and the year slider will simply not appear.
YEAR_COL = "year"
has_year = YEAR_COL in invasives.columns

# Fixed color for each before/after category so colors match across figures
categories = sorted(invasives["before_after"].dropna().unique().tolist())
palette = ["#2f6b8f", "#d08c1f", "#6a8f3b", "#8a4f7d"]
colors = {cat: palette[i % len(palette)] for i, cat in enumerate(categories)}

# Data for the species search map
observations = gpd.read_file(data_path / "inaturalist_cleaned.gpkg")
names = sorted(observations["common_name"].dropna().astype(str).unique().tolist())
xmin, ymin, xmax, ymax = observations.total_bounds

# Data for the summary table
summary_table = pd.read_csv(data_path / "invasives_summary_wide_nice.csv")

# Drop the plain row-number column pandas adds when saving, if there is one
first_col = summary_table.columns[0]
if first_col.startswith("Unnamed"):
    if summary_table[first_col].tolist() == list(range(len(summary_table))):
        summary_table = summary_table.drop(columns=first_col)
    else:
        summary_table = summary_table.rename(columns={first_col: "Species"})

# Keep only the columns we want to show
summary_table = summary_table.loc[:, ["common_name", "Before", "After"]]

# Find the column with species names, so the species search can filter the table
name_set = set(names)
species_col = next(
    (c for c in summary_table.columns if summary_table[c].astype(str).isin(name_set).any()),
    None,
)

# %%
# USER INTERFACE

# Sidebar filters, grouped by section
sidebar_items = [
    ui.h5("Prescribed fire map and chart"),
    ui.input_checkbox_group(
        "timing", "Observation timing", choices=categories, selected=categories
    ),
]
if has_year:
    years = invasives[YEAR_COL].dropna().astype(int)
    sidebar_items.append(
        ui.input_slider(
            "years",
            "Fire year",
            min=int(years.min()),
            max=int(years.max()),
            value=(int(years.min()), int(years.max())),
            sep="",
        )
    )
sidebar_items += [
    ui.hr(),
    ui.h5("Species map and table"),
    ui.input_selectize(
        "species",
        "Search by common name",
        choices=names,
        multiple=True,
        options={"placeholder": "Start typing a name..."},
    ),
    ui.p("Leave empty to show all observations."),
]

app_ui = ui.page_sidebar(
    ui.sidebar(*sidebar_items, title="Filters", width=320),
    ui.layout_columns(
        ui.value_box("Fire map: observations shown", ui.output_text("fire_n_obs")),
        ui.value_box("Species map: observations shown", ui.output_text("species_n_obs")),
    ),
    ui.layout_columns(
        ui.card(
            ui.card_header("Invasive plant observations within one year of a prescribed fire"),
            ui.output_plot("fire_map", height="600px"),
        ),
        ui.card(
            ui.card_header("Invasive plant species observations, 2009 to 2026"),
            ui.output_plot("species_map", height="600px"),
        ),
    ),
    ui.card(
        ui.card_header("Counts of invasive species observed within one year of a prescribed burn"),
        ui.output_plot("species_counts", height="650px"),
    ),
    ui.card(
        ui.card_header("Summary of invasive species observed before and after prescribed burns"),
        ui.output_data_frame("summary_table_out"),
    ),
    title="Invasive Plants in California",
)


# %%
# SERVER
def server(input, output, session):

    # ---------- Prescribed fire map ----------
    @reactive.calc
    def fire_filtered():
        df = invasives[invasives["before_after"].isin(input.timing())]
        if has_year:
            low, high = input.years()
            df = df[df[YEAR_COL].between(low, high)]
        return df

    @render.text
    def fire_n_obs():
        return f"{len(fire_filtered()):,}"

    @render.plot
    def fire_map():
        fig, ax = plt.subplots(figsize=(6, 7))
        cal_outline.boundary.plot(ax=ax, color="black", linewidth=0.5)

        df = fire_filtered()
        for cat, group in df.groupby("before_after"):
            group.plot(ax=ax, color=colors[cat], markersize=6, label=cat)

        if len(df) > 0:
            ax.legend(title="Timing")
        else:
            ax.text(
                0.5, 0.5, "No observations match these filters",
                transform=ax.transAxes, ha="center",
            )

        ax.set_xlabel("Eastings")
        ax.set_ylabel("Northings")
        return fig

    # ---------- Bar chart of species counts (uses the fire filters) ----------
    @render.plot
    def species_counts():
        df = fire_filtered()
        fig, ax = plt.subplots(figsize=(9, 8))

        if len(df) == 0:
            ax.text(
                0.5, 0.5, "No observations match these filters",
                transform=ax.transAxes, ha="center",
            )
            ax.axis("off")
            return fig

        hue_order = [c for c in ["after", "before"] if c in df["before_after"].unique()]
        sns.histplot(
            data=df,
            y="common_name",
            hue="before_after",
            hue_order=hue_order,
            palette=colors,
            multiple="stack",
            ax=ax,
        )
        ax.set(xlabel="Count", ylabel="Invasive Species")
        if ax.get_legend() is not None:
            ax.get_legend().set_title("Observation Relative to Fire")
        fig.tight_layout()
        return fig

    # ---------- Species map ----------
    @reactive.calc
    def species_filtered():
        selected = input.species()
        if not selected:
            return observations
        return observations[observations["common_name"].isin(selected)]

    @render.text
    def species_n_obs():
        return f"{len(species_filtered()):,}"

    @render.plot
    def species_map():
        fig, ax = plt.subplots(figsize=(6, 7))

        # All observations in light grey for context
        observations.plot(ax=ax, color="lightgrey", markersize=1)

        # Selected species on top
        if input.species():
            species_filtered().plot(ax=ax, markersize=6, color="#2f6b8f")

        ax.set_xlim(xmin, xmax)
        ax.set_ylim(ymin, ymax)
        ax.set_xlabel("Eastings")
        ax.set_ylabel("Northings")
        return fig

    # ---------- Summary table (uses the species search) ----------
    @render.data_frame
    def summary_table_out():
        selected = input.species()
        df = summary_table
        if selected and species_col is not None:
            df = df[df[species_col].astype(str).isin(selected)]
        return render.DataGrid(df, filters=True, height="450px")


app = App(app_ui, server)