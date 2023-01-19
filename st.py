import pandas as pd 
import numpy as np
import plotly.express as px
import streamlit as st
color_discrete_sequence = ['#1DB954']

st.markdown("""
<style>
.css-1hdmowm.egzxvld0
{
    visibility:hidden;
}
</style>

""",unsafe_allow_html=True)


@st.cache(allow_output_mutation=True)
def get_data(file_name,file_name2,file_name3):
    df = pd.read_csv(file_name)
    df2 = pd.read_csv(file_name2)
    df3 = pd.read_csv(file_name3)
    return df,df2,df3

artists,features,tracks=get_data('artists.csv','SpotifyFeatures.csv','tracks.csv')
st.title('welcome To Spotify Analysis')



st.header('Artist By Followers')
artist_list = artists.name.unique().tolist()
artist_options=[]
for artist_name in artist_list:
    if len(str(artist_name)) < 30:
        artist_options.append(artist_name)
top_artists = artists.sort_values('followers',ascending=False)
artista =st.multiselect('which artists you would like to see',artist_options,
['Ed Sheeran','Ariana Grande','Drake','Justin Bieber','Eminem',
'Rihanna','Billie Eilish','Taylor Swift','Imagine Dragons'])
top_artists = top_artists[top_artists["name"].isin(artista)]
fig = px.scatter( data_frame=top_artists,x="name", y="followers", color='name')
fig.update_layout({'showlegend': False},width=800,height=600)
st.write(fig)
st.text('Here we see that the most followed artist in spotify is Ed sheeran with almost 79 million follower')




st.header('Most Popular Songs on Spotify')
st.text('This is a table of the most 50 popular songs on spotify')
tracks['duration_min'] =round((tracks['duration_ms']/1000/60),1)
tracks_pop=tracks[['name', 'artists', 'release_date', 'popularity','duration_min']]
most_popular =tracks_pop.sort_values('popularity',ascending=False).head(50)
most_popular = most_popular.reset_index(drop=True)
st.dataframe(most_popular)
st.text('And The Most Popular Song on Spotify is Peaches by Justin Bieber')





st.header('Top & Bottom Songs By Duration on Spotify')
tracks['duration'] =round((tracks['duration_ms']/1000),1)
top10_tracksduration = tracks.sort_values('duration_min',ascending=False).head(10)
b10=tracks[tracks['name']!='Pause Track']
bottom10_tracksduration = b10.sort_values('duration',ascending=True).head(10)
fig_topdur= px.scatter( data_frame=top10_tracksduration,x="name", y="duration_min", color='name')
fig_topdur.update_layout({'showlegend': False},xaxis_title=" ",yaxis_title="duration By Min",width=800,height=600)
fig_bopdur= px.scatter( data_frame=bottom10_tracksduration,
x="name",
y="duration", 
color='name',
color_discrete_sequence=color_discrete_sequence)
fig_bopdur.update_layout({'showlegend': False},xaxis_title=" ",yaxis_title="duration By Sec",width=800,height=600)
rad = st.radio('what kind of analysis would you like to see',['Top 10 🔝' ,'Bottom 10'])
if rad == 'Top 10 🔝':
    st.write(fig_topdur)
else:
    st.write(fig_bopdur)




st.header('Number of Songs Produced By Year')
d = tracks.year.value_counts().index
s =tracks.year.value_counts()
fig_songs_by_year = px.histogram(
  			# Set the data and x variable
  			data_frame=tracks, x=d ,y=s
,nbins=200 ,color_discrete_sequence=color_discrete_sequence)
fig_songs_by_year.update_layout(
    xaxis_title="year",
    yaxis_title="Num of Songs",width=800,height=600)
st.write(fig_songs_by_year)
st.text('Here we see that the year 2020 is the first with almost 14k songs maybe cuse of the corona virus' )




st.header('Number of Songs By genre')
genre_ind = features.genre.value_counts().index
genre_f =features.genre.value_counts()
fig_songs_by_genre = px.histogram(
  			# Set the data and x variable
  			data_frame=features, x=genre_ind ,y=genre_f
,nbins=30,color_discrete_sequence=color_discrete_sequence)
fig_songs_by_genre.update_layout(
    xaxis_title="Genre",
    yaxis_title="Num of Songs",width=800,height=600)
st.write(fig_songs_by_genre)
st.text('Here we see that the comedy genre has the most songs')