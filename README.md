# Project Title: Advanced Power BI Visualizations

## Introduction

This project explores the integration of advanced visualization techniques within Power BI, leveraging enriched datasets, glassmorphism backgrounds, HTML cover art, Deneb visuals, and comprehensive formatting to create a visually appealing and insightful dashboard.

## Features

- **Enriched Dataset**: Utilization of ChatGPT & Python for dataset enrichment.
- **Glassmorphism Backgrounds**: Implementation of the latest UI design trend for background aesthetics.
- **Power BI Building**: Detailed data transformation and visualization process.
- **HTML Cover Art**: Dynamic visual elements using HTML.
- **Deneb Visuals**: Custom visuals created with Deneb for a unique look and feel.
- **Polished Formatting**: Attention to detail in visual formatting for clarity and visual appeal.

## Dashboard Screenshot

![Dashboard Screenshot](https://github.com/AbdessamadABIDAOUI/Spotify-most-streamed-songs-2023-with-Power-bi-SQL-Python/blob/main/Screenshot%202024-02-25%20131849.png)



## Tools & Resources Used

- **Power BI**: For data importation, transformation, visualization, and dashboard creation.
- **Python**: For dataset enrichment and data analysis.
- **Deneb Visuals**: For custom visualization creation within Power BI.
- **HTML & CSS**: For creating dynamic cover art and implementing glassmorphism backgrounds.

## How to Use

1. **Data Preparation**: Utilize Python scripts to enrich and prepare your dataset.
2. **Dashboard Design**: Import your dataset into Power BI and apply the visualization techniques as demonstrated.
3. **Customization**: Adjust the Deneb visuals and HTML elements as needed to fit your dataset and design preferences.
4. **Analysis**: Explore the insights provided by the advanced visualizations in your dashboard.

## Credits

- Dataset: [Kaggle](https://www.kaggle.com)
- Deneb Visuals Guide: [PowerBI-tips](https://github.com/PowerBI-tips/Deneb)
- Inspiration: [Ahmed Ashour](https://www.linkedin.com/posts/ahmedashourviz_powerbi-dashboard-activity-7108768101839609856-Xfdl?utm_source=share&utm_medium=member_desktop)

## Contact Information

For more information or to reach out for Power BI consulting, connect with me on LinkedIn:

- [Abidaoui Abdessamad](https://www.linkedin.com/in/abdessamad-abidaoui/)

Thank you for exploring this project. Feel free to share feedback or connect for collaboration opportunities.

## Data Description

This dataset contains a comprehensive list of the most famous songs of 2023 as listed on Spotify. The dataset offers a wealth of features beyond what is typically available in similar datasets. It provides insights into each song's attributes, popularity, and presence on various music platforms. The dataset includes information such as track name, artist(s) name, release date, Spotify playlists and charts, streaming statistics, Apple Music presence, Deezer presence, Shazam charts, and various audio features.

### Key Features:

- **track_name**: Name of the song
- **artist(s)_name**: Name of the artist(s) of the song
- **artist_count**: Number of artists contributing to the song
- **released_year**: Year when the song was released
- **released_month**: Month when the song was released
- **released_day**: Day of the month when the song was released
- **in_spotify_playlists**: Number of Spotify playlists the song is included in
- **in_spotify_charts**: Presence and rank of the song on Spotify charts
- **streams**: Total number of streams on Spotify
- **in_apple_playlists**: Number of Apple Music playlists the song is included in
- **in_apple_charts**: Presence and rank of the song on Apple Music charts
- **in_deezer_playlists**: Number of Deezer playlists the song is included in
- **in_deezer_charts**: Presence and rank of the song on Deezer charts
- **in_shazam_charts**: Presence and rank of the song on Shazam charts
- **bpm**: Beats per minute, a measure of song tempo
- **key**: Key of the song
- **mode**: Mode of the song (major or minor)
- **danceability_%**: Percentage indicating how suitable the song is for dancing
- **valence_%**: Positivity of the song's musical content
- **energy_%**: Perceived energy level of the song
- **acousticness_%**: Amount of acoustic sound in the song
- **instrumentalness_%**: Amount of instrumental content in the song
- **liveness_%**: Presence of live performance elements
- **speechiness_%**: Amount of spoken words in the song

### Potential Use Cases:

- **Music analysis**: Explore patterns in audio features to understand trends and preferences in popular songs.
- **Platform comparison**: Compare the song's popularity across different music platforms.
- **Artist impact**: Analyze how artist involvement and attributes relate to a song's success.
- **Temporal trends**: Identify any shifts in music attributes and preferences over time.
- **Cross-platform presence**: Investigate how songs perform across different streaming services.

## Python Script for Adding Image URLs to the Dataset

The Python script provided enhances the dataset by adding image URLs for each song. This addition allows for a richer analysis and presentation, enabling visual representation of album covers or artist images alongside the statistical data. The script achieves this by interfacing with the Spotify API to fetch image URLs based on track and artist information. Here's how it works:

### Key Features of the Script:

- **Spotify API Integration**: Utilizes the Spotify API to search for songs by their name and artist(s), retrieving detailed information including image URLs.
- **Data Enrichment**: Augments the existing dataset with a new column for image URLs, making the dataset not only informative in terms of numerical and categorical data but also visually engaging.
- **Automated Processing**: Iterates over each row in the dataset, ensuring that every track is queried and, if found, its image URL is added to the dataset.
- **Error Handling**: Implements checks to handle cases where a song might not be found on Spotify, ensuring the robustness of the script.

### Usage Instructions:

1. **API Credentials**: Obtain your Spotify API client ID and client secret by creating an app in the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2. **Dataset Preparation**: Ensure your dataset is in a CSV format with columns for track name, artist(s) name, and other relevant information.
3. **Script Execution**: Run the script, inputting your dataset file path and Spotify API credentials when prompted.
4. **Output**: The script outputs an enhanced version of the dataset with an additional column for image URLs, ready for further analysis or visualization.

### Prerequisites:

- Python installed on your machine.
- A Spotify Developer account to access API credentials.
- Pandas library for data manipulation (install with `pip install pandas`).
- Requests library for making API requests (install with `pip install requests`).

This Python enhancement significantly increases the dataset's value, paving the way for more dynamic and visually appealing data presentations and analyses.


