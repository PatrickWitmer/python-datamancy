# 🤘 HEAVY METAL FESTIVAL LINEUP ANALYSIS 🤘

```
██╗  ██╗███████╗ █████╗ ██╗   ██╗██╗   ██╗    ███╗   ███╗███████╗████████╗ █████╗ ██╗
██║  ██║██╔════╝██╔══██╗██║   ██║╚██╗ ██╔╝    ████╗ ████║██╔════╝╚══██╔══╝██╔══██╗██║
███████║█████╗  ███████║██║   ██║ ╚████╔╝     ██╔████╔██║█████╗     ██║   ███████║██║
██╔══██║██╔══╝  ██╔══██║╚██╗ ██╔╝  ╚██╔╝      ██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██║
██║  ██║███████╗██║  ██║ ╚████╔╝    ██║       ██║ ╚═╝ ██║███████╗   ██║   ██║  ██║███████╗
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  ╚═══╝     ╚═╝       ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝

███████╗███████╗███████╗████████╗██╗██╗   ██╗ █████╗ ██╗
██╔════╝██╔════╝██╔════╝╚══██╔══╝██║██║   ██║██╔══██╗██║
█████╗  █████╗  ███████╗   ██║   ██║██║   ██║███████║██║
██╔══╝  ██╔══╝  ╚════██║   ██║   ██║╚██╗ ██╔╝██╔══██║██║
██║     ███████╗███████║   ██║   ██║ ╚████╔╝ ██║  ██║███████╗
╚═╝     ╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═══╝  ╚═╝  ╚═╝╚══════╝

 █████╗ ███╗   ██╗ █████╗ ██╗  ██╗   ██╗███████╗██╗███████╗
██╔══██╗████╗  ██║██╔══██╗██║  ╚██╗ ██╔╝██╔════╝██║██╔════╝
███████║██╔██╗ ██║███████║██║   ╚████╔╝ ███████╗██║███████╗
██╔══██║██║╚██╗██║██╔══██║██║    ╚██╔╝  ╚════██║██║╚════██║
██║  ██║██║ ╚████║██║  ██║███████╗██║   ███████║██║███████║
╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝   ╚══════╝╚═╝╚══════╝
```

## Project Overview

This project analyzes the lineup data from a heavy metal festival to uncover insights about bands, genres, venues, and scheduling. Using Python data analysis tools, we explore patterns and relationships within the festival programming.

## Data Description

The dataset contains the following columns:

- `Day`: Festival day (e.g., Day 1, Day 2)
- `Date`: Specific date of performance
- `Venue`: Location/stage where the band performs
- `Band`: Name of the performing band
- `Genre`: Musical genre or subgenre of the band
- `More Info`: Additional information about the band or performance

## Analysis Features

### 1. Festival Overview

- Total number of bands performing
- Distribution of bands across festival days
- Distribution of bands across venues

### 2. Genre Analysis

- Most common genres at the festival
- Genre diversity analysis
- Trends in genre representation

### 3. Venue-Genre Relationship

- Which genres tend to play at which venues
- Dominant genre at each venue
- Genre composition analysis by venue

### 4. Timeline Analysis

- Performance scheduling patterns
- Genre distribution by day

## Requirements

- Python 3.x
- pandas
- matplotlib
- seaborn
- numpy

Install required packages with:

```bash
pip install pandas matplotlib seaborn numpy
```

## How to Use

1. Clone this repository
2. Place your festival lineup CSV file in the project directory
3. Run the analysis script:

```bash
python analyze_festival.py
```

## Key Visualizations

- Bar charts showing band distribution by day
- Pie charts of venue distribution
- Heatmaps of genre-venue relationships
- Stacked bar charts of genre composition by venue

## Future Enhancements

- Add time analysis if set times are available
- Include band popularity metrics
- Incorporate historical data from previous years
- Interactive dashboard development

## Credits

Created as a data analysis learning project, combining a passion for heavy metal music with data science fundamentals.

🔥 ROCK ON 🔥
