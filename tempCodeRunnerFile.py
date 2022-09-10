df_genre=pd.read_csv('SpotifyFeatures.csv')

plt.title("Duration of the songs in Different Genres")
sns.color_palette("rocket",as_cmap=True)
sns.barplot(y='genre',x='duration_ms',data=df_genre)
plt.xlabel("Duration(ms)")
plt.ylabel("Genres")
plt.xticks(rotation=90)
plt.show()